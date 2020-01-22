.PHONY: data
data:
	rm -f data/external/trilhas.txt
	rm -f data/external/palestras.json
	scrapy runspider data/trilhas-spider.py
	scrapy runspider data/palestra-spider.py -o data/external/palestras.json

process_data:
	rm -f data/raw/palestras.json
	python3 data/process_data.py
