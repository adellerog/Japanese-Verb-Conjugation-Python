class BlankInputError(Exception):
    def check_for_input(self, dict_form, masu_form):
        if len(dict_form) > 0 and len(masu_form) > 0:
            return True
        else:
            return False