class Reader:
    def __init__(self, reader_id, name, surname, year_birth):
        self.reader_id = reader_id
        self.name = name
        self.surname = surname
        self.year_birth = year_birth
        self.books_id_lst = []

    def __repr__(self):
        return f'\tid:\t\t\t\t{self.reader_id}\n\tname:\t\t\t{self.name}\n\tsurname:\t\t{self.surname}' \
               f'\n\tyear of birth:\t{self.year_birth}\n'

    def get_books_id_lst(self):
        return self.books_id_lst
