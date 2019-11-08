import random
# user_poem = input('Please enter your favorite poem. Poem should include original fomatting')
poem = """If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer...
If you're a pretender, come sit by my fire.
For we have some flax-golden tales to spin.
Come in!
Come in!"""
split = poem.split("\n")

def lines_printed_backwards(split):
    '''This function allows us to use the split poem and reverse the entire poem, including its line numbers'''
    split.reverse()
    len_poem = len(split)
    for i in range(len(split)):
        phrase = split[i]
        print(f'{len_poem}, {phrase}')
        len_poem -= 1
    
def lines_printed_random(split):
    '''This function will random choose lines from the poem and completely change the entire poem, maybe repeating or or not repeating the same line'''
    random_poem = []
    num_lines = len(split)
    while num_lines >= 0:
        rand_line = random.choice(split)
        random_poem.append(rand_line)
        for phrase in random_poem:
            print(f'{phrase}')
            num_lines -= 1

def add_random_line(split):
    '''This will add a random line from the given poem and add to the end of the poem'''
    random_words = random.choice(split)
    split.append(random_words)
    print(split)

# def print_random
# print(split_poem(poem))
# lines_printed_backwards(split)
# lines_printed_random(split)
add_random_line(split)