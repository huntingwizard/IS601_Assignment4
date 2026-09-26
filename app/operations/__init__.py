class Operations:    
    @staticmethod
    def addition(a:float,b:float) -> float:
        """
        function that adds two numbers, a is first number b is second number
        """
        return a+b
    @staticmethod
    def subtraction(a:float,b:float)-> float:
        """
        function that subtracts two numbers, a is first number b is second number
        """
        return a-b
    @staticmethod
    def multiplication(a:float,b:float)-> float:
        """
        function that multiply two numbers, a is first number b is second number
        """
        return a*b
    def power(a:float,b:float)-> float:
        """
        function that multiply two numbers, a is first number b is second number
        """
        return a**b
    @staticmethod
    def division(a:float,b:float)-> float:
        """
        function that divides two numbers, a is first number b is second number
        """
        if b == 0:
            raise ValueError("Can't Divide By Zero")
        return a/b 
    def modulo(a:float,b:float)-> float:
        """
        function that divides two numbers, a is first number b is second number
        """
        if b == 0:
            raise ValueError("Can't Divide By Zero")
        return a%b 