import astron
import stellargraph

def greeting():
    print("      ╭───────────.★..─╮  ")
    print("      |    Stellaron    |  ")
    print("      ╰─..★.───────────╯  ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⣀⡴⢧⣀⠀⠀⣀⣠⠤⠤⠤⠤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠘⠏⢀⡴⠊⠁⠀⠀⠀⠀⠀⠀⠈⠙⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠘⢶⣶⣒⣶⠦⣤⣀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⢀⣰⠃⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣟⠲⡌⠙⢦⠈⢧⠀")
    print("⠀⠀⠀⣠⢴⡾⢟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⣸⡴⢃⡠⠋⣠⠋⠀")
    print("⠐⠀⠞⣱⠋⢰⠁⢿⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⣀⣠⠤⢖⣋⡥⢖⣫⠔⠋⠀⠀⠀")
    print("⠈⠠⡀⠹⢤⣈⣙⠚⠶⠤⠤⠤⠴⠶⣒⣒⣚⣩⠭⢵⣒⣻⠭⢖⠏⠁⢀⣀⠀⠀⠀⠀")
    print("⠠⠀⠈⠓⠒⠦⠭⠭⠭⣭⠭⠭⠭⠭⠿⠓⠒⠛⠉⠉⠀⠀⣠⠏⠀⠀⠘⠞⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢤⣀⠀⠀⠀⠀⠀⠀⣀⡤⠞⠁⠀⣰⣆⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠘⠿⠀⠀⠀⠀⠀⠈⠉⠙⠒⠒⠛⠉⠁⠀⠀⠀⠉⢳⡞⠉⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("\n")

def menu():
    greeting()
    abc = "A. Print all constellation abbreviations and their ID number\nB. Display a constellation\nC. Exit"
    numc = "Type the ID number (0-87) of the constellation you want to check, OR press C to return: "
    exitmsg = "\n *   .        *       .       .       *  ˗ˏˋ ★ ˎˊ˗\n"
    donemsg = "\n˗ˏˋ ★ ˎˊ˗\n"
    while True:
        print(abc)
        op = input("Option: ")
        if op.lower() == 'c':
            op = False
            print(exitmsg)
            break
        elif op.lower() == 'a':
            print(astron.ct)
        elif op.lower() == 'b':
            while True:
                op = input(numc)
                if op.lower() == 'c':
                    print(exitmsg)
                    break
                elif (int(op) >= 0) and (int(op) <= 87):
                    print(astron.ct[int(op)])
                    stellargraph.ct_graph(int(op))
                    print(donemsg)
                else:
                    continue

# MAIN ----------------------------------------------------
if __name__ == "__main__":
    menu()