import logging 

logger = logging.getLogger("week-nine-comprehension")
logger.setLevel(logging.DEBUG) # DEBUG, INFO, WARNING, ERROR, CRITICAL

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

logger.addHandler(console)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_nums = [even_num for even_num in list1 if (even_num%2) == 0]
logger.info(even_nums)

list2 = ["hello", "How", "are", 'You!']

upper_case = [word.upper() for word in list2]
logger.info(upper_case)

list3 = ["hello", "Apple", "Banan", "Ptato", "Tomato"]
word_lens = [len(word) for word in list3]
logger.info(word_lens)

list4 = [-1, -2, -3, -0.5, 1, 3, 4, -2, 0]
neg_nums = [num if num > 0 else 0 for num in list4 ]
logger.info(neg_nums)

#even and odd using else if 

list5 = [12, 13, 14, 15, 16 ,17 ,18]

even_nums = ["Even" if num%2 == 0 else "Odd" for num in list5]
logger.info(even_nums)

# replace none with missing

list6 = ["Apple", "mango", None, "Help", None, None]
cleaned_up = ["Missing" if val == None else val for val in list6]
logger.info(cleaned_up)


