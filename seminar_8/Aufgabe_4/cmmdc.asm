global main
section .bss
    num1 resb 2 ; Rezerva 2 bytes pentru a stoca primul numar de la tastatura
    num2 resb 2 ; Rezerva 2 bytes pentru a stoca al doilea numar de la tastatura
    result resd 1 ; Rezultatul in format intreg
section .data
section .text

main:
    call read_number  ; Citeste primul numar de la tastatura
    mov r10, rax       ; Salveaza primul numar in r10

    call read_number  ; Citeste al doilea numar de la tastatura
    mov r11, rax       ; Salveaza al doilea numar in r11

    call calculate_gcd  ; Calculeaza CMMDc

    call display_result  ; Afiseaza rezultatul

    ; Terminarea programului
    mov rax, 60         ; syscall number pentru sys_exit
    xor rdi, rdi        ; cod de ieșire 0
    syscall

read_number:
    ; Citire număr de la tastatură
	mov rax, 0          ; syscall number pentru sys_read
    mov rdi, 0
    mov rsi, num1       ; adresa unde să fie stocat numărul citit
    mov rdx, 2
    syscall

    ; Convertirea cifrelor din ASCII în întreg
    movzx rax, byte [num1]   ; Încarcă cifra zecilor în rax
    sub rax, '0'            ; Convertire la format întreg
    ret

calculate_gcd:
    ; Calculul CMMDc folosind algoritmul Euclid
    cmp r10, r11
    je  exit_euclid
    jl  swap_values ; Dacă r10 < r11, interschimbă valorile
    sub r10, r11
	jmp euclid

exit_euclid:
    ret

swap_values:
    xchg r10, r11
    jmp euclid

euclid:
    cmp r10, r11
    je  exit_euclid
    jl  swap_values ; Dacă r10 < r11, interschimbă valorile
    sub r10, r11
    jmp euclid

display_result:
    ; Convertirea rezultatului la format ASCII și afișarea pe ecran
    add r11, '0'        ; Convertire la format ASCII
    mov [result], r11  ; Salvare rezultat în variabila result

    ; Afișarea rezultatului
    mov rax, 1          ; syscall number pentru sys_write
    mov rdi, 1
    mov rsi, result     ; adresa unde este stocat rezultatul
    mov rdx, 1
	syscall
    ret
	