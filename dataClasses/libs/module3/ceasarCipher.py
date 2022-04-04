import string

def build_coder_helper(char, shift):
    """Returns shifted character

    Args:
        char (str): character to be coded
        shift (int): shift setting

    Returns:
        str: containing shifted characted
    """
    list_of_chr_LC = ' ' + string.ascii_lowercase
    list_of_chr_UC = ' ' + string.ascii_uppercase

    if char in list_of_chr_LC:
        chr_index = list_of_chr_LC.index(char)
        shift_index = chr_index + shift
        if shift_index >= len(list_of_chr_LC):
            shift_index -= len(list_of_chr_LC)
        return list_of_chr_LC[shift_index]

    elif char in list_of_chr_UC:
        chr_index = list_of_chr_UC.index(char)
        shift_index = chr_index + shift
        if shift_index >= len(list_of_chr_UC):
            shift_index -= len(list_of_chr_UC)
        return list_of_chr_UC[shift_index]

    

def build_coder(shift: int): 
    """ 
    Returns a dict that can apply a Caesar cipher to a letter. 
    The cipher is defined by the shift value. Ignores non-letter characters 
    like punctuation and numbers. 
    shift: -27 < int < 27 
    returns: dict 
    Example: >>> build_coder(3) 
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J', 
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O', 
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X', 
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd', 
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l', 
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q', 
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z', 
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'} 
    (The order of the key-value pairs may be different.) 
    """ 
    if type(shift) is not int:
        raise TypeError('Shift not an int')
        
    elif shift < -27 or shift >= 27:
        raise ValueError('Shift is out-of-range')
    
    shifted_hash = {}
    list_of_chr = ' ' + string.ascii_letters
    for char in list_of_chr:
            shifted_hash[char] = build_coder_helper(char, shift)
    
    return shifted_hash

def build_encoder(shift): 
    """ 
    Returns a dict that can be used to encode a plain text. For example, you 
    could encrypt the plain text by calling the following commands 
    >>>encoder = build_encoder(shift) 
    >>>encrypted_text = apply_coder(plain_text, encoder) 
    The cipher is defined by the shift value. Ignores non-letter characters 
    like punctuation and numbers. 
    shift: 0 <= int < 27 
    returns: dict 
    Example: >>> build_encoder(3) 
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J', 
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O', 
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X', 
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd', 
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l', 
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q', 
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z', 
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'} 
    (The order of the key-value pairs may be different.) 
    HINT : Use build_coder. 
    """ 
    if type(shift) is not int:
        raise TypeError('Shift is not an int')
        
    elif shift < 0 or shift >= 27:
        raise ValueError('Shift is out-of-range')

    return build_coder(shift)

  
def build_decoder(shift): 
    """ 
    Returns a dict that can be used to decode an encrypted text. For example, 
    you 
    could decrypt an encrypted text by calling the following commands 
    >>>encoder = build_encoder(shift) 
    >>>encrypted_text = apply_coder(plain_text, encoder) 
    >>>decrypted_text = apply_coder(plain_text, decoder) 
    The cipher is defined by the shift value. Ignores non-letter characters 
    like punctuation and numbers. 
    shift: 0 <= int < 27 
    returns: dict 
    Example: >>> build_decoder(3) 
    {' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D', 
    'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I', 
    'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R', 
    'T': 'Q', 'W': 'T', 'V': 'S', 'Y': 'V', 'X': 'U', 'Z': 'W', 'a': 'y', 
    'c': ' ', 'b': 'z', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f', 
    'h': 'e', 'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k', 
    'q': 'n', 'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't', 
    'v': 's', 'y': 'v', 'x': 'u', 'z': 'w'} 
    (The order of the key-value pairs may be different.) 
    HINT : Use build_coder. 
    """ 
    if type(shift) is not int:
        raise TypeError('Shift is not an int')
        
    elif shift < 0 or shift >= 27:
        raise ValueError('Shift is out-of-range')

    return build_coder(-shift)

  
def apply_coder(text, coder): 
    """ 
    Applies the coder to the text. Returns the encoded text. 
    text: string 
    coder: dict with mappings of characters to shifted characters 
    returns: text after mapping coder chars to original text 
    Example: 
    >>> apply_coder("Hello, world!", build_encoder(3)) 
    'Khoor,czruog!' 
    >>> apply_coder("Khoor,czruog!", build_decoder(3)) 
    'Hello, world!' 
    """ 
    encoded_string = ""
    chr_to_encode = ' ' + string.ascii_letters
    for char in text:
        if char in chr_to_encode:
            encoded_string += coder[char]
        else:
            encoded_string += char

    return encoded_string
  
def apply_shift(text, shift): 
    """ 
    Given a text, returns a new text Caesar shifted by the given shift 
    offset. The empty space counts as the 27th letter of the alphabet, 
    so spaces should be replaced by a lowercase letter as appropriate. 
    Otherwise, lower case letters should remain lower case, upper case 
    letters should remain upper case, and all other punctuation should 
    stay as it is. 
    text: string to apply the shift to 
    shift: amount to shift the text 
    returns: text after being shifted by specified amount. 
    Example: 
    >>> apply_shift('This is a test.', 8) 
    'Apq hq hiham a.' 
    """ 
    if type(text) is not str:
        raise TypeError('Text in not of type str')
        
    if shift >= 0:
        return apply_coder(text, build_encoder(shift))
    else:
        return apply_coder(text, build_decoder(abs(shift)))

if __name__ == '__main__':
    decoded_string = "This is a test"
    encoded_string = "Apq hq hiham a."
    print(apply_shift(decoded_string, 8))
    print(apply_shift(encoded_string, -8))
