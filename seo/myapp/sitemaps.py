from django.contrib.sitemaps import Sitemap
from django.urls import reverse
import pandas , os , pathlib

class InfoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    def items(self):
        return ['search']
    def location(self, item):
        return reverse(item)


class DataSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    def items(self):
        result = []
        df = pandas.read_csv(os.path.join(pathlib.Path(__file__).resolve().parent , "static" , "data.csv") , engine='pyarrow')
        for index , row in df.iterrows():
            result.append(row['name'].lower())
        return result

    def location(self, item):
        return '/data/%s' % (item)
