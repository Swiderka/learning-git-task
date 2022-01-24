shopping_list= {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
  }
print(shopping_list)
for sklep, produkty in shopping_list.items():
  print("Idę do", sklep.capitalize(),", kupuję tu następujące rzeczy", [i.title()for i in produkty])
print("Pozdrawiam mojego wytrwałego Mentora :) trudny Kursant trafił się :D ")
