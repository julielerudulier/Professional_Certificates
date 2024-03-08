from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."

# Knowledge we get from the puzzle statement:
statement0 = And(AKnight, AKnave)

knowledge0 = And(
    # The character is either a knight or a knave:
    Or(AKnight, AKnave),

    # No character can bo two characters at the same time:
    Not(And(AKnight, AKnave)),

    # If the statement is true, then A is a knight. Otherwise if it is false, A is a knave:
    Biconditional(AKnight, statement0)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.

# Knowledge we get from the puzzle statement:
statement1 = And(AKnave, BKnave)

knowledge1 = And(
    # A is either a knight or a knave:
    Or(AKnight, AKnave),

    # B is either a knight or a knave:
    Or(BKnight, BKnave),

    # No character can bo two characters at the same time:
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    # If the statement is true, then the character who said - A - it is a knight. Otherwise if it is false, A is a knave:
    Biconditional(AKnight, statement1)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

# Knowledge we get from the puzzle statement:
statement2a = Or(And(AKnight, BKnight), And(AKnave, BKnave))
statement2b = Or(And(AKnight, BKnave), And(AKnave, BKnight))

knowledge2 = And(
    # A is either a knight or a knave:
    Or(AKnight, AKnave),

    # B is either a knight or a knave:
    Or(BKnight, BKnave),

    # No character can bo two characters at the same time:
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    # If the statement is true, then the character who said it is a knight. Otherwise if it is false, the character is a knave:
    Biconditional(AKnight, And(statement2a)),
    Biconditional(BKnight, And(statement2b))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

# Knowledge we get from the puzzle statement:
statement3a = Or(AKnight, AKnave)
statement3b = Biconditional(AKnight, AKnave)
statement3c = Biconditional(CKnight, CKnave)
statement3d = Biconditional(AKnight, AKnight)

knowledge3 = And(
    # A, B and C can either be knights or knaves:
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),

    # No character can bo two characters at the same time:
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    # If the statement is true, then the character who said it is a knight. Otherwise if it is false, the character is a knave:
    Biconditional(AKnight, And(statement3a)),
    Biconditional(BKnight, And(statement3b)),
    Biconditional(BKnight, And(statement3c)),
    Biconditional(CKnight, And(statement3d))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
