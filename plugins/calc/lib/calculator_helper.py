from time import sleep

class CalculatorHelper:
    results = {
        'sum': [],
        'sub': [],
        'mult': [],
        'div': [],
    }

    def __init__(self, bot):
        self._bot = bot
    
    def sum(self, num1, num2):
        result = float(num1) + float(num2)

        have = self.verify_if_exists(self.results['sum'], result)

        if have:
            return

        yield f"The sum of {num1} and {num2} is: {result}."
        
        self.results['sum'].append(result)

        return
    
    def sub(self, num1, num2):
        result = float(num1) - float(num2)

        have = self.verify_if_exists(self.results['sub'], result)

        if have:
            return

        yield f"The subtraction of {num1} and {num2} is: {result}."
        
        self.results['sub'].append(result)
        return
    
    def mult(self, num1, num2):
        if float(num1) == 0 or float(num2) == 0:
            yield "you can only be kidding with me to give a zero to multiply... right?"

        result = float(num1) * float(num2)

        have = self.verify_if_exists(self.results['mult'], result)

        if have:
            return

        yield f"The multiplication of {num1} and {num2} is: {result}."
        
        self.results['mult'].append(result)
        return
    
    def div(self, num1, num2):
        if float(num1) == 0 and float(num2) > 0:
            yield "Man... you really want to divide zero to a real number? ..."
        if float(num2) == 0:
            yield "... you know that anyone number divides to 0. Don't troll me."
            return

        result = float(num1) / float(num2)

        have = self.verify_if_exists(self.results['div'], result)

        if have:
            return

        yield f"The division of {num1} for {num2} is: {result}."
        
        self.results['div'].append(result)
        return
    
    def show_results(self, operation):
        data = self.results[operation]

        if data is None:
            yield "Oops, that operation doesn't exists!"
            return
        
        if len(data) == 0:
            yield "Oops, the list is empty!"
            return
        
        index = 1

        for result in data:
            yield f"Result nº{index}: {result}"

            index += 1
        
        return
    
    def verify_if_exists(self, list, result):
        try:
            have = list.index(result)

            if have is not None:
                print("That result is repeated... What i said about repeated values?")

            return True
        except:
            pass

        return False
