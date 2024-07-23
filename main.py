import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style, ttk

# Dictionary mapping characters to their Morse code equivalents
morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                   'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                   '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
                   '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
                   ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
                   '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
                   }

# Reverse dictionary for decoding Morse code to characters
reverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

def show_text_to_morse():
    """
    Show the text to Morse code translation interface.
    """
    home_frame.pack_forget()  # Hide the home frame
    translation_frame.pack()  # Show the translation frame
    translation_label.config(text="Input Text:")  # Update label text
    translation_button.config(text="Translate to Morse Code")  # Update button text
    translation_button.config(command=text_to_morse_code)  # Set button command

def show_morse_code_to_text():
    """
    Show the Morse code to text translation interface.
    """
    home_frame.pack_forget()  # Hide the home frame
    translation_frame.pack()  # Show the translation frame
    translation_label.config(text="Input Morse Code:")  # Update label text
    translation_button.config(text="Translate to Text")  # Update button text
    translation_button.config(command=morse_code_to_text)  # Set button command

def show_home_screen():
    """
    Show the home screen interface.
    """
    translation_frame.pack_forget()  # Hide the translation frame
    home_frame.pack()  # Show the home frame
    input_text.delete("1.0", "end")  # Clear the input text area
    output_text.delete("1.0", "end")  # Clear the output text area

def text_to_morse_code():
    """
    Translate text to Morse code and display the result.
    """
    text = input_text.get("1.0", "end").strip().upper()  # Get and format input text
    if not text:
        messagebox.showwarning("Empty Input", "Please enter some text.")  # Show warning if input is empty
        return
    for char in text:
        if char in morse_code_dict.values():
            messagebox.showwarning("Invalid Input", "Cannot input Morse code in this option.")  # Show warning if Morse code is detected
            return
    
    morse_code = ""
    for char in text:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + " "  # Convert each character to Morse code
        else:
            morse_code += char  # Keep non-convertible characters as is
    output_text.delete("1.0", "end")  # Clear the output text area
    output_text.insert("1.0", morse_code)  # Insert the Morse code

def morse_code_to_text():
    """
    Translate Morse code to text and display the result.
    """
    morse_code = input_text.get("1.0", "end").strip().split(" ")  # Get and format input Morse code
    if not morse_code:
        messagebox.showwarning("Empty Input", "Please enter some Morse code.")  # Show warning if input is empty
        return
    
    for code in morse_code:
        if code.isalpha():
            messagebox.showwarning("Invalid Input", "Cannot input letters in this option")  # Show warning if letters are detected
            return
    
    text = ""
    for code in morse_code:
        if code in reverse_morse_code_dict:
            text += reverse_morse_code_dict[code]  # Convert each Morse code to text
        else:
            text += code  # Keep non-convertible codes as is
    output_text.delete("1.0", "end")  # Clear the output text area
    output_text.insert("1.0", text)  # Insert the translated text

def clear_text():
    """
    Clear the input and output text areas and return to the home screen.
    """
    input_text.delete("1.0", "end")  # Clear the input text area
    output_text.delete("1.0", "end")  # Clear the output text area
    show_home_screen()  # Return to the home screen

# Initialize the main window
window = tk.Tk()
window.title("Morse Code Translator")
window.geometry("400x400")
style = Style(theme="flatly")  # Set the theme for ttkbootstrap

# Home frame setup
home_frame = ttk.Frame(window, padding="20")
home_frame.pack()

home_label = ttk.Label(home_frame, text="Select Translation Type:", font=('tk.DefaultFont', 20))
home_label.pack(pady=10)

text_to_morse_code_btn = ttk.Button(home_frame, text="Text to Morse Code", command=show_text_to_morse)
text_to_morse_code_btn.pack(pady=5)

morse_code_to_text_btn = ttk.Button(home_frame, text="Morse Code to Text", command=show_morse_code_to_text)
morse_code_to_text_btn.pack(pady=5)

# Translation frame setup
translation_frame = ttk.Frame(window, padding="20")

translation_label = ttk.Label(translation_frame, text="Input Text:", font=('tk.DefaultFont', 20))
translation_label.pack(pady=10)

input_text = tk.Text(translation_frame, height=5)
input_text.pack()

output_text_label = ttk.Label(translation_frame, text="Output Text:", font=('tk.DefaultFont', 20))
output_text_label.pack()

output_text = tk.Text(translation_frame, height=5)
output_text.pack()

translation_button = ttk.Button(translation_frame, text="Translate", command=None)
translation_button.pack(pady=15)

back_button = ttk.Button(translation_frame, text="Back", command=show_home_screen)
back_button.pack(pady=5)

translation_frame.pack_forget()  # Hide the translation frame initially

# Start the main event loop
window.mainloop()
a=50
