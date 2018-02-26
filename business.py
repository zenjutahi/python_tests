class Business:
    def __init__(self):
        self.business = {}

    def create_business(self, name, location):
        self.business[name] = location
        
        return {"message": "Business added succesfully"}