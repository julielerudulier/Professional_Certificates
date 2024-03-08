import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        # Iterate over all variables in domain:
        for var in self.domains:

            # Iterate over all existing values:
            for word in self.crossword.words:

                # If length of value does not match length of variable, remove value from variable's domain:
                if len(word) != var.length:
                    self.domains[var].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        # Set return value to `False` by default:
        revision = False

        # Initialize `overlap` variable to access self.crossword.overlaps and get the overlap between two variables, if any:
        overlap = self.crossword.overlaps[x, y]
        if overlap:

            # Initialize overlap's coordinates:
            i, j = overlap

            # Iterate over all values a variable x can have:
            for val_x in self.domains[x].copy():

                # Set overlap to False by default:
                overlaps = False

                # Iterate over all values a variable y can have:
                for val_y in self.domains[y]:

                    # If their coordinates are the same, then x and y have an overlap at characters #i and #j:
                    if val_x[i] == val_y[j]:
                        overlaps = True

                if not overlaps:

                    # Remove x's value from x's domain:
                    self.domains[x].remove(val_x)

                    # Set revision to True since a change was made:
                    revision = True 
                    
        return revision          

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # If there are no arcs:
        if arcs is None:

            # Initialize and empty list:
            arcs = []

            # Iterate over each variable:
            for var_x in self.domains:

                # Iterate over each variable's neighbor:
                for var_y in self.crossword.neighbors(var_x):

                    # If both variables are different:
                    if var_x != var_y:

                        # Add them to the list of arcs:
                        arcs.append((var_x, var_y))

        # Iterate over variables in arcs list:
        for var_x, var_y in arcs:
            
            # Call revise function to check whether a change to a domain was made, and if so, add additional arcs to the queue to ensure arc consistency:
            if self.revise(var_x, var_y):

                # If x's domain is empty after revision, then there is no solution:
                if not self.domains[var_x]:
                    return False

                # Otherwise if a change was made, update arcs list with all of x's neighbors:
                for neighbor in self.crossword.neighbors(var_x):
                    arcs.append((var_x, neighbor))

        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        # Iterate over all variables:
        for var in self.domains:

            # Check to see if each variable is in the assignment:
            if var not in assignment:
                return False
        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        # Iterate over all variables and their values contained in the assignment:
        for var, word in assignment.items():

            # If the length of each value does not match the length of the variable, return False:
            if var.length != len(word):
                return False
            
            # Otherwise, check to see if all values are distinct:
            for key, value in assignment.items():
                if var != key:
                    
                    # If they're the same, return False:
                    if word == value:
                        return False
                    
            # For a variable, iterate over each of its neighbors:
            for neighbor in self.crossword.neighbors(var):
                if neighbor in assignment.keys():

                    # Check to see if the variable and its neighbor overlap:
                    i, j = self.crossword.overlaps[var, neighbor]
                    if neighbor in assignment:

                        # If their coordinates i and j do not match, return False:
                        if word[i] != assignment[neighbor][j]:
                            return False
        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        # Initialize an empty dictionary where the final list of values is going to be stored:
        results = {}

        # Initialize a variable 'neighbors' that contains all of word's possible neighbors:
        neighbors = self.crossword.neighbors(var)

        # Initialize an int variable that will help us keep track of the number of values we are excluding:
        excluded = 0

        # Iterate over each value a variable can have:
        for word in self.domains[var]:

            # Exclude any variable already present in the assignment since it already has a value:
            if word not in assignment:
                for neigbor in neighbors:
                    if word in self.domains[neigbor]:
                        excluded += 1
                results[word] = excluded

        return sorted(results, key=lambda key: results[key])
                
    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        # Initialize an empty list where all unassigned variables are going to be stored:
        list_unassigned = []

        # Iterate over each variable:
        for var in self.crossword.variables:

            # If a variable is not in the assignment, add it to the list of unassigned variables:
            if var not in assignment:
                list_unassigned.append(var)

        # Initialize the first variable in the list of unassigned variables as the default target variable:
        target_var = list_unassigned[0]

        # Iterate over all variables present in the list of unassigned variables:
        for var in list_unassigned:
            if var != target_var:

                # Check to see which variables has the smallest number of remaining values in its domain:
                if len(self.domains[var]) < len(self.domains[target_var]):

                    # Update default target variable:
                    target_var = var

                # If there is a tie, choose the variable with the highest degree and update target variable:
                elif len(self.domains[var]) == len(self.domains[target_var]):
                    if len(self.crossword.neighbors(var)) >= len(self.crossword.neighbors(target_var)):
                        target_var = var
                        
        return target_var

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        # Check to see if the assignment is complete and if so, return it:
        if self.assignment_complete(assignment):
            return assignment

        # Otherwise, get all unassigned variables from assignment:
        unassigned_vars = self.select_unassigned_variable(assignment)

        # Iterate over each of their potential values:
        for val in self.order_domain_values(unassigned_vars, assignment):

            # Update unassigned variables with new values:
            assignment[unassigned_vars] = val

            # If assignment is consistent, run backtrack function on the new version of the assignment:
            if self.consistent(assignment):
                check = self.backtrack(assignment)

                # If backtrack function returns that the assignment is possible, return the assignment:
                if check:
                    return check
            
            # Otherwise, delete values and return None:
            del assignment[unassigned_vars]

        return None

def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
