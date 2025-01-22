import os
from dotenv import load_dotenv

# Load all ENV variables
load_dotenv()

# Application (client) ID of app registration
CLIENT_ID = os.getenv("CLIENT_ID")
# Application's generated client secret: never check this into source control!
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Pinecone Creds
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Open AI Creds
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
AUTHORITY = f"https://login.microsoftonline.com/{os.getenv('TENANT_ID', 'common')}"

REDIRECT_PATH = "/getAToken"  # Used for forming an absolute URL to your redirect URI.
# The absolute URL must match the redirect URI you set
# in the app's registration in the Azure portal.

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
# ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent
ENDPOINT = 'https://graph.microsoft.com/v1.0/me/messages?$filter=isRead eq false'  # This resource requires no admin consent
GRAPH_API_URL = "https://graph.microsoft.com/v1.0"

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All", "Mail.Read", "Mail.Send"]

# Tells the Flask-session extension to store sessions in the filesystem
SESSION_TYPE = "filesystem"
# Using the file system will not work in most production systems,
# it's better to use a database-backed session store instead.
