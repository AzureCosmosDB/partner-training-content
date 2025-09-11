# Lab 1 - Setup and Deployment

## Prerequisites

- Laptop or workstation with **administrator rights**
- Azure subscription with **owner rights**
- Subscription access to Azure OpenAI service. Start here to [Request Access to Azure OpenAI Service](https://aka.ms/oaiapply). If you have access, see below for ensuring enough quota to deploy.

### Checking Azure OpenAI quota limits

For this sample to deploy successfully, there needs to be enough Azure OpenAI quota for the models used by this sample within your subscription. This sample deploys a new Azure OpenAI account with two models, **gpt-4o** with **30K tokens** per minute and **text-embedding-3-small** with **5k tokens** per minute. For more information on how to check your model quota and change it, see [Manage Azure OpenAI Service Quota](https://learn.microsoft.com/azure/ai-services/openai/how-to/quota)

### Azure Subscription Permission Requirements

This solution deploys a [user-assigned managed identity](https://learn.microsoft.com/entra/identity/managed-identities-azure-resources/overview) and defines then applies Azure Cosmos DB and Azure OpenAI RBAC permissions to this as well as your own Service Principal Id. You will need the following Azure RBAC roles assigned to your identity in your Azure subscription or [Subscription Owner](https://learn.microsoft.com/azure/role-based-access-control/built-in-roles/privileged#owner) access which will give you both of the following.

- [Managed Identity Contributor](https://learn.microsoft.com/azure/role-based-access-control/built-in-roles/identity#managed-identity-contributor)
- [Cosmos DB Operator](https://learn.microsoft.com/azure/role-based-access-control/built-in-roles/databases#cosmos-db-operator)
- [Cognitive Services OpenAI User](https://learn.microsoft.com/azure/role-based-access-control/built-in-roles/ai-machine-learning#cognitive-services-openai-user)

## Get Started - Setup your local environment

1. To run the workshop locally on your machine, install the following:

   - [Git](https://git-scm.com/downloads). If you don't have Git, download the ZIP file directly from the GitHub repository and unzip it to a local folder.
   - [Azure Developer CLI (azd)](https://aka.ms/install-azd)
   - [Python 3.12+](https://www.python.org/downloads/)
   - To build and run the frontend component, you need to install [Node.js](https://nodejs.org/en/download/) and [Angular CLI](https://angular.dev/installation#install-angular-cli)
   - (Optional) Any Python IDE or [VS Code](https://code.visualstudio.com/Download) with the [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

2. Clone the repository and navigate to the folder:

   ```bash
   git clone https://github.com/abhirockzz/banking-workshop/
   cd banking-workshop
   ```

## Deployment

1. Log in with your Azure credentials using Azure Developer CLI (`azd`):

   ```shell
   azd auth login
   ```

2. Deploy the Azure services using `azd up`:

   ```shell
   azd up
   ```

3. When prompted for the environment name, enter: `workshop`
4. Press Enter to select the subscription listed.
5. Press Enter to select the default region listed.


## Validation

Before you proceed, make sure all Azure resources are deployed successfully. Navigate to the Azure Cosmos DB account in the Azure portal to view the containers. You should see pre-seeded transactional data in the `OffersData`, `AccountsData`, and `Users` containers, as well as other containers `Chat`, `ChatHistory`, `Checkpoints`, and `Debug`.