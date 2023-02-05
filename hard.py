# Задача HARD необязательная Имеется список чисел. Создайте список, в который попадают числа, описывающие 
# максимальную возрастающую последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]

# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]

# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]

# from random import randint
# x = randint(8,9)
# lst = list()
# for i in range(x) :
#     lst.append(randint(-1,10))
# print(lst)
lst = [1, 5, 2, 3, 4, 6, 1, 7]
x=8
count = 0
count_max=0
lst_max = 0
lst_min = 0
lst_maxm = 0
lst_minm = 0
for i in range(0,x-1):
    if lst[i]+1==lst[i+1]:
        count+=1
        lst_min=lst[i]
        lst_max = lst[i+1]
        for k in range(0,x):
            if lst_max+1==lst[k]:
                count+=1
                lst_max = lst[k]
         
            if  lst_min-1==lst[k]:
                count+=1
                lst_min = lst[k]
            if  count>count_max:
                count_max=count
                lst_maxm = lst_max
                lst_minm = lst_min
    count=0     
# print(count_max) 
print(lst_minm,lst_maxm) 
    
       
            
            
            
            

  
        
        
        
        

        

  




