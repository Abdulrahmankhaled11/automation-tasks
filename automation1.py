import inflect
n =inflect.engine()

numb = int(input('enter the number :'))
print( 'number in words :',n.number_to_words(numb))