"""2) შექმენით manual_max ფუნქცია რომელსაც პარამეტრად გადაეცემა სია და აბრუნებს ყველაზე დიდ მნიშვნელობას. ასევე შექმენით manual_len ფუნქცია რომელიც თვლის გადაცემული მიმდევრობის სიგრძეს"""


def manual_max(arr):
    max1 = arr[0]
    for number in arr:
        if number > max1:
            max1 = number
    return max1 

def manual_len(arr):
    count = 0
    for num in arr:
        count += 1
    return count