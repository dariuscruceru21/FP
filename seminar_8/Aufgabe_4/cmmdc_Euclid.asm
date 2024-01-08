section .data
    num1 dd 36         ; Primul număr
    num2 dd 48         ; Al doilea număr

section .bss
    result resd 1      ; Rezultatul în format intreg

section .text
    global main

main:
    ; Calculul CMMDc folosind algoritmul Euclid
    mov eax, [num1]    ; Se încarcă primul număr în registrul eax
    mov ebx, [num2]    ; Se încarcă al doilea număr în registrul ebx
    call euclid        ; Se apelează funcția euclid

    ; Afișarea rezultatului
    mov rax, 1          ; syscall number pentru sys_write
    mov rdi, 1
    mov rsi, result     ; adresa unde este stocat rezultatul
    mov rdx, 4          ; lungimea rezultatului în bytes
    syscall

    ; Terminarea programului
    mov rax, 60         ; syscall number pentru sys_exit
    xor rdi, rdi        ; cod de ieșire 0
    syscall

; Funcție pentru algoritmul Euclid
euclid:
    cmp ebx, 0          ; Verifică dacă al doilea număr (ebx) este zero
    je  euclid_done      ; Dacă da, saltă la eticheta euclid_done
    xchg eax, ebx       ; Schimbă valorile dintre eax și ebx
    idiv ebx            ; Efectuează împărțirea eax la ebx
    jmp euclid          ; Saltă la începutul funcției euclid pentru a continua calculul

euclid_done:
    mov [result], eax   ; Stochează rezultatul (CMMDc) în memoria rezultat
    ret                 ; Returnează controlul la apelant (main)
