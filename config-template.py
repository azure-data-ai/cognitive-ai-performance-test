import os

class DefaultConfig:
    """ Bot Configuration """
    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")

    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "")


    ## Speech SDK API config - Uncomment below code and update your key and region. (Provided values are dummy)
    # speech_key, service_region = "46c52f13e736ehd6yedyh433xxyyz031", "southeastasia"
    
    ## qna maker config - Uncomment below code and update your Endpoint and URL (Provided values are dummy)
    # url = "https://myqnamaker.azurewebsites.net/qnamaker/knowledgebases/4xxyy200-f23e-xxxx-a66c-5521xx95deff/generateAnswer"
    # EndpointKey = 'EndpointKey 2ayyyyyy4-44a8-4fcdx-b37c-1fbxxxxxx4d8a'