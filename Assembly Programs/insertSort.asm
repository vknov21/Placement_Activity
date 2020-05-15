section .data
	msg1 db "Enter elements count : ",0
	inp0 db "%d",0
	msg2 db "Done!",10,0
section .bss
	arr resd 10
	len resd 1

section .text
	global main
	extern printf, scanf

main:
	push msg1
	call printf
	add esp, 4

	push len
	push inp0
	call scanf
	add esp, 8

	mov ecx, dword[len]
	mov eax, arr

.mrk1:
	pusha
	push eax
	push inp0
	call scanf
	add esp, 8
	popa

	add eax, 4
	loop .mrk1

	mov ecx, dword[len]
	mov eax, arr
	xor edi, edi
.mrk2:
	mov edx, edi
	inc edx
	mov ebx, eax
	add ebx, 4	
.mrk3:
	mov esi, eax
	mov eax, dword[eax]
	cmp eax, dword[ebx]
	jg .xchg
.cnt:
	inc edx
	cmp edx, dword[len]
	jl .mrk3
	add eax, 4
	inc edi
	loop .mrk2
	jmp .exi

.xchg:
	pusha
	mov eax, dword[esi]
	mov esi, dword[ebx]
	mov ebx, eax
	popa
	jmp .cnt

.exi:
	mov eax, arr
	mov ecx, dword[len]
	
.mrk4:
	pusha
	push dword[eax]
	push inp0
	call printf
	add esp, 8
	popa
	add eax, 4
	loop .mrk4
