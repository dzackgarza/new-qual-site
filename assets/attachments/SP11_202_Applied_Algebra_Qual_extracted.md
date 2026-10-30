# Applied Algebra Qualifying Exam: Part II May 27, 2011

Do as many problems as you can, but you must attempt at least 5 problems where 1 of the problems is from problems 1-3, one of the problems is from problems 4-7 and at least 2 of the problems are from problems 7-9. The point values are relative values for this part of the exam. Your final score will be scaled so that this part of the exam will represent 60% of your point total.

$\mathbb { N } = \{ 0 , 1 , 2 , . . . \} , \mathbb { Z } = \{ 0 , \pm 1 , \pm 2 , . . . \}$ , Q equal the rationals and C denote the complex numbers.

If $\lambda = ( \lambda _ { 1 } \geq \lambda _ { 2 } \geq . . . \geq \lambda _ { k } )$ is a partition of n, let $A ^ { \lambda }$ denote the irreducible representation of the symmetric group $S _ { n }$ such that the Frobenius image of $\chi ^ { A ^ { \lambda } } = \chi ^ { \lambda }$ is the Schur function $S _ { \lambda } ( x _ { 1 } , \dots , x _ { N } )$ where $N > n$

1) (30 pts) Let G be a finite group and $A : G \to G L ( n , \mathbb { C } )$ be a representation of G.

(a) Show that if the only matrices S which commute with $A ( g )$ for all $g \in G$ are of the form λI, then A is irreducible.

(b) Show that if G is abelian, then there is an invertible matrix T such that for all $g \in G , T A ( g ) T ^ { - 1 }$ is a diagonal matrix.

(c) Show that if $g \in G$ is in the center of G, then $A ( g ) = c I _ { n }$ for some nonzero constant $c \in \mathbb { C }$

2) (30 pts.) (d) Prove that if $\lambda ( x )$ is a linear character of a finite group G, then for any irreducible character χ of G, the function $\chi ^ { * }$ defined by $\chi ^ { * } ( \sigma ) = \lambda ( \sigma ) \chi ( \sigma )$ for all $\sigma \in G$ is also an irreducible character of G.

(b) Given a partition λ of n, let ℓ(λ) denote the number of parts of λ and λ′ denote its conjugate partition. Let $\chi _ { \mu } ^ { \lambda }$ denote the value of the character of the irreducible representation $A ^ { \lambda }$ of $S _ { n }$ at the conjugacy class indexed by the partition µ. Show that $\chi _ { \mu } ^ { \lambda ^ { \prime } } = ( - 1 ) ^ { n - \ell ( \mu ) } \chi _ { \mu } ^ { \lambda }$

3) (40 pts.) Let $G = \{ g _ { 1 } , . . . , g _ { k } \}$ be a finite group. Introduce variables $x _ { g _ { 1 } } , \ldots , x _ { g _ { k } }$ and consider the $k \times k$ matrix

$$
X = [ x _ { g _ { i } g _ { j } ^ { - 1 } } ] .
$$

Let $\begin{array} { r } { X = \sum _ { i = 1 } ^ { k } A ( g _ { i } ) x _ { g _ { i } } } \end{array}$ so that we can define a map $g _ { i }  A ( g _ { i } )$

(a) Show that A is the left regular representation of G.

(b) Show that $d e t ( X ) = \prod _ { \nu = 1 } ^ { h } d e t ( \sum _ { g \in G } A ^ { ( \nu ) } ( g ) x _ { g } ) ^ { n _ { \nu } }$ where $A ^ { ( 1 ) } , \ldots , A ^ { ( h ) }$ are a complete set of representa-

tives of the irreducible representations of G and $n _ { \nu } = d i m ( A ^ { ( \nu ) } )$ for $\nu = 1 , \ldots , h$

c) Use part (b) to show that

$$
d e t \left[ \begin{array} { c c c c c } { x _ { 0 } } & { x _ { 1 } } & { x _ { 2 } } & { \ldots } & { x _ { n - 1 } } \\ { x _ { n - 1 } } & { x _ { 0 } } & { x _ { 1 } } & { \ldots } & { x _ { n - 2 } } \\ { x _ { n - 2 } } & { x _ { n - 1 } } & { x _ { 0 } } & { \ldots } & { x _ { n - 3 } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots \vdots } & { \vdots } \\ { x _ { 1 } } & { x _ { 2 } } & { x _ { 3 } } & { \ldots } & { x _ { 0 } } \end{array} \right] = \prod _ { r = 0 } ^ { n - 1 } ( x _ { 0 } + \epsilon ^ { r } x _ { 1 } + \epsilon ^ { 2 r } x _ { 2 } + \ldots \epsilon ^ { ( n - 1 ) r } x _ { n - 1 } )
$$

where $\epsilon = e ^ { 2 \pi i / n }$

4) (40 pts.)

(a) Use the Murnaghan-Nakayama rule to compute the value of the irreducible characters of $S _ { 5 }$ at the conjugacy class indexed by the partition (2, 3).

(b) Find the character table for $S _ { 3 } \times S _ { 2 }$ where $S _ { 3 } \times S _ { 2 }$ is the Young subgroup of $S _ { 5 }$ consisting of all permuations $\sigma \in S _ { 5 }$ such that

$$
\sigma ( 1 ) , \sigma ( 2 ) , \sigma ( 3 ) \in \{ 1 , 2 , 3 \} , \sigma ( 4 ) , \sigma ( 5 ) \in \{ 4 , 5 \} .
$$

(c) Find the values of the character of $A ^ { ( 1 , 4 ) }$ on the conjugacy classes of $S _ { 5 }$ .

(d) Decompose $A ^ { ( 1 , 4 ) } \downarrow _ { S _ { 3 } \times S _ { 2 } } ^ { S _ { 5 } }$ as a sum of irreducible representations of $S _ { 3 } \times S _ { 2 }$

5) (40 pts.)

(a) Let $A ^ { ( 1 , 1 , 2 ) } \times A ^ { ( 1 , 2 ) }$ denote the representation of $S _ { 4 } \times S _ { 3 }$ such that for all $( \sigma , \tau ) \in S _ { 4 } \times S _ { 3 }$

$$
A ^ { ( 1 , 1 , 2 ) } \times A ^ { ( 1 , 2 ) } ( \sigma , \tau ) = A ^ { ( 1 , 1 , 2 ) } ( \sigma ) \otimes A ^ { ( 1 , 2 ) } ( \tau )
$$

where for any matrices A and $B , \ A \otimes B$ denotes the tensor product of A and B. Decompose $A ^ { ( 1 , 1 , 2 ) } \times$ $A ^ { ( 1 , 2 ) } \uparrow _ { S _ { 4 } \times S _ { 3 } } ^ { S _ { 8 } }$ as a sum of irreducible representations of $S _ { 7 }$

(b) Show that $\{ A ^ { \lambda } \times A ^ { \mu } : \lambda \vdash 4$ and $\mu \vdash 3 \}$ is a complete set of representatives of the irreducible representations of $S _ { 4 } \times S _ { 4 }$ where $A ^ { \lambda } \times A ^ { \mu } ( \sigma , \tau ) \stackrel { . } { = } A ^ { \lambda } ( \sigma ) \otimes A ^ { \mu } ( \tau )$

Note: For parts (a) and (b) above, regard $S _ { 4 } \times S _ { 3 }$ as a subgroup of $S _ { 7 }$ by letting

$$
S _ { 4 } \times S _ { 4 } = \{ \sigma \in S _ { 7 } : \sigma ( 1 ) , \sigma ( 2 ) , \sigma ( 3 ) , \sigma ( 4 ) \in \{ 1 , 2 , 3 , 4 \} , \sigma ( 5 ) , \sigma ( 6 ) , \sigma ( 7 ) \in \{ 5 , 6 , 7 \} \} .
$$

(c) Let T denote the trivial representation. Decompose $T \uparrow _ { S _ { 1 } \times S _ { 3 } \times S _ { 3 } } ^ { S _ { 7 } }$ as a sum of irreducible representations of $S _ { 7 }$ where $S _ { 1 } \times S _ { 3 } \times S _ { 3 }$ is the Young subgroup of $S _ { 7 }$ consisting of all permutations $\sigma \in S _ { 7 }$ such that

$$
\sigma ( 1 ) = 1 , \sigma ( 2 ) , \sigma ( 3 ) , \sigma ( 4 ) \in \{ 2 , 3 , 4 \} , \sigma ( 5 ) , \sigma ( 6 ) , \sigma ( 7 ) \in \{ 5 , 6 , 7 \} .
$$

(d) Decompose $A ^ { ( 2 , 2 ) } \otimes A ^ { ( 2 , 2 ) }$ as a sum of irreducible representations of $S _ { 4 }$ where ⊗ represents the Kronecker product of the representations.

6) (40 pts.) Let $S _ { 4 }$ denote the symmetric group on 4 elements and $A _ { 4 }$ denote the alternating group, i.e. $A _ { 4 } = \{ \sigma \in S _ { 4 } : s i g n ( \sigma ) = 1 \}$

(a) Find the conjugacy classes of $A _ { 4 }$

(b) Let $D = \{ \epsilon , ( 1 , 2 ) ( 3 , 4 ) , ( 1 , 3 ) ( 2 , 4 ) , ( 1 , 4 ) ( 2 , 3 ) \}$ . Show that D is a normal subgroup of $A _ { 4 }$ and that $A _ { 4 } / D$ is isomorphic to $Z _ { 3 }$

(c) Give the character table for $Z _ { 3 }$

(d) Find the lifting of the irreducible characters of $Z _ { 3 }$ to $A _ { 4 }$

(e) Use (d) to complete the character table of $A _ { 4 }$

(7) (30 pts.)

(a) Two ideals I and J in $\mathbb { C } [ x _ { 1 } , \dots , x _ { n } ]$ are co-maximal if and only if $I + J = \mathbb { C } [ x _ { 1 } , \ldots , x _ { n } ]$

(i) Prove that I and J are co-maximal if and only if $V ( I ) \cap V ( J ) = \emptyset$

(ii) Show that if I and J are comaximal, then $I J = I \cap J$

(b) Suppose that I and J are ideals in $k [ x _ { 1 } , \dots , x _ { n } ]$ where k is field. Show that if $I \subseteq { \sqrt { J } }$ , then there is an $m \geq 1$ such that $I ^ { m } \subseteq J$ . (Hint: Use the Hilbert Basis Theorem.)

(8) (40 pts.)

Consider the equations

$$
x y + x ^ { 2 } = 1
$$

$$
y ^ { 2 } - 2 x ^ { 2 } = - 2
$$

(a) Let I be the ideal of $\mathbb { C } [ x , y ]$ generated by these equations. Find the Groebner basis for I relative to lexicographic order where $y > x$

(b) Find a Groebner basis for $\mathbb { C } [ x ] \cap I$

(c) Find all solutions to these equations that lie $\mathbb { C } ^ { 2 }$

(d) Find a vector space basis for $\mathbb { C } [ x , y ] / I$

(9) (40 pts.)

(a) Show that if I is an ideal in $\mathbb { C } [ x _ { 1 } , \dots , x _ { n } ]$ and $V ( I )$ is finite, then $\mathbb { C } [ x _ { 1 } , \ldots , x _ { n } ] / I$ is finite dimensional when considered as a vector space of C.

(b) Find a reduced Groebner basis for $I = \langle x ^ { 2 } + x y + y , x y + y ^ { 2 } \rangle$ with respect to the graded lexicographic order where $x > y$

(c) Show that $x ^ { 2 } + y ^ { 2 } \in { \sqrt { I } } - I$