section .data
    msg db "Input: ", 0
    len equ $ - msg
    correct_password db "result", 0

section .bss
    user_input resb 10

section .text
    global _start

_start:
    ; Display prompt
    mov eax, 4
    mov ebx, 1
    mov ecx, msg
    mov edx, len
    int 0x80

    ; Read user input
    mov eax, 3
    mov ebx, 0
    mov ecx, user_input
    mov edx, 10  ; Read up to 10 characters
    int 0x80

    ; Compare
    mov esi, user_input
    mov edi, correct_password

compare_loop:
    ; Load byte from input
    lodsb
    lodsb

    ; Compare
    cmp al, dl
    jne incorrect
    cmp al, 0
    je correct

    ; Loop
    jmp compare_loop

correct:
    mov eax, 4
    mov ebx, 1
    mov ecx, correct_message
    mov edx, correct_message_len
    int 0x80

    ; Exit
    mov eax, 1
    mov ebx, 0
    int 0x80

incorrect:
    mov eax, 4
    mov ebx, 1
    mov ecx, incorrect_message
    mov edx, incorrect_message_len
    int 0x80

    ; Exit
    mov eax, 1
    mov ebx, 0
    int 0x80

section .data
    correct_message db "Input Correct", 0
    correct_message_len equ $ - correct_message
    incorrect_message db "Input Incorrect", 0
    incorrect_message_len equ $ - incorrect_message
