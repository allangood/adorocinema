#!/usr/bin/python

from lxml import html
from requests import get
from urllib import quote_plus
from difflib import SequenceMatcher

class AdoroCinema():
    def __init__(self, searchtitle):
        self.baseurl = 'http://www.adorocinema.com'
        self.queryurl = self.baseurl + '/busca/?q='
        self.searchtitle = searchtitle.strip()

    def similar(self, a, b):
        return SequenceMatcher(None, a.lower(), b.lower()).ratio()

    def getinfo(self):
        searchresult = get(self.queryurl + quote_plus(self.searchtitle))
        root = html.fromstring(searchresult.content)
        names = []
        for t in root.xpath('//a[contains(@href, "/filmes/filme-")]/img/@alt'):
            names.append(self.similar(self.searchtitle, t))

        link = None
        if (len(names) > 0):
            index = names.index(max(names))
            link = root.xpath('//a[contains(@href, "/filmes/filme")]/img/ancestor::a/@href')[index]

        info = {}
        if link:
            infopage = get(self.baseurl + link)
            root = html.fromstring(infopage.content)

            title = root.xpath('//meta[@itemprop="name"]')
            if (len(title) == 1):
                info['title'] = title[0].attrib['content']
            plot = root.xpath('//*[@itemprop="description"]/text()')
            if (len(plot) == 1):
                info['plot'] = plot[0].strip()
            else:
                info['plot'] = root.xpath('//*[@itemprop="description"]/*/text()')
 
            company = root.xpath('//*[@itemprop="productionCompany"]/text()')
            if (len(company) == 1):
                info['company'] = company[0].strip()
            rating = root.xpath('//*[@itemprop="ratingValue"]')
            if (len(rating) == 1):
                info['rating'] = rating[0].attrib['content']
            info['genre'] = root.xpath('//*[@itemprop="genre"]/text()')
            info['cast'] = root.xpath('//*[@itemprop="actor"]/a/span[@itemprop="name"]/text()')
            info['director'] = root.xpath('//*[@itemprop="director"]/a/span[@itemprop="name"]/text()')
            poster = root.xpath('//img[@class="shot-img"]/@data-src')
            if (len(poster) > 0):
                info['poster'] = poster[0]
        return info
