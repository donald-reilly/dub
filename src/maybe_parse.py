
from figman import FigMan

class DubParser:
    """A parser for the Dub programming language."""

    def __init__(self):
        """Initialize the DubParser."""

        self.figman = FigMan()
        self.ast = self.figman("run_temp_name")
        # The operator priority is used to determine the order of operations when parsing expressions.
        self.operator_priority = {
            "(": 0,
            "^": 1,
            "*": 2,
            "/": 2,
            "+": 3,
            "-": 3
        }
    def _parse_expression(self, pyscript):
        """
        Parse a Dub script and return an abstract syntax tree (AST).

        Params:
            pyscript (str): The path to the Dub script to parse.
        Returns:
            The AST representing the parsed Dub script.
        """

        # For now, this method will just print the lvalue and rhs of each assignment in the Dub script.
        for line in self._load_file(pyscript):
            line = self._clean_line(line)
            assignment_index, arithmetic_index = self._get_operators(line)
            lvalue, rhs = self._split_expression(line, assignment_index)
            print(f"lvalue: {lvalue}, rhs: {rhs}, arithmetic_index: {arithmetic_index}")

    def _load_file(self, pyscript):
        """
        Load a Dub script from a file and yield its lines.
        
        Params:
            pyscript (str): The path to the Dub script to load.
        Yields:
            str: Each line of the Dub script.
        """

        # For now, this method will just yield the lines of the Dub script as strings.
        with open(pyscript, "r") as f:
            yield from f.readlines()

    def _clean_line(self, line):
        """
        Clean a line of code by stripping newlines and trailing whitespace.
        
        Params:
            line (str): The line of code to clean.
        Returns:
            str: The cleaned line of code.
        """

        # For now, this method will just strip newlines and trailing whitespace from the line of code.
        line = self._strip_new_line(line)
        line = self._strip_trailing_whitespace(line)
        return line
    
    def _strip_new_line(self, line):
        """
        Strip the newline character from the end of a line of code.
        
        Params:
            line (str): The line of code to strip the newline from.
        Returns:
            str: The line of code without the newline character.
        """

        # For now, this method will just check if the last character of the line is a newline character and remove it if it is.
        if line[-1] == "\n":
            line = line[:-1]
        return line
    
    def _strip_trailing_whitespace(self, line):
        """
        Strip trailing whitespace from a line of code.
        
        Params:
            line (str): The line of code to strip trailing whitespace from.
        Returns:
            str: The line of code without trailing whitespace.
        """

        while line and line[-1] in " \t\n\r":
            line = line[:-1]
        return line
    
    def _provide_chars(self, line):
        """
        Provide each character in a line of code along with its index.
        
        Params:
            line (str): The line of code to provide characters from.
        Yields:
            tuple: A tuple containing the character and its index.
        """

        for index, char in enumerate(line):
            yield char, index

    def _get_operators(self,line):
        """
        Get the indices of the assignment operator and arithmetic operators in a line of code.
        
        Params:
            line (str): The line of code to get operators from.
        Returns:
            tuple: A tuple containing the index of the assignment operator and a list of indices of arithmetic operators.
        """

        assignment_index = None
        arithmetic_index = [[],[],[],[]]
        for char, index in self._provide_chars(line):
                if char == "=":
                    assignment_index = index
                if char in self.operator_priority:
                    if char == "(" or char == "^":
                        arithmetic_index[self.operator_priority[char]].insert(0, index)
                    else:
                        arithmetic_index[self.operator_priority[char]].append(index)
        return assignment_index, arithmetic_index
    
    def _split_expression(self, line, assignment_index):
        """
        Split a line of code into the left-hand side (LHS) and right-hand side (RHS) of an assignment.
        
        Params:
            line (str): The line of code to split.
            assignment_index (int): The index of the assignment operator.
        Returns:
            tuple: A tuple containing the LHS and RHS of the assignment.
        """
        
        if assignment_index is not None:
            lvalue = line[:assignment_index]
            rhs = line[assignment_index + 1:]
            return lvalue, rhs

if __name__ == "__main__":
    dub_parser = DubParser()
    dub_parser._parse_expression("/home/donald-reilly/Programming/projects/unstable/dub/scripts/test_script.dub")  