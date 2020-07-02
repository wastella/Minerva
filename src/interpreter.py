#
# Creating object classes
# By: William Stella
#


# The only reason that I have a variable class is, if I want to add built-in-functions that operate on the variables, then they can be methods in this class:
class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Dragoon:
    def __init__(self):

        self.vars = {}

        self.keywords = ["declare"]

        self.operators = ["::"]

        self.built_in_funcs = ["print"]

        self.line_number = 0

    def add_var(self, var_name, var_value):

        self.vars.update({var_name: var_value})

    def print_func(self, message):

        while True:
            
            # If the argument is a string (In dragoon, this is denoted by the "" groupings):
            if message[0] == '\"' and message[-1] == '\"':
                print(str(message.replace('"', "")))

                break

            # If the argument is an int (In dragoon, this is denoted by the '' groupings):
            elif message[0] == "'" and message[-1] == "'":
                print(int(message.replace("'", "")))

                break

            # If the argument is a bool (In dragoon, this is denoted by the <> groupings):
            elif message[0] == "<" and message[-1] == ">":
                # Replacing the "<" char in message
                partially_replaced_message = message.replace("<", "")

                # Replacing the ">" char in message
                fully_replaced_message = partially_replaced_message.replace(">", "")

                print(fully_replaced_message)

                break

            # If the argument is not a string, int, or bool then it is a var:
            else:
                try:
                    message = self.vars[message.strip("\n")]

                except KeyError:
                    print("[Error] Syntax Error: The argument: {} on line {} was invalid".format(message, self.line_number))
                    break

    def tokenize(self, string, type):
        if type == "function":
            
            token_list = string.split("{")
            # Updating the token list
            token_list.append(token_list[1].replace("}", ""))
            token_list[1] = token_list[0].split(".")[0]
            token_list[0] = token_list[0].split(".")[1]

        elif type == "variable":
            token_list = string.split()
            if token_list[-2] != "::":
                token_list[-2] = token_list[-2] + " " + token_list[-1]
                token_list.pop(-1)
            

        elif type == "test":
            token_list = string.split()

        return token_list

    def is_func(self, string):
        if self.tokenize(string, "function")[0] in self.built_in_funcs and self.tokenize(string, "function")[1] == "dragoon":
            return True


    def parse(self, contents):

        for line in contents:

            line = line.strip()


            self.line_number += 1
            
            # Testing for what the file contents looks like so we can decide whether we should tokenize using the "variable" arg or the "function" arg.
            example_tokens = self.tokenize(line, "test")

            if line == "\n":
                continue

            elif line == "":
                continue

            elif line[0] == ">":
                continue

            # If they are declaring a var on the first line:
            elif example_tokens[0] == "define":

                tokens = self.tokenize(line, "variable")
                
                # Creating a new variable:
                new_var = Variable(tokens[1], tokens[3])
                self.vars.update({new_var.name : new_var.value})

            # If it is a function usage:
            elif self.is_func(line):
                tokens = self.tokenize(line, "function")
                self.print_func(tokens[2])

            else:
                print("[Error] Syntax Error: Syntax on line {} was unrecognizable.".format(self.line_number))
                break
