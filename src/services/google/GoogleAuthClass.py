# This code is a modified version of Google's Calendar API
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class GoogleAuth:
  
  creds = None
  tokenPath = "./token.json"
  credentialsPath = None
  service = None

  # If modifying these scopes, delete the file token.json.
  SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

  def __init__(self):
    self.creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(self.tokenPath):
      self.creds = Credentials.from_authorized_user_file(self.tokenPath, self.SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not self.creds or not self.creds.valid:
      if self.creds and self.creds.expired and self.creds.refresh_token:
        self.creds.refresh(Request())
        print("Credentials refreshed from " + str(self.tokenPath) + ".")
      else:
        print("Please provide a credentials.json file. Follow these instructions \
              [https://developers.google.com/calendar/api/quickstart/python#authorize_credentials_for_a_desktop_application] \
              to obtain a credentials file to allow this script to access your Google Calendar.")
        self.credentialsPath = input("Please input path to credentials.json:  ")
        if os.path.exists(self.credentialsPath):
          print("credentialsPath is [" + str(self.credentialsPath) + "]")
        else:
          print("FATAL: Please provide a valid path. The path provided [" + str(self.credentialsPath) + "] is not valid!")
          quit(1)

        flow = InstalledAppFlow.from_client_secrets_file(
            self.credentialsPath, self.SCOPES
        )
        self.creds = flow.run_local_server(port=0)
        print("Running local server to access Google Calendar...")

      # Save the credentials for the next run
      with open(self.tokenPath, "w") as token:
        token.write(self.creds.to_json())

    try:
      self.service = build("calendar", "v3", credentials=self.creds)
    except HttpError as error:
      print(f"An error occurred: {error}")

    print("Google Auth initalized")