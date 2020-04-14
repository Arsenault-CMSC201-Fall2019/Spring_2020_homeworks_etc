def flight(height):
    # the function that calculates how many steps it will
    # take before an object - a hailstone, in particular
    # falls to the ground on this strange new planet

    # first, write the base case code. What happens if the
    # hailstone is 1 foot or less from the ground?

    if height <= 1:
        return #complete the return statement

    elif:

    # now, there are two recursive cases. You have to
    # write the code for each of them. They are:
    # the height is an even number;

        height : #what makes a number even?
        # what should you do for an even number?
        # what should you return?

    # and the height
    # is an odd number

        else:
            # what do you do for an odd number?
            # what should you return? 

if __name__ == "__main__":

    # first, prompt the user to input the height in feet of the hailstone.
    # convert that height into an integer

    distance = int(input("How far above the ground is the hailstone?"))

    # Now write the initial call to the function. The return value
    # will be the number of steps it takes for the hailstone to
    # reach the ground

    steps = flight()  #insert the argument(s) needed

    # Now print out the result

    print("The hailstone fell to the ground in ", steps, " steps.")

    

        
