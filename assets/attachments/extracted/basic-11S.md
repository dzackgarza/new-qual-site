## Basic Exam Spring 2011

IMPORTANT. Write your university identification number on the upper right corner of each sheet of paper you use. Do not write your name anywhere on the exam

Test Instructions: Do any 10 of the following 12 problems. If you attempt more than 10 problems, indicate which 10 you wish to be graded. If you do not indicate, the first ten attempted problems will be graded. Each question is equally valued (10 points). Credit is based on correct work shown which is used to solve the problem. No credit will be given for answers without detailed justification. Partial credit will be given but not for vague work. The exam lasts 4 hours.

Problem Scores (NG=not graded)

1. Problem 1

2. Problem 2

3. Problem 3

4. Problem 4

5. Problem 5

6. Problem 6

7. Problem 7

8. Problem 8

9. Problem 9

10. Problem 10

11. Problem 11

12. Problem 12 .

Total

Problem 1 Let A be a 3 by 3 matrix with complex entries. Consider the set of such A that satisfy $T r ( A ) = 4 , T r ( A ^ { 2 } ) = 6$ and $T r ( A ^ { 3 } ) = \mathbb { i } 0 .$ For each similarity (i.e. conjugacy ) class of such matrices, give one member in Jordan normal form. The following identity may be helpful:

If $b _ { 1 } = a _ { 1 } + a _ { 2 } + a _ { 3 } , \ b _ { 2 } = a _ { 1 } ^ { 2 } + a _ { 2 } ^ { 2 } + a _ { 3 } ^ { 2 } .$ and $b _ { 3 } = a _ { 1 } ^ { 3 } + a _ { 2 } ^ { 3 } + a _ { 3 } ^ { 3 }$ , then 6a1a2a3 = $b _ { 1 } ^ { 3 } + 2 b _ { 3 } - 3 b _ { 1 } b _ { 2 }$

Problem 2 Show that a positive power of an invertible matrix with complex entries is diagonalizable if the matrix itself is diagonalizable.

Problem 3 Show that for any Hermitian (i.e. self-adjoint ) operator H on a finite dimensional inner product space there exists a unitary operator U such that $U H U ^ { \ast }$ is diagonal. Here as usual $v ^ { * }$ is the adjoint. (You may use a basis if you need to!)

Problem 4 Let A be an n by n real matrix. Define an LU decomposition of A. State a necessary and sufficient condition on A for the existence of such a decomposition. Suppose we normalize the decomposition by requiring that the diagonal entries of L are 1. Show that in this case, if the LU decomposition exists, then it is unique. Give the LU decomposition of the matrix

$$
\left( \begin{array} { l l } { 4 } & { 3 } \\ { 6 } & { 3 } \end{array} \right) .
$$

Problem 5 Let A be an n by n matrix with real entries, and let b be an n by 1 column vector with real entries. Prove that there exists an n by 1 column vector solution x to the equation $A \mathbf { x } = \mathbf { b }$ if and only if b is in orthocomplement of the kernel of the transpose of A.

Problem 6 Let V and W be finite dimensional real inner product spaces, and let $A : V  W$ be a linear transformation. Let w be an element of W. Show that the elements $\upsilon \in V$ for which the norm $| | A v - w | |$ is minimal are exactly the solutions to the equations $A ^ { * } A x = A ^ { * } y$

Problem 7 Prove that there is a real number x such that

$$
x ^ { 5 } - 3 x + 1 = 0 .
$$

Problem 8 Give examples:

1. A function $f ( x )$ on $[ 0 , 1 ]$ which is not Riemann integrable, for which $\vert f ( x ) \vert$ is Riemann integrable.

2. Continuous functions $f _ { \pi }$ and f on $[ 0 , 1 ]$ such that $f _ { \mathcal { n } } ( t )  f ( t )$ for all $t \in [ 0 , 1 ]$ but $\textstyle \int _ { 0 } ^ { 1 } f _ { \mathcal { n } } ( t ) d t$ does not converge to $\int \limits _ { 0 } ^ { 1 } f ( t ) d t$

Problem 9 Prove that if $f ( x )$ is a continuous function on $[ a , b ]$ and $f ( x ) \geq 0 .$ then $\int _ { a } ^ { b } f ( x ) = 0$ implies that $f = 0$

Problem 10 Suppose that f is a function defined on an open subset G of $\mathbb { R } ^ { 2 }$ and that $\left( x _ { 0 } , y _ { 0 } \right) \in G$

1. Define what it means for $f$ to be differentiable at $( x _ { 0 } , y _ { 0 } )$

2. Show that if $\frac { \partial f } { \partial x }$ and $\frac { \partial f } { \partial y }$ exist and are continuous on an open set containing $( x _ { 0 } , y _ { 0 } )$ , then f is differentiable at $( x _ { 0 } , y _ { 0 } ) \in G .$

## Problem 11

1. Show that a connected subset $A \subseteq \mathbb { R }$ is arcwise connected.

2. Give an example of subset of $\mathbb { R } ^ { 2 }$ which is connected but not arcwise connected.

Problem 12 Given a metric space M, and a constant $0 < r < 1$ , a continuous function $T : \mathcal { M } \to \mathcal { M }$ is said to be an r-contraction if it is continuous map and $d ( T ( x ) , T ( y ) ) < r d ( x , y )$ for all x and y. A well-known fixed point theorem states that if M is complete and $T$ an r-contraction, then it must have a unique fixed point (don't prove this). This result is often used to prove the existence of solutions of differential equations with initial conditions.

1. Illustrate this technique for the (trivial) case

$$
f ^ { \prime } ( t ) = f ( t ) , f ( 0 ) = 1
$$

by letting M be the space of continuous functions $C ( [ 0 , c ] )$ for $0 < c <$ 1 with the uniform distance

$$
d ( f , g ) = \operatorname* { s u p } \left\{ | f ( t ) - g ( t ) | \right\} ,
$$

and defining $\begin{array} { r } { ( T f ) ( x ) = 1 + \int _ { 0 } ^ { x } f ( t ) d t } \end{array}$ Carefully explain your steps.

2. What approximations do you obtain from the sequence

$$
T ( 0 ) , T ^ { 2 } ( 0 ) , T ^ { 3 } ( 0 ) \ldots ?
$$