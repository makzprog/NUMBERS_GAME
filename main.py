from game_logic import NumberGenerator, ConsoleUI, GameEngine

if __name__ == "__main__":
    # Dependency Injection: create objects and pass them to the engine
    num_gen = NumberGenerator()
    console_ui = ConsoleUI()
    
    game = GameEngine(num_gen, console_ui)
    game.run()