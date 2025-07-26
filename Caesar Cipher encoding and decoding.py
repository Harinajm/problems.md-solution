def caesar_cipher(message: str, shift: int, mode: str) -> str:
    """
    Encodes or decodes a message using the Caesar cipher technique.


    Args:
        message (str): The input string to be encoded or decoded.
        shift (int): The number of positions to shift letters.
        mode (str): The operation mode, either 'encode' or 'decode'.


    Returns:
        str: The resulting encoded or decoded message.
       
    Raises:
        ValueError: If the mode is not 'encode' or 'decode'.
    """
    if mode.lower() not in ['encode', 'decode']:
        raise ValueError("Mode must be either 'encode' or 'decode'.")


    # For decoding, we simply shift in the opposite direction.
    if mode.lower() == 'decode':
        shift = -shift


    result = []
   
    for char in message:
        if char.isalpha():
            # Determine the base ASCII value (for 'a' or 'A')
            start = ord('a') if char.islower() else ord('A')
           
            # Calculate the shifted character
            # 1. Find the position of the character in the alphabet (0-25)
            # 2. Add the shift
            # 3. Use modulo 26 to wrap around the alphabet
            # 4. Convert back to ASCII and then to a character
            offset = (ord(char) - start + shift) % 26
            shifted_char = chr(start + offset)
            result.append(shifted_char)
        else:
            # Non-alphabetic characters are not changed
            result.append(char)
           
    return "".join(result)


# --- Example Usage ---
if __name__ == "__main__":
    original_message = "The quick brown fox jumps over the lazy dog!"
    shift_amount = 3


    # Encoding
    encoded_message = caesar_cipher(original_message, shift_amount, 'encode')
    print(f"Original Message:  {original_message}")
    print(f"Encoded Message:   {encoded_message}")
    print("-" * 20)


    # Decoding
    decoded_message = caesar_cipher(encoded_message, shift_amount, 'decode')
    print(f"Message to Decode: {encoded_message}")
    print(f"Decoded Message:   {decoded_message}")
   
    # Example from the problem description
    print("-" * 20)
    print("Example: with a left shift of 3, D would be replaced by A.")
    print(f"Encoding 'D' with shift 3: {caesar_cipher('D', 3, 'encode')}") # Should be G (right shift)
    # The problem description "left shift of 3, D would be replaced by A" is equivalent
    # to a negative shift or decoding with a positive shift.
    print(f"Decoding 'D' with shift 3: {caesar_cipher('D', 3, 'decode')}") # Should be A
