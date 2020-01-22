import scrapy

class PalestraSpider(scrapy.Spider):
    name = "trilhaspider"
    with open("data/external/trilhas.txt", "r") as file:
        start_urls = eval(file.readline())

    def parse(self, response):
        url = response.request.url
        url_words = url.split("/")
        ano = url_words[4]
        cidade = url_words[5]
        trilha = url_words[-1]

        if len(response.css("table")) == 0:
            palestra = {}
            palestra["title"] = "Não encontrada"
            palestra["description"] = "Não encontrada"
            palestra["trilha"] = trilha
            palestra["ano"] = ano
            palestra["cidade"] = cidade
            palestra["trilha_url"] = url
            yield palestra

        for palestra in response.css("table"):
            titles = palestra.css("a.palestra::text").getall()
            titles = filter(lambda x: not x.isspace(), titles)
            descriptions = []
            for desc in response.css(".conteudo > .descricao"):
                descriptions.append(desc.css("p::text").getall())
            for t,d in zip(titles,descriptions):
                palestra = {}
                palestra["title"] = t
                palestra["description"] = d
                palestra["trilha"] = trilha
                palestra["ano"] = ano
                palestra["cidade"] = cidade
                palestra["trilha_url"] = url
                yield palestra
