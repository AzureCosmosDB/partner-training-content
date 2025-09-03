import json
import os
from pathlib import Path
from azure.cosmos import CosmosClient
from azure.cosmos import PartitionKey
from azure.identity import DefaultAzureCredential
from typing import Any, Dict, List

def main():
    """
    Main function to load banking data into Cosmos DB containers.
    """
    # Get Cosmos DB endpoint from environment variable
    cosmos_endpoint = os.getenv("COSMOSDB_ENDPOINT")
    if not cosmos_endpoint:
        raise ValueError("COSMOSDB_ENDPOINT environment variable is not set.")
    
    # Initialize Azure credential
    credential = DefaultAzureCredential()
    
    # Create Cosmos DB client
    cosmos_client = CosmosClient(
        url=cosmos_endpoint,
        credential=credential
    )
    
    try:
        # Get database and containers
        database = cosmos_client.get_database_client("MultiAgentBanking")
        users_container = database.get_container_client("Users")
        offers_container = database.get_container_client("OffersData")
        accounts_container = database.get_container_client("AccountsData")
        
        # Get the directory where this script is located
        script_dir = Path(__file__).parent
        
        # Define file paths
        accounts_data_path = script_dir / "AccountsData.json"
        offers_data_path = script_dir / "OffersData.json"
        user_data_path = script_dir / "UserData.json"
        
        # Load and insert accounts data
        print("Loading accounts data...")
        load_accounts_data(accounts_container, accounts_data_path)
        
        # Load and insert offers data
        print("Loading offers data...")
        load_offers_data(offers_container, offers_data_path)
        
        # Load and insert user data
        print("Loading user data...")
        load_user_data(users_container, user_data_path)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise
        
    print("Data loading complete.")

def load_accounts_data(container, file_path: Path):
    """
    Load accounts data with hierarchical partition key (tenantId + accountId).
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        items = json.load(file)
    
    # Create items with hierarchical partition key
    for item in items:
        try:
            container.upsert_item(
                body=item
            )
            print(f"Successfully inserted item: {item.get('id', 'Unknown')}")
        except Exception as e:
            print(f"Error inserting item {item.get('id', 'Unknown')}: {str(e)}")

def load_offers_data(container, file_path: Path):
    """
    Load offers data with single partition key (tenantId).
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        items = json.load(file)
    
    # Create items with tenantId as partition key
    for item in items:
        try:
            container.upsert_item(
                body=item
            )
            print(f"Successfully inserted item: {item.get('id', 'Unknown')}")
        except Exception as e:
            print(f"Error inserting item {item.get('id', 'Unknown')}: {str(e)}")

def load_user_data(container, file_path: Path):
    """
    Load user data with single partition key (tenantId).
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        items = json.load(file)
    
    # Create items with tenantId as partition key
    for item in items:
        try:
            container.upsert_item(
                body=item
            )
            print(f"Successfully inserted item: {item.get('id', 'Unknown')}")
        except Exception as e:
            print(f"Error inserting item {item.get('id', 'Unknown')}: {str(e)}")

if __name__ == "__main__":
    main()