import requests
import json
import os

#Got help from chatGPT on this part 

google_api_key = os.environ.get('GOOGLE_API_KEY')


def classifyImage(imageUrl: str):
    url = "https://vision.googleapis.com/v1/images:annotate?key={}".format(google_api_key)

    payload = {
    "requests": [
        {
        "image": {
            "source": {
            "imageUri": imageUrl
            }
        },
        "features": [
            {
            "type": "LABEL_DETECTION",
            "maxResults": 5
            }
        ]
        }
    ]
    }

    # Send the API request
    response = requests.post(url, json=payload)

    # Parse the response JSON
    result = json.loads(response.text)
    
    classificationData = []
    for label in result["responses"][0]["labelAnnotations"]:
      #  print(label["description"], label["score"])
        classificationData.append(label["description"] + " " + str(label["score"]))
    print(classificationData)

    return classificationData


