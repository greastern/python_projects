import os
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Load environment variables
load_dotenv()

# Get configuration from environment variables
SCOPES = [os.getenv('GOOGLE_SHEETS_SCOPE')]
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), os.getenv('GOOGLE_SERVICE_ACCOUNT_FILE'))
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
SHEET_NAME = os.getenv('SHEET_NAME')

# Set up credentials
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build the Sheets API
service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()

