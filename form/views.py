from django.shortcuts import render, redirect
from .models import FormTemplate
from django.http import JsonResponse

# Create your views here.

def index(request):
    form = FormTemplate.objects.all()
    context = {
        "form": form
    }
    return render(request, "index.html", context)


def PostForm(request):
    try:
        if request.method == "POST":
            name = request.POST['name']
            field_name_1 = request.POST['email'],
            field_name_2 = request.POST['telephone']
            integer = int(field_name_2)
            print(type(field_name_1))
            if field_name_2[:2] == "+7" and type(integer) != str and len(field_name_2) > 5:
                arr_1 = list(map(lambda x: x.name, FormTemplate.objects.all()))
                arr_2 = list(map(lambda x: x.field_name_1, FormTemplate.objects.all()))
                arr_3 = list(map(lambda x: x.field_name_2, FormTemplate.objects.all()))
                print(arr_1, arr_2, arr_3)
                if name in arr_1:
                    return JsonResponse({"name": name, "Error !": "This data already exists"})
                elif field_name_1 in arr_2:
                    return JsonResponse({"field_name_1": field_name_1, "Error !": "This data already exists"})
                elif field_name_2 in arr_3:
                    return JsonResponse({"field_name_2": field_name_2, "Error !": "This data already exists"})
                else:
                    FormTemplate.objects.create(
                        name = name,
                        field_name_1 = field_name_1,
                        field_name_2 = field_name_2
                    )
                    return JsonResponse({"name": name, "field_name_1": field_name_1, "field_name_2": field_name_2, "success":"created"})
            else:
                return JsonResponse({"Correcr the number": "eror", "Example": "+7 xxx xx xx"})
    except:
        return JsonResponse({"Error": "Function is not working", "Or": "You can enter the latter AND try entering numbers"})