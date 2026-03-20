
from figman import FigMan

class MaybeParse:
    def __init__(self):
        self.figman = FigMan()
        self.ast = self.figman("run_temp_name")
        self.pemdas_map = {
            "(": 0,
            "^": 1,
            "*": 2,
            "/": 2,
            "+": 3,
            "-": 3
        }
    def _parse_expression(self, pyscript):
        for line in self._load_file(pyscript):
            line = self._clean_line(line)
            assignment_index, arithmetic_index = self._get_operators(line)
            lvalue, rhs = self._split_expression(line, assignment_index)
            print(f"lvalue: {lvalue}, rhs: {rhs}, arithmetic_index: {arithmetic_index}")
    def _load_file(self, pyscript):
        with open(pyscript, "r") as f:
            yield from f.readlines()
    def _clean_line(self, line):
        line = self._strip_new_line(line)
        line = self._strip_trailing_whitespace(line)
        return line
    def _strip_new_line(self, line):
        if line[-1] == "\n":
            line = line[:-1]
        return line
    def _strip_trailing_whitespace(self, line):
        while line and line[-1] in " \t\n\r":
            line = line[:-1]
        return line
    def _provide_chars(self, line):
        for index, char in enumerate(line):
            yield char, index
    def _get_operators(self,line):
        assignment_index = None
        arithmetic_index = [[],[],[],[]]
        for char, index in self._provide_chars(line):
                if char == "=":
                    assignment_index = index
                if char in self.pemdas_map:
                    if char == "(" or char == "^":
                        arithmetic_index[self.pemdas_map[char]].insert(0, index)
                    else:
                        arithmetic_index[self.pemdas_map[char]].append(index)
        return assignment_index, arithmetic_index
    def _split_expression(self, line, assignment_index):
        if assignment_index is not None:
            lvalue = line[:assignment_index]
            rhs = line[assignment_index + 1:]
            return lvalue, rhs

if __name__ == "__main__":
    maybe_parse = MaybeParse()
    maybe_parse._parse_expression("/home/donald-reilly/Programming/projects/unstable/dub/scripts/test_script.dub")  