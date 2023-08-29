from .models import Solution

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def jugs_riddle(request):
    x, y, z = int(request.POST.get("x")), int(
        request.POST.get("y")), int(request.POST.get("z"))
    sol = Solution(x, y, z)
    steps = sol.minSteps()
    return render(request, 'web/steps.html', {"steps": steps})


@csrf_exempt
def jugs_riddle_api(request):
    try:
        x, y, z = int(request.POST.get("x")), int(
            request.POST.get("y")), int(request.POST.get("z"))
    except TypeError:
        return JsonResponse({"steps": []})
    if any(elem < 0 or elem == 0 for elem in [x, y, z]):
        return JsonResponse({"teps": []})
    sol = Solution(x, y, z)
    steps = sol.minSteps()
    return JsonResponse({"steps": steps})


def index(request):
    return render(request, 'web/index.html')
