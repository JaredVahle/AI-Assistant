import openai
import env

openai.api_key = env.API_KEY

models = openai.Model.list()
for model in models['data']:
    print(model['id'])
