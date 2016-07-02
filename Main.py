from Speech import Speech
from Bomb import Bomb
import modules.Wires as Wires
import modules.Button as Button
import modules.Keypad as Keypad
import modules.Simon as Simon
import modules.Memory as Memory

r = Speech()
r.calibrate(duration=2)

b = Bomb()

while True:
    print("1. On the Subject of Wires")
    print("2. On the Subject of The Button")
    #print("3. On the Subject of The Keypad")
    print("4. On the Subject of Simon Says")
    print("6. On the Subject of Memory")
    print("12. Run Setup") # run setup
    print("13. Reset Memory")
    print("20. Reset everything") # wipe past data
    r.say("Select a module")
    choice = r.listen("grammars/menu.gram")
    # select module
    if choice == "defuse wires":
        Wires.solve(r, b)
    elif choice == "defuse button":
        Button.solve(r, b)
    #elif choice == "defuse keypad":
        #Keypad.solve(r, b)
    elif choice == "defuse simon says":
        Simon.solve(r, b)
    elif choice == "defuse memory":
        Memory.solve(r, b)

    elif choice == "bomb setup":
        b.setup(r)

    elif choice == "reset memory":
        Memory.reset(r)
    elif choice == "terminate" or choice == "exit":
        print("---Exit---")
        r.say("goodbye")
        break
