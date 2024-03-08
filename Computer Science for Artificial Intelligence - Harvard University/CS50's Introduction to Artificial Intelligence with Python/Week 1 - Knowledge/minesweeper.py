import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly   
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        # iterate over cells in sentence and add them to the set of cells known to be mines:
        if len(self.cells) == self.count:
            return set(self.cells)
        return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        # iterate over cells in sentence and add them to the set of cells known to be safe:
        if self.count == 0:
            return set(self.cells)
        return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        # Check to see if the cell known to be a mine is in the sentence:
        if cell in self.cells:
            
            # If so, remove the cell from the sentence:
            self.cells.remove(cell)

            # Decrease count by 1:
            self.count -= 1
            return None

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        # Check to see if the cell known to be safe is in the sentence:
        if cell in self.cells:

            # If so, remove the cell from the sentence:
            self.cells.remove(cell)

            # No need to decrease count
            return None



class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # Mark the cell as a move that has been made:
        self.moves_made.add(cell)

        # Mark the cell as safe:
        self.mark_safe(cell)

        # Add a new sentence to the AI's knowledge base based on the vale of `cell` and `count`
        # To do so, we can dupplicate here the nearby_mines function:

        # Keep count of nearby cells
        count_nearbyCells = set()

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count with (i, j) set if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if (i, j) not in self.moves_made and (i, j) not in self.safes:
                        count_nearbyCells.add((i, j))

        # Update knowledge:
        if len(count_nearbyCells) != 0:
            self.knowledge.append(Sentence(count_nearbyCells, count))

        # Mark any additional cells as safe or as mines if possible:
        # Check for mines:
        for sentence in self.knowledge:
            for cell in sentence.known_mines():
                if cell not in self.mines:
                    self.mark_mine(cell)

        # Check for safe cells:
        for sentence in self.knowledge:
            for cell in sentence.known_safes():
                if cell not in self.safes:
                    self.mark_safe(cell)
 
        # Add any new sentences to the knowledge base if possible:
        # First, we iterate over all sentences already in the knowledge base:
        for sentence in self.knowledge:
            for i in range(len(self.knowledge)):

                # Then we check to see if the sentence we want to update is equal or different than the one we're iterating with:
                if sentence != self.knowledge[i]:

                    # If both sentences are different, we then check to see if the cells in our original sentence are a subset of the cells contained in the other sentence:
                    if sentence.cells.issubset(self.knowledge[i].cells):

                        # If that's the case, we can update our sentence and the cells count values according to the background information provided:
                        self.knowledge[i].cells -= sentence.cells
                        self.knowledge[i].count -= sentence.count

                    # We can also check to see if the cells contained in the sentence we're currently looking at are a subset of the celles contained in our original sentence:
                    if self.knowledge[i].cells.issubset(sentence.cells):

                        # If that's the case, we can update our knowledge base:
                        sentence.cells -= self.knowledge[i].cells
                        sentence.count -= self.knowledge[i].count


    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        
        # First, we iterate over all cells already identified as safe:
        for cell in self.safes:
            
            # Then, we check to see if this cell is not a mine and it's not already been played, in which case we can return it:
            if cell not in self.moves_made and cell not in self.mines:
                return cell    


    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        # First, we iterate over all cells in the board:
        for i in range(self.height):
            for j in range(self.width):
                
                # Then we check to see if a particular cell has not already been played and is not a mine:
                cell = (i, j)
                if cell not in self.moves_made and cell not in self.mines:
                    return cell
