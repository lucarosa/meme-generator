class QuoteModel():
    """
    A class representing a quote with its associated author.

    Attributes:
        body (str): The body or content of the quote.
        author (str): The author of the quote.

    """

    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        return f'{self.body} - {self.author} '
