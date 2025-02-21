def count_words(text):
    """Counts the number of words in the given text."""
    words = text.split()  # Split the input text into words using whitespace as a delimiter
    return len(words)  # Return the number of words in the list

def main():
    """Main function to handle user input and display word count."""
    while True:
        user_input = input("Enter a sentence or paragraph (or type 'exit' to quit): ").strip()  # Prompt user input and remove leading/trailing whitespace
        
        if user_input.lower() == 'exit':  # Check if user wants to exit
            print("Exiting the program. Goodbye!")  # Display exit message
            break  # Exit the loop
        elif not user_input:  # Check if input is empty
            print("Error: Input cannot be empty. Please enter some text.")  # Display error message
        else:
            word_count = count_words(user_input)  # Call function to count words in user input
            print(f"Word Count: {word_count}")  # Display the word count

if __name__ == "__main__":
    main()  # Execute main function when script is run

