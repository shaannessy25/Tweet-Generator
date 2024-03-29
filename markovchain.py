from dictogram import Dictogram
from histogram import histogram_dict, book
import random

class MarkovChain(dict):
    def __init__(self, word_list=None):
        #intialize the super class
        super(MarkovChain, self).__init__()
        
        #if word list is passed, create a markov chain 
        if word_list is not None:
            self.create_markov(word_list)
    
    def word_text(self, path = 'lyrics.txt'):
        words = book(path)
    
        return words 
    
    def create_markov(self, word_list):
        num_words = len(word_list)

        for i, key in enumerate(word_list):

            if self.get(key) is None:
                self[key] = Dictogram()
            
            if num_words > i + 1:
                word = word_list[i + 1]
                self.get(key).add_count(word)
    
    def generate_sentence(self, word_list, num_words):
        random_index = random.randint(0, len(word_list) - 1)

        random_word = word_list[random_index]

        word = random.choice(list(self.get(random_word)))

        sentence = word 

        for _ in range(num_words):
            word = self[word].sample()

            sentence += " " + word 
        
        return sentence
    


if __name__ == "__main__":
    word_list = MarkovChain.word_text("lyrics.txt")
    markov_chain = MarkovChain(word_list)



    print(markov_chain)

    print(markov_chain.generate_sentence(word_list, 10))

