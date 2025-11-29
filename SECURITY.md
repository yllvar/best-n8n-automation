# Security Policy

> Best practices for secure automation with n8n workflows

## 🔒 Security Overview

This repository contains automation workflows that integrate with various third-party services and APIs. Following security best practices is essential to protect your data, credentials, and systems.

## 🛡️ Security Principles

### 1. Never Hardcode Credentials

**❌ Wrong:**
```json
{
  "parameters": {
    "apiKey": "sk-1234567890abcdef"
  }
}
```

**✅ Right:**
Use n8n's built-in credential manager for all API keys, tokens, and secrets.

### 2. Use Environment Variables

Store sensitive configuration in environment variables, not in workflow files.

```bash
# .env file (never commit to Git)
OPENAI_API_KEY=your_actual_key_here
```

### 3. Principle of Least Privilege

Grant only the minimum permissions necessary:
- Use read-only API keys when possible
- Limit access to specific resources
- Create dedicated service accounts for automation

### 4. Validate All Inputs

Sanitize and validate data from external sources:
- Check data types and formats
- Validate file uploads
- Filter malicious content
- Set reasonable size limits

## 🔐 Credential Management

### n8n Credential Manager

**Best Practices:**
- Use n8n's built-in credential storage
- Enable credential encryption
- Set up credential access controls
- Rotate credentials regularly

**Setup:**
1. Go to **Settings > Credentials**
2. Create credentials for each service
3. Use descriptive names
4. Enable two-factor authentication

### Environment Variables

**Required Variables:**
```bash
# Core security
N8N_JWT_SECRET=your_strong_random_secret
N8N_ENCRYPTION_KEY=your_encryption_key

# API Keys (never commit these)
OPENAI_API_KEY=your_openai_key
GOOGLE_AI_API_KEY=your_google_key
# ... other API keys
```

**Generating Secrets:**
```bash
# Generate JWT secret
openssl rand -base64 32

# Generate encryption key
openssl rand -hex 32
```

## 🌐 Network Security

### HTTPS Configuration

**Production Setup:**
```bash
# Enable HTTPS
N8N_PROTOCOL=https
N8N_HOST=your-domain.com
N8N_PORT=443

# SSL Certificate
SSL_CERT_PATH=/path/to/cert.pem
SSL_KEY_PATH=/path/to/key.pem
```

### Firewall Rules

**Recommended Ports:**
- `5678` - n8n web interface (restrict access)
- `443` - HTTPS (public)
- `22` - SSH (admin access only)

### VPN Access

For remote access:
- Use VPN instead of exposing to internet
- Implement IP whitelisting
- Set up reverse proxy with authentication

## 🔍 Data Protection

### Sensitive Data Handling

**Guidelines:**
- Encrypt sensitive data at rest
- Use TLS for data in transit
- Implement data retention policies
- Regular data backups

**Data Classification:**
- **Public**: Non-sensitive workflow metadata
- **Internal**: Business process data
- **Confidential**: API keys, credentials
- **Restricted**: Personal data, financial info

### Workflow Data

**Best Practices:**
- Don't store sensitive data in workflow files
- Use external databases for data storage
- Implement data purging mechanisms
- Log access to sensitive operations

## 🚨 Common Security Risks

### 1. Exposed API Keys

**Risk:** API keys in workflow files or commits
**Prevention:**
- Use `.gitignore` for `.env` files
- Scan repository for secrets
- Use pre-commit hooks

### 2. Insecure Webhooks

**Risk:** Unauthenticated webhook endpoints
**Prevention:**
- Validate webhook signatures
- Use secret tokens
- Implement rate limiting

### 3. Overprivileged Accounts

**Risk:** Service accounts with excessive permissions
**Prevention:**
- Create dedicated automation accounts
- Grant minimum required permissions
- Regular permission audits

### 4. Data Leakage

**Risk:** Sensitive data in logs or outputs
**Prevention:**
- Filter sensitive data from logs
- Use data masking
- Implement secure logging practices

## 🔧 Security Configuration

### n8n Security Settings

**Recommended Configuration:**
```bash
# Authentication
N8N_AUTH=jwt
N8N_JWT_AUTH_HEADER=authorization
N8N_JWT_AUTH_HEADER_VALUE_PREFIX=Bearer

# Encryption
N8N_ENCRYPTION_KEY=your_encryption_key
N8N_USER_MANAGEMENT_DISABLED=false

# Security Headers
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=secure_password
```

### Docker Security

**Secure Docker Setup:**
```bash
# Run as non-root user
docker run -u 1000:1000 n8nio/n8n

# Read-only filesystem
docker run --read-only --tmpfs /tmp n8nio/n8n

# Resource limits
docker run --memory=2g --cpus=2 n8nio/n8n
```

## 📋 Security Checklist

### Before Deployment

- [ ] No hardcoded credentials in workflows
- [ ] Environment variables configured
- [ ] HTTPS enabled
- [ ] Firewall rules configured
- [ ] Backup strategy implemented
- [ ] Access controls configured
- [ ] Logging and monitoring enabled

### Ongoing Maintenance

- [ ] Regular credential rotation
- [ ] Security updates applied
- [ ] Access logs reviewed
- [ ] Permission audits performed
- [ ] Backup restoration tested
- [ ] Security scan results reviewed

## 🚨 Incident Response

### Security Incident Process

1. **Detection**
   - Monitor for unusual activity
   - Review access logs
   - Check for data breaches

2. **Containment**
   - Isolate affected systems
   - Revoke compromised credentials
   - Block suspicious IPs

3. **Investigation**
   - Analyze logs and data
   - Identify root cause
   - Document findings

4. **Recovery**
   - Restore from clean backups
   - Update security measures
   - Monitor for recurrence

5. **Reporting**
   - Document incident
   - Notify stakeholders
   - Update security policies

## 📞 Reporting Security Issues

### Vulnerability Disclosure

**Found a security issue? Please report it privately:**

1. **Email**: security@domain.com
2. **Encrypted**: Use PGP key if available
3. **Timeline**: Response within 48 hours

**What to Include:**
- Detailed description of the issue
- Steps to reproduce
- Potential impact assessment
- Any screenshots or logs

### Security Policy

- **No public disclosure** until fixed
- **Credit given** for responsible disclosure
- **Coordination** for disclosure timeline
- **Reward program** for critical issues

## 📚 Additional Resources

### Security Tools

- **n8n Security**: [Security documentation](https://docs.n8n.io/security/)
- **OWASP**: [Web security guidelines](https://owasp.org/)
- **Snyk**: [Dependency vulnerability scanner](https://snyk.io/)
- **GitGuardian**: [Secret detection in Git](https://www.gitguardian.com/)

### Best Practices

- [12-Factor App Security](https://12factor.net/security_process)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [CIS Controls](https://www.cisecurity.org/controls/)

---

## 🎯 Security Commitment

Security is an ongoing process. We regularly:
- Review and update security practices
- Audit workflows for vulnerabilities
- Monitor for security threats
- Update dependencies promptly

**Stay secure, automate safely!** 🔒
