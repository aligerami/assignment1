import time
class time_:
    def __init__(self):
        self.set_time(int(time.time() ))
    def get_hour(self):
        return self.__hour
    def get_minute(self):
        return self.__minute
    def get_second(self):
        return self.__second
    def set_time(self,elaps_time):
        self.__hour=elaps_time//3600
        time_in_second=elaps_time-self.__hour*3600
        self.__minute=time_in_second//60
        time_in_second=time_in_second-self.__minute*60
        self.__second=time_in_second
        if self.__hour>24:
            self.__hour=self.__hour%24
    def print(self):
        print("Time is ", self.get_hour(),":",self.get_minute(),":",self.get_second())       

def main():
    t=time_()
    t.print()
    t.set_time(55550505)
    t.print()
main()

        
    
        