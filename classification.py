import requests

API_URL = "https://api-inference.huggingface.co/models/jaimin/soundclassification"
headers = {"Authorization": "Bearer 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"}

def query(filename=r'static\generated\output_file.mp3'):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json() 


if __name__ == '__main__':
    #to access the query function
         result=print(query())