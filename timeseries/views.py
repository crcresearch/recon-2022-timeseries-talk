from django.http import JsonResponse
from .models import Metric
from .serializers import MetricSerializer
from datetime import datetime
from pymongo import MongoClient
from django.conf import settings
from dateutil import parser
import json
from bson import ObjectId


# Create your views here.
def query_postgres(request):
    records = Metric.objects.filter(
        time__gte=request.GET.get('start_time'),
        time__lte=request.GET.get('end_time')
    )

    serializer = MetricSerializer(records, many=True)

    return JsonResponse(serializer.data, safe=False)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S.%f%Z+%')
        return json.JSONEncoder.default(self, o)

def query_mongo(request):
    print("Looking at mongo")
    client = MongoClient(
        f"mongodb://{settings.MONGO_HOST}:{settings.MONGO_PORT}"
    )
    db = client[settings.MONGO_DB]
    collection = db['timeseries']

    data = collection.find({ 
        "timestamp": { 
            "$gte": parser.parse(request.GET.get('start_time')),
            "$lte": parser.parse(request.GET.get('end_time'))
        }
    })

    return JsonResponse(json.loads(JSONEncoder().encode(list(data))), safe=False)