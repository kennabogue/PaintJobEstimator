#Paint Job Estimator

print("This program estimates the cost to complete a paint job.")

do_calculation = True
while (do_calculation):

#Operation Costs
    labor_hours = float("6")
    labor_per_hour = float("62.25")
    base_paint_gallon = float("1")
    base_wall_space = float("350")

#Ask the user to enter square feet of wall space and price of paint
    while (True):
        try:
            job_wall_space = float(input("Enter the square feet of wall space to be painted: "))
            if (job_wall_space < 0):
                print("Negative values are not valid. Only positive values are valid.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break
    while (True):
        try:
            price_of_paint = float(input("Enter the price of paint per gallon: "))
            if (price_of_paint < 0):
                print("Negative values are not valid. Only positive values are valid.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break
        

# perform the calculation
    import math
    total_gallons = (math.ceil(job_wall_space / base_wall_space * base_paint_gallon))
    total_hours = (job_wall_space / base_wall_space * labor_hours)
    paint_cost = (total_gallons * price_of_paint)
    labor_cost = (total_hours * labor_per_hour)
    job_cost = (paint_cost + labor_cost)
    

# output the result
    print("\nThe number of gallons of paint required is", total_gallons)
    print("\nThe hours of labor required is", round(total_hours, 1))
    print("\nThe cost of the paint is $", round(paint_cost, 2))
    print("\nThe labor charges are $", round(labor_cost, 2))
    print("\nThe total cost of the paint job $", round(job_cost, 2))
    
     
# ask user to repeat
    another_calculation = input("Do you want to perform another calculation? (y/n): ")
    if (another_calculation != "y"):
        do_calculation = False


