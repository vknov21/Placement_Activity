section .data
	msg1 db "Enter elements count : ",10,0
	msg2 db "Sorted elements are : ",0
	msg3 db "Enter %d elements - ",10,0
	inp0 db "%d",0
	inp1 db "%d ",0
	Ten db 10,0

section .bss
	len resd 1
	arr resd 10

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

	push dword[len]
	push msg3
	call printf
	add esp, 8

	mov eax, arr
	mov ecx, dword[len]
	
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

.mrk2:
	mov edx, 1
	mov eax, arr
.mrk3:
	mov ebx, eax
	add ebx, 4
	mov ebx, dword[ebx]
	cmp dword[eax], ebx
	jg .xchg

.cnt:
	add eax, 4
	inc edx
	cmp edx, dword[len]
	jl .mrk3
	loop .mrk2
	jmp .exi

.xchg:
	pusha
	mov ecx, dword[eax]
	add eax, 4
	mov eax, dword[eax]
	mov dword[arr+edx*4], ecx
	dec edx
	mov dword[arr+edx*4], eax
	popa
	jmp .cnt

.exi:
	push msg2
	call printf
	add esp, 4

	mov eax, arr
	xor edx, edx
	mov ecx, dword[len]

.mrk4:
	pusha
	push dword[eax+edx*4]
	push inp1
	call printf
	add esp, 8
	popa

	inc edx
	loop .mrk4

	mov eax, 4
	mov ebx, 1
	mov ecx, Ten
	mov edx, 1
	int 0x80
	
	mov eax, 4
	mov ebx, 1
	mov ecx, Ten
	mov edx, 1
	int 0x80

	ret
