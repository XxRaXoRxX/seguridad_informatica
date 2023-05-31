#Im going to cypher a text with the Cesar cypher and Fibonacci sequence.

class Cypher():

    def __init__(self, text=str, action=bool):
        self.text = text
        self.action = action
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def run(self):
        self.cipher()


    def cipher(self):
        print(f"Text to cipher: {self.text}")
        alpabeth = self.alphabet
        text = self.text.lower()
        positions = len(text)
        #Fibonacci sequence
        for i in range(1, positions+1):
            positions = self.rec_fib(i)

        text_cyphered = "" #This is the Ceasar cypher text.
        for letter in text: 
            if letter in alpabeth: #This is the Ceasar cypher
                index = alpabeth.index(letter)
                if self.action == False:
                    new_index = (index - positions ) % len(alpabeth)
                else:
                    new_index = (index + positions ) % len(alpabeth) 
                while new_index > len(alpabeth):
                    new_index -= len(alpabeth)
                text_cyphered += alpabeth[new_index]
            else:
                print(f"Letter {letter} not in alphabet. Continue with the next letter.")
                text_cyphered += letter


        print(f"Text cyphered: {text_cyphered}")

    def rec_fib(self,n):
        if n > 1:
            return self.rec_fib(n-1) + self.rec_fib(n-2)
        return n
    

if __name__ == "__main__":
    text = "krph"
    action = False
    cypher = Cypher(text, action)
    cypher.run()


