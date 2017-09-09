CURRENT_US_POPULATION=312032486
SECONDS_IN_ONE_YEAR=365*24*60*60

BIRTH_RATE=7
DEATH_RATE=13
IMMIGRATION_RATE=45

for x in (1,2,3,4,5):
    population_in_first_year = CURRENT_US_POPULATION + ((( x * SECONDS_IN_ONE_YEAR)//BIRTH_RATE)
    +((x*SECONDS_IN_ONE_YEAR)//IMMIGRATION_RATE)-((x*SECONDS_IN_ONE_YEAR)// DEATH_RATE))
    print("population in next",x, " year is :" ,population_in_first_year)



