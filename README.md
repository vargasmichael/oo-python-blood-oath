Blood Oath Lab
==============

In this project, we will be practicing object relationships in Python, with a particular emphasis on the `has many` `through` relationship (aka: many-to-many). Please read the whole README before writing any code!

## Introduction

You've been approached by your local cult leaders to build out a foundation for a new app they are all using to gather recruits. As the open-minded freelancers that you are, you've agreed to do so!

---

## Setup (Code Overview)

You can now view all of your Python files for your models in the `lib` folder. They will be automagically available for you so long as you use the `python debug.py` file to test your code.

Through this file, we've provided to you a console that you can use to test your code. To enter a console session, run `python debug.py` from the command line. You'll be able to test out the functionality that you write there. Take a look at that file to see how you can pre-define variables and create object instances, rather than manually doing it in every single console session.


---

## Deliverables

### Domain Modeling

First step is to model the domain you are building out. As a non-discriminatory cult recruitment platform, `Cult`s will have many `Follower`s while `Follower`s will be allowed to join many `Cult`s. How do they keep track of this? `BloodOath`s of course! You cannot join a `Cult` without making a `BloodOath`.

* What are your models?
* What does your schema look like?
* What are the relationships between your models?

---

### Basic Class Attributes, Properties, and Methods

With your domain modeled, you now need to build out some basic functionality so both `Cult`s and `Follower`s can use your platform to make `BloodOath`s. A social network of cults if you will. So general searching type functionality.

Questions you should ask yourself:

* Do I need any other attributes?
* Should I write any other methods?
* Am I following _Single Source of Truth_?

### A note about notation
When you see a '#', this means the functionality will be related to the instance, a '.', the class. 


**`Cult`**

* `Cult#name`
  * returns a `String` that is the cult's name
* `Cult#location`
  * returns a `String` that is the city where the cult is located
* `Cult#founding_year`
  * returns a `Integer` that is the year the cult was founded
* `Cult#slogan`
  * returns a `String` that is this cult's slogan
* `Cult#recruit_follower`
  * takes in an argument of a `Follower` instance and adds them to this cult's list of followers
* `Cult#cult_population`
  * returns a `Integer` that is the number of followers in this cult
* `Cult.all`
  * returns an `List` of all the cults
* `Cult.find_by_name`
  * takes a `String` argument that is a name and returns a `Cult` instance whose name matches that argument
* `Cult.find_by_location`
  * takes a `String` argument that is a location and returns an `List` of cults that are in that location
* `Cult.find_by_founding_year`
  * takes a `Integer` argument that is a year and returns a list of all the cults founded in that year

**`Follower`**

* `Follower#name`
  * returns a `String` that is the follower's name
* `Follower#age`
  * returns a `Integer` that is the age of the follower
* `Follower#life_motto`
  * returns a `String` that is the follower's life motto
* `Follower#cults`
  * returns an `List` of this follower's cults
* `Follower#join_cult`
  * takes in an argument of a `Cult` instance and adds this follower to the cult's list of followers
* `Follower.all`
  * returns an `List` of all the followers
* `Follower.of_a_certain_age`
  * takes a `Integer` argument that is an age and returns an `List` of followers who are the given age or older

**`BloodOath`**

* `BloodOath#initiation_date`
  * returns a `String` that is the initiation date of this blood oath in the format _YYYY-MM-DD_.
* `BloodOath.all`
  * returns an `List` of all the blood oaths

---

### Advanced Methods - Analytics!

Our cult social network platform is working well. Let's first make a commit!

Now we want to build out some useful features so `Cult`s and `Follower`s and get more value out of our app.

**`Cult`**

* `Cult#average_age`
  * returns a `Float` that is the average age of this cult's followers
* `Cult#my_followers_mottos`
  * prints out all of the mottos for this cult's followers
* `Cult.least_popular`
  * returns the `Cult` instance who has the least number of followers :
* `Cult.most_common_location`
  * returns a `String` that is the location with the most cults

**`Follower`**

* `Follower#my_cults_slogans`
  * prints out all of the slogans for this follower's cults
* `Follower.most_active`
  * returns the `Follower` instance who has joined the most cults
* `Follower.top_ten`
  * returns an `List` of followers; they are the ten most active followers

**`BloodOath`**

* `BloodOath.first_oath`
  * returns the `Follower` instance for the follower that made the very first blood oath

---

### BONUS!

Our platform is done! Let's commit our code!

Now one highly requested feature from `Follower`s using your app that you plan to paywall ($$$) is to see your fellow cult members. See if you can implement this method.

* `Follower#fellow_cult_members`
  * returns a unique `List` of followers who are in the same cults as you

A highly requested feature from `Cult`s using your app that you plan to paywall ($$$) is to restrict ages for recruits. See if you can implement this functionality.

* `Cult#minimum_age`
  * returns a `Integer` that is the minimum age required for followers joining this cult
* `Cult#recruit_follower`
  * takes in an argument of a `Follower` instance and adds them to this cult's list of followers
  * NOW this is changed such that if the given `Follower` instance is not of age:
    * do not let them join the cult
    * print out a friendly message informing them that they are too young
* `Follower#join_cult`
  * takes in an argument of a `Cult` instance and adds this follower to the cult's list of followers
  * NOW this is changed such that if you don't meet the minimum age requirement of the given `Cult` instance:
    * do not let them join the cult
    * print out a friendly message informing them that they are too young

Congrats on finishing your cult social network platform. Time to rake in the $$$!
