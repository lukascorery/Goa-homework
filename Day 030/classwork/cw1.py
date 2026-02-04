"""1) თითოეულ მეთოდზე: len, append, insert, pop, remove მეთოდებზე გააკეთეთ 3-3 მაგალითი. len ფუნქციაზე მოიყვანეთ string-ის მაგალითიც"""



print(len("hello"))  
print(len([1, 2, 3, 4, 5])) 
print(len([]))  



my_list = [1, 2, 3]
my_list.append(4)  
my_list.append(5)  
my_list.append(6)  


my_list.insert(0, 0)  
my_list.insert(3, 3.5)  
my_list.insert(7, 7)  
print(my_list)


my_list.pop()  
my_list.pop(0)  
my_list.pop(2)  
print(my_list)
