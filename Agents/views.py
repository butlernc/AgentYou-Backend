
from Agents import models
from django.template import RequestContext
from django.shortcuts import render_to_response
# Creates a new Agent, save's their email and password
# along with the face data

def create(request):

    context = RequestContext(request)

    if request.method == 'GET':
        email = context['email']
        password = context['password']
        id_pic_address = ''

        new_agent = models.AgentUser(email=email, password=password)
        new_agent.save()

        # id_pic_address goes to the C++ file
        # returns data to save in FaceData.DATA_0

        data = "1"
        new_agent_face_data = models.FaceData(email=email, DATA_0=data)
        new_agent_face_data.save()

        context_dict = {'worked': True}
    return render_to_response(create_user.html, context_dict, context)
