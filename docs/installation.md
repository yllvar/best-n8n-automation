# Installation Guide

> Setting up n8n for the automation portfolio

## 🚀 Quick Installation

### Option 1: Docker (Recommended)
```bash
# Create n8n directory
mkdir n8n && cd n8n

# Start n8n with Docker
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

### Option 2: npm
```bash
# Install globally
npm install n8n -g

# Start n8n
n8n start
```

### Option 3: n8n Cloud
1. Visit [n8n.cloud](https://n8n.cloud/)
2. Sign up for an account
3. Choose your plan (free tier available)

## 🔧 Initial Configuration

### 1. Access n8n
- Open `http://localhost:5678` in your browser
- Create your admin account
- Set up two-factor authentication (recommended)

### 2. Configure Credentials
Go to **Settings > Credentials** to add:
- **OpenAI API Key** (for AI workflows)
- **Google Cloud credentials** (for Workspace integrations)
- **Database credentials** (PostgreSQL, MongoDB, etc.)
- **Messaging platform tokens** (Telegram, WhatsApp, etc.)

### 3. Environment Variables
Create a `.env` file in your n8n directory:
```bash
# Copy the example file
cp .env.example .env

# Edit with your credentials
nano .env
```

## 📋 System Requirements

### Minimum Requirements
- **RAM:** 2GB (4GB recommended for AI workflows)
- **Storage:** 10GB free space
- **CPU:** 2 cores (4 cores recommended)
- **Network:** Stable internet connection for API calls

### Recommended Setup
- **RAM:** 8GB+ (for multiple concurrent workflows)
- **Storage:** 50GB+ SSD
- **CPU:** 4+ cores
- **Docker:** Latest version
- **Node.js:** v18+ (if not using Docker)

## 🔒 Security Setup

### 1. Secure Credentials
- Use n8n's built-in credential manager
- Never hardcode API keys in workflows
- Rotate keys regularly

### 2. Network Security
- Use HTTPS in production
- Configure firewall rules
- Set up VPN if accessing remotely

### 3. Data Protection
- Enable workflow encryption
- Set up regular backups
- Use environment variables for sensitive data

## 🚀 Next Steps

1. **Test basic workflow** - Import a simple workflow to verify setup
2. **Configure credentials** - Add API keys for services you'll use
3. **Explore workflows** - Browse the [WORKFLOWS.md](../WORKFLOWS.md) index
4. **Start automating** - Import your first production workflow

## 🆘 Troubleshooting

### Common Issues

**n8n won't start**
```bash
# Check Docker logs
docker logs n8n

# Check port availability
lsof -i :5678
```

**Workflow execution fails**
- Verify API credentials
- Check network connectivity
- Review workflow error logs

**Performance issues**
- Increase allocated RAM
- Check workflow complexity
- Monitor resource usage

### Getting Help
- [n8n Documentation](https://docs.n8n.io/)
- [n8n Community](https://community.n8n.io/)
- [GitHub Issues](https://github.com/n8n-io/n8n/issues)

---

## 📚 Additional Resources

- [n8n Official Documentation](https://docs.n8n.io/)
- [n8n YouTube Channel](https://www.youtube.com/c/n8nio)
- [n8n Community Discord](https://discord.gg/xpS9QK4KZv)
- [Workflow Examples](https://n8n.io/workflows/)
