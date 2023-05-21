class QuoteModel():
    """
    A class representing a quote with its associated author.

    Attributes:
        body (str): The body or content of the quote.
        author (str): The author of the quote.

    """

    def __init__(self, body, author):
        """
        Initialize a new instance of the QuoteModel class.

        Args:
            body (str): The body or content of the quote.
            author (str): The author of the quote.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Return a string representation of the QuoteModel instance."""
        return f'{self.body} - {self.author} '
