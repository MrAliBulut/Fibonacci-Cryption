---

# Fibonacci Encryption and Decryption

This Python script implements a simple encryption and decryption algorithm based on the Fibonacci sequence.

## How It Works

1. **Fibonacci Calculator:**
   - The `fibonacciCalculator(n, memo={})` function calculates the value of a given index in the Fibonacci sequence using memoization for efficiency.

2. **Fibonacci Sequence Initialization:**
   - The `FibonacciSequence(memory={})` function initializes a dictionary with pre-computed Fibonacci values (256 entries for ASCII values).

3. **Find Value in Dictionary:**
   - The `findvalue(value)` function returns the key of a given value in the Fibonacci sequence dictionary.

4. **Encryption:**
   - The `encrypt(text)` function translates a text message into a series of Fibonacci values, separated by "99919". It utilizes ASCII values for characters.

5. **Decryption:**
   - The `decrypt(text)` function reverses the encryption process, converting Fibonacci values back into characters.

6. **User Interface:**
   - The program runs in a loop, allowing the user to choose between encryption, decryption, or exiting the loop.

## Usage

1. Run the script and follow the prompts to choose an operation.
2. For encryption, input the message you want to encrypt.
3. For decryption, input the encrypted message.
4. To exit the program, select the corresponding option.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Special Thanks

Special thanks to ChatGPT for assistance in refining the description.

---
