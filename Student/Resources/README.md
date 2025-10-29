# Student Resources

This directory contains all the resources needed to complete the Azure Cosmos DB for AI & Modern Applications challenges.

## Directory Structure

### banking-workshop/
Complete banking application used in Challenge 01 and Challenge 03:
- **backend/** - Python API service with multi-agent architecture
- **frontend/** - Angular web application for chat interface
- **infra/** - Azure infrastructure as code (Bicep templates)
- **azure.yaml** - Azure Developer CLI configuration
- **lab1.md** - Original deployment instructions (for reference)
- **lab3.md** - Original application guide (for reference)

### Challenge02/
Sample data files for the data modeling challenge:
- **customers.json** - Customer and sales order sample data
- **products.json** - Product catalog sample data  
- **categories-and-tags.json** - Product categories and tags data

## Usage Instructions

### For Challenge 01 (Environment Setup)
1. Extract this entire directory to your local machine
2. Navigate to the `banking-workshop/` folder
3. Follow the instructions in Challenge 01 to deploy the infrastructure

### For Challenge 02 (Data Modeling)
1. Use the JSON files in `Challenge02/` as sample data
2. Create containers in Azure Cosmos DB Data Explorer
3. Import the sample data using the portal or SDK
4. Run the experiments outlined in the challenge

### For Challenge 03 (AI-Powered Search)
1. Use the deployed banking application from Challenge 01
2. Start the backend and frontend services as described in the challenge
3. Test the multi-agent conversation capabilities
4. Explore the vector search functionality

### For Challenge 04 (Security & Cost Optimization)
1. Continue working with your existing Cosmos DB resources
2. Apply security configurations and cost optimizations
3. Monitor performance and cost implications

## Important Notes

- **Cost Management:** Monitor your Azure spending during the hack. The resources created can incur costs.
- **Resource Cleanup:** Delete resources after completing the challenges to avoid ongoing charges.
- **Shared Resources:** If using shared Azure OpenAI resources, coordinate with your coach and other teams.
- **Support:** Contact your coach if you encounter issues with any of the provided resources.

## File Formats

- **.json** - Data files that can be imported into Cosmos DB
- **.md** - Markdown documentation files
- **.yaml/.yml** - Configuration files for Azure Developer CLI
- **.py** - Python source code files
- **.ts** - TypeScript source code files

## Prerequisites

Before using these resources, ensure you have completed Challenge 00 and have:
- Azure Developer CLI (azd) installed
- Python 3.12+ installed
- Node.js and Angular CLI installed
- Git installed
- Azure subscription access
- Azure OpenAI service access