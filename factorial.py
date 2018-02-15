class Factorial(object):

    def recur_factorial(self, n):
        """ this function returns the factorial of a 
                number using recursion """
        number_types = (int, float, complex)

        while isinstance(n, number_types):
            if n == 1:
                return n
            else:
                return n * self.recur_factorial(n-1)
        else:
            raise ValueError


