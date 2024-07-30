'''
def temp_func(number):
    collector='0'
    sub_rule={'0':'1','1':'2','2':'0'}
    while len(collector)<int(number):
        temp=''.join(sub_rule[i] for i in collector)
        collector+=temp
    return int(list(collector)[int(number)])



def temp_func(set1,set2):
    set_fin1=set(set1.replace('\n','').split(' '))
    set_fin2=set(set2.replace('\n','').split(' '))
    return {x for x in set_fin1 if (x in set_fin2)}


print(temp_func(setA,setB))

'''
