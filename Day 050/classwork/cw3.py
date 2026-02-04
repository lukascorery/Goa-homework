"3) შექნებით რიცხვების სია, შექმენით ახალი ცლვადი სახელად squares, რომელიც შეინახავთ ყველა რიცხვს რომელიც იყო თავდაპირველ სიაში ოღონდ აყვანილ მეორე ხარისხში, ამისთვის გამოიყენეთ list, map და lambda ფუნქციები. ასევე ცვლადი even-ს რომელშიც შეინახავთ თადავპირველ სიაში არსებულ მხოლოდ ლუწ რიცვებს, ამ შემთხვევაში გამოიყენეთ filter ფუნქცია. დაამატეთ manual_map და manual_filter თქვენს დავალებას თუ დრო დაგრჩათ და კომენტარებით ახსენით როგორ მუშაობს map და filter ფუნქცია, ასევე დაწერეთ რა არის lambda გამოსახულება და რატომ არის კარგი"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def square(n):
    return n ** 2

def is_even(n):
    return n % 2 == 0

#  lambda ფუნქცია არის ფუნქცია, რომელიც შეიძლება გამოყენებულ იქნას როგორც map-ის, ასევე filter-ის პარამეტრად და არ საჭიროებს სახელის მინიჭებას
res = list(map(lambda n: n ** 2, numbers))
print(res)

evens = list(filter(lambda x: x% 2 == 0, numbers))
print(evens)

#  map ფუნქცია მუშაობს როგორც ფუნქცია რომელიც გადის iterable-ის ყველა ელემენტზე და ახდენს მათ შეცვლას

res = []
def manual_map(func, iterable):
    for i in iterable:
        res.append(func(i))
    return res

# filter ფუნქცია ფილტრავს iterable-ის ელემენტებს და აბრუნებს მხოლოდ იმ ელემენტებს, რომლებიც აკმაყოფილებენ გარკვეულ პირობას
res1 = []
def manual_filter(func, iterable):
    for i in iterable:
        if func(i):
            res1.append(i)
    return res1


