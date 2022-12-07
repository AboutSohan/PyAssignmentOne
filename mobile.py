import random
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
    phone_model_random = [
        f'{phone_model} is an Android smartphone.',
        f'A new smartphone {phone_model} has been released today.',
        f'{phone_model} is a latest smartphone in the market.',
    ]
    phone_model_para = random.choice(phone_model_random)

    phone_country_random = [
        f'It is made in {phone_country}.',
        f'This phone is made in {phone_country}.',
        f'This phone has been assembled in {phone_country}.',

    ]
    phone_country_para = random.choice(phone_country_random)

    phone_price_random = [
        f'The price of this phone is {phone_price} in the global market.',
        f'{phone_price} is the global market price.',
        f'The starting price of this handset is {phone_price} in the global market.',

    ]
    phone_price_para = random.choice(phone_price_random)

    price_bdt_random = [
        f'The expected price of this phone is {price_bdt} Taka in Bangladesh.',
        f'The price of this phone can be about {price_bdt} Taka in Bangladesh.',
        f'{price_bdt} Taka is the estimated price of this phone in Bangladesh.',

    ]
    bd_price_para = random.choice(price_bdt_random)

    # sentence = f"{phone_model} is an Android smartphone. It is made in {phone_country}. The price of this phone is {phone_price} in the global market. The expected price of this phone is {price_bdt} Taka in Bangladesh."

    sentence = f'{phone_model_para} {phone_country_para} {phone_price_para} {bd_price_para}'
    print(sentence)
    print('*' *100)


""" আওয়াল ভাই আমি এইটা মোটেও ১৫ মিনিটে শেষ করতে পারিনাই; বুঝার সময় খুব ভালোই বুঝতে পারি; ইমপ্লিমেন্ট করতে গিয়ে দেখলাম; প্রচুর প্র্যাকটিস করা দরকার আরও আরও আরও"""

