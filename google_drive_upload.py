from apiclient import discovery, errors
from googleapiclient.http import MediaFileUpload, MediaInMemoryUpload
from httplib2 import Http
from oauth2client import client, file, tools

# define path variables
credentials_file_path = '../credentials/credentials.json'
clientsecret_file_path = '../credentials/client_secret.json'

# define API scope
SCOPE = 'https://www.googleapis.com/auth/drive'

# define store
store = file.Storage(credentials_file_path)


def drive_upload(file, name):
    credentials = store.get()
    # get access token
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(clientsecret_file_path, SCOPE)
        credentials = tools.run_flow(flow, store)
    # define API service
    http = credentials.authorize(Http())
    drive = discovery.build('drive', 'v3', http=http)
    file_metadata = {'name': name}
    media = MediaInMemoryUpload(file, mimetype='image/jpeg', resumable=True)
    uploaded_file = drive.files().create(body=file_metadata,
                                         media_body=media,
                                         fields='id').execute()
    # print('File ID: %s' % uploaded_file.get('id'))

