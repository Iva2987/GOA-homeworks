#იტერატორაცია არის ობიექტი, რომელიც შეიცავს მნიშვნელობების თვლად რაოდენობას. 
# იტერაცია არის ობიექტი, რომელიც შეიძლება განმეორდეს,
#  რაც იმას ნიშნავს, რომ თქვენ შეგიძლიათ გადაუაროთ ყველა მნიშვნელობას.
#for loop- გამოიყენება თანმიმდევრობით გამეორებისთის. 
# ესენი შეიძლება იყოს: სია,სტრიქონი, ლექსიკონი, ნაკრები.
#for loop-არ ჭირდება ინდექსის ცვლადის წინასწარ დაყენება
#for loop-გვაძლევს საშვალებას გამოვიყენოთ იგივე ოპერაცია ციკლის ნებისმიერ დროს 

#while loop-ის მეშვეობით ჩვენ შეგვიძლია შევასრულოთ განცხადედების ნაკრები იქამდე სანამ შედეგი რჩება სწორად(მართლად).

i = 1
while i < 6:
  print(i)
  i += 1

  for x in range(1, 22, 2):
    print(x)