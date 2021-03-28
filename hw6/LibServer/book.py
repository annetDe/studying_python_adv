class Book:
    id_counter = 1

    def __init__(self,
                 title: str,
                 author: str,
                 year: int,
                 id_: int = None,
                 reader_id: int = None) -> None:
        if id_:
            self.__id = id_
        else:
            self.__id = Book.id_counter
            Book.id_counter += 1
        self.__title = title
        self.__author = author
        self.__year = year
        self.__reader_id = reader_id if reader_id else None

    def get_id(self) -> int:
        return self.__id

    def get_title(self) -> str:
        return self.__title

    def get_author(self) -> str:
        return self.__author

    def get_year(self) -> int:
        return self.__year

    def get_reader_id(self) -> int:
        return self.__reader_id

    def set_reader_id(self, reader_id: int) -> None:
        self.__reader_id = reader_id

    def dict(self) -> dict:
        return {
            'id': self.__id,
            'title': self.__title,
            'author': self.__author,
            'year': self.__year,
            'reader_id': self.__reader_id
        }

    @classmethod
    def from_dict(cls, book_dict: dict):
        return cls(
            title=book_dict['title'],
            author=book_dict['author'],
            year=book_dict['year'],
            id_=book_dict['id'],
            reader_id=book_dict['reader_id'],
        )

    def __str__(self) -> str:
        return f'{self.__id} "{self.__title}". {self.__author}, {self.__year}.'

    def __repr__(self) -> dict:
        self.dict()
