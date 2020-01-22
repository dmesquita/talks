import scrapy

trilhas = []

class TrilhaSpider(scrapy.Spider):
    name = "trilhaspider"
    start_urls = []
    for cidade in ["saopaulo", "florianopolis","belohorizonte","portoalegre"]:
        for ano in range(2014, 2020):
            l = "http://www.thedevelopersconference.com.br/tdc/{}/{}/trilhas".format(ano,cidade)
            start_urls.append(l)
    
    def parse(self, response):
        for links in response.css(".btn"):
            for a in links.css("a::attr(href)"):
                link = ("http://www.thedevelopersconference.com.br"+a.get())
                trilhas.append(link)

        with open("data/external/trilhas.txt", "w") as f:
            f.write(str(trilhas))
