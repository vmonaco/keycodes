'''
Created on Oct 18, 2013

@author: vinnie
'''

import string
from itertools import product
from collections import defaultdict

keyboard = {
            'back_quote': (4, 1),
            '1': (4,2),
            '2': (4,3),
            '3': (4,4),
            '4': (4,5),
            '5': (4,6),
            '6': (4,7),
            '7': (4,8),
            '8': (4,9),
            '9': (4,10),
            '0': (4,11),
            'dash': (4,12),
            'equals': (4,13),
            'backspace': (4,14.5),
            
            'tab':(3,1.25),
            'q':(3,2.25),
            'w':(3,3.25),
            'e':(3,4.25),
            'r':(3,5.25),
            't':(3,6.25),
            'y':(3,7.25),
            'u':(3,8.25),
            'i':(3,9.25),
            'o':(3,10.25),
            'p':(3,11.25),
            'open_bracket':(3,12.25),
            'close_bracket':(3,13.25),
            'back_slash':(3,14.75),
            
            
            
            'windows': (1.5, ),
            'alt': (),
            'space': (),
            'alt': (),
            'windows': (),
            
            
            'escape': (5, 1.5),
            }

keycode = defaultdict(dict)

keycode['default'][0] = 'unknown'
keycode['default'][8] = 'backspace'
keycode['default'][9] = 'tab'
keycode['default'][13] = 'enter'
keycode['default'][16] = 'shift'
keycode['default'][17] = 'ctrl'
keycode['default'][18] = 'alt'
keycode['default'][19] = 'pause'
keycode['default'][20] = 'caps_lock'
keycode['default'][27] = 'escape'
keycode['default'][32] = 'space'
keycode['default'][33] = 'page_up'
keycode['default'][34] = 'page_down'
keycode['default'][35] = 'end'
keycode['default'][36] = 'home'
keycode['default'][37] = 'left'
keycode['default'][38] = 'up'
keycode['default'][39] = 'right'
keycode['default'][40] = 'down'
keycode['default'][45] = 'insert'
keycode['default'][46] = 'delete'
keycode['default'][48] = '0'
keycode['default'][49] = '1'
keycode['default'][50] = '2'
keycode['default'][51] = '3'
keycode['default'][52] = '4'
keycode['default'][53] = '5'
keycode['default'][54] = '6'
keycode['default'][55] = '7'
keycode['default'][56] = '8'
keycode['default'][57] = '9'
keycode['default'][59] = 'semicolon'
keycode['default'][61] = 'equals'
keycode['default'][65] = 'a'
keycode['default'][66] = 'b'
keycode['default'][67] = 'c'
keycode['default'][68] = 'd'
keycode['default'][69] = 'e'
keycode['default'][70] = 'f'
keycode['default'][71] = 'g'
keycode['default'][72] = 'h'
keycode['default'][73] = 'i'
keycode['default'][74] = 'j'
keycode['default'][75] = 'k'
keycode['default'][76] = 'l'
keycode['default'][77] = 'm'
keycode['default'][78] = 'n'
keycode['default'][79] = 'o'
keycode['default'][80] = 'p'
keycode['default'][81] = 'q'
keycode['default'][82] = 'r'
keycode['default'][83] = 's'
keycode['default'][84] = 't'
keycode['default'][85] = 'u'
keycode['default'][86] = 'v'
keycode['default'][87] = 'w'
keycode['default'][88] = 'x'
keycode['default'][89] = 'y'
keycode['default'][90] = 'z'
keycode['default'][91] = 'left_windows'
keycode['default'][92] = 'right_windows'
keycode['default'][96] = 'numpad_0'
keycode['default'][97] = 'numpad_1'
keycode['default'][98] = 'numpad_2'
keycode['default'][99] = 'numpad_3'
keycode['default'][100] = 'numpad_4'
keycode['default'][101] = 'numpad_5'
keycode['default'][102] = 'numpad_6'
keycode['default'][103] = 'numpad_7'
keycode['default'][104] = 'numpad_8'
keycode['default'][105] = 'numpad_9'
keycode['default'][106] = 'numpad_multiply'
keycode['default'][107] = 'numpad_add'
keycode['default'][109] = 'numpad_subtract'
keycode['default'][110] = 'numpad_decimal'
keycode['default'][111] = 'numpad_divide'
keycode['default'][112] = 'f1'
keycode['default'][113] = 'f2'
keycode['default'][114] = 'f3'
keycode['default'][115] = 'f4'
keycode['default'][116] = 'f5'
keycode['default'][117] = 'f6'
keycode['default'][118] = 'f7'
keycode['default'][119] = 'f8'
keycode['default'][120] = 'f9'
keycode['default'][121] = 'f10'
keycode['default'][122] = 'f11'
keycode['default'][123] = 'f12'
keycode['default'][144] = 'num_lock'
keycode['default'][145] = 'scroll_lock'
keycode['default'][188] = 'comma'
keycode['default'][189] = 'dash'
keycode['default'][190] = 'period'
keycode['default'][191] = 'slash'
keycode['default'][192] = 'back_quote'
keycode['default'][219] = 'open_bracket'
keycode['default'][220] = 'back_slash'
keycode['default'][221] = 'close_bracket'
keycode['default'][222] = 'quote'
keycode['default'][224] = 'left_apple'

keycode['native'][10] = 'enter'
keycode['native'][24] = 'quote'
keycode['native'][44] = 'comma'
keycode['native'][45] = 'dash'
keycode['native'][46] = 'period'
keycode['native'][47] = 'slash'
keycode['native'][91] = 'open_bracket'
keycode['native'][92] = 'back_slash'
keycode['native'][93] = 'close_bracket'
keycode['native'][127] = 'delete'
keycode['native'][155] = 'insert'
keycode['native'][524] = 'windows'

keycode['native'][129] = 'back_quote'
keycode['native'][151] = '8'
keycode['native'][152] = 'quote'
keycode['native'][154] = 'print_screen'
keycode['native'][156] = 'help'
keycode['native'][157] = 'alt'
keycode['native'][160] = 'comma'
keycode['native'][161] = 'open_bracket'
keycode['native'][162] = 'close_bracket'
keycode['native'][512] = '2'
keycode['native'][513] = 'semicolon'
keycode['native'][515] = '4'
keycode['native'][517] = '1'
keycode['native'][519] = '9'
keycode['native'][520] = '3'
keycode['native'][521] = 'equals'
keycode['native'][522] = '0'
keycode['native'][523] = 'dash'
keycode['native'][525] = 'menu'

keycode['opera'][59] = 'semicolon'
keycode['opera'][61] = 'equals'
keycode['opera'][109] = 'dash'
keycode['opera'][219] = 'windows'
keycode['opera'][0] = 'menu'

keycode['MSIE'][186] = 'semicolon'
keycode['MSIE'][187] = 'equals'
keycode['MSIE'][189] = 'dash'
keycode['MSIE'][91] = 'windows'
keycode['MSIE'][93] = 'menu'

keycode['firefox'][59] = 'semicolon'
keycode['firefox'][107] = 'equals'
keycode['firefox'][109] = 'dash'
keycode['firefox'][91] = 'windows'
keycode['firefox'][93] = 'menu'

keycode['safari'][186] = 'semicolon'
keycode['safari'][187] = 'equals'
keycode['safari'][189] = 'dash'
keycode['safari'][91] = 'windows'
keycode['safari'][93] = 'menu'

keycode['chrome'][186] = 'semicolon'
keycode['chrome'][187] = 'equals'
keycode['chrome'][189] = 'dash'
keycode['chrome'][91] = 'windows'
keycode['chrome'][93] = 'menu'

def lookup_key(kc, agent='default'):
    
    if kc in keycode[agent]:
        return keycode[agent][kc]
    elif kc in keycode['default']:
        return keycode['default'][kc]
    else:
        print 'Warning: unknown keycode', kc, 'with agent', agent
        return None
    
def transitions(set_a, set_b):
    
    return set(['%s__%s' %(k1,k2) for k1,k2 in product(set_a, set_b)])
    
# key sets
vowels          = set('aeiou')
consonants      = set('bcdfghjklmnpqrstvwxyz')
freq_cons       = set('tnsrh')
next_freq_cons  = set('ldcpf')
least_freq_cons = set('mwybg')
other_cons      = set('jkqvxz')
left_letters    = set('qwertasdfgzxcvb')
right_letters   = set('yuiophjklnm')

left_hand = set('qwertasdfgzxcvb12345')
right_hand = set('yuiophjklnm67890')

digits          = set(string.digits)
letters         = set(string.ascii_lowercase)
all_keys        = set([k for agent in keycode.values() for k in agent.values()])

non_letters     = set([c for c in all_keys if c not in set(letters)])
punctuation     = set(['period', 'comma', 'quote', 'back_quote', 'slash', 'semicolon', 'open_bracket', 'close_bracket'])
punctuation_other = set(['back_quote', 'slash', 'semicolon', 'open_bracket', 'close_bracket'])
other_non_letters = set([c for c in all_keys if c not in set().union(letters, punctuation, digits, set(['space', 'shift']))])


# sets of transitions
left_hand__left_hand = transitions(left_hand, left_hand)
left_hand__right_hand = transitions(left_hand, right_hand)
right_hand__left_hand = transitions(right_hand, left_hand)
right_hand__right_hand = transitions(right_hand, right_hand)

all_keys__all_keys = transitions(all_keys, all_keys)
letters__letters = transitions(letters, letters)
letters__non_letters = transitions(letters, non_letters)
non_letters__letters = transitions(non_letters, letters)
non_letters__non_letters = transitions(non_letters, non_letters)
consonants__consonants = transitions(consonants, consonants)
vowels__consonants = transitions(vowels, consonants)
consonants__vowels = transitions(consonants, vowels)
vowels__vowels = transitions(vowels, vowels)

double__letters = set(['%s__%s' %(k1,k2) for k1,k2 in zip(letters, letters)])

letters__space = transitions(letters, ['space'])
letters__punctuation = transitions(letters, punctuation)
shift__letters = transitions(['shift'], letters)
space__letters = transitions(['space'], letters)
punctuation__space = transitions(punctuation, ['space']) 

left_pointer = set('rtfgvb')
left_middle = set('dec')
left_index = set('wsx')
left_pinky = set('qaz')
     
right_pointer = set('yuhjvm')
right_middle = {'i', 'k', 'comma'}
right_index = {'o', 'l', 'period'}
right_pinky = {'p', 'semicolon', 'slash'}

left_pointer__left_pointer = transitions(left_pointer, left_pointer)
left_pointer__left_middle = transitions(left_pointer, left_middle)
left_pointer__left_index = transitions(left_pointer, left_index)
left_pointer__left_pinky = transitions(left_pointer, left_pinky)
left_pointer__right_pointer = transitions(left_pointer, right_pointer)
left_pointer__right_middle = transitions(left_pointer, right_middle)
left_pointer__right_index = transitions(left_pointer, right_index)
left_pointer__right_pinky = transitions(left_pointer, right_pinky)

left_middle__left_pointer = transitions(left_middle, left_pointer)
left_middle__left_middle = transitions(left_middle, left_middle)
left_middle__left_index = transitions(left_middle, left_index)
left_middle__left_pinky = transitions(left_middle, left_pinky)
left_middle__right_pointer = transitions(left_middle, right_pointer)
left_middle__right_middle = transitions(left_middle, right_middle)
left_middle__right_index = transitions(left_middle, right_index)
left_middle__right_pinky = transitions(left_middle, right_pinky)

left_index__left_pointer = transitions(left_index, left_pointer)
left_index__left_middle = transitions(left_index, left_middle)
left_index__left_index = transitions(left_index, left_index)
left_index__left_pinky = transitions(left_index, left_pinky)
left_index__right_pointer = transitions(left_index, right_pointer)
left_index__right_middle = transitions(left_index, right_middle)
left_index__right_index = transitions(left_index, right_index)
left_index__right_pinky = transitions(left_index, right_pinky)

left_pinky__left_pointer = transitions(left_pinky, left_pointer)
left_pinky__left_middle = transitions(left_pinky, left_middle)
left_pinky__left_index = transitions(left_pinky, left_index)
left_pinky__left_pinky = transitions(left_pinky, left_pinky)
left_pinky__right_pointer = transitions(left_pinky, right_pointer)
left_pinky__right_middle = transitions(left_pinky, right_middle)
left_pinky__right_index = transitions(left_pinky, right_index)
left_pinky__right_pinky = transitions(left_pinky, right_pinky)

right_pointer__left_pointer = transitions(right_pointer, left_pointer)
right_pointer__left_middle = transitions(right_pointer, left_middle)
right_pointer__left_index = transitions(right_pointer, left_index)
right_pointer__left_pinky = transitions(right_pointer, left_pinky)
right_pointer__right_pointer = transitions(right_pointer, right_pointer)
right_pointer__right_middle = transitions(right_pointer, right_middle)
right_pointer__right_index = transitions(right_pointer, right_index)
right_pointer__right_pinky = transitions(right_pointer, right_pinky)

right_middle__left_pointer = transitions(right_middle, left_pointer)
right_middle__left_middle = transitions(right_middle, left_middle)
right_middle__left_index = transitions(right_middle, left_index)
right_middle__left_pinky = transitions(right_middle, left_pinky)
right_middle__right_pointer = transitions(right_middle, right_pointer)
right_middle__right_middle = transitions(right_middle, right_middle)
right_middle__right_index = transitions(right_middle, right_index)
right_middle__right_pinky = transitions(right_middle, right_pinky)

right_index__left_pointer = transitions(right_index, left_pointer)
right_index__left_middle = transitions(right_index, left_middle)
right_index__left_index = transitions(right_index, left_index)
right_index__left_pinky = transitions(right_index, left_pinky)
right_index__right_pointer = transitions(right_index, right_pointer)
right_index__right_middle = transitions(right_index, right_middle)
right_index__right_index = transitions(right_index, right_index)
right_index__right_pinky = transitions(right_index, right_pinky)

right_pinky__left_pointer = transitions(right_pinky, left_pointer)
right_pinky__left_middle = transitions(right_pinky, left_middle)
right_pinky__left_index = transitions(right_pinky, left_index)
right_pinky__left_pinky = transitions(right_pinky, left_pinky)
right_pinky__right_pointer = transitions(right_pinky, right_pointer)
right_pinky__right_middle = transitions(right_pinky, right_middle)
right_pinky__right_index = transitions(right_pinky, right_index)
right_pinky__right_pinky = transitions(right_pinky, right_pinky)

