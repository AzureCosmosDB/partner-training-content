# Challenge 01 - Environment Setup & First Steps - Coach's Guide

**[< Previous Challenge](./Solution-00.md)** - **[Home](../../README.md)** - **[Next Challenge >](./Solution-02.md)**

## Solution Overview

This challenge deploys the complete banking application infrastructure using Azure Developer CLI. The deployment creates Azure Cosmos DB, Azure OpenAI, and supporting services with proper security configurations.

## Expected Deployment Components

### Azure Resources Created
1. **Azure Cosmos DB Account**
   - SQL API with multiple containers
   - Global distribution (single region initially)
   - Configured with proper indexing policies

2. **Azure OpenAI Service**
   - GPT-4o model deployment (30K TPM)
   - text-embedding-3-small model deployment (5K TPM)

3. **User-Assigned Managed Identity**
   - Cosmos DB Data Contributor role
   - Cognitive Services OpenAI User role

4. **Supporting Infrastructure**
   - Resource group
   - Application Insights (if configured)
   - Storage account (for application logs)

### Cosmos DB Containers Created
- `OffersData` - Banking product offers with vector embeddings
- `AccountsData` - Customer account information
- `Users` - Customer profile data
- `Chat` - Real-time chat messages
- `ChatHistory` - Conversation history
- `Checkpoints` - Application state management
- `Debug` - Debugging and diagnostic information

## Detailed Solution Steps

### Step 1: Initial Setup Verification
```bash
# Verify authentication
azd auth login
az login

# Verify subscription access
az account list
az account show
```

### Step 2: Clone and Navigate to Application
```bash
# If not already done in Challenge 00
git clone https://github.com/abhirockzz/banking-workshop/
cd banking-workshop
```

### Step 3: Deploy Infrastructure
```bash
# Initialize and deploy
azd up

# When prompted:
# Environment name: workshop (or team-specific name)
# Subscription: Select the appropriate subscription
# Region: Select closest region with OpenAI availability
```

### Step 4: Deployment Validation
```bash
# List created resources
az resource list --resource-group <resource-group-name> --output table

# Check Cosmos DB account
az cosmosdb list --output table

# Check OpenAI deployment
az cognitiveservices account deployment list --name <openai-account-name> --resource-group <resource-group-name>
```

## Common Issues and Solutions

### 1. Azure OpenAI Quota Exceeded
**Symptoms:** Deployment fails with quota errors
**Solutions:**
- Check current quota usage: Portal > Cognitive Services > Quotas
- Request quota increase (may take time)
- Consider reducing model capacity in deployment
- Share OpenAI resources across teams

### 2. Insufficient Permissions
**Symptoms:** RBAC assignment failures
**Solutions:**
- Verify user has Owner or User Access Administrator role
- Check subscription-level permissions
- Try deploying to a resource group where user has appropriate access

### 3. Resource Naming Conflicts
**Symptoms:** Resources with duplicate names
**Solutions:**
- Use unique environment names per team
- Add team identifier to environment name
- Delete existing resources if redeploying

### 4. Region Availability Issues
**Symptoms:** Services not available in selected region
**Solutions:**
- Choose regions with both Cosmos DB and OpenAI availability
- Consider: East US, West Europe, Southeast Asia
- Check Azure service availability by region

## Coaching Points

### During Deployment (10-15 minutes)
- Explain what each service does while deployment runs
- Show the Azure portal and navigate to created resources
- Discuss the benefits of Infrastructure as Code (IaC)
- Explain managed identity and RBAC concepts

### Post-Deployment Verification
1. **Azure Portal Navigation**
   - Show participants how to find their resource group
   - Navigate to Cosmos DB Data Explorer
   - Explore container structure and sample data

2. **Cost Monitoring Setup**
   - Show Cost Management + Billing
   - Set up spending alerts if not already configured
   - Explain RU consumption concepts

3. **Security Review**
   - Show managed identity in the portal
   - Review RBAC assignments
   - Explain network access configurations

## Validation Checklist

### Resources Created ✓
- [ ] Resource group exists
- [ ] Cosmos DB account is running
- [ ] OpenAI service is deployed
- [ ] Managed identity is created
- [ ] RBAC roles are assigned

### Cosmos DB Validation ✓
- [ ] Database contains expected containers
- [ ] Sample data is loaded in containers
- [ ] Can query data using Data Explorer
- [ ] Throughput is configured appropriately

### OpenAI Validation ✓
- [ ] Model deployments are successful
- [ ] Models show \"Running\" status
- [ ] Quota consumption is within limits

## Troubleshooting Commands

```bash
# Check deployment status
azd env list
azd env show

# View deployment logs
azd deploy --debug

# Check resource group contents
az group show --name <resource-group-name>
az resource list --resource-group <resource-group-name>

# Cosmos DB specific checks
az cosmosdb show --name <cosmosdb-name> --resource-group <resource-group-name>
az cosmosdb sql database list --account-name <cosmosdb-name> --resource-group <resource-group-name>

# OpenAI specific checks
az cognitiveservices account show --name <openai-name> --resource-group <resource-group-name>
```

## Time Management

- **Expected Duration:** 45-60 minutes
- **Deployment Time:** 10-15 minutes
- **Validation Time:** 15-20 minutes
- **Troubleshooting Buffer:** 10-20 minutes

## Advanced Coaching Topics (if time permits)

### Infrastructure as Code Discussion
- Explain the benefits of azd and Bicep templates
- Show how to customize deployments
- Discuss version control for infrastructure

### Security Deep Dive
- Explain managed identity vs service principals
- Discuss network isolation options
- Review encryption at rest and in transit

### Cost Optimization Preview
- Show current cost estimates in portal
- Explain autoscale vs manual throughput
- Discuss spending alerts and budgets

## Success Criteria Validation

A team has successfully completed this challenge when:
1. ✅ All Azure resources are deployed and running
2. ✅ Cosmos DB contains all expected containers with sample data
3. ✅ OpenAI models are successfully deployed and accessible
4. ✅ Team can navigate Azure portal and find their resources
5. ✅ Basic queries work in Cosmos DB Data Explorer
6. ✅ No deployment errors or warnings remain

## Preparation for Next Challenge

Before moving to Challenge 02:
- Ensure teams understand their resource group structure
- Verify they can access Cosmos DB Data Explorer
- Confirm they understand basic RU consumption concepts
- Make sure they know how to monitor costs