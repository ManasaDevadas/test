from datetime import datetime, timedelta
import time
import uuid
import random


class OrdersManager:
     #step 2 initialize few variables. 1st __orders is a List. 
    __orders = []
    __orders_processed = 0
    __last_printed_log = datetime.now()

    #step3 init method calls __generate_fake_orders with quantity set to 1000; def is the syntax for function(method) definition
    def __init__(self) -> None:
    #calling __generate_fake_orders
        self.__generate_fake_orders(quantity=1_000)

#step4  __generate_fake_orders 4.1 call method __log function, 4.2.sets the list of array of __orders to random UUIDS, 4.3 again calls __log.
    def __generate_fake_orders(self, quantity):
        self.__log(f"Generating fake orders")
    # 4.2.sets the list of array of __orders to random UUIDS
    # eg of first two elements generated by below line of code - 
    #[(UUID('8e12fa0c-aee0-4c3c-b528-21c1b942a941'), 0), (UUID('c6423cfe-a749-4372-9969-5142b51663c3'), 1)]
        self.__orders = [(uuid.uuid4(), x) for x in range(quantity)]
        self.__log(f"{len(self.__orders)} generated...")

# this method is called in multiple places to just do a print.
    def __log(self, message):
        print(f"{datetime.now()} > {message}")

# the below method splits the list of tuples and saves first element UUID to id and number to number.
# then logs a message
# then sleeps . This method is not called inside process_orders. , so this comes as step 8.
    def __fake_save_on_db(self, order):
        id, number = order

        self.__log(
            message=f"Order [{id}] {number} was successfully prosecuted."
        )

        time.sleep(random.uniform(0, 1))

#this method calls fake_save db(above method, increments order_processed, 
#compares current time to last printed log time, increments to 5 seconds. Actually 5 seconds is not lapsed. 
#just addingit
    def process_orders(self):
        for order in self.__orders:
            self.__fake_save_on_db(order=order)
            self.__orders_processed += 1

            if datetime.now() > self.__last_printed_log:
                self.__last_printed_log = datetime.now() + timedelta(seconds=5)
                self.__log(
                    message=f"Total orders executed: {self.__orders_processed}/{len(self.__orders)}"
                )


#
#
# ---
######step1 Instantiating OrderManager class, this will run all functions you CALL inside the class. 
#start from init. 
#The __init__ method is the Python equivalent of the C++ constructor in an object-oriented approach. 
#The __init__ function is called every time an object is created from a class. 
#The below statement is creating an object.

orders_manager = OrdersManager() 

start_time = time.time()

#step 7 call process orders.
orders_manager.process_orders()

#current time - starttime gives delay, print it finally
delay = time.time() - start_time

print(f"{datetime.now()} > Tiempo de ejecucion: {delay} segundos...")