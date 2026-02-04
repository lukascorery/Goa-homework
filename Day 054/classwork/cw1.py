# 1) შექმენით პროდუქტების dictionary. შემდეგ გაფილტრეთ ეს dictionary და დატოვეთ ის პროდუქტები რომელთა ფასი ნაკლებია 100-ზე. საბოლოოდ დაბეჭდეთ ეს dictionary.


products = {
    "apple": 50,
    "banana": 30,
    "cherry": 120,
    "blueberry": 90,
    "watermelon": 150

}


filtered_products = {product: price for product, price in products.items() if price < 100}

print(filtered_products)