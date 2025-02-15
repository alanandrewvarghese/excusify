from django.shortcuts import render
from .utils import generate_random_excuse

def home(request):
    excuse = generate_random_excuse().get('cringe_excuse',"No excuse available")
    print(excuse)
    context = {
        "excuse":excuse
    }
    return render(request, 'home.html', context=context)

def custom_excuse(request):
    if request.method == "POST":
        context = {}
        vibe = request.POST.get("vibe", "")
        desperation = request.POST.get("desperation", "")
        situation = request.POST.get("situation", "")

        prompt = f"""
        Vibe: {vibe}
        Desperation Level: {desperation}
        Situation: {situation}
        ''' 
        """
        excuse = generate_random_excuse(prompt).get('cringe_excuse',"No excuse available")
        context = {
            "excuse":excuse
        }
    return render(request, 'custom_excuse.html', context)