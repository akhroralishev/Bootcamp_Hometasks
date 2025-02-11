#**Restaurant Bill Calculator**
   #- Create variables for meal cost, tip percentage, and number of people
   #- Calculate and print the total bill and split amount per person
#2-masala
#Choyxona hisob kalkulyatori
meal_cost=27000   #ovqat narxi
tip_percentage=10  #afitsanka foizi
num_people=7 #odamlar soni
# Umumiy hisobni chiqaramiz
total_bill = meal_cost+tip_amount
# Choychaqa miqdorini hisoblash
tip_amount = (meal_cost * tip_percentage) / 100
# Har bir kishi to'lashi kerak bo'lgan summa
split_amount = total_bill / num_people
#natijani chiqaramiz
print(f"Umumiy hisob: {total_bill:.2f} so'm")
print(f"Har bir odam tolashi kerak: {split_amount:.2f} so'm")
