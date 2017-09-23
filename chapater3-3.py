import math
ATLANTA_X=33.7489954
ATLANTA_Y=-84.3879824
ORLANDO_X=28.5383355
ORLANDO_Y=-81.3792365
SAVANNAH_X=32.0835407
SAVANNAH_Y=-81.0998342
CHARLOTTE_X=35.2270869
CHARLOTTE_Y=-80.8431267

RADIOUS=6371.01

def calculate_distance(x1,y1,x2,y2):
    return RADIOUS*(math.acos(math.sin(math.radians(x1))*math.sin(math.radians(x2))+math.cos(math.radians(x1))
                           *math.cos(math.radians(x2))*math.cos(math.radians(y1-y2))))
    
def get_area(s1,s2,s3):
    s = (s1+s2+s3)/2   
    return math.sqrt(s*(s-s1)*(s-s2)*(s-s3))

    
ATLANTA_TO_ORLANDO=calculate_distance(ATLANTA_X, ATLANTA_Y, ORLANDO_X, ORLANDO_Y)
ORLANDO_TO_SAVANNAH=calculate_distance(ORLANDO_X, ORLANDO_Y,SAVANNAH_X,SAVANNAH_Y)
ATLANTA_TO_SAVANNA=calculate_distance(ATLANTA_X,ATLANTA_Y,SAVANNAH_X,SAVANNAH_Y)
SAVANNAH_TO_CHARLOTTE=calculate_distance(SAVANNAH_X, SAVANNAH_Y, CHARLOTTE_X, CHARLOTTE_Y)
CHARLOTTE_TO_ATLANTA=calculate_distance(CHARLOTTE_X, CHARLOTTE_Y,ATLANTA_X,ATLANTA_Y)

total_area=get_area(ATLANTA_TO_ORLANDO, ORLANDO_TO_SAVANNAH, ATLANTA_TO_SAVANNA) +get_area(ATLANTA_TO_SAVANNA, SAVANNAH_TO_CHARLOTTE, CHARLOTTE_TO_ATLANTA)

print ("{0:.2f}".format(total_area) , " km2")


