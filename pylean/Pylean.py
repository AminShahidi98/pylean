from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import keyword
from nltk.corpus import wordnet
from nltk.corpus import words
class manager:
    def __init__(self, master):
        self.show = Text(master , width=70 , height=27)
        self.show.place(x=15 , y = 90)
        self.show.config(background='white' , foreground='darkblue' ,borderwidth=1)
        self.show.config(wrap='char')          
        self.general = Text(master, width=26, height=27)
        self.general.place(x=585 , y=90)
        self.general.config(wrap='word')
        self.general.config(background='lightgray' , foreground='black' , borderwidth=1)
        self.frame = ttk.Frame(master , width=780 , height=80)
        self.frame.config(relief=RIDGE)
        self.frame.place(x=15 , y=2)
        self.path = ttk.Entry(self.frame, width=97)
        self.path.insert(0,'')
        self.path.place(x=7, y=7)
        self.path.config(foreground = 'black')
        self.label = ttk.LabelFrame(self.frame , width=1000 , height=70 , text='Tip')
        self.label.place(x=7 , y=35)
        self.help = Label(self.label ,
        text='Enter your directory in the entery field , then the results will be shown in lower screen. the lower right field shows you general informations.     ').pack()
        self.b1=ttk.Button(self.frame, text = "       Analize     ",command = self.action).place(x=600 , y=5)    
        self.b2=ttk.Button(self.frame, text = "  Clear Results ",command = self.clear).place(x=690 , y=5)
    def clear(self):
        self.general.delete('1.0' , 'end lineend')
        self.show.delete('1.0' , 'end lineend')
    def separate (self , given_list):
        the_list = given_list
        the_list2 = []
        for i in range(0,len(given_list)):
            z = []
            y = []
            if('_' in the_list[i]):
                z = the_list[i].split('_')
                for j in z:
                    if(j != ''):
                        y.append(j)
                the_list2.append(y)
            else:
                the_list2.append(the_list[i])
        return the_list2
    
    def change_text_to_list (self, path ):
        reserved=['abs' , 'all' , 'any' ,'ascii' ,'bin' ,'bool' ,'bytearray' ,'bytes' ,'callable','chr','classmethod' ,'compile' ,'complex' ,'delattr' ,'dir' ,'divmod' ,'enumerate' ,'eval','exec' ,'filter' ,'float' ,'format' ,'frozenset' ,'getattr' ,'globals' ,'hasattr','hash' ,'help' ,'hex' ,'id' ,'input' ,'int' ,'isinstance' ,'issubclass' ,'iter','len' ,'list' ,'locals' ,'maptem' ,'max' ,'memoryview' ,'min' ,'next' ,'object','oct' ,'open' ,'ord' ,'pow' ,'print' ,'property' ,'range' ,'repr' ,'reversed' ,'round','set' ,'setattr' ,'slice' ,'sorted' ,'str' ,'sum' ,'super' ,'tuple','type' ,'vars' ,'zip' ,'capitalize' ,'casefold' ,'center' ,'count' ,'encode' ,'endswith','expandtabs' ,'find' ,'format' ,'format_map' ,'index' ,'isalnum' ,'isalpha' ,'isdecimal','isdigit' ,'isidentifier' ,'islower' ,'isnumeric' ,'isprintable' ,'isspace' ,'istitle','isupper' ,'join' ,'ljust' ,'lower' ,'lstrip' ,'maketrans' ,'partition' ,'replace','rfind' ,'rindex' ,'rjust' ,'rpartition' ,'rsplit' ,'rstrip' ,'split' ,'splitlines','startswith' ,'strip' ,'swapcase' ,'title' ,'translate' ,'upper' ,'zfill' ,'append','clear' ,'copy' ,'count' ,'extend' ,'index' ,'insert' ,'pop' ,'remove' ,'reverse','sort' ,'clear' ,'copy' ,'fromkeys' ,'get' ,'items' ,'keys' ,'pop' ,'popitem' ,'setdefault','update' ,'values' ,'count' ,'index' ,'add' ,'clear' ,'copy' ,'difference' ,'difference_update','discard' ,'intersection' ,'intersection_update' ,'isdisjoint' ,'issubset' ,'issuperset','pop' ,'remove' ,'symmetric_difference' ,'symmetric_difference_update' ,'union' ,'update','close' ,'detach' ,'fileno' ,'flush' ,'isatty' ,'read' ,'readable' ,'readline' ,'readlines','seek' ,'seekable' ,'tell' ,'truncate' ,'writeable' ,'write' ,'writelines']
        grabed_text_file = open( path , 'r')
        lines = []
        auxilary_string = ''
        auxilary_list = []
        count = 0
        is_callable = 0
        for i in grabed_text_file:
            lines.append(repr(i))
            lines[count] = list(lines[count])
            count = count + 1
        for j in range(0,len(lines)):
            for k in range (1,len(lines[j])-1):
                auxilary_string = auxilary_string + lines[j][k]
            auxilary_list.append(auxilary_string)
            auxilary_string = ''
        lines = auxilary_list
        auxilary_list = []
        return lines

    def word_recognize ( self,listed_text ):
        reserved=['abs' , 'all' , 'any' ,'ascii' ,'bin' ,'bool' ,'bytearray' ,'bytes' ,'callable','chr','classmethod' ,'compile' ,'complex' ,'delattr' ,'dir' ,'divmod' ,'enumerate' ,'eval','exec' ,'filter' ,'float' ,'format' ,'frozenset' ,'getattr' ,'globals' ,'hasattr','hash' ,'help' ,'hex' ,'id' ,'input' ,'int' ,'isinstance' ,'issubclass' ,'iter','len' ,'list' ,'locals' ,'maptem' ,'max' ,'memoryview' ,'min' ,'next' ,'object','oct' ,'open' ,'ord' ,'pow' ,'print' ,'property' ,'range' ,'repr' ,'reversed' ,'round','set' ,'setattr' ,'slice' ,'sorted' ,'str' ,'sum' ,'super' ,'tuple','type' ,'vars' ,'zip' ,'capitalize' ,'casefold' ,'center' ,'count' ,'encode' ,'endswith','expandtabs' ,'find' ,'format' ,'format_map' ,'index' ,'isalnum' ,'isalpha' ,'isdecimal','isdigit' ,'isidentifier' ,'islower' ,'isnumeric' ,'isprintable' ,'isspace' ,'istitle','isupper' ,'join' ,'ljust' ,'lower' ,'lstrip' ,'maketrans' ,'partition' ,'replace','rfind' ,'rindex' ,'rjust' ,'rpartition' ,'rsplit' ,'rstrip' ,'split' ,'splitlines','startswith' ,'strip' ,'swapcase' ,'title' ,'translate' ,'upper' ,'zfill' ,'append','clear' ,'copy' ,'count' ,'extend' ,'index' ,'insert' ,'pop' ,'remove' ,'reverse','sort' ,'clear' ,'copy' ,'fromkeys' ,'get' ,'items' ,'keys' ,'pop' ,'popitem' ,'setdefault','update' ,'values' ,'count' ,'index' ,'add' ,'clear' ,'copy' ,'difference' ,'difference_update','discard' ,'intersection' ,'intersection_update' ,'isdisjoint' ,'issubset' ,'issuperset','pop' ,'remove' ,'symmetric_difference' ,'symmetric_difference_update' ,'union' ,'update','close' ,'detach' ,'fileno' ,'flush' ,'isatty' ,'read' ,'readable' ,'readline' ,'readlines','seek' ,'seekable' ,'tell' ,'truncate' ,'writeable' ,'write' ,'writelines']
        words = []
        columns = []
        rows = []
        types = []
        last_a = ''
        a = ''
        is_func = 0
        comment_temp = 0
        for_counter = []
        for i in range (0,len(listed_text)):
            for j in range (0,len(listed_text[i])-1):
                if( listed_text[i][j] == '#' ):
                    a=''
                    break
                elif( listed_text[i][j] == 'a' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'b' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'c' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'd' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'e' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'f' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'g' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'h' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'i' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'j' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'k' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'l' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'm' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'n' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'o' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'p' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'q' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'r' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 's' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 't' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'u' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'v' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'w' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'x' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'y' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'z' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'A' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'B' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'C' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'D' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'E' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'F' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'G' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'H' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'I' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'J' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'K' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'L' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'M' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'N' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'O' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'P' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'Q' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'R' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'S' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'T' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'U' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'V' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'W' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'X' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'Y' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == 'Z' ):
                    a = a + listed_text[i][j]
                elif( listed_text[i][j] == '0' ):
                    if( len(a)!=0):
                        a = a + listed_text[i][j]
                    else:
                        a=''
                elif( listed_text[i][j] == '1' ):
                    if( len(a)!=0):
                        a = a + listed_text[i][j]
                    else:
                        a=''
                elif( listed_text[i][j] == '2' ):
                    if( len(a)!=0):
                        a = a + listed_text[i][j]
                    else:
                        a=''
                elif( listed_text[i][j] == '3' ):
                    if( len(a)!=0):
                        a = a + listed_text[i][j]
                    else:
                        a=''
                elif( listed_text[i][j] == '4' ):
                    if( len(a)!=0):
                        a = a + listed_text[i][j]
                    else:
                        a=''
                elif( listed_text[i][j] == '5' ):
                    if( len(a)!=0):
                        a = a + listed_text[i][j]
                    else:
                        a=''
                elif( listed_text[i][j] == '6' ):
                    if( len(a)!=0):
                        a = a + listed_text[i][j]
                    else:
                        a=''
                elif( listed_text[i][j] == '7' ):
                    if( len(a)!=0):
                        a = a + listed_text[i][j]
                    else:
                        a=''
                elif( listed_text[i][j] == '8' ):
                    if( len(a)!=0):
                        a = a + listed_text[i][j]
                    else:
                        a=''
                elif( listed_text[i][j] == '9' ):
                    if( len(a)!=0):
                        a = a + listed_text[i][j]
                    else:
                        a=''
                elif( listed_text[i][j] == '_'):
                    a = a + listed_text[i][j]
                else:
                    for z in range(j , len(listed_text[i])-1):
                        if(listed_text[i][z] == ''):
                            pass
                        elif(listed_text[i][z] == '('):
                            is_callable = 1
                            break
                        else:
                            is_callable = 0
                            break
                    if(len(a) != 0):
                        words.append(a)
                        columns.append(i+1)
                        temp = j + 1 - len(a)
                        rows.append(temp)
                        if(last_a.lower() == 'class'):
                            types.append('Class')
                        elif(last_a.lower() == 'import'):
                            types.append('Include Library')
                        elif(keyword.iskeyword(a.lower())):
                            types.append('Keyword')
                        elif( a in reserved):
                            types.append('Reserved')
                        elif(last_a.lower() == 'def' or is_callable):
                            types.append('Function')
                        else:
                            types.append('Variable')
                        last_a = a
                        a = ''
                    else:
                        a=''
        finalized = [words , columns , rows , types]
        return finalized

    def change_text_to_str (self , path ):
        grabed_text_file = open( path , 'r')
        lines = []
        auxilary_string = ''
        auxilary_list = []
        count = 0
        total = ''
        for i in grabed_text_file:
            lines.append(i)
            lines[count] = list(lines[count])
            count = count + 1
        for j in range(0,len(lines)):
            for k in range (0,len(lines[j])-1):
                auxilary_string = auxilary_string + lines[j][k]
            auxilary_list.append(auxilary_string)
            auxilary_string = ''    
        lines = auxilary_list
        auxilary_list = []
        total = lines
        eq = 0
        sem_count = 0
        aux_count = 0
        sem_list = []
        sem_list_col = []
        sem_list_row = []
        for k in range (0,len(total)):
            for i in range(0 , len(total[k])):
                if(total[k][i] == '='):
                    eq = 1
                elif(total[k][i] == ' '):
                    pass
                elif(total[k][i] == '('):
                    aux_count = aux_count + 1
                    if(eq == 0):
                        for j in range(i+1 , len(total[k])):
                            if(total[k][j] == ','):
                                if(aux_count == 1):
                                    sem_count = sem_count + 1
                            elif(total[k][j] == '('):
                                aux_count = aux_count + 1
                            elif(total[k][j] == ')'):
                                aux_count = aux_count - 1
                                if(aux_count == 0):
                                    break
                            else:
                                pass
                    eq = 0
                    if(aux_count == 0):
                        if(sem_count != 0):
                            sem_list.append(sem_count+1)
                        else:
                            sem_list.append(sem_count)
                        sem_list_col.append(i+1)
                        sem_list_row.append(k+1)
                        sem_count = 0
                else:
                    eq = 0
                    pass
        fin = [sem_list , sem_list_col , sem_list_row]
        return fin

    def for_index_recognize(self,words , columns , rows):
        ret_val = []
        for i in range(0 , len(words)):
            if(type(words[i] != list)):
                if(words[i] == 'for'):
                    index_keeper = words[i+1]
                    for_column = columns[i]
                    for_start_row = rows[i]
                    for_end_row = rows[len(words)-1]
                    for j in range(i+1 , len(words)):
                        if(columns[j] <= for_column):
                            for_end_row = rows[j]
                            break
                    for_token = [index_keeper , for_start_row , for_end_row-1 , for_column]
                    ret_val.append(for_token)
                    for_end_row = rows[len(words)-1]
        return ret_val

    def wrong_for_indexes(self , words , rows , fors):
        ret_val = []
        for i in range(0 , len(words)):
            flag=0
            if (type(words[i]) == str):
                if(len(words[i]) == 1):
                    for t in fors:
                        if(words[i] == t[0]):
                            if(rows[i] in range(t[1] , t[2]+1)):
                                flag = 1
                    if(flag):
                        pass
                    else:
                        temp = [words[i] , rows[i]]
                        ret_val.append(temp)
        return ret_val

    def is_not_verb (self , words , types , rows):
        words_list = []
        rows_list = []
        for i in range(0,len(words)):
            flag=0
            if(types[i] == 'Function'):
                if(type(words[i]) == str):
                    syns = wordnet.synsets(words[i])
                    for j in syns:
                        if(j.pos() == "v"):
                            flag = 1
                            break
                    if(flag):
                        pass
                    else:
                        words_list.append(words[i])
                        rows_list.append(rows[i])
                else:
                        words_list.append("_".join(words[i]))
                        rows_list.append(rows[i])
        ret_val = [words_list,rows_list]
        return ret_val

    def is_eng_word(self ,wordss , rows , columns , types):
        w_words = []
        w_columns = []
        w_rows =[]
        for i in range(0 , len(wordss)):
            if(types[i] == "Variable" or types[i] == "Class"):
                if("".join(wordss[i]).lower() in words.words()):
                    pass
                else:
                    w_words.append("".join(wordss[i]))
                    w_rows.append(rows[i])
                    w_columns.append(columns[i])
        ret_val = [w_words , w_rows , w_columns]
        return ret_val

    def show_functions_having_more_than_4_arguments(self):
        count = 0
        text='Functions detected with more than 4 arguments:\n'
        self.show.insert('end' , '----------------------------------------------------------------------\n')
        self.show.insert('end' , text)
        self.show.insert('end' , '----------------------------------------------------------------------\n')
        functions_inputes_number = self.change_text_to_str (self.path.get())
        extra_input_functions=[[],[],[]]
        for i in range(0,len(functions_inputes_number[0])):
            if(functions_inputes_number[0][i] >4):
                count = count + 1
                self.show.insert('end' , 'In:')
                self.show.insert('end' , '\n')
                self.show.insert('end' , 'Row:')
                self.show.insert('end' , str(functions_inputes_number[2][i]))
                self.show.insert('end' , '\n')
                self.show.insert('end' , 'Column:')
                self.show.insert('end' , str(functions_inputes_number[1][i]))
                self.show.insert('end' , '\n')
                self.show.insert('end' , str(functions_inputes_number[0][i]))
                self.show.insert('end' , ' given arguments.')
                self.show.insert('end' , '\n')
                self.show.insert('end' , '\n')
        self.general.insert('end' , 'Number of functions having more than 4 arguments: ')
        self.general.insert('end' , count)
        self.general.insert('end' , '\n')
        self.general.insert('end' , '\n')

    def show_variables_and_classes_having_meaningless_names (self):
        count = 0
        text='Variables and classes detected with meaningless names:\n'
        self.show.insert('end' , '----------------------------------------------------------------------\n')
        self.show.insert('end' , text)
        self.show.insert('end' , '----------------------------------------------------------------------\n')
        answer1 = self.word_recognize(self.change_text_to_list(self.path.get()))
        separated_words = self.separate(answer1[0])
        answer1[0] = separated_words
        wrong_eng_words = self.is_eng_word(answer1[0] , answer1[1] , answer1[2] , answer1[3])
        for i in range(0,len(wrong_eng_words[0])):
            count = count +1
            self.show.insert('end' , 'The variable: ')
            self.show.insert('end' , wrong_eng_words[0][i])
            self.show.insert('end' , '\n')
            self.show.insert('end' , 'In row:')
            self.show.insert('end' , wrong_eng_words[1][i])
            self.show.insert('end' , '\n')
            self.show.insert('end' , 'In column:')
            self.show.insert('end' , wrong_eng_words[2][i])
            self.show.insert('end' , '\n')
            self.show.insert('end' , '\n')
        self.general.insert('end' , 'Number of variables and classes with meaningless names: ')
        self.general.insert('end' , count)
        self.general.insert('end' , '\n')
        self.general.insert('end' , '\n')

    def show_functions_which_their_names_are_not_verb (self):
        count = 0
        text='Functions detected with meaningless names:\n'
        self.show.insert('end' , '----------------------------------------------------------------------\n')
        self.show.insert('end' , text)
        self.show.insert('end' , '----------------------------------------------------------------------\n')
        answer1 = self.word_recognize(self.change_text_to_list(self.path.get()))
        separated_words = self.separate(answer1[0])
        answer1[0] = separated_words
        wrong_functions_name=self.is_not_verb(answer1[0],answer1[3],answer1[1])
        for i in range(0,len(wrong_functions_name[0])):
            count = count + 1
            self.show.insert('end' , 'The Function: ')
            self.show.insert('end' , wrong_functions_name[0][i])
            self.show.insert('end' , '\n')
            self.show.insert('end' , 'In row:')
            self.show.insert('end' , wrong_functions_name[1][i])
            self.show.insert('end' , '\n')
            self.show.insert('end' , '\n')
        self.general.insert('end' , 'Number of functions with meaningless names: ')
        self.general.insert('end' , count)
        self.general.insert('end' , '\n')
        self.general.insert('end' , '\n')
        

    def show_length_1_indexes_that_does_not_belong_to_a_for(self):
        count = 0
        text='Wrong detected indexes:\n'
        self.show.insert('end' , '----------------------------------------------------------------------\n')
        self.show.insert('end' , text)
        self.show.insert('end' , '----------------------------------------------------------------------\n')
        answer1 = self.word_recognize(self.change_text_to_list(self.path.get()))
        separated_words = self.separate(answer1[0])
        answer1[0] = separated_words
        fors_token = self.for_index_recognize(answer1[0],answer1[2],answer1[1] )
        wrong_char_indexes=self.wrong_for_indexes(answer1[0] , answer1[1] , fors_token)
        for i in range(0,len(wrong_char_indexes)):
            count = count +1
            self.show.insert('end' , 'The index: ')
            self.show.insert('end' , wrong_char_indexes[i][0])
            self.show.insert('end' , '\n')
            self.show.insert('end' , 'In row:')
            self.show.insert('end' , wrong_char_indexes[i][1])
            self.show.insert('end' , '\n')
            self.show.insert('end' , '\n')
        self.general.insert('end' , 'Number of wrong indexes: ')
        self.general.insert('end' , count)
        self.general.insert('end' , '\n')
        self.general.insert('end' , '\n')

    def show_pylint(self):
        os.system('pylint '+self.path.get()+' > tmp')
        info=open('tmp', 'r').read()
        self.show.insert('end' , '\n')
        self.show.insert('end' , '----------------------------------------------------------------------\n')
        self.show.insert('end' , 'Pylinter results:\n\n\n')
        self.show.insert('end' , info)
        self.show.insert('end' , '\n')
             
    def startup(self):
        a = self.path.get()
        count = 0
        self.clear()
        if os.path.isfile(a):
            self.general.insert('end' , 'File opened correctly.\n\n')
            grabed_text_file = open( a , 'r')
            for i in grabed_text_file:
                count = count + 1
            self.general.insert('end' , 'Number of opened file lines: ')
            self.general.insert('end' , count)
            self.general.insert('end' , '\n\n')
            fsize=os.stat(a)
            size = 'size:' + fsize.st_size.__str__() + ' Bytes'
            self.general.insert('end' , size)
            self.general.insert('end' , '\n\n')           
        else:
            self.general.insert('end' , 'Enter a correct directory!\n')
        return

    def action(self):
        self.startup()
        self.show_functions_having_more_than_4_arguments()
        self.show_variables_and_classes_having_meaningless_names()
        self.show_functions_which_their_names_are_not_verb()
        self.show_length_1_indexes_that_does_not_belong_to_a_for()
        self.show_pylint()
        
def main():            
    root = Tk()
    root.geometry('800x540')
    root.title('Pylean')                         
                
    app = manager(root)
    root.mainloop()

if __name__ == "__main__": main()

