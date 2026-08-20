import logging

#Create logger
logger = logging.getLogger("week-seven-warus-prac")
logger.setLevel(logging.DEBUG)

#create console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

#Add console to logger
logger.addHandler(console)

if num := int(input("Enter a number: "))%2 == 0:
    logger.debug(f"Entered number {num} is EVEN.")
else:
    logger.debug(f"Entered number {num} is ODD.")


