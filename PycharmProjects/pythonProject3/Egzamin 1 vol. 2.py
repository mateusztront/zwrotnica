from random import randint


def shorten(long_text):
    out = ""
    for word in long_text.split():
        out += word[0].upper()
    return out

print(shorten("Don't repeat yourself"))
print(shorten("Read the fine manual"))
print(shorten("All terrain armoured transport"))

def name_sorter(name_list):
    male_list = []
    female_list = []
    for name in name_list:
        if name[-1] == 'a':
            female_list.append(name)
        else:
            male_list.append(name)
    male_list.sort()
    female_list.sort()
    out = {}
    out['male'] = male_list
    out['female'] = female_list
    return out

names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara", "Gienio", "Hanna", "Ula", "Maja"]
print(name_sorter(names))

def check_palindrome(text_chain):
    splitted = text_chain.split()
    joined = "".join(splitted)
    joined = joined.lower()

    for x in range(1, len(joined)):
        if joined[x-1] == joined[-x]:
            continue
        else:
            return False
    return True

print(check_palindrome('In girum imus nocte et consumimur igni'))


def div(numb1, numb2):
    out = []
    for x in range(numb1, numb2+1):
        if x % 2 == 0 and x % 3 != 0:
            out.append(x)
    return out

print(div(0,20))

def roll(numb_dices, dice_type=6, modifier=0):
    possible_dices = [3, 4, 6, 8, 10, 12, 100]
    sum = 0
    if dice_type in possible_dices:
        for x in range(numb_dices):
            sum += randint(1, dice_type)
        return sum + modifier
    else:
        raise Exception("No such dice!")

print(roll(2, 100, 2))
print(roll(3,6,-3))

from flask import Flask, request

app = Flask(__name__)


movies = {
    "favourite": ["A New Hope", "Empire Strikes Back", "Return of the Jedi",
                  "The Force Awakens", "Jaws", "Predator", "Mad Max",
                  "Back to the Future", "2001: A Space Odyssey", "Robocop",
                  "The Hitchhiker's Guide to the Galaxy", "Doctor Who",
                  "Aliens", "Alien", "Terminator", "Blade Runner", "Matrix"],

    "hated": ["The Phantom Menace", "Attack of the Clones", "Star Trek",
              "Alien Resurrection", "Twilight"]

}
@app.route('/')
def hello():
    return "Hello World!"


@app.route('/movies', methods=['GET', 'POST'])
def movies_check():
    html = """
            <form method='POST'>
            Insert title<input type='text' name='title'>
            <p><input type=submit value=Submit>
            </form>
            """
    if request.method == 'GET':
        return html
    elif request.method == 'POST':
        if request.form['title'] in movies['favourite']:
            return html + ' favourite'
        elif request.form['title'] in movies['hated']:
            return html + ' hated'
        else:
            return html + 'No such movie!'

if __name__ == '__main__':
    app.run()
