class Reader:
    id_counter = 1

    def __init__(self,
                 name: str,
                 surname: str,
                 year_birth: int,
                 id_: int = None,
                 books_id_lst: list = None) -> None:
        if id_:
            self.__id = id_
        else:
            self.__id = Reader.id_counter
            Reader.id_counter += 1
        self.__name = name
        self.__surname = surname
        self.__year_birth = year_birth
        self.__books_id_lst = books_id_lst if books_id_lst else []

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_surname(self) -> str:
        return self.__surname

    def get_year_birth(self) -> int:
        return self.__year_birth

    def get_books_id_lst(self) -> list:
        return self.__books_id_lst

    def add_book_id(self, book_id: int) -> None:
        self.__books_id_lst.append(book_id)

    def remove_book_id(self, book_id: int) -> None:
        self.__books_id_lst.remove(book_id)

    def dict(self) -> dict:
        return {
            'id': self.__id,
            'name': self.__name,
            'surname': self.__surname,
            'year_birth': self.__year_birth,
            'books_id_lst': self.__books_id_lst
        }

    @classmethod
    def from_dict(cls, reader_dict: dict):
        return cls(
            name=reader_dict['name'],
            surname=reader_dict['surname'],
            year_birth=reader_dict['year_birth'],
            id_=reader_dict['id'],
            books_id_lst=reader_dict['books_id_lst'],
        )

    def __str__(self):
        return f'{self.__id} {self.__name} {self.__surname}, {self.__year_birth}.'

    def __repr__(self) -> dict:
        self.dict()
