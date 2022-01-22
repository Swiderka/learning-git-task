shopping_list= {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
  }
print(shopping_list)
for sklep, produkty in shopping_list.items():
  print("Idę do", sklep ,", kupuję tu następujące rzeczy", [i for i in produkty])
  