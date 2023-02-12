from bs4 import BeautifulSoup
import requests


class Parser:
	html = ""
	res = []
	
	def __init__(self, url, path1):
		self.url = url
		self.path1 = path1
	
	def get_html(self):
		req = requests.get(self.url).text
		self.html = BeautifulSoup(req, 'lxml')
	
	def parsing(self):
		news1 = self.html.find_all("div", class_="caption")
		for item in news1:
			title = item.find("h3").text
			href = item.find("a").get('href')
			author = item.find("a", class_="topic-info-author-link").text.strip()
			description = item.find("div", class_="topic-content text").text.strip()
			self.res.append({
				"title": title,
				"href": href,
				"author": author,
				"description": description,
			})
			
	def server(self):
		with open(self.path1, "w") as f:
			i = 1
			for item in self.res:
				f.write(f'Кино и сериалы №{i}\n\nНазвание: {item["title"]}.\n'
						f'Описание:{item["description"]}\nАвтор: {item["author"]}'
						f'\nСсылка: {item["href"]}\n\n{"*" * 25}\n')
				i += 1
	
	def run(self):
		self.get_html()
		self.parsing()
		self.server()
		



