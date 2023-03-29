from .bloodoath import BloodOath
from .follower import Follower


class Cult:

    all = []


    def __init__(self, name, location, founding_year, slogan):
        self.name = name
        self.location = location
        self.founding_year = founding_year
        self.slogan = slogan
        self.cult_list = []
        Cult.all.append(self)

    

    def recruit_follower(self, follower):
        if follower not in self.cult_list:
            self.cult_list.append(follower)

    @classmethod 
    def find_by_name(cls, string):
        for cult in cls.all:
            if cult.name == string:
                return cult
        
    def cult_population(self):
        return len(self.cult_list)

    @classmethod
    def find_by_location(cls, string):
        cult_location_list = []
        for local in cls.all:
            if local.location == string:
                cult_location_list.append(local)
        return cult_location_list
        
    
    @classmethod
    def find_by_founding_year(cls, integer):
        cult_year_list = []
        for cult in cls.all:
            if cult.founding_year == integer:
                cult_year_list.append(cult)
        return cult_year_list
        

    def average_age(self):
        cult_followers = []
        total = 0
        count = len(cult_followers)
        if count == 0:
            return 0
        for follower in cult_followers:
            total += follower.age
        return total / count
    
    def my_followers_mottos(self):
        for follower in self.cult_list:
            print(follower.life_motto)

    def least_popular(self):
        pass