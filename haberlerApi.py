import requests

class NewsApi:
    businessList=[]
    entertainmentList=[]
    healthList=[]
    scienceList=[]
    sportsList=[]
    technologyList=[]
    
    def __init__(self) -> None:
        self._url="https://newsapi.org/v2/top-headlines?"
        self._apiKey="96d4893062974f74ab84841ce82c5096"
        self._country="tr"

    def get_news(self,category,liste):
        response=requests.get(self._url,params={"apiKey":self._apiKey, "country":self._country ,"category":category})
        news=response.json()["articles"]
        
        for new in news:
            liste.append(new["title"])
            liste.append(new["url"])
                
    def get_business(self):
        self.get_news("business",NewsApi.businessList)

    def get_entertainment(self):
        self.get_news('entertainment',NewsApi.entertainmentList)
        
    def get_health(self):
        self.get_news('health',NewsApi.healthList)
        
    def get_science(self):
        self.get_news('science',NewsApi.scienceList)
        
    def get_sports(self):
        self.get_news('sports',NewsApi.sportsList)
        
    def get_technology(self):
        self.get_news('technology',NewsApi.technologyList)    
             
news=NewsApi()