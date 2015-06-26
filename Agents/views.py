from django.http import HttpResponse
from Agents import models
from django.views.decorators.csrf import csrf_exempt

# Creates a new Agent, save's their email and password
# along with the face data

@csrf_exempt
def create(request):
    email = request.POST['email']
    password = request.POST['password']
    id_pic_address = ''

    new_agent = models.AgentUser(email=email, password=password)
    new_agent.save()

    # id_pic_address goes to the C++ file
    # returns data to save in FaceData.DATA_0

    data = "1"
    new_agent_face_data = models.FaceData(email=email, DATA_0=data)
    new_agent_face_data.save()
    response = "what upppp niggaaa"

    return HttpResponse(response)
