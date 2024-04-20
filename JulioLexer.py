# symbols 
#   + - * / ( ) = == != < > <= >= , ; { } [ ]
# keywords
#   Julio Says, Julio Wants, Julio Lets, Julio Gets, is, fr?, Int, Float, None, Char, String, Bool, YES, NO

import re

# tokens
TOKENS = {
    'STRING_LITERAL': r'".*?"',
    'CHAR_LITERAL': r"'.*?'",
    'FLOAT_LITERAL': r'\d+\.\d+',
    'INT_LITERAL': r'\d+',
    'BOOL_LITERAL': r'YES|NO',
    'NONE_LITERAL': r'None',
    'KEYWORD': r'Julio Says|Julio Wants|Julio Lets|Julio Gets|Julio Opens|Julio Writes|Julio Asks|is|fr\?',
    'TYPE': r'Int|Float|None|Char|String|Bool',
    'OPERATOR': r'\+|-|\*|/|==|!=| < | > | <= | >= | % | ! | =',
    'LPAREN': r'\(',
    'RPAREN': r'\)',
    'LBRACE': r'\{',
    'RBRACE': r'\}',
    'LBRACKET': r'\[',
    'RBRACKET': r'\]',
    'COMMA': r',',
    'SEMICOLON': r';',
    'COLON': r':',
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'COMMENT': r'//.*',
    'SKIP': r'[ \t]+',
    'NEWLINE': r'\n',
    'EOF': r'\0',
    'MISMATCH': r'.',
}

class JulioTokens:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value: return f'{self.type}: {self.value}'
        return f'{self.type}'
    
class JulioLexer:
    def __init__(self):
        self.pos = 0
        self.current_tk = None
        self.tokens = []
        self.compile_tk = {tok: re.compile(regex) for tok, regex in TOKENS.items()}

    def tokenize(self, text, line_number=1):

        while (self.pos < len(text)):
            match = None
            for token, regex in self.compile_tk.items():
                match = regex.match(text, self.pos)
                if match:
                    value = match.group(0)
                    if token == 'SKIP':
                        pass
                    elif token == 'NEWLINE':
                        self.tokens.append(JulioTokens('NEWLINE'))
                    elif token == 'EOF':
                        self.tokens.append(JulioTokens('EOF'))
                    elif token == 'MISMATCH':
                        raise RuntimeError(f'Token {value} not recognized: line {line_number} column {self.pos}')
                    else:
                        self.tokens.append(JulioTokens(token, value))
                    self.pos = match.end(0)
                    break
            if not match:
                raise RuntimeError(f'Could not match any token at position {self.pos}')
        return self.tokens
    
    def __repr__(self):
        return f'{self.tokens}'
    
lexer = JulioLexer()
lexer.tokenize('Julio Wants String: Print(String message){}')
print(lexer)

        
        