import turtle

def convert_from_kawuub(kawuub_str):
    # Split the input string into a list of binary values
    binary_values = kawuub_str.split()

    # Initialize an empty string to store the ASCII output
    ascii_characters = ""

    # Process each binary value
    for b in binary_values:
        # Ensure the binary value is exactly 8 bits
        octolong_binary = b.zfill(8)[:8]

        # Convert the 8-bit binary value to an ASCII character
        try:
            ascii_char = chr(int(octolong_binary, 2))
            ascii_characters += ascii_char
        except ValueError:
            print(f"Error converting {octolong_binary} to an ASCII character.")
            ascii_characters += '?'

    return ascii_characters
    
def kawuubify(phrase,line_length):
    # Function to lift the pen, move to a new position, and lower the pen
    def lift_and_go(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    # Initialize the turtle and screen
    t = turtle.Turtle()
    screen = turtle.Screen()
    
    # Set up the screen to fullscreen mode
    screen.setup(width=1.0, height=1.0)
    
    # Define starting positions and dimensions
    start_x = -930
    start_y = 450
    char_width = 3 * line_length
    bound_x = abs(start_x)
    
    # Move turtle to the starting position
    lift_and_go(start_x, start_y)
    
    # Set turtle speed and disable animation for instant drawing
    turtle.tracer(0)
    # Iterate through each character in the phrase
    for char in phrase:
        current_x = t.xcor()
        current_y = t.ycor()
        
        # Move to the next line if the current line is out of bounds
        if current_x + char_width > bound_x:
            lift_and_go(start_x + char_width, current_y - char_width)
        else:
            lift_and_go(current_x + char_width, current_y)
        
        # Replace space with a circle
        if char == " ":
            t.circle(5)  # Draw a circle with radius 5
        else:
            # Draw a small dot for the character position
            t.dot(3)
            
            binary_representation = bin(ord(char))[2:].zfill(8)  # Zero-fill to 8 bits
            print(f'{char}: {binary_representation}')
            
            if len(binary_representation) > 8:
                lift_and_go(current_x + char_width, current_y - line_length)
                t.write(char, align="center", font=("Arial", char_width - line_length, "normal"))
                lift_and_go(current_x + char_width, current_y)
            else:
                # Draw lines based on binary representation of the character
                t.seth(90)
                for bit in binary_representation:
                    t.left(45)
                    if bit == "1":
                        t.forward(line_length)
                        t.backward(line_length)
        
        # Update the screen after each character
        turtle.update()
    
    # Hide the turtle and finish drawing
    t.hideturtle()
    turtle.update()
    turtle.done()

