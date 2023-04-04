import requests
import json

#Got help from chatGPT on options and setup for image detection
api_key = ''

# Define the endpoint URL
def classifyImage():
    url = "https://vision.googleapis.com/v1/images:annotate?key={}".format(api_key)

    # Define the request payload
    payload = {
    "requests": [
        {
        "image": {
            "source": {
            "imageUri": "https://i2.wp.com/www.kuddly.co/wp-content/uploads/2016/02/Dollarphotoclub_87149759.jpg?resize=5184%2C3456"
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

#classifyImage()

