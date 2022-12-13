from django.shortcuts import render
from . import views
import os
import pandas
from pathlib import Path

# Create your views here.


def Search(request):
    results = []
    if request.method == "POST":
        df = pandas.read_csv(os.path.join(Path(__file__).resolve().parent , "static" , "data.csv") , engine= 'pyarrow')
        for index , row in df.iterrows():
            if row['name'].lower() == request.POST.get('searchStr').lower():
                results.append(row)
        print(results)
    else:
        pass
    return render(request , "Search.html" , {'results' : results})
