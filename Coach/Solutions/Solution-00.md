# Challenge 00 - Prerequisites - Coach's Guide

**[Home](../../README.md)** - **[Next Challenge >](./Solution-00a.md)**

## Solution Overview

This challenge ensures all participants have the necessary tools, permissions, and access to complete the subsequent challenges successfully. As a coach, you should verify that each team has completed all prerequisites before moving to Challenge 01.

## Prerequisites Validation Checklist

### Development Environment
- [ ] Each participant has a laptop/workstation with administrator rights
- [ ] All required development tools are installed and functional
- [ ] Azure CLI or Azure PowerShell is configured and authenticated

### Azure Access
- [ ] Azure subscription with Owner-level permissions (required for creating managed identities and RBAC assignments)
- [ ] Azure OpenAI service access approved (can take several days - plan ahead)
- [ ] Sufficient Azure OpenAI quota available

### Common Issues and Solutions

#### 1. Azure OpenAI Access
**Problem:** Participants don't have Azure OpenAI access
**Solutions:**
- Request access at https://aka.ms/oaiapply (can take 1-2 business days)
- For training events, consider providing shared Azure OpenAI resources
- Have backup subscriptions with pre-approved access

#### 2. Azure OpenAI Quota
**Problem:** Insufficient quota for required models
**Solutions:**
- Check quota limits at: Azure Portal > Cognitive Services > Quotas
- Request quota increases if needed (can take time)
- Share resources across teams if necessary
- Consider using lower-throughput models for training

#### 3. Azure Subscription Permissions
**Problem:** Participants don't have Owner rights
**Solutions:**
- Ensure subscription owners grant proper permissions before the event
- Consider providing dedicated training subscriptions
- Use resource groups with Contributor + User Access Administrator roles as alternative

#### 4. Tool Installation Issues
**Problem:** Participants can't install required tools
**Solutions:**
- Provide pre-configured Azure DevBox or GitHub Codespaces environments
- Share portable/zip versions of tools where possible
- Have technical support available for installation issues

## Validation Commands

Have participants run these commands to verify their setup:

```bash
# Verify Azure CLI installation and authentication
az --version
az login
az account list

# Verify Azure Developer CLI
azd version

# Verify Python installation
python --version
pip --version

# Verify Node.js and npm
node --version
npm --version

# Verify Angular CLI
ng version

# Verify Git
git --version
```

## Pre-Event Preparation for Coaches

### 1. Azure Resources Preparation (1-2 weeks before)
- Create test Azure subscriptions if needed
- Request Azure OpenAI access for all subscriptions
- Verify quota limits for required models
- Test the complete deployment process

### 2. Environment Testing (1 week before)
- Deploy the banking application end-to-end
- Test all challenges and verify success criteria
- Document any environment-specific issues
- Prepare troubleshooting guides

### 3. Resource Sharing Strategy (if needed)
- Decide on resource sharing approach for Azure OpenAI
- Prepare shared connection strings/endpoints
- Create separate resource groups for each team
- Plan resource cleanup procedures

## During the Challenge

### Team Readiness Assessment
For each team, verify:
1. **Tools Test:** Can run all validation commands successfully
2. **Azure Access:** Can create resources in their subscription  
3. **OpenAI Access:** Can access Azure OpenAI or shared resources
4. **File Access:** Have extracted and can access Resources.zip

### Time Management
- Allow 30-45 minutes for this challenge
- Some teams may need additional time for tool installation
- Be prepared to help with permission issues
- Don't let teams get stuck too long on prerequisites

### Common Coaching Points
- Emphasize that these tools will be used throughout all challenges
- Explain the importance of proper Azure permissions for the hack
- Show how to check Azure OpenAI quota and usage
- Demonstrate basic Azure CLI commands for resource management

## Success Validation

A team has successfully completed this challenge when:
- All team members can run the validation commands without errors
- They can create and list Azure resources using Azure CLI
- They have access to Azure OpenAI services (direct or shared)
- They have extracted and can access the Resources.zip file
- They understand the importance of monitoring Azure costs during the hack

## Troubleshooting Guide

### Azure CLI Issues
```bash
# If login issues occur
az logout
az login --use-device-code

# If subscription access issues
az account set --subscription \"subscription-name\"
az account show
```

### Azure Developer CLI Issues
```bash
# If authentication issues
azd auth logout
azd auth login

# Verify authentication
azd auth login --check-status
```

### Azure OpenAI Quota Issues
- Direct participants to: Portal > Cognitive Services > Quotas
- Show how to request quota increases
- Explain the difference between quota and usage
- Monitor total quota consumption across all teams

## Additional Resources for Coaches

- [Azure OpenAI Service Quotas](https://learn.microsoft.com/azure/ai-services/openai/quotas-limits)
- [Azure Developer CLI Troubleshooting](https://learn.microsoft.com/azure/developer/azure-developer-cli/troubleshoot)
- [Azure RBAC Best Practices](https://learn.microsoft.com/azure/role-based-access-control/best-practices)