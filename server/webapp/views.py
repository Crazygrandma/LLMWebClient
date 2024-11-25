from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")



# from gpt4all import GPT4All

# class GPTManager:

#     def __init__(self,model,system_prompt='',device='gpu'):
#         # self.sytem_prompt = system_prompt
#         self.model = f'c:/Users/henry/AppData/Local/nomic.ai/GPT4All/{model}'
#         self.gpt = GPT4All(model_name=self.model,device=device, allow_download=False)

#     def setDevice(self,device="gpu"):
#         self.device = device

#     def getResponse(self,prompt):
#         response = self.gpt.generate(
#             prompt=prompt,
#             streaming=True
#         )
#         return response


# def main():
#     system_prompt = ''''''
#     # model = "mistral-7b-instruct-v0.1.Q4_0.gguf"
#     # model = "em_german_mistral_v01.Q4_0.gguf"
#     model = "em_german_leo_mistral.Q4_0.gguf"
#     # model = "em_german_7b_v01.Q4_K_M.gguf"
#     # model = "mistral-7b-openorca.Q4_0.gguf"
#     # model = "Llama-3.2-1B-Instruct-Q4_0.gguf"
#     # model = 'c:/Users/henry/AppData/Local/nomic.ai/GPT4All/mistral-7b-openorca.Q4_0.gguf'
    
    
    
#     mygpt = GPTManager(model)
#     clientinput = ""
#     tokenGenerator = mygpt.gpt.generate(clientinput);
    
#     # print(tokenGenerator
#     # next(tokenGenerator)
#     reponseText = ""
#     for value in tokenGenerator:
#         # print(value)
#         reponseText += value
        
#         if len(reponseText) >= 50:
            
#             print(reponseText)
#             reponseText = ""
