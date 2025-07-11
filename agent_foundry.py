import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.agents.models import ListSortOrder
from azure.ai.projects.models import ConnectionType
from dotenv import load_dotenv

load_dotenv()

PROJECT_ENDPOINT = os.getenv("PROJECT_ENDPOINT")
AGENT_ID = os.getenv("AGENT_ID")
MODEL_DEPLOYMENT_NAME = os.getenv("MODEL_DEPLOYMENT_NAME")


def init_project_client():
    project_client, conn_id = None, None
    try:
        project_client = AIProjectClient(
            endpoint=PROJECT_ENDPOINT,
            credential=DefaultAzureCredential(),
        )
        all_connections = project_client.connections.list()
        for c in all_connections:
            if c.type == ConnectionType.AZURE_AI_SEARCH:
                conn_id = c.id
                print(f"Found existing Azure AI Search connection: {conn_id}")
                break
        print("✅ Successfully initialized AIProjectClient")
    except Exception as e:
        print(f"❌ Error initializing project client: {e}")

    if not project_client or not conn_id:
        print(
            "❗️ Could not find an Azure AI Search connection. Please create one in the Azure AI Foundry portal."
        )
        print("Exiting...")
        exit(1)

    return project_client, conn_id


def get_agent_with_search(project_client):
    if project_client:
        agent = project_client.agents.get_agent(AGENT_ID)
        return agent


def run_agent_query(project_client, agent, thread, question):
    # Create a user message
    message = project_client.agents.messages.create(
        thread_id=thread.id, role="user", content=question
    )
    print(f"💬 Created user message, ID: {message.id}")

    # Create and process agent run
    run = project_client.agents.runs.create_and_process(
        thread_id=thread.id, agent_id=agent.id
    )
    print(f"🤖 Agent run status: {run.status}")

    if run.last_error:
        print("⚠️ Run error:", run.last_error)

    # Retrieve all messages in the thread
    messages = project_client.agents.messages.list(
        thread_id=thread.id, order=ListSortOrder.ASCENDING
    )
    # Print the assistant's last reply
    for message in messages:
        if message.text_messages:
            print(f"{message.role}: {message.text_messages[-1].text.value}")


def delete_agent(project_client, agent_id):
    try:
        project_client.agents.delete_agent(agent_id)
        print(f"🗑️ Deleted agent with ID: {agent_id}")
    except Exception as e:
        print(f"❌ Error deleting agent: {e}")


if __name__ == "__main__":
    project_client, conn_id = init_project_client()
    agent = get_agent_with_search(project_client)

    if agent:
        thread = project_client.agents.threads.create()
        print(f"📝 Created thread, ID: {thread.id}")

        while True:
            q = input("You: ")
            if q.lower() in ("exit", "quit"):
                break
            run_agent_query(project_client, agent, thread, q)
