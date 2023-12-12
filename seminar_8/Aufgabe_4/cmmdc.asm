section .bss
    num resb 2 ; Rezerva 2 bytes pentru a stoca numarul de la tastatura
    result resd 1 ; Rezultatul in format intreg


section .data

section .text
    global main

main:
    ; Citire număr de la tastatură
    mov rax, 0          ; syscall number pentru sys_read
    mov rdi, 0          ; file descriptor pentru stdin
    mov rsi, num        ; adresa unde să fie stocat numărul citit
    mov rdx, 2          ; lungimea maximă a buffer-ului (2 bytes)
    syscall

    ; Convertirea cifrelor din ASCII în întreg
    movzx rax, byte [num]   ; Încarcă cifra zecilor în rax
    sub rax, '0'            ; Convertire la format întreg
    movzx rbx, byte [num + 1] ; Încarcă cifra unităților în rbx
    sub rbx, '0'            ; Convertire la format întreg

    ; Inițializare registre
    mov r10, rax    ; r10 = cifra zecilor în format întreg
    mov r11, rbx    ; r11 = cifra unităților în format întreg

    ; Calculul CMMDc folosind algoritmul Euclid
    cmp r10, r11
    je  exit_euclid
    jl  swap_values ; Dacă r10 < r11, interschimbă valorile
    sub r10, r11
    jmp euclid

swap_values:
    xchg r10, r11
    jmp euclid

euclid:
    cmp r10, r11
    je  exit_euclid
    jl  swap_values ; Dacă r10 < r11, interschimbă valorile
    sub r10, r11
    jmp euclid

exit_euclid:
    ; Convertirea rezultatului la format ASCII și afișarea pe ecran
    add r11, '0'        ; Convertire la format ASCII
    mov [result], r11  ; Salvare rezultat în variabila result
	 ; Afișarea rezultatului
    mov rax, 1          ; syscall number pentru sys_write
    mov rdi, 1          ; file descriptor pentru stdout
    mov rsi, result     ; adresa unde este stocat rezultatul
    mov rdx, 1          ; lungimea buffer-ului
    syscall

    ; Terminarea programului
    mov rax, 60         ; syscall number pentru sys_exit
    xor rdi, rdi        ; cod de ieșire 0
    syscall