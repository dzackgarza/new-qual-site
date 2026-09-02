# Qual Problems #10

D. Zack Garza

December 3, 2019

## Contents

1 Problem 1 1\
1.1 Part 1 1\
1.2 Part 2 1\
1.3 Part 3 2\
2 Problem 2 2\
3 Problem 3 2\
3.1 Part 1 2

## 1 Problem 1

## 1.1 Part 1

Since 0 is an eigenvalue, there exists an eigenvector v such that $L \mathbf { v } = 0 \mathbf { v } = 0$ . But then $\mathbf { v } \in \ker ( L )$ so dim ker $( L ) \geq 1$ . Since ker $( L ) \neq 0 ,$ , L can not be injective.

By the rank-nullity theorem, we must also have 5 = dim ker(L)+dim im (L). But then dim im $( L ) \leq$ $\mathrm { 5 = d i m } \mathbb { R } ^ { \mathrm { 5 } }$ , so L can not be surjective either.

## 1.2 Part 2

Since all eigenvalues are roots of the minimal polynomial and complex roots occur in conjugate pairs, we must have

$$
\mathrm { S p e c } ( L ) = \{ 0 , 1 \pm i , 1 \pm 2 i \} .
$$

Moreover, since this is a $5 \times 5$ matrix and we have 5 eigenvalues, this is all of them, and we have the characteristic polynomial

$$
\chi _ { L } ( x ) = x ( x ^ { 2 } - 2 x + 2 ) ( x ^ { 2 } - 2 x + 5 ) \in \mathbb { R } [ x ]
$$

Since the minimal polynomial $p _ { L } ( x )$ must divide the characteristic polynomial and have every eigenvalue as a root, this forces

$$
p _ { L } ( x ) = \chi _ { L } ( x ) .
$$

## 1.3 Part 3

If $L \mathbf { x } = \mathbf { x }$ , then x is an eigenvector with eigenvalue $\lambda = 1$ . Since $1 \not \in \mathrm { S p e c } ( L )$ , such an x can not exist, so L has only one fixed point: namely $\mathbf { x } = \mathbf { 0 }$

## 2 Problem 2

Let M be an $n \times n$ matrix such that $M _ { i j } = 1$ for all $i , j ,$ and consider the possible eigenvectors of M .

We have

$$
M [ 1 , 1 , \cdot \cdot \cdot , 1 ] ^ { t } = [ n , n , \cdot \cdot \cdot , n ] ^ { t } = n [ 1 , 1 , \cdot \cdot \cdot , 1 ] ^ { t } ,
$$

which exhibits $\mathbf { x } = [ 1 , 1 , \cdots , 1 ]$ as an eigenvector with eigenvalue $\lambda = n$

Now consider

$$
\mathbf { x } _ { j } : = \mathbf { e } _ { 1 } - \mathbf { e } _ { j } = [ 1 , 0 , 0 , \cdots , 0 , - 1 , 0 , \cdots , 0 ]
$$

which has a 1 in the 1st coordinate and a −1 in the jth coordinate.

Then

$$
M \mathbf { x } _ { j } = \left[ { 1 + 0 + \cdots + 0 + ( - 1 ) + 0 + \cdots + 0 \atop 1 + 0 + \cdots + 0 + ( - 1 ) + 0 + \cdots + 0 } \right] = [ 0 , 0 , \cdots , 0 ] ^ { t } ,
$$

which exhibits each $\mathbf { x } _ { j }$ as an eigenvector with eigenvalue $\lambda = 0$

But the set $\left\{ \mathbf { x } _ { j } ~ \Big | ~ 2 \leq j \leq n \right\}$ with eigenvalue 0 contains n − 1 distinct eigenvectors, and we have an additional 1 eigenvector with eigenvalue 1, which yields n distinct eigenvectors.

So M is fact diagonalizable and given by

$$
J C F ( M ) = ( n - 1 ) J _ { 0 } ^ { 1 } \oplus J _ { n } ^ { 1 } = { \left[ \begin{array} { l l l l l } { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { n } \end{array} \right] }
$$

## 3 Problem 3

## 3.1 Part 1

Note that we can’t have $T ^ { j } = 0$ for any $j \le 4$ , since then $T ^ { 5 } = T ^ { 5 - k } T ^ { k } = T ^ { 5 - k } 0 = 0$ , contradicting $T ^ { 5 } \neq 0$

So in fact $p _ { T } ( x ) = x ^ { 6 }$ is the minimal polynomial of T , and since V is 6 dimensional, the degree of the characteristic polynomial $\chi _ { T } ( x )$ is 6. Since $p _ { T } \mid \chi _ { T }$ , and both are monic polynomials of degree 6, we in fact have

$$
p _ { T } ( x ) = \chi _ { T } ( x ) = x ^ { 6 } .
$$

But this means T has eigenvalue $\lambda = 0$ with multiplicity 6. This means

• The size of the largest Jordan block associated to $\lambda = 0$ is size 6, since 0 has multiplicity 6 in $p _ { T } .$ and

• The sum of the sizes of all Jordan blocks associated to $\lambda = 0$ is 6, since 0 has multiplicity 6 in $\chi _ { T }$

which forces $J C F ( T )$ to have a single Jordan block of size $6 ,$ i.e.

$$
J C F ( T ) = J _ { 0 } ^ { 6 } = { \left[ \begin{array} { l l l l l l } { 0 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] }
$$

## Part 2

By part (1), we know that these conditions uniquely specify their Jordan forms, so we have $M : =$ $J C F ( T ) = J C F ( S )$

Moreover, since $M = J C F ( T )$ , we know there is a matrix P such that $T = P M P ^ { - 1 }$

Similarly, we know there is a matrix Q such that $S = Q M Q ^ { - 1 }$

But then $P ^ { - 1 } T P = M$ , and so

$$
S = Q M Q ^ { - 1 } = Q ( P ^ { - 1 } T P ) Q ^ { - 1 } = ( Q P ^ { - 1 } ) T ( Q P ^ { - 1 } ) ^ { - 1 } : = A T A ^ { - 1 }
$$

where $A = Q P ^ { - 1 }$ is a product of invertible matrices and thus invertible.
