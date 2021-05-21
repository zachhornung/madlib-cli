import re, random

WIDTH = 50

chars = ['#', '*', '+', '&', '$']
p = '(?<={)[a-zA-Z\s\'0-9-]*'



def upper_and_lower_border(string, char='*'):
  return string.center(WIDTH, char)

def center_string(string):
  return string.center(WIDTH-2, ' ')


def read_template(path):
  with open(path) as f:
    string = f.read()
  return string


def parse_template(string):
  expected_parts = tuple(re.findall(p, string))
  expected_stripped = re.sub(p, '', string)
  return (expected_stripped, expected_parts)


def merge(stripped_string, tuple_to_insert):
  return stripped_string.format(*tuple_to_insert)


def get_stuff_from_madlib(path):
  string = read_template(path)
  stripped_template, parts = parse_template(string)
  return (stripped_template, parts)


# def print_message(char):


# TODO: format the hello message and instructions for doing the madlib
hello_message = f"""
{upper_and_lower_border('*')}
*{center_string('Hello There!')}*
*{center_string('Welcome to Terminal MadLibs!')}*
*{center_string('Enter the first word that comes to mind')}*
*{center_string('based on the prompt')}*
*{center_string('dont think too hard')}*
*{center_string('or it wont be as much fun')}*
*{center_string('quit at any time by typing "quit"')}*
{upper_and_lower_border('*')}
"""

quit_message = f"""
{upper_and_lower_border('*')}
*{center_string('Hope you had fun')}*
*{center_string('Come back soon!')}*
{upper_and_lower_border('*')}
"""

print(hello_message)

template, madlib_prompt = get_stuff_from_madlib('assets/madlib_template.txt')
words_from_user = []
if __name__ == "__main__":
  for word in madlib_prompt:
    char = random.choice(chars)

    prompt_message = f"""
    {upper_and_lower_border(char, char)}
    {char}{center_string(f'Give me an {word}')}{char}
    {upper_and_lower_border(char, char)}
    """
    print(prompt_message)
    response = input('> ')
    words_from_user.append(response)
    if response == 'quit':
      print(quit_message)
      break
  if len(words_from_user) == len(madlib_prompt):
    with open('assets/completed_madlib.txt', 'w') as f:
      f.write(merge(template, tuple(words_from_user)))
    print(merge(template, tuple(words_from_user)))