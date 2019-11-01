# user_poem = input('Please enter your favorite poem. Poem should include original fomatting')
poem = """If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer...
If you're a pretender, come sit by my fire.
For we have some flax-golden tales to spin.
Come in!
Come in!"""

def lines_printed_backwards(poem):
    split_poem = (poem.split("\n"))
    len_poem = len(split_poem)-1
    for _ in split_poem:
        print(split_poem[len_poem])
        len_poem -= 1

def print_index_number(poem):
    split_poem = (poem.split("\n"))
    for line_num in split_poem:
        print(split_poem.index(line_num))

# def print_random
lines_printed_backwards(poem)
print_index_number(poem)