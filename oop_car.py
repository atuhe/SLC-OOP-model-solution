class Car(object):
    def __init__(self, name="Corona", model="T2016", type="Toyota"):
        self.type = type
        self.model = model
        self.name = name
        self.speed = 0
        
        if self.type == "Toyota" or self.type == "mark11":
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
        if self.type == "Lorry":
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4
            
    def is_saloon(self):
        if self.type == "lorry":
            return False
        else:
            return True
        
    def drive(self, speed):
        self.speed += speed
        return self.speed
    
#mycar = Car("Corona", "T2016", "Toyota")
#print (mycar.drive(400))
