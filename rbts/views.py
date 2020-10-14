from django.http import HttpResponse


async def index(request):
    return HttpResponse("1 2 3... testing async Django")
