# Module 3 - Hash tables

Hash table is a very popular data structure in practice. It is a simple concept, but quite powerful when you use it effectively. For example, when you type www.engineeringwithutsav.com on your browser, your browser basically looks at your ISPs routing table, also called the DNS server, for the exact IP address of my web server that hosts the contents of my website. That routing table is basically a giant table with two columns: the domain name, which is the key, and the IP address, which is the value. And that's what a hash table is. It stores a bunch of unique keys that have certain values. You give it a key, and it will give you the value very quickly. In this case, you give it the domain name, and it gives you the IP address so that your browser can fetch the webpage to render. So yeah, you are basically relying on giant distributed hash tables every time you type a domain name on your browser.

## Project - Caesar Cipher

A Caesar cipher is a simple method of encoding messages. Caesar ciphers use a substitution method where letters in the alphabet are shifted by some fixed number of spaces to yield an encoding alphabet. A Caesar cipher with a shift of 1 would encode an A as a B, an M as an N, and a Z as an A, and so on. The method is named after Roman leader Julius Caesar, who used it in his private correspondence.

Write a program to encrypt plaintext into ciphertext using the Caesar cipher. Here is the program skeleton:
> def build_coder(shift):<br>
 """ <br>
 Returns a dict that can apply a Caesar cipher to a letter. <br>
 The cipher is defined by the shift value. Ignores non-letter characters <br>
 like punctuation and numbers. <br>
 shift: -27 < int < 27 <br>
 returns: dict <br>
 Example: >>> build_coder(3) <br>
 {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J', <br>
 'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O', <br>
 'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X', <br>
 'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd', <br>
 'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l', <br>
 'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q', <br>
 'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z', <br>
 'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'} <br>
 (The order of the key-value pairs may be different.) <br>
 """ 
 <!--  ### YOUR CODE GOES HERE --><br>

  
> def build_encoder(shift): <br>
 """ <br>
 Returns a dict that can be used to encode a plain text. For example, you <br>
 could encrypt the plain text by calling the following commands <br>
 >>>encoder = build_encoder(shift) <br>
 >>>encrypted_text = apply_coder(plain_text, encoder) <br>
 The cipher is defined by the shift value. Ignores non-letter characters <br>
 like punctuation and numbers. <br>
 shift: 0 <= int < 27 <br>
 returns: dict <br>
 Example: >>> build_encoder(3) <br>
 {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J', <br>
 'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O', <br>
 'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X', <br>
 'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd', <br>
 'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l', <br>
 'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q', <br>
 'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z', <br>
 'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'} <br>
 (The order of the key-value pairs may be different.) <br>
 HINT : Use build_coder. <br>
 """ <br>
 <!--  ### YOUR CODE GOES HERE --><br>

  
> def build_decoder(shift): <br>
 """ <br>
 Returns a dict that can be used to decode an encrypted text. For example, <br>
you <br>
 could decrypt an encrypted text by calling the following commands <br>
 >>>encoder = build_encoder(shift) <br>
 >>>encrypted_text = apply_coder(plain_text, encoder) <br>
 >>>decrypted_text = apply_coder(plain_text, decoder) <br>
 The cipher is defined by the shift value. Ignores non-letter characters <br>
 like punctuation and numbers. <br>
 shift: 0 <= int < 27 <br>
 returns: dict <br>
 Example: >>> build_decoder(3) <br>
 {' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D', <br>
 'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I', <br>
 'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R', <br>
 'T': 'Q', 'W': 'T', 'V': 'S', 'Y': 'V', 'X': 'U', 'Z': 'W', 'a': 'y', <br>
 'c': ' ', 'b': 'z', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f', <br>
 'h': 'e', 'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k', <br>
 'q': 'n', 'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't', <br>
 'v': 's', 'y': 'v', 'x': 'u', 'z': 'w'} <br>
 (The order of the key-value pairs may be different.) <br>
 HINT : Use build_coder. <br>
 """ <br>
 <!--  ### YOUR CODE GOES HERE --><br>

  
> def apply_coder(text, coder): <br>
 """ <br>
 Applies the coder to the text. Returns the encoded text. <br>
 text: string <br>
 coder: dict with mappings of characters to shifted characters <br>
 returns: text after mapping coder chars to original text <br>
 Example: <br>
 >>> apply_coder("Hello, world!", build_encoder(3)) <br>
 'Khoor,czruog!' <br>
 >>> apply_coder("Khoor,czruog!", build_decoder(3)) <br>
 'Hello, world!' <br>
 """ <br>
 <!--  ### YOUR CODE GOES HERE --><br>

  
> def apply_shift(text, shift): <br>
 """ <br>
 Given a text, returns a new text Caesar shifted by the given shift <br>
 offset. The empty space counts as the 27th letter of the alphabet, <br>
 so spaces should be replaced by a lowercase letter as appropriate. <br>
 Otherwise, lower case letters should remain lower case, upper case <br>
 letters should remain upper case, and all other punctuation should <br>
 stay as it is. <br>
 text: string to apply the shift to <br>
 shift: amount to shift the text <br>
 returns: text after being shifted by specified amount. <br>
 Example: <br>
 >>> apply_shift('This is a test.', 8) <br>
 'Apq hq hiham a.' <br>
 """ <br>
 <!--  ### YOUR CODE GOES HERE --><br>

## Resources

- [Intro to Hash tables](https://www.youtube.com/watch?v=h2d9b_nEzoA)

- [Intro to Hash tables (alternate)](https://www.youtube.com/watch?index=1&list=PLTxllHdfUq4f7-uHOpxXnBUbsuLiI9pmb&v=MfhjkfocRR0)

- [Hashing and chaining](https://www.youtube.com/watch?v=0M_kIqhwbFo)

- [Simple Hash table in Python](https://www.youtube.com/watch?v=pO6L8WEup_I)

## Self Assessment

- [Two Sum](https://leetcode.com/problems/two-sum/)

- [Unique email addresses](https://leetcode.com/problems/unique-email-addresses/)

- [Intersection of two arrays](https://leetcode.com/problems/intersection-of-two-arrays-ii/)

- [Missing number](https://leetcode.com/problems/missing-number/)

- [Subdomain visit count](https://leetcode.com/problems/subdomain-visit-count/)