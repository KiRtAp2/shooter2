class InputForm(object):

    def __init__(self, type, text):
        #type:
        # 0 = int
        # 1 = string

        if type==0:
            self.input_type = "int"
            while True:
                try:
                    self.input = int(input(text))
                    break
                except:
                    print("Error. Please try again.")

        elif type==1:
            self.input_type = "string"
            while True:
                try:
                    self.input = input(text)
                    break
                except:
                    print("Error. plase try again.")


    @input.getter
    def input(self):
        return self.input


    @staticmethod
    def get_string(text):
        form = InputForm(1, text)
        return form.input
