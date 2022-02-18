# KLimitRLL
In this project we will be implementing the Run-Length-Limited algorithm.

Our solution is implemented in Python, based on the classical algorithm described in [1]. We support any k starting from 3.
We provide the following API:
- EncodeFile(str filename, int k)
 Used to encode a file. The output is an encoded file that has no k-or-longer zero runs.
- DecodeFile(str filename, int k)
A decoding function that returns the original file.
- EncodeAnyRun(str word, int k)
Used to encode a word. The output is an encoded word that has no k-or-longer zero runs. 
- DecodeAnyRun(str word, int k)
A decoding function that returns the original word.
 - kLimitRLLTest(int iters, int min_k, int max_k, int min_length, int max_length)
A test function that runs for iters iterations, each time generating a binary word of size between min_length and max_length and a k of size between min_k and max_k. Checking whether the encoded word does not have zero-runs longer or equal to k, and that the decoded-encoded word is equal to the original one.


Notes:
1. In each of these functions, if no k was provided, the functions will assume k=⌈log⁡n ⌉+1, where n is the line/word length (as defined in the classical RLL algorithm).
2. Our functions provide support for words over the binary alphabet  Σ={0,1}.
