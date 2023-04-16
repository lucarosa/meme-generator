from QuoteEngine import Ingestor


quotes = Ingestor.parse("./_data/DogQuotes/DogQuotesDOCX.docx")
for quote in quotes:
    print(quote)

quotes = Ingestor.parse("./_data/DogQuotes/DogQuotesTXT.txt")
for quote in quotes:
    print(quote)

quotes = Ingestor.parse("./_data/DogQuotes/DogQuotesPDF.pdf")
for quote in quotes:
    print(quote)

quotes = Ingestor.parse("./_data/DogQuotes/DogQuotesCSV.csv")
for quote in quotes:
    print(quote)
