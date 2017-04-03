from pathlib import Path


def main():
    books = open("wiki_books.txt", "r");

    i = 0;
    print("books = [")
    for title in books.readlines():
        #did someone say I should use regex? N O p E Da t DI Gud S T U FF
        formated = title.lower().replace(" ", "_").replace("-", "_").replace(".", "").replace(",", "").replace("?", "").replace("!", "").replace("'", "").replace("\n", "");
        txt_file_name = str(i) + "_" + formated + ".txt";
        Path("books/"+txt_file_name).touch();
        print("\""+txt_file_name+"\", ");
        i += 1;

    print("];");

if __name__ == "__main__":
    main();
