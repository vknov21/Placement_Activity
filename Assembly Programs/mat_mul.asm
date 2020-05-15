section .data
	msg0 db "Enter row and column count : ",10,0
	msg1 db "Enter value (%d, %d) : ",0
	inp0 db "%d",0
	inp1 db "%d ",0

section .bss
	col resd 1
	row resd 1
	mat0 resd 100
	mat1 resd 100
	mat2 resd 100
	val0 resd 1
	val1 resd 1
	tmp0 resd 1

section .text
	global main
	extern printf, scanf

main:	push msg0
	call printf
	add esp, 4

	push col
	push inp0
	call scanf
	push row
	push inp0
	call scanf
	add esp, 16

	mov eax, mat0

	mov ecx, dword[row]

.mrk0:	mov ebx, dword[col]
.mrk1:	pusha
	push eax
	push inp0
	call scanf
	add esp, 8
	popa
	add eax, 4
	dec ebx
	cmp ebx, 0
	jg .mrk1
	loop .mrk0

	mov eax, mat0
	mov ecx, dword[col]
	
.mrk2:	mov ebx, dword[row]
.mrk3:	pusha
	push eax
	push inp0
	call scanf
	add esp, 8
	popa
	add eax, 4
	dec ebx
	cmp ebx, 0
	jg .mrk1
	loop .mrk0

	mov eax, 0
	mov ebx, 0

.mrk4:	mov ecx, val0
	mov dword[val0], dword[mat0+eax]
	mov dword[val1], dword[mat0+eax]
	mov ecx, dword[val1]
	mul dword[val0], ecx
.mrk5:	pusha
	push eax
	push inp0
	call scanf
	add esp, 8
	popa
	add eax, 4
	dec ebx
	cmp ebx, 0
	jg .mrk1
	loop .mrk0


