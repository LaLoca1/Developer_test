from django.shortcuts import render
import csv, io
from django.contrib import messages 
from django.contrib.auth.decorators import permission_required
from .models import building_info


from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

@permission_required('admin.can_add_log_entry')
def building_upload(request): 
    template = "building_upload.html"

    prompt = {
        'order': 'Order of the CSV should be building_id, id, fuel, unit'
    }

    if request.method == "GET":
        return render(request, template, prompt) 
        # Get request will retrieve data and render will merge the request, template, prompt
        # to give appropiate output. 
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'): 
        messages.error(request, 'This is not a csv file ')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set) # Gives you access to work with strings within file 
    next(io_string) # to skip header of csv file 
    for column in csv.reader(io_string, delimiter=',', quotechar="|"): 
        _, created = building_info.objects.update_or_create(
            building_id=column[0],
            id=column[1],
            fuel=column[2],
            unit=column[3],
        )
        
    context = {} # any additional info 
    return render(request, template, context)


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
   
    def get(self, request, format = None):
        csvFilePath = "halfhourly_data.csv"
        chartdata = []
        labels = []
        with open(csvFilePath, "r") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                chartdata.append(row[0])
                labels.append(row[2])

        chartLabel = "electricity"
        data = {
                    "labels":labels,
                    "chartLabel": chartLabel,
                    "chartdata": chartdata, 
            }
        return Response(data)
                

def buildings_details(request):
    template = "Table.html"
    return render(request, template)

def aberdeen_site(request):
    template = "Aberdeen.html"
    return render(request, template)

def ashton_site(request):
    template = "Ashton.html"
    return render(request, template)

def bournemouth_site(request):
    template = "Bournemouth.html"
    return render(request, template)

def bristol_site(request):
    template = "Bristol.html"
    return render(request, template)

def bury_site(request):
    template = "Bury.html"
    return render(request, template)

def cardiff_site(request):
    template = "Cardiff.html"
    return render(request, template)

def cheadle_site(request):
    template = "Cheadle.html"
    return render(request, template)

def coventry_site(request):
    template = "Coventry.html"
    return render(request, template)

def dudley_site(request):
    template = "Dudley.html"
    return render(request, template)

def edinburgh_site(request):
    template = "Edinburgh.html"
    return render(request, template)

def elstree_site(request):
    template = "Elstree.html"
    return render(request, template)

def farnborough_site(request):
    template = "Farnborough.html"
    return render(request, template)

def glasgow_site(request):
    template = "Glasgow.html"
    return render(request, template)

def heronsreach_site(request):
    template = "HeronsReach.html"
    return render(request, template)

def hull_site(request):
    template = "Hull.html"
    return render(request, template)

def hyde_site(request):
    template = "Hyde.html"
    return render(request, template)

def leeds_site(request):
    template = "Leeds.html"
    return render(request, template)

def liverpool_whiston_site(request):
    template = "Liverpool_Whiston.html"
    return render(request, template)

def maidstone_site(request):
    template = "Maidstone.html"
    return render(request, template)

def newcastle_site(request):
    template = "Newcastle.html"
    return render(request, template)

def nottingham_site(request):
    template = "Nottingham.html"
    return render(request, template)

def portsmouth_site(request):
    template = "Portsmouth.html"
    return render(request, template)

def solihull_site(request):
    template = "Solihull.html"
    return render(request, template)

def southleeds_site(request):
    template = "SouthLeeds.html"
    return render(request, template)

def stdavids_site(request):
    template = "StDavids.html"
    return render(request, template)

def swansea_site(request):
    template = "Swansea.html"
    return render(request, template)

def swindon_site(request):
    template = "Swindon.html"
    return render(request, template)

def walsall_site(request):
    template = "Walsall.html"
    return render(request, template)

def warrington_site(request):
    template = "Warrington.html"
    return render(request, template)

def wirral_site(request):
    template = "Wirral.html"
    return render(request, template)


