import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

YOUR_API_KEY= os.getenv("API_KEY")

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = YOUR_API_KEY

youtube = build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)

def comment_threads(vid, to_csv=False):

    request = youtube.commentThreads().list(
        part="id,snippet",
        videoId=vid
    )
    response = request.execute()
    print(response)




def main():
    comment_threads('XTjtPc0uiG8')
 
   # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"



if __name__ == "__main__":
    main()