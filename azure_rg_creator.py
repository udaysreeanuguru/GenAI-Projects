"""
azure_rg_creator.py

Simple script to create an Azure Resource Group using Azure Python SDK.

Requirements:
    pip install azure-mgmt-resource azure-identity

Environment:
    - AZURE_CLIENT_ID
    - AZURE_CLIENT_SECRET
    - AZURE_TENANT_ID
    - AZURE_SUBSCRIPTION_ID
-TESTing 1234

"""
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
import os

def create_resource_group(resource_group_name, location):
    """
    Create an Azure Resource Group.
    """
    credential = DefaultAzureCredential()
    subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
    resource_client = ResourceManagementClient(credential, subscription_id)

    rg_params = {"location": location}

    result = resource_client.resource_groups.create_or_update(
        resource_group_name,
        rg_params
    )

    print(f"Provisioned resource group {result.name} in {result.location}")

if __name__ == "__main__":
    create_resource_group("genai-rg", "eastus")