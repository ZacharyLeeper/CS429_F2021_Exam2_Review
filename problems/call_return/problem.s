# This was compiled with gcc -O1 -o problem.s -S problem.c
# Any unncessary lines of code were removed.
# Note here that .L9 is the case we jump to if the code replaced
# by COND is taken, otherwise there would be some ambiguity in
# the solution.

foo:
	movl	$0, %eax
	testq	%rdi, %rdi
	jle	.L6
	subq	$8, %rsp
	movslq	%esi, %rax
	cmpq	%rdi, %rax
	jl	.L9
	subq	$1, %rdi
	call	foo
	addl	$1, %eax
.L1:
	addq	$8, %rsp
	ret
.L9:
	subq	%rax, %rdi
	call	foo
	addl	$1, %eax
	jmp	.L1
.L6:
	ret