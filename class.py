class Car(object):

  def __init__(self, model, company, color, speed_limit):
    self.color = color 
    self.company = company 
    self.speed = speed_limit
    self.model = model  

  def start(self):
    print("started")

  def stop(self):
    print("stopped")

  def accelarate(self):
    print("accelarating")

  def change_gear(self, gear_type):
    print("change_gear")   

audi = Car("a6", "red","audi",80)
     
      


       
print(audi.start())
print(audi.stop())
print(audi.accelarate())        