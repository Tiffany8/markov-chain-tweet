
from sys import argv
from random import choice



class SimpleMarkovGenerator(object):
    char_lmt = None
    #read_file = None

    def read_file(self, filename):
     

        #opened_filename = open(filename)
        read_filename = (open(filename)).read()
        #read_file = self.read_file.append(read_filename)
        return read_filename

    def make_chains(self, read_filename):
        """Takes input text as string; returns dictionary of markov chains."""


        words = read_filename.split()

        word_dict = {}

        for i in range(len(words)-2):
            key = (words[i], words[i + 1])
            value = words[i + 2]

            if key not in word_dict:
                word_dict[key] = []
            word_dict[key].append(value)


        return word_dict
        
    # """
    # for statement looks through out txt file using the dict keys as unique identifiers
    # every time the for loop finds a matching pair, the loop will take the next word (the third word) 
    # append the list associated with that uniue key

    # check: print dict
    # """

    def make_text(self, chains, count = None):
        """Takes dictionary of markov chains; returns random text."""
        
        
        key = choice(chains.keys())
        
        markov_chn = key[0] +" " + key[1]

        while key in chains:
            key_value = choice(chains[key])
            markov_chn = markov_chn + " " + key_value
            key = (key[1], key_value)
        
        

        if self.char_lmt > 140:
            markov_chn = markov_chn[:140]
            return markov_chn
          #  print len(markov_chn)
           # print "Its a tweet!"
        else:
            return markov_chn
            #print len(markov_chn)
            #print "Its not a tweet..."
            #print len(markov_chn)
            #cut off the markov_chn at 140 char

        # print count

    # Change this to read input_text from a file, deciding which file should
    # be used by examining the `sys.argv` arguments (if neccessary, see the
    # Python docs for sys.argv)



class TweetableMarkovGenerator(SimpleMarkovGenerator):

    def make_text(self, chains):
        return super(TweetableMarkovGenerator, self).make_text(chains, 141)


if __name__ == "__main__":
    script, filename = argv

    #print argv


    #instance = SimpleMarkovGenerator()
    
    #instance_2 = SimpleMarkovGenerator()
    #instance_2.char_lmt = 300

    tweet_instance = TweetableMarkovGenerator()
    tweet_instance.char_lmt = 141


    #### NNED TO MAKE THIS PART PRINT ME THE MARKOV GENERATOR!
    #chain_dict = instance.make_chains(instance.read_file(filename))
    #chain_dict = instance_2.make_chains(instance_2.read_file(filename))
    chain_dict = tweet_instance.make_chains(tweet_instance.read_file(filename))
    #print "this is chain dict %s" % chain_dict

    #random_text = instance.make_text(chain_dict)
    #random_text = instance_2.make_text(chain_dict)
    random_text = tweet_instance.make_text(chain_dict)

    #print chain_dict
    #print random_text

