from class_definitions import adjective

'''There are 2 adjective classes in Japanese.  This is a subclass for the NA Adjective class.
The class determines how the adjective behaves.  The Na adjectives function very similarly to 
nouns in Japanese.  For example, if the Na adjective precedes a noun, then the particle NA is 
required to go before them.  For example, 'kirei na hito' which means 'pretty person'.  The 
particle na comes after the adjective and before the noun.  This is similar to when a noun 
is used to modify another noun, but the particle NO is used instead of NA for two nouns.  For
example: 'watashi no tomodachi no pen', which means 'My friend's pen'. '''
class NaAdjective(adjective.Adjective):
    def __init__(self, adj, adj_type):
        super().__init__(adj, adj_type)
        #Inherited forms
        self.root = super().find_root()
        self.te_form = super().find_te_form()
        #Polite Forms
        self.polite_present = self.adj + ' desu'
        self.polite_present_negative = self.adj + ' dewa arimasen'
        self.polite_past = self.adj + ' deshita'
        self.polite_past_negative = self.adj + ' dewa arimasendeshita'
        #Plain Forms
        self.plain_present = self.adj + ' da'
        self.plain_present_negative = self.adj + ' ja nai'
        self.plain_past = self.adj + ' datta'
        self.plain_past_negative = self.adj + ' ja nakatta'


if __name__ == '__main__':
    test_adjective = NaAdjective('kirei', 'na')

    print('Root: {}, Te-Form: {}'.format(test_adjective.root, test_adjective.te_form))
    print('Polite: {}, {}, {}, {}'.format(test_adjective.polite_present, test_adjective.polite_present_negative, test_adjective.polite_past, test_adjective.polite_past_negative))
    print('Plain: {}, {}, {}, {}'.format(test_adjective.plain_present, test_adjective.plain_present_negative, test_adjective.plain_past, test_adjective.plain_past_negative))
