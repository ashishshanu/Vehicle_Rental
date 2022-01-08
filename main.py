import uuid
from csv import *
from datetime import datetime


def show_customer_list():
    with open('customer.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            if not row:
                pass
            else:
                print(row)


def show_inventory_list():
    with open('inventory.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        res = [ele for ele in list_of_rows if ele != []]
        print(res)


def show_booking_list():
    with open('booked_vehicles.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        res = [ele for ele in list_of_rows if ele != []]
        print(res)


class Customer:
    def __init__(self, customer_name, mobile_number, emaail):
        self.name = customer_name
        self.mobile = mobile_number
        self.email = emaail

    def customer_list(self):
        id = uuid.uuid1()
        temp_list = [id, self.name, self.mobile, self.email]

        with open('customer.csv', 'a', newline=None) as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(temp_list)
            f_object.close()
            print('Customer Added Successfully', ' : ', 'Customer ID is: ', id)


class Vehicles:
    def __init__(self, v_type):
        self.v_type = v_type

    def inventory_list(self):
        id = uuid.uuid1()
        temp_list = [id, self.v_type]

        with open('inventory.csv', 'a', newline=None) as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(temp_list)
            f_object.close()


def vehicle_return():
    vehicle_number = input('Please Enter Vehicle Number Here: ')
    with open('booked_vehicles.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        booked_vehicle = [ele for ele in list_of_rows if ele != []]
        for i in range(len(booked_vehicle)):
            if booked_vehicle[i][4] == vehicle_number:
                inventory_item = booked_vehicle[i][4:6]
                booked_vehicle.remove(booked_vehicle[i])
                with open('inventory.csv', 'a', newline=None) as c_object:
                    writer_object = writer(c_object)
                    writer_object.writerow(inventory_item)
                    c_object.close()
                with open('booked_vehicles.csv', 'w', newline=None) as c_object:
                    writer_object = writer(c_object)
                    for c in booked_vehicle:
                        writer_object.writerow(c)
                    c_object.close()


def booking_rentals():
    with open('inventory.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        l_l = [ele for ele in list_of_rows if ele != []]
    with open('customer.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_row = list(csv_reader)
        c_l_l = [ele for ele in list_of_row if ele != []]
    customer_wants_to_book = input("please enter what you want to book"
                                   "'car', bike, boat: ")
    booked_customer_list = []
    if len(l_l) > 0:
        for i in range(len(l_l)):
            if l_l[i][1] == customer_wants_to_book:
                customer_id = str(input("please enter customer_id: "))
                booked_vehicles = l_l[i]
                l_l.remove(l_l[i])
                for j in range(len(c_l_l)):
                    if c_l_l[j][0] == customer_id:
                        customer_details = c_l_l[j]
                        c_l_l.remove(c_l_l[j])
                        customer_details.extend(booked_vehicles)
                        now = datetime.now()
                        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                        customer_details.append(str(dt_string))

                        with open('booked_vehicles.csv', 'a', newline=None) as a_object:
                            writer_object = writer(a_object)
                            writer_object.writerow(customer_details)
                            a_object.close()
                        with open('inventory.csv', 'w', newline=None) as b_object:
                            writer_object = writer(b_object)
                            for l in l_l:
                                writer_object.writerow(l)
                            b_object.close()
                        with open('customer.csv', 'w', newline=None) as c_object:
                            writer_object = writer(c_object)
                            for c in c_l_l:
                                writer_object.writerow(c)
                            c_object.close()
                            print("Booking Successfully")

                            break
                    else:
                        print('Customer Not Added to Databse')
            else:
                print('Vehicle Not Available for Booking! Sorry for inconvenience')
                break
    else:
        print('No Vehicle Available for Booking')


def create_customer():
    c = Customer(customer_name=input('Please Enter Customer Name: '), mobile_number=int(input('Please Enter '
                                                                                              'Mobile Number: '
                                                                                              '')),
                 emaail=input('Please Enter Customer E-mail: '))
    c.customer_list()


def create_vehicle():
    v = Vehicles(v_type=input('Please Enter Vehicle Type: '))
    v.inventory_list()


def terminate():
    print('Bye bye')


if __name__ == '__main__':

    choice = 0
    options = {
        0: print(),
        1: create_customer,
        2: booking_rentals,
        3: show_customer_list,
        4: show_booking_list,
        5: show_inventory_list,
        6: create_vehicle,
        7: vehicle_return,
        8: terminate
    }
   
    print('----------Welcome-----------')
    while choice != 8:
        print("1. Add Customer")
        print("2. Add Rental Booking")
        print("3. See customer list")
        print("4. See rental booking list")
        print("5. See inventory of vehicles available")
        print("6. Add inventory")
        print("7. Vehicle Return")
        print("8. Exit")
        try:
            choice = int(input("Please enter your choice: "))
            options[choice]()
        except KeyError as ke:
            print('Please Enter Valid Input!!')
