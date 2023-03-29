from .bloodoath import BloodOath


class Follower:

    all = []

    def __init__(self, name, age, life_motto):
        self.name = name
        self.age = age
        self.life_motto = life_motto
        self.f_cults_list = []
        self.cult_followers = []
        
        Follower.all.append(self)

    def followers_cults(self, cult):
        if cult not in self.f_cults_list:
            self.f_cults_list.append(cult)

    def join_cult(self, cult):
        if cult not in self.cult_followers:
            self.cult_followers.append(cult)

    @classmethod
    def of_a_certain_age(cls, integer):
        age_list = []
        for follower in cls.all:
            if follower.age > integer:
                age_list.append(follower.name)
        return age_list
       

    # @classmethod
    # def most_common_location(cls):
    #     location_list = []
    #     for follower in cls.all:
    #         location_list.append(follower.location)
    #     return max(location_list, key=location_list.count)

    @classmethod
    def most_common_location(cls):
        locations = [cult.location for cult in cls.all]
        location_counts = [(location, locations.count(location)) for location in set(locations)]
        most_common_location = max(location_counts, key=lambda x: x[1])
        return most_common_location[0]


   