# import ipdb
#from lib import *

from lib import Follower, Cult, BloodOath
# test your code here
# e.g.

f1 = Follower( 'Emiley', 31, 'Living the Dream' )
f2 = Follower( 'Jenny', 29, 'Living the Dream' )
f3 = Follower( 'Creed', 72, 'Born in the US of A Baby')
f4 = Follower( 'Michael', 40, 'I am the best boss ever' )

c1 = Cult( 'Heavens Gate', 'San Diego', 1974, 'Human Metamorphosis' )
c2 = Cult( 'The Order', 'San Diego', 1975, 'The New World Order' )
c3 = Cult( 'Heavens Gate', 'Dallas', 1962, 'Sell sell sell' )
c4 = Cult( 'The Church of Scientology', 'Los Angeles', 1954, 'Dianetics' )

bo1 = BloodOath( '2019-09-16', f1, c1 )
bo2 = BloodOath( '2020-02-14', f2, c2 )
bo3 = BloodOath( '1985-07-09', f3, c3 )
bo4 = BloodOath( '2019-09-16', f4, c4 )
bo4 = BloodOath( '2019-09-16', f2, c4 )


# c1.followers => ???
# f1.cults => ???



#print( c1, f1, bo1 )
#print(Cult.find_by_location('San Diego'))
# print(Cult.find_by_name('Heavens Gate').founding_year)
# ipdb.set_trace()ß
# print(Follower.cults(f1))
print(c1.name)
f1.followers_cults(c1)

# print(f1.all[0].name)

# print(Follower.of_a_certain_age(30))

# print(f1.cult_followers[0])

# print(c2.average_age())

# print(c1.cult_list[0].name)

# print(c1.cult_list[0].age)

# print(c1.cult_list[0].life_motto)

# print(c1.cult_population())

# print(c1.least_popular)
# print(Cult.most_common_location().name)
#print(c1.most_common_location)

locations = Cult.find_by_location('San Diego')
n = locations[0]
n. 
print(Cult.find_by_location('San Diego')[0].name)
