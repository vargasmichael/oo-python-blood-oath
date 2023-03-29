class BloodOath:

    all = []

    def __init__(self, date, follower, cult):

        self.date = date
        self.follower = follower
        self.cult = cult
        BloodOath.all.append(self)

    def initiation_date(self):
        return self.date.strftime('%Y-%m-%d')