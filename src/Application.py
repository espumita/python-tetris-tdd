from controllers.GameController import GameController

game_controller = GameController()
game_controller.start()

while True:
    game_controller.iterate()
    game_controller.sleep()
    game_controller.event_handling_process()
