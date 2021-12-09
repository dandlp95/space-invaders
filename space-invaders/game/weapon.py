from game.actor import Actor
import random
from game.point import Point


class Weapon:
    
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
            
            # We remove the previous beam in the array and add the new one.
            
            cast["beams"].append(beam)
        

        invaders_array_size = len(cast["invaders"])
        invader_i = random.randrange(0, invaders_array_size * 20)
        
        if invader_i < invaders_array_size:
            invader_beam = Actor()
            invader_ship = cast["invaders"][invader_i]
            position = invader_ship.get_position()
            velocity = invader_ship.get_beam_velocity()
            invader_beam.set_position(position)
            invader_beam.set_text("*")
            invader_beam.set_velocity(velocity)

            cast["invader_beams"].append(invader_beam)







