import tkinter as tk
from class_definitions.i_adjective import IAdjective as i
from class_definitions.verb import Verb as v
import os

from custom_exceptions.blank_input_error import BlankInputError
from custom_exceptions.not_alphabetic_error import NotAlphabeticError
from custom_exceptions.not_long_enough_error import NotLongEnoughError

m = tk.Tk()

m.title('Verb Conjugation Tool')
description = tk.Label(text="Welcome!  Use this tool to generate common forms of Japanese verbs. \n You can even "
                            "get a conjugation table for the volitional form of verbs.  \nYou just need to enter"
                            "the dictionary and masu-forms of a verb")
description.pack()

user_input_frame = tk.Frame(master=m, height=100)
user_input_frame.pack(fill=tk.X)

dict_frame = tk.Frame(master=user_input_frame, height=50)
dict_frame.pack()
dict_label = tk.Label(master=dict_frame, text="Dictionary Form: ")
dict_label.pack(side=tk.LEFT)
dict_entry = tk.Entry(master=dict_frame)
dict_entry.pack(side=tk.RIGHT)


masu_frame = tk.Frame(master=user_input_frame)
masu_frame.pack()
masu_label = tk.Label(master=masu_frame, text="Masu Form: ")
masu_label.pack(side=tk.LEFT)
masu_entry = tk.Entry(master=masu_frame)
masu_entry.pack(side=tk.RIGHT)


radio_frame = tk.Frame(master=m)
radio_frame.pack()
choice_label = tk.Label(master=radio_frame, text="Do you want to include the full volitional conjugation?")
choice_label.pack()
var_show_volitional = tk.BooleanVar()
radio_yes = tk.Radiobutton(master=radio_frame, text="Yes", variable=var_show_volitional, value=True)
radio_yes.pack()
radio_no = tk.Radiobutton(master=radio_frame, text="no", variable=var_show_volitional, value=False)
radio_no.pack()

def conjugate():
    var_dictionary_form = dict_entry.get().lower()
    var_masu_form = masu_entry.get().lower()

    try:
        var_masu_form.isnumeric()
        var_dictionary_form.isnumeric()
    except NotAlphabeticError:
        message_label.config(text="Romaji Input Only")
        raise NotAlphabeticError()

    def check_for_input(dict_form, masu_form):
        if len(dict_form) > 0 and len(masu_form) > 0:
            return False
        else:
            return True

    def check_input_length(dict_form, masu_form):
        if len(dict_form) > 1 and len(masu_form) > 1:
            return True
        else:
            return False

    try:
        check_for_input(var_dictionary_form, var_masu_form)
    except BlankInputError:
        message_label.config(text="Blank entry detected.  You MUST enter both requested forms")
        raise BlankInputError
    try:
        check_input_length(var_dictionary_form, var_masu_form)
    except NotLongEnoughError:
        message_label.config(text="One letter is too small to be a Japanese verb")
        raise NotLongEnoughError

    user_verb = v(var_dictionary_form, var_masu_form)
    volitional = i(user_verb.find_volitional(), 'i')
    f = open("conjugation.txt", "a")
    if var_show_volitional == True:
        f.write(user_verb.to_string())
        f.write(volitional.to_string())
        message_label.config(text="Your conjugation tables have been created!")
    else:
        f.write(user_verb.to_string())
        message_label.config(text="Your conjugation table has been created!")
    f.close()

button_frame = tk.Frame(master=m)
button_frame.pack()
submit_button = tk.Button(
    master=button_frame,
    text="Submit",
    width=15,
    height=2,
    bg="green",
    command=conjugate
)
submit_button.pack(side=tk.LEFT)


def clear_file():
    if os.path.exists("conjugation.txt"):
        os.remove("conjugation.txt")
        message_label.config(text="File Deleted!")
    else:
        message_label.config(text="Sorry, but no file was found to delete")

clear_button = tk.Button(
    master=button_frame,
    text="Clear File",
    width=15,
    height=2,
    bg="red",
    command=clear_file
)
clear_button.pack(side=tk.RIGHT)

message_frame = tk.Frame(master=m)
message_frame.pack()
message_label = tk.Label(master=message_frame, text="")
message_label.pack()





m.mainloop()




