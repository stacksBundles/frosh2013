# Create your views here.
from django.shortcuts import render, redirect
from directory.models import Image, House, Vassal, Sponsor
from django.http import HttpResponseNotFound, HttpResponseRedirect
from directory.forms import ImageForm, SponsorForm, HouseForm, VassalForm
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt


def index(request):

    null = "string"

    context = {
        "null": null,
        }

    return render(request, "index.html", context)


def faq(request):

    null = "null"

    context = {
        "null": null,
        }

    return render(request, "faq.html", context)

def sponsors(request):

    sponsorList = Sponsor.objects.all().order_by('rank')

    context = {
        "sponsorList": sponsorList,
        }

    return render(request, "sponsors.html", context)

def propaganda(request):

    null = "null"

    context = {
        "null": null,
        }

    return render(request, "proppage.html", context)

def houses(request):

    house = House.objects.get(pk=int(8))

    memberList = Vassal.objects.all().filter(house = house)

    houseList = House.objects.all()

    imageList = Image.objects.all()

    context = {
        "houseList": houseList,
        "imageList": imageList,
        "memberList": memberList,
        "house": house,
        }

    return render(request, "houseEffect.html", context)

def edit(request):    
    
    houseList = House.objects.all()

    vassalList = Vassal.objects.all()

    imageList = Image.objects.all()

    houseForm = HouseForm()

    context = {
        "houseForm": houseForm,
        "houseList": houseList,
        "vassalList": vassalList,
        "imageList": imageList,
        }

    return render(request, "houseForm.html", context)

def houseLookup(request):

        iD = request.POST["field"]

        houseList = House.objects.all()

        vassalList = Vassal.objects.all()

        houseForm = HouseForm()

        context = {
            "requestedHouse": requestedHouse,
            "requestedVassals": requestedVassals,
            "houseForm": houseForm,
        }

        return render(request, 'houseForm.html', context)
        
@csrf_exempt
def vassalLookup(request):
    
    if request.method == "POST" and request.is_ajax():

        iD = request.POST["id"]

        try:
            
            instance = Vassal.objects.get(pk=int(iD))

            print("received request for iD = " + str(iD) + ", member: " + str(instance))
        
        except ObjectDoesNotExist:
            
            return HttpResponseNotFound("Please contact site administrator with subject: 'model not found'")

        forms = VassalForm(instance = instance)
        
        context = {
            "forms": forms,
            "vassal": instance,
        }

        return render(request, 'vassal.html', context)

def vassalEdit(request, iD):

    if request.method == "POST" and request.is_ajax():

        instance = Vassal.objects.get(pk=int(iD))

        editedForm = VassalForm(request.POST, instance = instance)

        if editedForm.is_valid():

            s = editedForm.save()

            houseList = House.objects.all()

            vassalList = Vassal.objects.all()

            imageList  = Image.objects.all()
            
            context = {
                "houseList": houseList,
                "vassalList": vassalList,
                "imageList": imageList,
            }

            return render(request, "houseRefresh.html", context)

        else:

            return HttpResponseNotFound("form didn't save")

def register(request):

    if request.method == "GET":

        return HttpResponseRedirect('http://ssmu-frosh.openface.ca')

@csrf_exempt
def imageForm(request, iD):

    if request.method == "POST" and request.is_ajax():

        vassal = Vassal.objects.get(pk=int(iD))

        print("generating form for id = " + str(iD) + ", member name: " + str(vassal) + " ... ")

        instance = Image.objects.get(vassal = vassal)

        imageForm = ImageForm(instance = instance)

        context = {
            "imageForm": imageForm,
            "image": instance,
            }

        return render(request, "imageUpload.html", context)

def imageUpload(request, iD):
    
    if request.method == "POST":

        instance = Image.objects.get(pk=int(iD))

        print("found instance: " + str(instance))

        print("editing image for member: " + str(instance.vassal))

        print(request.POST)

        print(str(type(request.FILES)))

        editedForm = ImageForm(request.POST, request.FILES, instance = instance)

        if editedForm.is_valid():

            s = editedForm.save()

            print("saved ... ")

            houseList = House.objects.all()

            vassalList = Vassal.objects.all()

            imageList  = Image.objects.all()
            
            context = {
                "houseList": houseList,
                "vassalList": vassalList,
                "imageList": imageList,
            }

            return redirect(edit)

        else:
	    print("Form has errors")
	    response = 'Errors:'
            print("Else loop is called")
	    form = StoryForm(request.POST)
	    for key in form.errors.keys():
                value = form.errors[key]
		errors = ''
		for error in value:
		    errors = errors + error + ' '
		    response = response + ' ' + key + ': ' + errors
	    return HttpResponse('<li class="error">' + response + '</li>')


@csrf_exempt
def houseRetrieve(request, iD):

    if request.method == "POST" and request.is_ajax():

        print("request received")

        house = House.objects.get(pk=int(iD))

        print("requesting members of: " + str(house.house_name))

        memberList = Vassal.objects.all().filter(house = house)

        houseList = House.objects.all()

        imageList = Image.objects.all()

        if memberList and houseList and imageList:

            print("ready to rock")

        context = {
            "house": house,
            "memberList": memberList,
            "houseList": houseList,
            "imageList": imageList,
            }

        return render(request, "houseRequest.html", context)
    
