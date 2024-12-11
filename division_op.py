import datetime

def division(dividend, divisor):
    
    try:
        result = dividend / divisor
        status = "No error"
    except Exception as e:
        result = f"ERROR OCCURED : {e}"
        status = "Shit encountered  !"
    finally:
        final = "CODE EXECUTED SUCCESSFULLY"
 
    date = datetime.datetime.now().strftime(" %d - %m - %Y ")
    time = datetime.datetime.now().strftime(" %H : %M : %S ")

    log_entry = f"""DATE : {date}, TIME : {time}, DIVIDEND : {dividend},
      DIVISOR : {divisor}, RESULT : {result}, STATUS : {status}, {final} \n\n"""
    
    with open("DATA", "a") as file:
        file.write(log_entry)

while True:
    dividend = float(input("Enter the DIVIDEND : "))
    divisor = float(input("Enter the DIVISOR : "))
    division(dividend, divisor)

# while True:
#     user_input = input("Enter 'c' to continue (or) 'q' to quit : ")

#     if user_input.lower == "c":
#         try:
#             dividend = float(input("Enter the DIVIDEND : "))
#             divisor = float(input("Enter the DIVISOR : "))
#             division(dividend, divisor)
#         except ValueError:
#             print("INVALID INPUT ! Enter 'c' to continue (or) 'q' to quit. ")
#     elif user_input.lower == "q":
#         print("Exiting the program")
#         break
#     else:
#         pass