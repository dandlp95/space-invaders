from game.actor import Actor


class Weapon:
    
    def execute(self, cast):

        ship = cast["player_ship"][0]
        
        if ship.is_shooting():

            beam = Actor()
            velocity = ship.get_beam_velocity()
            beam.set_position = ship.get_position()
            beam.set_text("|")
            beam.set_velocity(velocity)
            
            # We remove the previous beam in the array and add the new one.
            cast["beam"] = []
            cast["beam"].append(beam)






