
# Azure AI Foundry Agent w/ Azure AI Search 

This sample demonstrates how to integrate an agent created in Azure AI Foundry with Azure AI Search.

### ⚙️ Prerequisites

To run this sample, you need to deploy an Azure AI Foundry project and agent, and configure Azure AI Search as a knowledge source.

### 🔐 Role-based access control in Azure AI Foundry portal

- Azure AI Foundry does not support `DefaultAzureCredential`. To access an Azure AI Foundry project, assign the Azure AI User role to the user or service: [RBAC](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-azure-ai-foundry)

### 📚 Learn more 

- [Azure AI Foundry Workshop](https://workshop.aifoundry.app/workshop/) [git](https://github.com/Azure/ai-foundry-workshop)
    - [Agent - AI Search](https://workshop.aifoundry.app/2-notebooks/2-agent_service/5-agents-aisearch/): `DO NOT USE.' The samples are using deprecated objects.
    - [Build your code-first agent with Azure AI Foundry](https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/)
    - [Azure AI Foundry Agents Samples](https://github.com/Azure-Samples/ai-foundry-agents-samples)
    - [Azure AI Projects client library for Python](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-projects/samples): Official Samples