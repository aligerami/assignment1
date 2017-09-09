def is_valid(number):
    card_type="none"
    if prefix_matched(number,4):
        card_type="VISA"
    elif prefix_matched(number, 5):
        card_type="MASTER"
    elif prefix_matched(number, 37):
        card_type="AMRICAN EXPRESS"
    elif prefix_matched(number, 6):
        card_type="DISCOVER"
    else:
        return "CARD NUMBER IS INVALID"
    if(sum_of_double_even_place_number(number)+sum_of_odd_place_digit_number(number))%10==0:
        return card_type+" CARD NUMBER IS VALID"
    else :
        return "CARD NUMBER IS INVALID"
        

def sum_of_double_even_place_number(number):
    sum=0
    counter=0
    number_as_string=str(number)
    if(len(number_as_string)%2==0):
        counter=counter+1
    for i in number_as_string:
        counter=counter+1
        if(counter%2==0):
            sum=get_digit_number(int(i)*2)+sum
    return sum 
   
def get_digit_number(number):
    if(number<10):
        return number
    sum=0
    for i in range (0,len(str(number))):
        sum=sum+number%10
        number=number//10
    return sum
        
def sum_of_odd_place_digit_number(number):
    sum=0
    counter=0
    number_as_string=str(number)
    if(len(number_as_string)%2==0):
        counter=counter+1

    for i in number_as_string:
        counter=counter+1
        
        if(counter%2==1):
            sum=int(i)+sum
    return sum
    
def prefix_matched(number,d):
    return d==get_prefix(number, len(str(d)))

def get_size(number):
    return(len(str(number)))

def get_prefix(number,k):
    if(len(str(number))<k):
        return number
    return int(str(number)[0:k])

print(is_valid(4388576018410707))
print(is_valid(4388576018402626))
