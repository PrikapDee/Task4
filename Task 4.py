#PAT 4 ques1 create a python class called circle with constructior which will take a list as an argument for task.
#The list is [10,501,22,37,100,999,87,351]
#define class as a circle
class Circle: 
    #private variable declaration
    __private_var=3.141 
#init constructor with parameter as list
    def __init__(self,list): 
        self.list=list
        
#creation of area of circle funtion
    def Areaofcircle(self): 
        area=[]
        for i in self.list:
            area=area + [i*i]
        return area
      
#creation od function to calculate parimeter of circle
    def ParimeterofCircle(self):
        parimter=[]
        for i in self.list:
            parimter= parimter + [2*self.__private_var*i]
        return parimter
#Object of circle class creation
obj1=Circle([10,501,22,37,100,999,87,351]) 
# calling of function to calcualte area of circle
print(obj1.Areaofcircle()) 
#Calling of function to calcualte parimter of circle
print(obj1.ParimeterofCircle())



#Pat 4 Qyes 2 convert from UML diagram
 #Parent class TV
class Tv: 
    channel=1
    price=0
    inches=0
    onoff_status=True
    Volume=50
    #init cosntructor
    def __init__(self,brand,channel,volume,onoff_status): 
        self.brand=brand
        self.channel=channel
        self.volume=volume
        self.onoff_status=onoff_status
        #function to set volumne
    def set_volume(self): 
        if self.volume<0 or self.volume>100:
            pass
            return("no change in volume")
        else:
             return self.volume
         #function to set channel in TV
    def set_channel(self): 
        if self.channel>50:
            pass
         
        else:
           return self.channel
          #function to reset TV
    def reset_TV(self): 
         self.channel="1"
         self.volume="50"
         return("value set {} channel, {} volumne".format(self.channel,self.volume))
               
    #to show status of TV
    def display_status(self): 
         return ("{} at channel {} , volume {}".format(self.brand,self.channel,self.volume))

       

#child class in inherit from TV class
class LED(Tv):
    
 
    def __init__(self,brand,channel,volume,onoff_status,thickness,usage, Lifespan,rate,viewangle,mode): #init cosntructor
        self.thickness=thickness
        self.usgae=usage
        self.Lifespan=Lifespan
        self.rate=rate
        self.viewangle=viewangle
        self.mode=mode

        Tv.__init__(self,brand,channel,volume,onoff_status)
        
    
    def viewangel(self,viewangle): 
        if self.viewangle>=5 and self.viewangle<=15:
            return("best view angle ")
        else :
            return("adjust the view angle in between 5 to 15 degress")

    def display_details(self):
        print("child class function led")
        return("Brandname {},volume {},thickness {},usage {},lifespan {},energyrate {}".format(self.brand,self.channel,self.volume,self.thickness,self.usgae,self.Lifespan,self.rate))

    def backlight_feature(self,mode): 
       if self.mode==True:
           return("brightness in room")
       else :
       
          return"no brightness in room"


   
class Plasma(Tv): 

    def __init__(self,brand,channel,volume,onoff_status,thickness,usage,Lifespan,rate,viewangle,mode):
        self.thickness=thickness
        
        self.usgae=usage
        self.Lifespan=Lifespan
        self.rate=rate
        self.viewangle=viewangle
        self.mode=mode

        Tv.__init__(self,brand,channel,volume,onoff_status)

    def viewangel(self,viewangle): 
        if self.viewangle>=5 and self.viewangle<=15:
            return("best view angle ")
        else :
            return("adjust the view angle in between 5 to 15 degress")

    def backlight_feature(self,mode): 
       if self.mode==True:
           return("brightness in room")
       else :
       
          return("no brightness in room")

    def display_details(self):
        print("child class function Plasma")
        return("Brandname {},volume {},thickness {},usage {},lifespan {},energyrate {}".format(self.brand,self.channel,self.volume,self.thickness,self.usgae,self.Lifespan,self.rate))



obj1=Tv("onida",20,120,"on")
print(obj1.set_volume())
print(obj1.display_status())
print(obj1.reset_TV())
print(obj1.display_status())
obj2=LED("Panasonic",30,23,"on",5.3,5,"4years","5Kwh",5,"TRUE")
print(obj2.display_status())
print(obj2.display_details())
print(obj2.viewangel(5))
print(obj2.backlight_feature(True))
obj3=Plasma("sony",30,23,"on",5.3,5,"4years","5Kwh",29,"false")
print(obj3.display_status())
print(obj3.display_details())
print(obj3.viewangel(40))
print(obj3.backlight_feature(False))


    
    
		
    

    