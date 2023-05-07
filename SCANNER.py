import ply.lex as lex
from prettytable import PrettyTable
import sys
# Define the list of token names
tokens = ( 
    'ID',
     'VALENCIA',
     'ENLACE',
    'TIPO',
    'ASIGNACION',
     'FIN_DE_LINEA',
     'ELEMENTO_QUIMICO',
    'OPERACION',
    'PARAENTESIS_IZQ',
    'PARAENTESIS_DER',
    'PALABRAS_RESERVADAS',
    'INICIO', 'DEFINA', 'COMO', 'FIN',
     'COR_IZQ',
     'COR_DER'
 )



with open (sys.argv[1],'r') as file:
    i = file.read()


# Define a regular expression

def t_ASIGNACION(t):
    r':='
    return t

def t_TIPO(t):
    r'modelo'
    return t

def t_PALABRAS_RESERVADAS(t):
    r'(inicio|defina|como|fin)'
    if t.value == 'inicio':
        t.type = 'INICIO'
    elif t.value == 'fin':
        t.type = 'FIN'
    elif t.value == 'defina':
        t.type = 'DEFINA'
    elif t.value == 'como':
        t.type = 'COMO'
    return t

def t_ELEMENTO_QUIMICO(t):
    r'Ag|Al|Ar|As|At|Au|Ba|Be|Bh|Bi|Br|Ca|Cd|Cl|Co|Cr|Cs|Cu|Db|Fe|Fr|Ga|Ge|He|Hf|Hg|Hn|Ir|Jl|Kr|Li|ln|Mg|Mn|Mo|Mt|Na|Nb|Ne|Ni|Os|Pb|Pd|Po|Pt|Ra|Rb|Re|Rf|Rh|Rn|Ru|Sb|Sc|Se|Si|Sn|Sr|Ta|Tc|Te|Ti|Tl|Xe|Zn|Zr|B|C|F|H|I|K|N|O|P|S|V|W|Y'
    return t

def t_OPERACION(t):
    r'graficar2d|graficar3d|pesomolecular'
    return t

def t_VALENCIA(t):
    r'[1-9]'
    return t



# Define the regular expression for each token
t_FIN_DE_LINEA=r'\;'
t_ID= r'[a-zA-Z][a-zA-Z0-9_]*'
t_ENLACE=r'\-|\:\:|\:|\='
t_PARAENTESIS_IZQ= r'\('
t_PARAENTESIS_DER= r'\)'
t_COR_IZQ=r'\['
t_COR_DER=r'\]'

# Define a function to handle errors
def t_error(t):
    print(f"Error: Illegal character '{t.value[0]}'")
    t.lexer.skip(1)
t_ignore = ' '     

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def find_column(i, t):
    line_start = i.rfind('\n', 0, t.lexpos) + 1
    return (t.lexpos - line_start) + 1



# Build the lexer
lexer = lex.lex()



# Test the lexer

lexer.input(i)
tokens =[]


for tok in lexer:
    tokens.append((tok.type,tok.value,tok.lineno,tok.lexpos))
    

x = PrettyTable()
x.field_names = ["Token", "Lexema","Linea","Columna"]
for prod in tokens:
    x.add_row(prod)

print(x)

