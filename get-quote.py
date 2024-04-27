def main():
    print("Quotes")

if __name__ == "__main__":
    with open("quotes.txt", "r") as f:
        quotes = f.readlines()
        for quote in quotes:
            print(quote.strip())
    
    main()
