## UTCTF2025 - SafeWord

### Introduction and First thoughts

The idea of this challenge is hinted at the word "safe" at its name. The ELF isn't a normal flag checker with a simple success message, instead we can say that the flag is correct if the program is executed safely, without any crashing. A simple test with a random flag will crash as shown below:

```
Flag> utflag{wrong_fl4g}
Instrução ilegal (imagem do núcleo gravada)
```

While the error message is in portuguese (because it is my OS language), it is simply translated as "illegal instruction", meaning that one of the instructions that is executed during the execution flow with the provided input isn't valid.

### Initial Analysis

The only analysis tools that I used for my solve were  the free disassembler and decompiler IDA Free and an online [disassembler](https://defuse.ca/online-x86-assembler.htm). One problem that some competitors may have faced when trying to decompile the main function of the challenge is it's big size, that requires a change in the max decompilation size in the HexRays plugin, which can be done as shown in [Igor's Tip of the week #166](https://hex-rays.com/blog/igors-tip-of-the-week-166-dealing-with-too-big-function) (a great resource that I reccomend for any IDA user). After changing the settings and doing some minor tweaks with variable names and types, the decompiled main function will look like this:

```c
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  int ret_value; // [rsp+8h] [rbp-18h]
  int i; // [rsp+Ch] [rbp-14h]
  char *s; // [rsp+10h] [rbp-10h]
  _QWORD *v7; // [rsp+18h] [rbp-8h]

  some_ptr = (__int64 *)mmap(0LL, 0x1000uLL, 7, 0x22, 0xFFFFFFFF, 0LL);
  if ( some_ptr == (__int64 *)0xFFFFFFFFFFFFFFFFLL )
  {
    perror("Error: couldn't mmap instruction buffer ");
    exit(0xFFFFFFFF);
  }
  s = (char *)malloc(0x23uLL);
  printf("Flag> ");
  fgets(s, 0x22, stdin);
  v7 = malloc(0x40000uLL);
  ret_value = 0x5B;
  v7[0x5B00] = 0x733E626CLL;
  v7[0x5B01] = 0x2B742276LL;
  v7[0x5B02] = 0x997C9787LL;
  v7[0x5B03] = 0x57F44D65LL;
  v7[0x5B04] = 0xE81C529LL;
  v7[0x5B05] = 0x6B3E8E9BLL;
  ...
  v7[0x176] = 0x10E3D636LL;
  v7[0x177] = 0x6C1145BALL;
  v7[0x178] = 0x3A9D244BLL;
  v7[0x179] = 0xD3E62824LL;
  v7[0x17A] = 0xDF93632ALL;
  v7[0x17B] = 0xC042AB9ELL;
  v7[0x17C] = 0x5D16D40LL;
  v7[0x17D] = 0xC3585B6ALL;
  v7[0x17E] = 0x89DF9C92LL;
  v7[0x17F] = 0xE8E7E32FLL;
  v7[0x7200] = 0xC358006ALL;
  for ( i = 0; i <= 0x20; ++i )
    ret_value = interpret(v7[0x100 * ret_value + s[i]]);
  return 0LL;
}
```

Notice that the biggest part of the function is simply a collection of assignments to the (VERY BIG) array "v7". This array is essential to the last part of the code, the loop that will call the (named intuitively by the nature of the challenge) "interpret" function. This kind of big array initially made me think that we would have some kind of VM bytecode inside the array, however, the analysis of the interpret function proved me wrong. Notice that the integer values shown here are in hexadecimal because of another change from default HexRays settings (and this will be useful in the last stage of the solve). 

Notice that the interpret function receives one of the integers from the array as its input, with the index of the array determined by the current character of the string "s" (which is the inserted flag) and a multiplication of the variable "ret_value" (initial value 0x5B) with 0x100. The variable ret_value is named this way because it receives the return value of the function "interpret". Below, we can see the decompilation of the last two important functions of this file.

```c
__int64 __fastcall interpret(__int64 a1)
{
  *some_ptr = a1;
  return execute();
}
```

The first function is simple, but it must be correctly interpreted. Notice that the integer received by the interpret function, that comes from the v7 array, is assigned to the memory position pointed by the global variable "some_ptr". This memory region is allocated during the start of the main function, using mmap to allow for execution permission in this memory region. After this, the execute function is called, and it's return value is used as the return value for the interpret function.

```c
__int64 execute()
{
  return ((__int64 (*)(void))some_ptr)();
}
```

The execute function contains only one line, but it may be more complex for everyone who is not familiar with function pointers. Basically, this functions treats the integer contained in the address pointed by "some_ptr" as the compiled assembly code of a function, then the function is called and it's return value is used as the return value of the execute function. For those not used to the notation of function pointers, the following assembly code of the function execute may be clearer.

```assembly
execute         proc near               ; 
endbr64
push    rbp
mov     rbp, rsp
mov     rax, cs:some_ptr
call    rax ; some_ptr
pop     rbp
retn
```



TLDR: When the function "interpret" is called, the integer passed as a parameter is treated as assembly code and executed.

Knowing this, it is understandable why the program is crashing with the execution of illegal instructions, the integers passed to the interpret function aren't always valid functions, with most not containing even the final ret instruction! But how can we find the characters that will lead to the right flag? 

### Assembly and Hexadecimals

The most simple way to continue the solve from here is to analyze what happens when the first character is "u", from "utflag{...}", then look for the following characters. With the character "u", the first index of the v7 array that will be used is 0x5B * 0x100 + 0x75 = 0x5B75 (notice how the base-16 made the math easier). The corresponding integer is 0xC3580B6A and it can be easily disassembled using any online or offiline tool (make sure that you are using the x64 version of the disassembler), however, it is important to remember that this integer is stored using [Little Endian](https://en.wikipedia.org/wiki/Endianness), so the assembly is actually the byte sequence "6A 0B 58 C3". The corresponding assembly in this case is, then:

```assembly
0:  6a 0b                   push   0xb
2:  58                      pop    rax
3:  c3                      ret
```

This is a valid function, which will be executed correctly and return the value 0xB, because it is pushed to the stack then popped back to the rax register, responsible for return values. But how will we use this to find the next character in the flag? In this case, we already know it will be "t", since we are still in the start of the flag, so let's calculate the index again. **IMPORTANT: ** We must use the new value of the variable "ret_value", which now is 0xB, returned from the previous assembly code.

The calculation 0xB * 0x100 + 0x74 shows us that the next index will be 0xB74, corresponding to the integer 0xC358646A. Disassembling this integer, we get a very similar assembly code, which can be seen below.

```assembly
0:  6a 64                   push   0x64
2:  64                      pop    rax
3:  c3                      ret
```

The structure of the code is exactly the same, but the return value is slightly changed, being 0x64 this time. Will this pattern continue until we get to the "{" of the flag? The answer is yes. The sequence of indexes until the "{" is (from the start): 0x5B75, 0xB74, 0x6466, 0x236C, 0x761, 0x4667, 0x177B.

Knowing this pattern, how can we find the unknown part of the flag?

### Finding the flag

From here, there are many ways to find the rest of the flag, from disassembling each character and seeing which ones will lead to the assembly of a valid function (Capstone may be useful to automate this), to write scripts to interact with the binary bruteforcing the next character and checking the instruction count to see if the code progressed past the function call. My first method while solving this is closer to the first one, but manual and skipping the disassembly part. Let's analyze the disassembly of the function call related to the "{", with index 0x177B and integer value 0xC358476A. 

```assembly
0:  6a 47                   push   0x47
2:  64                      pop    rax
3:  c3                      ret
```



Notice that the disassembly is almost identical to the ones we saw previously, but with the return value 0x47, so the index chosen by the next character will be in the format 0x47XX. This return value could be easily deduced without using any tools, because the number 0xC358YY6A will always be executed as the function:



```assembly
0:  6a YY                   push   0xYY
2:  64                      pop    rax
3:  c3                      ret
```

Therefore, we can identify this nice patter 0xC358YY6A and know not only that a function call will not crash, but that the return value (and then, the value of the variable ret_value after this function call) will be 0xYY. Knowing this, we just need to look through the assignments made to the array v7 with indexes starting with 0x47, then check if the assigned integer is in the format 0xC358YY6A. Doing this, we find that the only assignment that will be useful for us is the assignment: "v7[0x4731] = 0xC3582E6A", then the next character must have value 0x31 in the ASCII table, corresponding to the digit "'1", while the follow up character will be related to an index of format 0x2EXX in the array v7. 

This process is slow, but can be done manually, leading to the full flag "utflag{1_w4nna_pl4y_hypix3l_in_c}". Note that there were multiple strings that would avoid crashing (because some return values allowed for two different follow up characters), but this was the only one that made sense and followed the UTCTF standard flag format.

### Accelerating the process

When I first solved the challenge, I did it manually, but not fully. I copy and pasted the assignments of the array v7 to a txt file and opened it in neovim, then I cleaned the file so that we would only have two columns with index and value separated by a space, instead of the full C syntax, which allowed for a symplex regex search accelerating the process. The regex search was: "/0xYY.. 0xC358..6A". Inserting the value of 0xYY, I read the empty spaces, with the last byte of the index representing the new character and the return value representing the new "0xYY", which could be replaced to find the next character until the end of the flag.

Although this process works, it is very boring and error prone, so I wrote a simple python script to parse this text file in the same way and print all the strings that avoid crashing the program.

```python
from functools import lru_cache

def check_valid_function(int_code):
    is_valid = True
    is_valid = is_valid and ((0xFF000000 & int_code) == 0xC3000000)
    is_valid = is_valid and ((0xFF0000 & int_code) == 0x580000)
    is_valid = is_valid and ((0xFF & int_code) == 0x6A)
    return is_valid

def possible_strings(data, ret_value, length = 0):
    if length == 33:
        return [""]
    possible_strings_ret = []
    possible_characters_ret_pair = []


    for index in range(ret_value * 0x100, (ret_value + 1) * 0x100):
        if index in data:
            if check_valid_function(data[index]):
                new_ret = (data[index] & 0xFF00) >> 8
                possible_characters_ret_pair.append((chr(index - ret_value * 0x100), new_ret))
    
    for p in possible_characters_ret_pair:
        possible_strings_ret += [p[0] + x for x in possible_strings(data, p[1], length+1)]
    
    return possible_strings_ret

def main():
    data = {}
    with open("data", "r") as datafile:
        for line in datafile.readlines():
            x,y = line.rstrip().split(" ")
            x = int(x, 16)
            y = int(y, 16)
            data[x] = y

    all_strings = possible_strings(data, 0x5B)
    all_strings = list(dict.fromkeys(all_strings))
    for s in all_strings:
        print(s)


if __name__ == "__main__":
    main()
```

The output of this program, containing both the correct flag and all the other strings (of appropriate size) which won't crash the program can be seen below.

```
utflagf_hypimpimpimpimpimpimpimpi
utflagf_hypimpimpimpimpimpimpix3l
utflagf_hypimpimpimpimpimpix3l_in
utflagf_hypimpimpimpimpimpix3la3l
utflagf_hypimpimpimpimpix3l_in_c}
utflagf_hypimpimpimpimpix3la3l_in
utflagf_hypimpimpimpimpix3la3la3l
utflagf_hypimpimpimpix3l_in_c}utf
utflagf_hypimpimpimpix3la3l_in_c}
utflagf_hypimpimpimpix3la3la3l_in
utflagf_hypimpimpimpix3la3la3la3l
utflagf_hypimpimpix3l_in_c}utflag
utflagf_hypimpimpix3la3l_in_c}utf
utflagf_hypimpimpix3la3la3l_in_c}
utflagf_hypimpimpix3la3la3la3l_in
utflagf_hypimpimpix3la3la3la3la3l
utflagf_hypimpix3l_in_c}utflagf_h
utflagf_hypimpix3l_in_c}utflag{1_
utflagf_hypimpix3la3l_in_c}utflag
utflagf_hypimpix3la3la3l_in_c}utf
utflagf_hypimpix3la3la3la3l_in_c}
utflagf_hypimpix3la3la3la3la3l_in
utflagf_hypimpix3la3la3la3la3la3l
utflagf_hypix3l_in_c}utflagf_hypi
utflagf_hypix3l_in_c}utflag{1_iut
utflagf_hypix3l_in_c}utflag{1_w4n
utflagf_hypix3la3l_in_c}utflagf_h
utflagf_hypix3la3l_in_c}utflag{1_
utflagf_hypix3la3la3l_in_c}utflag
utflagf_hypix3la3la3la3l_in_c}utf
utflagf_hypix3la3la3la3la3l_in_c}
utflagf_hypix3la3la3la3la3la3l_in
utflagf_hypix3la3la3la3la3la3la3l
utflag{1_iutflagf_hypimpimpimpimp
utflag{1_iutflagf_hypimpimpimpix3
utflag{1_iutflagf_hypimpimpix3l_i
utflag{1_iutflagf_hypimpimpix3la3
utflag{1_iutflagf_hypimpix3l_in_c
utflag{1_iutflagf_hypimpix3la3l_i
utflag{1_iutflagf_hypimpix3la3la3
utflag{1_iutflagf_hypix3l_in_c}ut
utflag{1_iutflagf_hypix3la3l_in_c
utflag{1_iutflagf_hypix3la3la3l_i
utflag{1_iutflagf_hypix3la3la3la3
utflag{1_iutflag{1_iutflagf_hypim
utflag{1_iutflag{1_iutflagf_hypix
utflag{1_iutflag{1_iutflag{1_iutf
utflag{1_iutflag{1_iutflag{1_w4nn
utflag{1_iutflag{1_w4nna_pl4u4nna
utflag{1_iutflag{1_w4nna_pl4y_hyp
utflag{1_w4nna_pl4u4nna_pl4u4nna_
utflag{1_w4nna_pl4u4nna_pl4y_hypi
utflag{1_w4nna_pl4y_hypimpimpimpi
utflag{1_w4nna_pl4y_hypimpimpix3l
utflag{1_w4nna_pl4y_hypimpix3l_in
utflag{1_w4nna_pl4y_hypimpix3la3l
utflag{1_w4nna_pl4y_hypix3l_in_c}
utflag{1_w4nna_pl4y_hypix3la3l_in
utflag{1_w4nna_pl4y_hypix3la3la3l
```

**CORRECT FLAG:** **utflag{1_w4nna_pl4y_hypix3l_in_c}**
