import requests
import time

API_KEY = "AIzaSyDCIWm9mNpav9Fwo2FMsBUDFoNG0KJSOFM"

# address = '533 McCormick Ave Apt 7, Madison, WI'
address = '600 N Park St, Madison, WI 53706'

params = {
    'key': API_KEY,
    'address': address
}
# https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY

base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

response = requests.get(base_url, params=params)
# print(response.json())

# print(response.json().keys())

# https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants%20in%20Sydney&key=YOUR_API_KEY

base_url_text_search = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

params1 = {
    'query': 'restaurants near ' + address,
    'radius': 300, # 500m considered as walking distance
    'key': API_KEY
}

response1 = requests.get(base_url_text_search, params=params1)
# print(response1.json())

ratings = {}
print(response1.json().keys())
params1['pagetoken'] = response1.json()['next_page_token']
print(params1)
time.sleep(3)
response2 = requests.get(base_url_text_search, params=params1)
print(response2.json().keys())
results1 = response1.json()['results']
results2 = response2.json()['results']
print(results2)
print([result['rating'] for result in results1])
print([result['rating'] for result in results2])


# print(len(response1.json()['results']))
# print(response1.json()['results'][0])
# print(response1.json()['results'][0].keys())
# open_ai_api_key = "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"
# import openai

# openai.api_key = open_ai_api_key
# def prompt_text(res, food_type):
#     prompt = f'''
#     The following are the close restaurants near me {res},
#     I want {food_type} of food. 
#     Choose three best restarants I'd likely choose. 
#     Provide the location, rating, open status, necessary information you think should be provided but try to be concise too.
#     '''
#     return prompt 

# # def model_response(prompt):
# #     response = openai.ChatCompletion.create(
# #         model="gpt-3.5-turbo",
# #         messages=[{'role': 'user', 'content': prompt}],
# #         temperature=0
# #     )
# #     return response.choices[0].message['content'], response.usage.total_tokens

# # prom = prompt_text(response1, 'soup')
# # output, total_tokens = model_response(prom)
# # import json
# # output_refine = json.loads(output.replice('\n',''))
# # print(output_refine)

# from openai import OpenAI


# client = OpenAI(
#     api_key=open_ai_api_key
# )

# chat_completion = client.chat.completions.create(
#     messages=[
#         {'role': 'user', 'content': prompt_text(response1, 'soup')}
#     ],
#     model='gpt-3.5-turbo'
# )

# print(chat_completion)