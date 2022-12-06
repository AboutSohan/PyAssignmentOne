mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here
i = 0
while i < len(mobile_data.get('data')):
    phone_model = mobile_data.get('data')[i].get('name')

    phone_price = float(mobile_data.get('data')[i].get('price').split()[0]) # Accessing, Splitting and converted to float in a single line.
    price_bdt = round(phone_price * float(mobile_data.get('exchnage_rate')),2)
    phone_country = mobile_data.get('data')[i].get('made')

    i = i + 1

    sentence = f"{phone_model} is an Android smartphone. It is made in {phone_country}. The price of this phone is {phone_price} in the global market. The expected price of this phone is {price_bdt} Taka in Bangladesh."
    print(sentence)
    print('*' *100)

""" আওয়াল ভাই আমি এইটা মোটেও ১৫ মিনিটে শেষ করতে পারিনাই; বুঝার সময় খুব ভালোই বুঝতে পারি; ইমপ্লিমেন্ট করতে গিয়ে দেখলাম; প্রচুর প্র্যাকটিস করা দরকার আরও আরও আরও"""

