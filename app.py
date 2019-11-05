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
    

def print_index_number(poem):
    split_poem = (poem.split("\n"))
    for i, line_num in enumerate(split_poem, 1):
        print(i, split_poem)

# def print_random
# print(split_poem(poem))
lines_printed_backwards(split)
# print_index_number(poem)