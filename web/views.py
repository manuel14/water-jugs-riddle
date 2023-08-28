from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Jug, Solution


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def Pour(toJugCap: Jug, fromJugCap: Jug, amountToMeassure: int) -> list[dict]:
    # TODO if possible make a type for steps list
    fromJugCap.fill()
    steps = []
    steps.append(
        {"operation": "fill",
         "jug": fromJugCap.name,
         "amount": fromJugCap.capacity,
         toJugCap.name: toJugCap.state,
         fromJugCap.name: fromJugCap.state
         }
    )
    while ((fromJugCap.state != amountToMeassure) and (toJugCap.state != amountToMeassure)):
        # this min assures recipient jug will never be transferred with more than it's capacity
        temp = min(fromJugCap.state, toJugCap.capacity - toJugCap.state)
        steps.append({"operation": "transfer", "from": fromJugCap.name, "amount": fromJugCap.state,
                     "to": toJugCap.name})
        toJugCap.state = toJugCap.state + temp
        fromJugCap.state = fromJugCap.state - temp
        steps[-1][fromJugCap.name] = fromJugCap.state
        steps[-1][toJugCap.name] = toJugCap.state
        if ((fromJugCap.state == amountToMeassure) or (toJugCap.state == amountToMeassure)):
            break
        # If fromJugCap is empty fill it
        if fromJugCap.state == 0:
            # fromJugCap.state = fromJugCap.capacity
            fromJugCap.fill()
            steps.append(
                {"operation": "fill", "jug": fromJugCap.name, "amount": fromJugCap.capacity, toJugCap.name: toJugCap.state,
                 fromJugCap.name: fromJugCap.state})
        # If toJugCap is full empty it
        if toJugCap.state == toJugCap.capacity:
            toJugCap.empty()
            steps.append({"operation": "empty", "jug": toJugCap.name, toJugCap.name: toJugCap.state,
                          fromJugCap.name: fromJugCap.state})
    return steps


def minSteps(j1: int, j2: int, d):
    # time complexity is O(n) where n is the greater value between j1 and j2
    # try both x being the jug filled and y being the jug filled
    if j2 > j1:
        temp = j2
        j2 = j1
        j1 = temp
    if (d % (gcd(j1, j2)) != 0):
        return []
    pour = Pour(Jug(capacity=j1, name="x"), Jug(capacity=j2, name="y"), d)
    pour_inverse = Pour(Jug(capacity=j2, name="y"),
                        Jug(capacity=j1, name="x"), d)
    if len(pour) <= len(pour_inverse):
        return pour
    return pour_inverse


def jugs_riddle(request):
    x, y, z = int(request.POST.get("x")), int(
        request.POST.get("y")), int(request.POST.get("z"))
    # steps = minSteps(x, y, z)
    sol = Solution(x, y, z)
    steps = sol.minSteps()
    print(len(steps))
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
