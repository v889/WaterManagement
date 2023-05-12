import math

# Constants
CORPORATION_WATER_COST = 1
BOREWELL_WATER_COST = 1.5
SLAB_RATES = [
    (500, 2),
    (1500, 3),
    (3000, 5),
    (math.inf, 8)
]

# Global variables
apartment_type = None
apartment_person=0
corporation_ratio = None
borewell_ratio = None
total_guests = 0
total_water_consumed = 0
total_cost = 0

def allot_water(apartment, ratio):
    global apartment_type, corporation_ratio, borewell_ratio, total_water_consumed
    apartment_type = apartment

    ratios = ratio.split(':')
    corporation_ratio = int(ratios[0])
    borewell_ratio = int(ratios[1])

    total_water_consumed = 0

def add_guests(num_guests):
    global total_guests
    total_guests += num_guests

def calculate_water_cost():
    global total_water_consumed, total_cost
    if (apartment_type == 2):
        apartment_person = 3
    else:
        apartment_person = 5
    total_water_apartment_person=apartment_person*10*30

    corporation_water = (total_water_apartment_person* corporation_ratio)/(corporation_ratio+borewell_ratio)
    borewell_water = (total_water_apartment_person * borewell_ratio)/(corporation_ratio+borewell_ratio)
    total_water_consumed += total_water_apartment_person
    total_water_consumed+=total_guests*10*30
    tanker_water = total_water_consumed - (corporation_water + borewell_water)
    total_cost = corporation_water * CORPORATION_WATER_COST + borewell_water * BOREWELL_WATER_COST

    for slab, rate in SLAB_RATES:
        if tanker_water <= 0:
            break
        if tanker_water > slab:
            water_in_slab = slab
        else:
            water_in_slab = tanker_water
        total_cost += water_in_slab * rate
        tanker_water -= water_in_slab

def print_bill():
    global total_water_consumed, total_cost
    print(total_water_consumed, total_cost)

# Main program
while True:
    command = input().split()
    if command[0] == "ALLOT_WATER":
        allot_water(int(command[1]), command[2])
    elif command[0] == "ADD_GUESTS":
        add_guests(int(command[1]))
    elif command[0] == "BILL":
        calculate_water_cost()
        print_bill()
        break
