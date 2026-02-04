"""7) დაწერეთ ფუნქცია tuple_info, რომელიც მიიღებს tuple-ს და დაბეჭდავს მის სიგრძეს, პირველ და ბოლო ელემენტს"""
def tuple_info(input_tuple):
    print(f"Tuple სიგრძე: {len(input_tuple)}")
    print(f"პირველი ელემენტი: {input_tuple[0]}")
    print(f"ბოლო ელემენტი: {input_tuple[-1]}")