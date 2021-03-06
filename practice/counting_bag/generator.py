import random
from datetime import datetime

MULTIPLIER = 1000000

CAPS_ALPH = 65

ALPH = 97

SPECIAL_CHARS = ['_', '*', '@']

N_SPECIAL_CHARS = 3

SEED = dt = datetime.now().microsecond 

class Generator:
    
    def __init__(self):
        self.chars = []
        
        for i in range(0, 10):
            self.chars.append(i)
            
        for i in range(0, 26):
            self.chars.append(chr(ALPH + i))
            
        for i in range(0, 26):
            self.chars.append(chr(CAPS_ALPH + i))
    
        
    def generate(self, length):
        random.seed(SEED)
        
        password_chars = [length]
    
        for i in range(0, length):
            password_chars.append(self.rand_char())
        
        special_indices = []
        for i in range(0, N_SPECIAL_CHARS):
            special_indices.append(self.rand_num(max=length))
            
            
        for index in special_indices:
            password_chars[index] = self.rand_special()
            
        password = ""
        for char in password_chars:
            password += str(char)
            
        return password
    
    
    def rand_num(self, max=1):
        return (int(random.random() * MULTIPLIER) % max)
    
    
    def rand_char(self):
        max = len(self.chars)
        return self.chars[self.rand_num(max=max)]
    
    
    def rand_special(self):
        max = len(SPECIAL_CHARS)
        return SPECIAL_CHARS[self.rand_num(max=max)]