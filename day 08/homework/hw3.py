"""6) კომენტარებით დაწერეთ რით განსხვავდება integer და float მონაცემთა ტიპები"""
#integer - ინტეგერი წარმოადგენს მთელ რიცხვებს, ის არ მოიცავს წილადებს. ინტეგერის დროს ჩვენ ზუსტ პასუხს არ ვიღებთ
#float - ფლოათი მოიცავს წილადებს, ის არ მოიცავს მთელ რიცხვებს. ფლოათს ვიყენებთ როცა საჭიროა მივიღოთ ზუსტი პასუხი

"""7) integer და float მონაცემთა ტიპის ცვლადებზე შეასრულეთ 20 მაგალითი ოპერატორებით: +, -, *, /, **, %"""

int1 = 10
float1 = 3/4
int2 = 20
float2 = 1/2
int3 = 25
float3 = 1/4
int4 = 50
float4 = 1/10

print(int1 + float1)
print(int2 - float2)
print(int3 * float3)
print(int4 / float4)
print(int1 ** int2)
print(float1 % float2)
print(int3 + int4)
print(float3 - float4)
print(int1 * float4)
print(float1 / int4)
print(int2 ** float3)
print(float2 % int3)
print(int3 - float2)
print(float3 * int2)
print(int4 / float1)
print(float4 ** int1)
print(int1 % int4)
print(int2 + int3)
print(float1 * float4)
print(float2 / float3)
