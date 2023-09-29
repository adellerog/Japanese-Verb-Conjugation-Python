#import adjective
from class_definitions import adjective
'''I Adjectives are one of two classes of adjectives in japanese.  They are called I Adjectives because they
have a suffix -i attached to the end of their root.  Their counterpart, Na Adjectives, do not have such a suffix,
although their root my still end in i.  For example, kirei is a Na Adjective because the final i is a part of the root,
not a suffix like in the adjectives oishii or takai.  I adjectives behave similarly to verbs.  Also, the volitional form
of a verb is essentially an i adjective.  There is only one irregular adjective in japanese, and that is the adjective 
'ii' which means 'Good'.  Japanese word formation is incredibly regular in its rules with exceptionally few exceptions'''
class IAdjective(adjective.Adjective):
    def __init__(self, adj, adj_type):
        super().__init__(adj, adj_type)
        #Inherited forms
        self.root = super().find_root()
        self.te_form = super().find_te_form()
        #New Derived Form
        self.ku_form = self.find_ku_form()  #Acts as stem for certain adjective forms, but can also be used as an adverb (hayai 'fast' -> hayaku 'quickly')
        #Polite Forms
        self.polite_present = self.adj + ' desu'
        self.polite_present_negative = self.ku_form + ' arimasen'
        self.polite_past = self.root + 'katta desu'
        self.polite_past_negative = self.polite_present_negative + 'deshita'
        #Plain Forms
        self.plain_present = self.adj
        self.plain_present_negative = self.ku_form + 'nai'
        self.plain_past = self.root + 'katta'
        self.plain_past_negative = self.ku_form + 'nakatta'

    def find_ku_form(self):
        ku_form = self.root + 'ku'
        return ku_form

    def to_string(self):
        line_one = 'Volitional: {}, Plain Past: {}, Te form: {}, Ku Form: {}'.format(self.plain_present, self.plain_past, self.te_form, self.ku_form)
        line_two = 'Plain Negative: {}, Plain Past Negative: {}'.format(self.plain_present_negative,
                                                                        self.plain_past_negative)
        line_three = 'Polite Present: {}, Polite Past: {}'.format(self.polite_present, self.polite_past)
        line_four = 'Polite Negative: {}, Polite Past Negative: {}'.format(self.polite_present_negative,
                                                                           self.polite_past_negative)
        return '\n {} \n {} \n {} \n {} \n'.format(line_one, line_two, line_three, line_four)


if __name__ == '__main__':
    test_adjective = IAdjective('ii', 'i')

    print(test_adjective.to_string())
