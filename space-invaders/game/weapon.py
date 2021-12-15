#
# Description:
#   The following class creates a projectile, an Actor coming from the Ship that 
#   that "fired it" and sets its velocity towards the opposite direction.
#
# OOP Principles Used:
#   Abstraction.
#   Polymorphism.
#   Inheritance.
#
# Reasoning:
#   Polymorphism because the class alters the Execute method actions from the Action class.
#   Inheritance because it inherits the Action class.
#   Abstraction because a lot of the complexity behind creating the Actor beam is hidden by 
#   working with mostly actors and their methods under each if statement.


from game.actor import Actor
import random
from game.point import Point
from game.action import Action


class Weapon(Action):
    
    def execute(self, cast):

        ship = cast["player_ship"][0]
        
        if ship.is_shooting():

            cast["beams"] = []
            beam = Actor()
            velocity = ship.get_beam_velocity()
            position = ship.get_position()
            position = position.add(Point(1, 0))
            beam.set_position(position)
            beam.set_text("|")
            beam.set_velocity(velocity)
            ship.set_shooting(False)
            
            # We remove the previous beam in the array and add the new one.
            
            cast["beams"].append(beam)
        

        invaders_array_size = len(cast["invaders"])
        invader_i = random.randrange(0, invaders_array_size * 6)
        
        if invader_i < invaders_array_size:
            invader_beam = Actor()
            invader_ship = cast["invaders"][invader_i]
            position = invader_ship.get_position()
            velocity = invader_ship.get_beam_velocity()
            invader_beam.set_position(position)
            invader_beam.set_text("*")
            invader_beam.set_velocity(velocity)

            cast["invader_beams"].append(invader_beam)







