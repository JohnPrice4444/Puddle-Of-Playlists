import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
import requests

def error_on_request(error_msg):
    return JsonResponse({"error": error_msg}, status=400)

def bad_request():
    return error_on_request("bad request")

@csrf_exempt
def handle_login(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                print("donuts")
                return JsonResponse({"username": user.username}, status=200)
            
    except Exception as e:
        return error_on_request(str(e))
    
    return bad_request()

@csrf_exempt
def handle_logout(request):
    try:
        if request.method == "POST":
            logout(request)
            print("donuts")
            return JsonResponse(data={"Status": "Successful logout"}, status=200)
        
    except Exception as e:
        return error_on_request(str(e))
    
    return bad_request()





# def get_lyrics(request):
#     try:
#         data = json.loads(request.body)
#         print(data)
#         searchItem1 = data["artistName"]
#         searchItem2 = data["songName"]
#         response = requests.get(f'https://api.lyrics.ovh/v1/{searchItem1}/{searchItem2}')
#         print(response)
#         return JsonResponse(data={"Lyrics": response}, status=200)
#     except Exception as e:
#         return error_on_request(str(e))
    
#     return bad_request()


# def handle_artmaker(request):
#     try:
#         if request.method == "POST":
#             data = json.loads(request.body)
#             inputData = data["inputData"]
            
#             headers = {
#                 'Authorization': 'lbk6SOe9YUnsQ0vVOLk3nHSum28pZQpuVTER9eG290cF7',
#             }
#             body = {
#                 'inputText': (None, inputData),
#                 'outputWidth': (None, '256'),
#             }
        
#             response = requests.post('https://api.hotpot.ai/make-art', headers=headers, files=body)
#             # resData = json.loads(response.json())
#             # responseData = response.json()
#             print(response)
#             # newResponse = requests.get(responseData['url'], headers=headers)
#             # print(newResponse)
#             return JsonResponse(data={"response": response.json()}, status=200)
#     except Exception as e:
#         return error_on_request(str(e))
#     return bad_request()

# lbk6SOe9YUnsQ0vVOLk3nHSum28pZQpuVTER9eG290cF7



