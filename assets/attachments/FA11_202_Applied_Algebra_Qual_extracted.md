# Applied Algebra Qualifying Exam: Part II September 6, 2011

Do as many problems as you can, but you must attempt at least 5 problems where two of the problems are from problems 1-5 and two of the problems are from problems 6-9. The point values are relative values for this part of the exam.
Your final score will be scaled so that this part of the exam will represent 60% of your point total.

Let $\mathbb { N } = \{ 0 , 1 , 2 , . . . \} , \mathbb { Z } = \{ 0 , \pm 1 , \pm 2 , . . . \}$ , Q equal the rationals and C denote the complex numbers.
Suppose that $\lambda = ( \lambda _ { 1 } \geq \lambda _ { 2 } \geq . . . \geq \lambda _ { k } )$ is a partition of n. Then $A ^ { \lambda }$ denotes the irreducible representation of the symmetric group $S _ { n }$ such that the Frobenius image of $\chi ^ { A ^ { \lambda } } = \chi ^ { \lambda }$ is the Schur function $S _ { \lambda } ( x _ { 1 } , \dots , x _ { N } )$ where $N > n$ and $S _ { \lambda _ { 1 } } \times \cdots \times S _ { \lambda _ { k } }$ denotes the Young subgroup of $S _ { n }$ corresponding to λ.

(1) (30 pts)

(a) Use the Murnaghnam-Nakayama rule to compute the character table of $S _ { 4 }$ .

(b) Express $\chi ^ { A ^ { ( 2 , 2 ) } \downarrow _ { S _ { 2 } \times S _ { 2 } } ^ { S _ { 4 } } }$ as a sum of irreducible characters of $S _ { 2 } \times S _ { 2 }$ . (Hint: First write out the character table for $S _ { 2 } \times S _ { 2 } . )$

(2) (40 pts) Let G be the group of order 21 defined by the relations

$$
a ^ { 7 } = b ^ { 3 } = 1 { \mathrm { ~ a n d ~ } } b ^ { - 1 } a b = a ^ { 2 } .
$$

(a) Verify that the conjugacy classes of G are

$$
C _ { 1 } = \{ 1 \}
$$

$$
C _ { 2 } = \dot { \{ a , a ^ { 2 } , a ^ { 4 } \} }
$$

$$
C _ { 3 } \{ a ^ { 3 } , a ^ { 5 } , a ^ { 6 } \}
$$

$$
C _ { 4 } = \{ a ^ { k } b : k = 0 , \ldots , 6 \}
$$

$$
C _ { 5 } \{ a ^ { k } b ^ { 2 } : k = 0 , \ldots , 6 \}
$$

(b) Show that $H = \{ a ^ { k } : k = 0 , \ldots , 6 \}$ is a normal subgroup of G for which $G / H$ is isomorphic to $Z _ { 3 }$ . Give the character character table for the lifting of the 3 linear characters of $G / H$ to G.

(c) Let $\chi$ be the linear character of H given by

$$
\chi ( a ^ { k } ) = \eta ^ { k } \mathrm { f o r } k = 0 , . . . 6
$$

where $\eta = e ^ { 2 \pi i / 7 }$ . Show that $\chi \uparrow _ { H } ^ { G }$ is an irreducible character of $G _ { \ l }$

(d) Use parts (b) and (c) to give a complete character table for G.

(3) (30 pts)

(a) Find the decomposition of $A ^ { ( 2 , 1 ^ { 2 } ) } \times A ^ { ( 2 , 2 ) } \uparrow _ { S _ { 4 } \times S _ { 4 } } ^ { S ^ { 8 } }$ as a sum of irreducible representations of $S _ { 8 }$

(b) Let T denote the trivial representation on the Young subgroup $S _ { 3 } \times S _ { 2 } \times S _ { 1 }$ of $S _ { 7 }$ and Alt denote the alternating representation on the Young subgroup $S _ { 3 } \times S _ { 2 } \times S _ { 1 }$ of $S _ { 7 }$ . Find the decompositon of

$$
T \uparrow _ { S _ { 3 } \times S _ { 2 } \times S _ { 1 } } ^ { S _ { 6 } } \mathrm { a n d } A l t \uparrow _ { S _ { 3 } \times S _ { 2 } \times S _ { 1 } } ^ { S _ { 6 } } .
$$

as a sum of irreducible representations of $S _ { 7 }$

(c) Find the decomposition of the Kronecker product $A ^ { ( 3 , 2 ) } \otimes A ^ { ( 3 , 2 ) }$ as a sum of irreducible representations of $S _ { 5 }$

(4) (30 pts) Let H be a subgroup of G and let $G = \tau _ { 1 } H + . . . + \tau _ { k } H$ be its coset decomposition.
Define a permutation representation L of G by

$$
\sigma \langle \tau _ { 1 } H , \ldots , \tau _ { k } H \rangle = \langle \sigma \tau _ { 1 } H , \ldots , \sigma \tau _ { k } H \rangle\tag{1}
$$

$$
= \langle \tau _ { 1 } H , \dots , \tau _ { k } H \rangle L ( \sigma )\tag{2}
$$

so that $L ( \sigma ) _ { i , j } = \chi ( \tau _ { i } H = \sigma \tau _ { j } H )$

(a) Prove that L is a representation.

(b) Consider the special case where $G = S _ { n }$ and $H = S _ { n - 1 } \times S _ { 1 } = \{ \sigma \in S _ { n } : \sigma ( n ) = n \}$

(i) Show that the coset decompostion of G relative to H is given by $G = H + ( 1 , n ) H + \ldots ( n - 1 , n ) H$ where (i, n) denotes the transposition which interchanges i and n.

(ii) Show that $\chi ^ { L } ( \sigma ) = f i x ( \sigma )$ where $f i x ( \sigma )$ denotes the number of fixed points of $\sigma .$

(c) In the special case where $G = S _ { 4 }$ and $H = S _ { 3 } \times S _ { 1 }$ , use part (b) to decompose L a sum of irreducible representations of $S _ { 4 }$

(5) (30 pts.)
Let G and H be finite groups and let $A : G \to G L _ { n } ( C )$ and $B :  G L _ { m } ( C )$ be representations of $G$ and H respectively.

a) Show that $A \times B : G \times H \to G L _ { n m } ( C )$ is representation where for $( \sigma , \tau ) \in G \times H$

$$
A \times B ( ( \sigma , \tau ) ) = A ( \sigma ) \otimes B ( \tau )
$$

and for matrices M and N , $M \otimes N$ is the Kronecker product of M and N .

b) Show that if A is an irreducible representation of G and B is an irreducible representation of H, then $A \times B$ is an irreducible representation of $G \times H$

c) Show that every irreducible representation of $G \times H$ is of the form $A \times B$ where A is an irreducible representation of G and B is an irreducible representation of H.

(6) (30 pts.)
Let $\langle A , + , \cdot \rangle$ be a commutative ring with identity 1 and let < be a linear order on A such that for all $a , b , x$ in A

(I) $a < b \Rightarrow a + x < b + x$ and

(II) $a < b , 0 < x \Rightarrow a \cdot x < b \cdot x .$

(a) Prove that $\langle A , + , \cdot \rangle$ is an integral domain.

(b) Let $A ^ { + } = \{ a \in A : 0 < a \}$ . Prove the following:

(i) $A ^ { + }$ is closed under multiplication and addition.

(ii) If $a \in A .$ , then exactly one of the following holds: $a \in A ^ { + } , - a \in A ^ { + } , a = 0$

(iii) $1 \in A ^ { + }$

(7) (40 pts.)
Consider the equations

$$
x ^ { 2 } + y = - 2
$$

$$
\begin{array} { l l l } { { 2 x y } } & { { = } } & { { y ^ { 2 } - 2 y } } \end{array}
$$

(a) Let I be the ideal of ${ \bf C } [ \boldsymbol { x } , \boldsymbol { y } ]$ generated by these equations.
Find the Groebner basis for I relative to lexicographic order where $x > y$

(b) Find a Groebner basis for $\mathbf { C } [ y ] \cap I$

(c) Find all solutions to these equations that lie $\mathbf { C } ^ { 2 }$

(d) Find a vector space basis for $\mathbf { C } [ x , y ] / I .$

(8) (40 pts.)
Let I and J be ideals in $k [ x _ { 1 } , \dots , x _ { n } ]$ where k is field.

(i) Prove $I \cap J = ( t I + ( 1 - 1 ) J ) \cap k [ x _ { 1 } , \dotsc , x _ { n } ] .$

(ii) Prove that $\mathbf { V } ( \mathbf { I } \cap \mathbf { J } ) = \mathbf { V } ( \mathbf { I } ) \cup \mathbf { V } ( \mathbf { J } )$ where for any set $X \subseteq k [ x _ { 1 } , \ldots , x _ { n } ] , \mathbf { V } ( X )$ is the affine variety defined by X.

(iii) Prove that $\sqrt { I \cap J } = \sqrt { I } \cap \sqrt { J } .$

(iv) Let $I = \langle x ^ { 3 } y \rangle$ and $J = \langle x y ^ { 3 } + x y \rangle$ be ideals in $k [ x , y ]$ . Find a Gr¨obner basis for $I \cap J$ relative to lexicographic order where x $> y .$

(9) (30 pts.)
Let k be a field.

(a) State Hilbert’s Nullstellensatz Theorem.

(b) Prove that if $I = \langle f _ { 1 } , \dots , f _ { s } \rangle \subseteq k [ x _ { 1 } , \dots , x _ { n } ]$ is an ideal, then $f \in \sqrt { I }$ if and only if $1 \in \langle f _ { 1 } , \ldots , f _ { s } , 1 -$ $y f \rangle \subseteq k [ x _ { 1 } , \dotsc , x _ { n } , y ]$

(c) Prove that if $f \in k [ x _ { 1 } , \ldots , x _ { n } ]$ and $J = \langle f \rangle$ is the principal ideal generated by $f ,$ then ${ \sqrt { J } } = \langle f _ { 1 } f _ { 2 } \cdot \cdot \cdot f _ { r } \rangle$ where $f = f _ { 1 } ^ { a _ { 1 } } f _ { 2 } ^ { a _ { 2 } } \cdot \cdot \cdot \stackrel { \textstyle - } { f _ { r } ^ { a _ { r } } }$ is the factorization of $f$ into a product of distinct irreducible polynomials in $k [ x _ { 1 } , \dots , x _ { n } ]$
