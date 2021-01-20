class Home():
    def __init__(self, structure="unspecified", driveway="unknown", garden="unknown", rooms="unknown", bathroom="uknown", kitchen="unknown", bedrooms="unknown"):
        self.structure = structure
        self.driveway = driveway
        self.garden = garden
        self.rooms = rooms
        self.bathroom = bathroom
        self.kitchen = kitchen
        self.bedrooms = bedrooms
        print('The house is a' , self.structure , 'Outside we have' , self.driveway , 'We also have a lovely' , self.garden , 'This house has' , self.rooms , 'This house has' , self.bathroom , 'The house has a' , self.kitchen , 'lastly it has' , self.bedrooms)


home1 = Home("detached","a drive way","small garden","13 rooms","2 bathrooms","one kitchen","4 bedrooms")