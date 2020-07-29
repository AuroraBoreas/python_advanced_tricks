import sys, os
sys.path.append(os.path.dirname(__file__))
import fpy_34_decoraters

if __name__ == "__main__":
    ### u may see this crystal-clear evidence. decorator @register in this case is running during import
    print("bonjour tout le monde")
    """
    hello add <function f1 at 0x011628A0> into registry
    hello add <function f2 at 0x01162978> into registry
    hello add <function f3 at 0x011629C0> into registry
    bonjour tout le monde
    """