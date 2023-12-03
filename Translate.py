import re
import sys
import json
import os
from deep_translator import GoogleTranslator
from colorama import Fore, Style

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print the banner and clear the screen
def print_banner_and_clear_screen():
    clear_screen()
    banner = (
        f"{Fore.LIGHTGREEN_EX} ██████╗░██╗░░██╗██╗░░░██╗██████╗░██╗░░░██╗░█████╗░\n"
        f"{Fore.LIGHTGREEN_EX} ██╔══██╗██║░░██║╚██╗░██╔╝██╔══██╗██║░░░██║██╔══██╗\n"
        f"{Fore.LIGHTGREEN_EX} ██████╔╝███████║░╚████╔╝░██████╔╝██║░░░██║╚██████║\n"
        f"{Fore.LIGHTGREEN_EX} ██╔══██╗██╔══██║░░╚██╔╝░░██╔══██╗██║░░░██║░╚═══██║\n"
        f"{Fore.LIGHTGREEN_EX} ██║░░██║██║░░██║░░░██║░░░██║░░██║╚██████╔╝░█████╔╝\n"
        f"{Fore.LIGHTCYAN_EX}╔══════════════════════════════════════════════════╗\n"
        f"{Fore.LIGHTCYAN_EX}║ {Style.BRIGHT}{Fore.GREEN}• {Fore.WHITE}AUTHOR         {Fore.LIGHTCYAN_EX}    |{Fore.WHITE}    github.com/rhymsc      {Fore.LIGHTCYAN_EX}║\n"
        f"{Fore.LIGHTCYAN_EX}╚══════════════════════════════════════════════════╝\n"
    )
    print(banner)

# Split the text into smaller groups up to 5000 characters without breaking lines so need to split on new lines
def split_text(text, max_len=4500):
    # Split the text into lines
    lines = text.split("\n")
    # List of chunks
    chunks = []
    # Chunk buffer
    chunk = ""

    # Loop through the lines
    for line in lines:
        # If the chunk is too long, add it to the list and reset the chunk
        if len(chunk + line) > max_len:
            chunks.append(chunk)
            chunk = ""
        # Add the line to the chunk
        chunk += line + "\n"

    # Add the last chunk to the list
    if chunk:
        chunks.append(chunk)

    # Return the list of chunks
    return chunks

def translate(text, source, target):
    # Split the text into smaller groups up to 5000 characters without breaking lines so need to split on new lines
    chunks = split_text(text)

    # Translate the text
    translated_chunks = []
    for chunk in chunks:
        if source is None:
            source = 'auto'
        translated = GoogleTranslator(source=source, target=target).translate(text=chunk)
        translated_chunks.append(translated)

    # Return the translated chunks
    return translated_chunks

if __name__ == "__main__":
    args = sys.argv

    # Handling the case when no file is passed
    if len(args) == 1:
        print("Please pass a file to translate")
        sys.exit(1)
    elif len(args) == 2:
        print("Please pass a target language")
        sys.exit(1)
    elif len(args) >= 3:
        text = str(open(args[1], encoding='utf8', newline='\n').read()).strip()

        # Handling `<filename> <target>`
        if len(args) == 3:
            translated_chunks = translate(text, None, args[2])
        # Handling `<filename> <from> <target>`
        elif len(args) == 4:
            translated_chunks = translate(text, args[2], args[3])

        with open("result.txt", "w", encoding="utf-8") as output_file:
            output_file.write('\n'.join(translated_chunks))

        print("Translation saved to result")
