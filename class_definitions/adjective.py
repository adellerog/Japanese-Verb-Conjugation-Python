class Adjective:
    def __init__(self, adj, adj_type):
        self.adj = adj
        self.adj_type = adj_type
        self.root = self.find_root()
        self.te_form = self.find_te_form()


    def find_root(self):
        if self.adj_type == 'i':
            if self.adj == 'ii':  #ii 'good' is the one irregular adjective in Japanese, it is only 'ii' in the plain present affirmative, all other forms it uses the root 'yo'
                root = 'yo'
            else:
                root = self.adj[0:len(self.adj)-1]
        else:
            root = self.adj
        return root

    def find_te_form(self):
        if self.adj_type == 'i':
            te_form = self.root + 'kute'
        else:
            te_form = self.root + 'de'
        return te_form


if __name__ == '__main__':
    test_i_adjective = Adjective('takai', 'i')
    test_na_adjective = Adjective('kirei', 'na')
    test_irregular = Adjective('ii', 'i')

    print('Roots: {}, {}, {}'.format(test_i_adjective.root, test_na_adjective.root, test_irregular.root))
    print('Te-Forms: {}, {}, {}'.format(test_i_adjective.te_form, test_na_adjective.te_form, test_irregular.te_form))
