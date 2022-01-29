file1 = open('words.txt', 'r');
Lines = file1.readlines();
 
WORD_LEN = 5;

LETTERS_SOMEWHERE = [];
LETTERS_IN_PLACE = ['', '', '', '', ''];
LETTERS_NOWHERE = [];
LETTERS_NOT_HERE = [[], [], [], [], []];

input_str = ""
while (input_str != "q"):
    input_str = input("What word did you put in (q to quit): ");
    if (input_str == "q"):
        break;
    data_str = input("Data (o Not there, - Somewher, x Here):");
    i = 0;
    for letter in data_str:
        if (letter == 'o'):
            LETTERS_NOWHERE.append(input_str[i]);
        elif (letter == '-'):
            LETTERS_SOMEWHERE.append(input_str[i]);
            LETTERS_NOT_HERE[i].append(input_str[i]);
        elif (letter == 'x'):
            LETTERS_IN_PLACE[i] = input_str[i];
        i += 1;
    for line in Lines:
        line = line.lower();
        if (len(line)-1 == WORD_LEN):
            _pass = True;
            le_co = 0;
            for letter_in_place in LETTERS_IN_PLACE:
                if (letter_in_place != '' and line[le_co] != letter_in_place):
                    _pass = False;    
                le_co += 1;

            for letter_somewhere in LETTERS_SOMEWHERE:
                if (not letter_somewhere in line):
                    _pass = False;
                    break;
            for letter_nowhere in LETTERS_NOWHERE:
                if (letter_nowhere in line):
                    _pass = False;

            j = 0;
            for letters_not_here_arr in LETTERS_NOT_HERE:
                for letter in letters_not_here_arr:
                    if (line[j] == letter):
                        _pass = False;
                        break;
                j += 1;
            if (_pass):
                print(line, end="");
file1.close();

