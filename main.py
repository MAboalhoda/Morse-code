morse_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

running = True
while running == True:
    model = input("Please Type 'E' to encode or 'D' to Decode 'Exit' to exit: ")
    if model.lower() == "e":
        text = input("Please input your text: ").upper()
        encoded_txt = ""
        for letter in text:
            try:
                if letter == " ":
                    encoded_txt = encoded_txt + " / "
                else:
                    encoded_txt = encoded_txt + " " + morse_dict[letter]
            except KeyError:
                encoded_txt = encoded_txt

        print(f"Your Morse encoded text is:\n{encoded_txt}")

    elif model.lower() == "d":
        code_txt = input("Please input your Morse Code: ").upper()
        code_list = []
        for code in code_txt.split(" "):
            code_list.append(code)
        decoded_txt = ""
        for elem in code_list:
            for key, value in morse_dict.items():
                if elem == value and elem != "/":
                    decoded_txt += key
                elif elem == "/":
                    elem = " "
                    decoded_txt += elem
        print(decoded_txt)

    else:
        running = False