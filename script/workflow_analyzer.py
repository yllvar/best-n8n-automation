import os
import json
from collections import defaultdict
from typing import Dict, List, Any
import logging
import re

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class N8nWorkflowAnalyzer:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.node_types = defaultdict(int)
        self.node_connections = defaultdict(list)
        self.node_parameters = defaultdict(list)
        self.workflow_patterns = []
        self.error_files = []

    def find_workflow_files(self) -> List[str]:
        """Find all .json files containing n8n workflows"""
        workflow_files = []
        for root, _, files in os.walk(self.root_dir):
            for file in files:
                if file.endswith('.json') and not file.endswith('README.md'):
                    workflow_files.append(os.path.join(root, file))
        return workflow_files

    def parse_workflow(self, file_path: str) -> Dict[str, Any]:
        """Parse a single workflow file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Try to find the first valid JSON object
                try:
                    return json.loads(content)
                except json.JSONDecodeError:
                    # If the file contains multiple JSON objects, try to parse the first one
                    start_idx = content.find('{')
                    end_idx = content.rfind('}')
                    if start_idx != -1 and end_idx != -1:
                        try:
                            return json.loads(content[start_idx:end_idx+1])
                        except json.JSONDecodeError:
                            self.error_files.append((file_path, "Invalid JSON format"))
                            return {}
                    else:
                        self.error_files.append((file_path, "No JSON object found"))
                        return {}
        except Exception as e:
            self.error_files.append((file_path, str(e)))
            logger.error(f"Error parsing {file_path}: {str(e)}")
            return {}

    def fix_workflow_conventions(self, workflow: Dict[str, Any]) -> Dict[str, Any]:
        """Fix workflow to follow n8n conventions"""
        if not workflow:
            return workflow
            
        # Ensure required fields exist
        if 'name' not in workflow:
            workflow['name'] = 'Untitled Workflow'
            
        if 'nodes' not in workflow:
            workflow['nodes'] = []
            
        if 'connections' not in workflow:
            workflow['connections'] = {}
            
        if 'active' not in workflow:
            workflow['active'] = False
            
        # Fix node naming conventions
        for i, node in enumerate(workflow.get('nodes', [])):
            # Ensure node has required fields
            if 'id' not in node:
                node['id'] = f"node_{i}"
                
            if 'name' not in node:
                node['name'] = f"Node {i}"
                
            if 'type' not in node:
                node['type'] = 'n8n-nodes-base.noOp'
                
            if 'typeVersion' not in node:
                node['typeVersion'] = 1
                
            if 'position' not in node:
                node['position'] = [i * 200, i * 100]
                
            # Ensure parameters field exists
            if 'parameters' not in node:
                node['parameters'] = {}
                
        # Fix connections format
        if 'connections' in workflow:
            fixed_connections = {}
            for source_node, connections in workflow['connections'].items():
                if isinstance(connections, dict):
                    fixed_connections[source_node] = connections
                elif isinstance(connections, list):
                    # Convert old format to new format
                    fixed_connections[source_node] = {'main': connections}
                    
            workflow['connections'] = fixed_connections
            
        return workflow

    def validate_workflow(self, workflow: Dict[str, Any]) -> List[str]:
        """Validate workflow and return list of issues"""
        issues = []
        
        if not workflow:
            issues.append("Empty workflow")
            return issues
            
        # Check required fields
        required_fields = ['name', 'nodes', 'connections']
        for field in required_fields:
            if field not in workflow:
                issues.append(f"Missing required field: {field}")
                
        # Validate nodes
        node_ids = set()
        for i, node in enumerate(workflow.get('nodes', [])):
            if 'id' not in node:
                issues.append(f"Node {i} missing ID")
            elif node['id'] in node_ids:
                issues.append(f"Duplicate node ID: {node['id']}")
            else:
                node_ids.add(node['id'])
                
            if 'type' not in node:
                issues.append(f"Node {i} missing type")
            elif not node['type'].startswith('n8n-nodes-'):
                issues.append(f"Node {i} has invalid type format: {node['type']}")
                
        # Validate connections reference existing nodes
        if 'connections' in workflow:
            for source_node, connections in workflow['connections'].items():
                if source_node not in node_ids:
                    issues.append(f"Connection references non-existent node: {source_node}")
                    
                if isinstance(connections, dict):
                    for target_list in connections.values():
                        if isinstance(target_list, list):
                            for target in target_list:
                                if isinstance(target, dict) and 'node' in target:
                                    if target['node'] not in node_ids:
                                        issues.append(f"Connection references non-existent target node: {target['node']}")
                                        
        return issues

    def analyze_workflow(self, workflow: Dict[str, Any], file_name: str):
        """Analyze a single workflow's structure"""
        if not workflow:
            return

        # Fix workflow conventions first
        workflow = self.fix_workflow_conventions(workflow)
        
        # Validate and collect issues
        issues = self.validate_workflow(workflow)
        if issues:
            self.error_files.append((file_name, f"Validation issues: {'; '.join(issues)}"))

        # Analyze nodes
        for node in workflow.get('nodes', []):
            node_type = node.get('type', '')
            node_name = node.get('name', '')
            
            # Track node types
            self.node_types[node_type] += 1
            
            # Track node parameters
            if 'parameters' in node:
                self.node_parameters[node_type].append(node['parameters'])

        # Analyze connections
        connections = workflow.get('connections', {})
        for source, targets in connections.items():
            if not isinstance(targets, dict):
                continue
            for target_list in targets.values():
                if not isinstance(target_list, list):
                    continue
                for target in target_list:
                    if isinstance(target, dict) and 'node' in target:
                        self.node_connections[source].append(target['node'])

        # Track workflow pattern
        pattern = self._extract_workflow_pattern(workflow)
        if pattern:
            self.workflow_patterns.append({
                'file': file_name,
                'pattern': pattern
            })

    def _extract_workflow_pattern(self, workflow: Dict[str, Any]) -> List[str]:
        """Extract the sequence of node types in the workflow"""
        try:
            nodes = {node['id']: node['type'] for node in workflow.get('nodes', [])}
            pattern = []
            
            # Find start nodes
            start_nodes = [node for node in workflow.get('nodes', []) 
                          if node.get('type') == 'n8n-nodes-base.start']
            
            for start in start_nodes:
                current = start['id']
                while current in workflow.get('connections', {}):
                    pattern.append(nodes.get(current, ''))
                    next_nodes = workflow['connections'][current].get('main', [[]])[0]
                    if not next_nodes:
                        break
                    current = next_nodes[0]['node']
            
            return pattern
        except Exception as e:
            logger.error(f"Error extracting workflow pattern: {str(e)}")
            return []

    def generate_syntax_manual(self) -> str:
        """Generate a comprehensive syntax manual"""
        manual = []
        
        # Section A: Node Types & Frequency
        manual.append("Section A: Node Types & Frequency")
        manual.append("-" * 40)
        for node_type, count in sorted(self.node_types.items(), key=lambda x: x[1], reverse=True):
            manual.append(f"- {node_type}: {count} uses")
        manual.append("\n")

        # Section B: Common Node Connections
        manual.append("Section B: Common Node Connections")
        manual.append("-" * 40)
        for source, targets in self.node_connections.items():
            manual.append(f"- {source} → {', '.join(targets)}")
        manual.append("\n")

        # Section C: Workflow Patterns
        manual.append("Section C: Common Workflow Patterns")
        manual.append("-" * 40)
        pattern_counts = defaultdict(int)
        for pattern in self.workflow_patterns:
            pattern_str = " → ".join(pattern['pattern'])
            pattern_counts[pattern_str] += 1
        
        for pattern, count in sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True):
            manual.append(f"- {pattern}: {count} occurrences")
        manual.append("\n")

        # Section D: Node Parameters
        manual.append("Section D: Node Parameter Patterns")
        manual.append("-" * 40)
        for node_type, params_list in self.node_parameters.items():
            if params_list:
                manual.append(f"\n{node_type}:")
                # Analyze common parameters
                param_keys = set()
                for params in params_list:
                    param_keys.update(params.keys())
                manual.append(f"  Common parameters: {', '.join(sorted(param_keys))}")

        # Section E: Error Report
        if self.error_files:
            manual.append("\nSection E: Files with Errors")
            manual.append("-" * 40)
            for file_path, error in self.error_files:
                manual.append(f"- {os.path.basename(file_path)}: {error}")

        return "\n".join(manual)

    def save_fixed_workflow(self, workflow: Dict[str, Any], file_path: str):
        """Save a fixed workflow back to file"""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(workflow, f, indent=2, ensure_ascii=False)
            logger.info(f"Fixed workflow saved: {file_path}")
        except Exception as e:
            logger.error(f"Error saving fixed workflow {file_path}: {str(e)}")

    def analyze_all_workflows(self, fix_files: bool = False):
        """Analyze all workflows in the directory"""
        workflow_files = self.find_workflow_files()
        logger.info(f"Found {len(workflow_files)} workflow files")

        for file_path in workflow_files:
            logger.info(f"Analyzing {file_path}")
            workflow = self.parse_workflow(file_path)
            
            # Fix workflow conventions
            fixed_workflow = self.fix_workflow_conventions(workflow.copy())
            
            # Validate and collect issues
            issues = self.validate_workflow(fixed_workflow)
            if issues:
                self.error_files.append((os.path.basename(file_path), f"Validation issues: {'; '.join(issues)}"))
            
            # Save fixed workflow if requested
            if fix_files and issues:
                self.save_fixed_workflow(fixed_workflow, file_path)
            
            self.analyze_workflow(fixed_workflow, os.path.basename(file_path))

        return self.generate_syntax_manual()

def main():
    # Update this to your actual workflow directory
    root_dir = "/Users/apple/n8n-automation-2025-AI-Agent-Suite-main"
    
    analyzer = N8nWorkflowAnalyzer(root_dir)
    
    # Ask user if they want to fix files
    fix_files = input("Fix workflow files with issues? (y/n): ").lower().startswith('y')
    
    syntax_manual = analyzer.analyze_all_workflows(fix_files=fix_files)
    
    # Save the syntax manual
    with open("n8n_syntax_manual.txt", "w", encoding="utf-8") as f:
        f.write(syntax_manual)
    
    logger.info("Syntax manual generated successfully!")
    logger.info(f"Found {len(analyzer.error_files)} files with issues")
    
    if fix_files:
        logger.info("Fixed files have been saved with proper n8n conventions")

if __name__ == "__main__":
    main()