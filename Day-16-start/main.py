import another_module

import turtle
from prettytable import PrettyTable

if __name__ == '__main__':
    table = PrettyTable()
    table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
    table.add_column("Type", ["Electric", "Water", "Fire"])
    table.align = "l"

    print(table)
    

    # timmy = turtle.Turtle()
    # timmy.shape("turtle")
    # timmy.color("#009999")
    # timmy.forward(100)
    
    # my_screen = turtle.Screen()
    # my_screen.exitonclick()

    # print(another_module.another_var)

