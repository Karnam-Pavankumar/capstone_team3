import logging
logging.basicConfig(filename="mylogdetails.txt",level=logging.INFO)
logging.info("A New Log came")
try:
    n1=int(input("Enter the First Number"))
    n2=int(input("Enter The Second Number"))
    print(n1/n2)
except ZeroDivisionError as e:
    print("Cannot Divide With Zero")
    logging.exception(e)
except ValueError as msg:
    print("value only")
    logging.exception(msg)
logging.info("Log is Recorded")