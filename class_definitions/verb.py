class Verb:
    def __init__(self, dictionary_form, masu_form):
        self.dictionary_form = dictionary_form  #Also known as "casual present affirmative"
        self.masu_form = masu_form    #Also known as "polite present affirmative"
        self.pre_masu_stem = self.find_pre_masu_stem()
        self.verb_type = self.determine_type()
        self.root = self.find_root()
        self.te_form = self.find_te_form()  #Te form can be used as an imperative, and can also link multiple verbs together - there is no direct english equivalent

        self.plain_present_negative = self.find_plain_negative()  #"is not"
        self.polite_present_negative = self.find_polite_negative() #"is not"
        self.plain_past_affirmative = self.find_plain_past() #"was"
        self.polite_past_affirmative = self.find_polite_past() #"was"
        self.plain_past_negative = self.find_plain_neg_past()    #"wasn't"
        self.polite_past_negative = self.find_polite_neg_past()  #"wasn't"
        self.volitional = self.find_volitional() #'want to be'

    #This determines whether the verb is irregular or belongs to the 'ichidan' or 'godan' conjugation types
    #Japanese Verbs conjugation classes are determined by the root of the verb.  Roots that end in consonants are 'godan'
    #Roots that end in a vowel are 'ichidan'.  Then there are just 2 fully irregular verbs and one slightly irregular verb
    def determine_type(self):
        if self.dictionary_form in ['suru', 'kuru', 'iku']:
            type = 'irregular'
        elif self.dictionary_form[len(self.dictionary_form) - 2:len(self.dictionary_form)] == 'ru':
            if self.pre_masu_stem[len(self.pre_masu_stem) - 2:len(self.pre_masu_stem)] == 'ri':
                type = 'godan'
            else:
                type = 'ichidan'
        else:
            type = 'godan'
        return type

    def find_pre_masu_stem(self):
        pre_masu = self.masu_form[0:(len(self.masu_form) - 4)]
        return pre_masu

    #It's important to determine the last consonant of a godan verb's root. Root forms are especially important for
    #Conjugating the negative forms of verbs.
    def find_root(self):
        if self.verb_type == 'ichidan': #ichidan verbs always maintain the same stem (MIru -> MInai)
            root = self.dictionary_form[0:len(self.dictionary_form) - 2]
        elif self.verb_type == 'godan':
            w_stem_tuple = ('a', 'o', 'i')
            if self.dictionary_form[len(self.dictionary_form)-2] in w_stem_tuple:
                base = self.dictionary_form[0:len(self.dictionary_form)-1]
                root = base + 'w'
            elif self.dictionary_form[len(self.dictionary_form) - 3: len(self.dictionary_form)] == 'tsu':
                root = self.dictionary_form[0:len(self.dictionary_form) - 2]
            else:
                root = self.dictionary_form[0:len(self.dictionary_form) - 1]
        else:
            if self.dictionary_form == 'suru':
                root = 'su'
            elif self.dictionary_form == 'kuru':
                root = 'ku'
            else:
                root = 'ik'
        return root

    def find_plain_negative(self):
        if self.verb_type == 'ichidan':
            plain_neg = self.root + 'nai'
        elif self.verb_type == 'godan':
            plain_neg = self.root + 'anai'
        else:
            if self.dictionary_form == 'suru':
                plain_neg = 'shinai'
            elif self.dictionary_form == 'kuru':
                plain_neg = 'konai'
            else:
                plain_neg = 'ikanai'
        return plain_neg

    def find_polite_negative(self):  #tabemasu -> tabemasen
        polite_neg = self.masu_form[0:len(self.masu_form)-1] + 'en'
        return polite_neg

    def find_polite_neg_past(self):  #tabemasen -> tabemasendeshita
        polite_neg_past = self.find_polite_negative() + 'deshita'
        return polite_neg_past

    def find_plain_neg_past(self): #tabenai -> tabenakatta
        neg_base = self.find_plain_negative()
        plain_neg_past = neg_base[0:len(neg_base)-1] + 'katta'
        return plain_neg_past

    def find_polite_past(self): #tabemasu -> tabemashita
        polite_past = self.pre_masu_stem + 'mashita'
        return polite_past

    def find_volitional(self): #tabemasu -> tabetai
        volitional = self.pre_masu_stem + 'tai'
        return volitional

    def find_te_form(self): #taberu -> tabete, hanasu -> hanashite, kiku -> kiite, etc.
        if self.verb_type == 'ichidan':
            te_form = self.root + 'te'
        elif self.verb_type == 'irregular':
            if self.dictionary_form == 'suru':
                te_form = 'shite'
            elif self.dictionary_form == 'kuru':
                te_form = 'kite'
            else:
                te_form = 'itte'
        else:
            if self.root[len(self.root)-1] == 's':
                te_form = self.root + 'hite'
            elif self.root[len(self.root)-1] == 'k':
                te_form = self.root[0: len(self.root)-1] + 'ite'
            elif self.root[len(self.root)-1] == 'g':
                te_form = self.root[0: len(self.root)-1] + 'ide'
            elif (self.root[len(self.root)-1] == 'm') or (self.root[len(self.root)-1] == 'n') or (self.root[len(self.root)-1] == 'b'):
                te_form = self.root[0: len(self.root)-1] + 'nde'
            else: #root ends in 't', 'r', 'w'
                te_form = self.root[0: len(self.root) - 1] + 'tte'
        return te_form

    def find_plain_past(self): #taberu -> tabeta, hanasu -> hanashita, kiku -> kiita, etc.
        base_form = self.find_te_form()
        plain_past = base_form[0: len(base_form)-1] + 'a'
        return plain_past

    #Method to print results
    def to_string(self):
        line_one = 'Dictionary Form: {}, Te-Form: {}, Plain Past: {}'.format(self.dictionary_form, self.te_form, self.plain_past_affirmative)
        line_two = 'Plain Negative: {}, Plain Past Negative: {}'.format(self.plain_present_negative, self.plain_past_negative)
        line_three = 'Masu-Form: {}, Polite Past: {}, Volitional: {}'.format(self.masu_form, self.polite_past_affirmative, self.volitional)
        line_four = 'Polite Negative: {}, Polite Past Negative: {}'.format(self.polite_present_negative, self.polite_past_negative)
        line_five = 'Verb Type: {}, Verb Root: {}'.format(self.verb_type, self.root)
        return '\n' + line_one + '\n' + line_two + '\n' + line_three + '\n' + line_four + '\n' + line_five + '\n'


#Initial testing
if __name__ == '__main__':
    test_verb = Verb('katsu', 'kachimasu')
    print(test_verb.to_string())
