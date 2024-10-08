# Given a list of dictionaries representing credit cards, sort the list in
# descending order according to the `num_users` property. Do the sort out-of
# place without mutating the original list, using the `sorted` built in
# function, and then return only the company names in a list, in the correct
# sorted order.

cards = [
    {
        "company": "Wells Fargo",
        "card_name": "Active Cash",
        "annual_fee": 0,
        "intro_reward_type": "cash",
        "intro_reward_amount": 200,
        "num_users": 20
    },
    {
        "company": "Chase",
        "card_name": "Sapphire Preferred",
        "annual_fee": 95,
        "intro_reward_type": "points",
        "intro_reward_amount": 60000,
        "num_users": 54
    },
    {
        "company": "Citi",
        "card_name": "Diamond Preferred",
        "annual_fee": 0,
        "intro_reward_type": "cash",
        "intro_reward_amount": 150,
        "num_users": 13
    }
]

# Write your code here.
#!!ADD
def sort_cards(card_list):
    pass
#!!END_ADD
#!!START SILENT
# Sorting function to provide the `sorted` built in function
def sorter(card):
    return card['num_users']

def sort_cards(card_list):
    sorted_info = sorted(card_list, key=sorter, reverse=True)
    only_company_names = map(lambda company: company['company'], sorted_info)
    return list(only_company_names)
#!!END

print(sort_cards(cards))        # ['Chase', 'Wells Fargo', 'Citi']