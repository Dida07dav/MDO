import pickle
import os.path


class Article:
	def __init__(self, movie_title, genre, director, year_of_issue, duration, studio, actors):
		self.movie_title = movie_title
		self.genre = genre
		self.director = director
		self.year_of_issue = year_of_issue
		self.duration = duration
		self.studio = studio
		self.actors = actors
	
	def __str__(self):
		return f"{self.movie_title} ({self.genre}) ({self.director})" \
			   f"({self.year_of_issue}) ({self.duration})" \
			   f"({self.studio}) ({self.actors})"


class ArticleModel:
	def __init__(self):
		self.db1_name = 'db1.txt'
		self.articles = self.load_data()
	
	def add_article(self, dict_article):
		article = Article(*dict_article.values())
		self.articles[article.movie_title] = article
		
	def get_all_articles(self):
		return self.articles.values()

	def get_singe_article(self, user_title):
		article = self.articles[user_title]
		dict_article = {
			"название": article.movie_title,
			"жанр": article.genre,
			"режиссер": article.director,
			"год выпуска": article.year_of_issue,
			"длительность": article.duration,
			"студия": article.studio,
			"актеры": article.actors
		}
		return dict_article
	
	def remove_article(self, user_title):
		return self.articles.pop(user_title)
	
	def load_data(self):
		if os.path.exists(self.db1_name):
			with open(self.db1_name, 'rb') as f:
				return pickle.load(f)
		else:
			return dict ()
	
	def save_data(self):
		with open(self.db1_name, 'wb') as f:
			pickle.dump(self.articles, f)