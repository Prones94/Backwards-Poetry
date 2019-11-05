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
    split.reverse()
    len_poem = len(split)
    for i in range(len(split)):
        phrase = split[i]
        print(f'{len_poem}, {phrase}')
        len_poem -= 1
    
def lines_printed_random(split):
    random_poem = []
    num_lines = len(split)
    while num_lines >= 0:
        line_num = 1
        print(num_lines)
        rand_line = random.choice(split)
        random_poem.append(rand_line)
        for phrase in random_poem:
            print(f'This works')
            num_lines -= 1
            print(num_lines)
            line_num += 1
            print(line_num)

def rearrange_poem(split):
    pass
# def print_random
# print(split_poem(poem))
lines_printed_backwards(split)
lines_printed_random(split)