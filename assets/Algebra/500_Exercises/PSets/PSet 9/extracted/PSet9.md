## Problem Set 9

D. Zack Garza

November 26, 2019

## Contents

1 Problem 1 1\
1.1 Part 1 1\
1.2 Part 2 3\
2 Problem 2 3\
2.1 Part 1 3\
2.2 Part 2 . 3\
3 Problem 3 4\
4 Problem 4 4\
5 Problem 5 6\
5.1 Part 1 6\
5.2 Part 2 7\
5.3 Part 3 7\
5.4 Part 4 8\
6 Problem 6 8\
Note: I use the convention that a denotes a column vector and $\mathbf { a } ^ { t }$ a row vector, and if A is a\
matrix, then $( A ) _ { i j } = a _ { i j }$ denotes the entry in the ith row and jth column.

## 1 Problem 1

## 1.1 Part 1

Let $A = \left( a _ { i j } \right)$ and consider $\epsilon _ { i j }$ , the matrix with a 1 in the ith row and jth column and zeros elsewhere.

Then, for a fixed $( i , j )$ , if we write $A = [ \mathbf { a } _ { 1 } ^ { t } , \mathbf { a } _ { 2 } ^ { t } , \cdot \cdot \cdot , \mathbf { a } _ { n } ^ { t } ]$ as a block matrix of column vectors, we have

$$
A \mathbf { e } _ { i j } = [ 0 , 0 , \cdots , \mathbf { a } _ { i } ^ { t } , 0 , \cdots , 0 ]
$$

as a block matrix where $\mathbf { a } _ { i } ^ { t }$ occurs as the jth column.

In other words, right-multiplication by ${ \bf e } _ { i j }$ selects column i from A, placing it in column j of a matrix of zeros.

For example, for $( i , j ) = ( 3 , 2 )$ we have

$$
A \mathbf { e } _ { 3 2 } = { \binom { a _ { 1 1 } } { a _ { 2 1 } } } \quad a _ { 1 2 } \quad a _ { 1 3 }  \\ { a _ { 2 2 } \quad a _ { 2 2 } \quad a _ { 2 3 } } \\ { a _ { 2 1 } \quad a _ { 2 2 } \quad a _ { 3 3 } { \left( \begin{array} { l l l } { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \end{array} \right) } = { \left( \begin{array} { l l l } { 0 } & { a _ { 1 3 } } & { 0 } \\ { 0 } & { a _ { 2 3 } } & { 0 } \\ { 0 } & { a _ { 3 3 } } & { 0 } \end{array} \right) } , }
$$

which is a matrix that contains column 3 of A (the i value) as its 2nd column (the j value).

On the other hand, left multiplication by ${ \bf e } _ { i j }$ selects the jth row of A and places it the ith row of a zero matrix, so for example we have

$$
\mathbf { e } _ { 3 2 } A = { \left( \begin{array} { l l l } { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \end{array} \right) } { \left( \begin{array} { l l l } { a _ { 1 1 } } & { a _ { 1 2 } } & { a _ { 1 3 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 3 3 } } \end{array} \right) } = { \left( \begin{array} { l l l } { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \\ { a _ { 2 1 } } & { a _ { 2 2 } } & { a _ { 2 3 } } \end{array} \right) }
$$

In general, these two products will not be equal, since the first has a nontrivial column and the latter has a nontrivial row.
If $A \in Z ( M _ { n } ( R ) )$ , these two must be equal, so we can equate corresponding entries to find that

$a _ { 2 1 } = 0$ , from comparing entries in row 3, column 1,

$a _ { 2 3 } = 0$ , from comparing entries in row 3, column 3

$a _ { 2 2 } = a _ { 3 3 }$ by comparing entries in row 3, column 2.

Letting the multiplication run over all possibilities for ${ \bf e } _ { i j }$ yields $a _ { i i } = a _ { j j }$ for every pair $i , j$ and $a _ { i j } = 0$ whenever $i \neq j$ . Setting $r = a _ { i i } = a _ { j j }$ for all $1 \leq i , j \leq n$ forces A to be a matrix of the form

$$
A = { \left( \begin{array} { l l l l l } { r } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { r } & { 0 } & { \cdots } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { r } \end{array} \right) } : = r I _ { n } .
$$

To see that we must have $r \in Z ( R )$ , let $s I _ { n } \in Z ( M _ { n } ( R ) )$ be arbitrary, where s is not assumed to be in $Z ( R )$ . Then $( r I _ { n } ) ( s I _ { n } ) = ( s I _ { n } ) ( r I _ { n } )$ by assumption, since these are matrices in the center of $M _ { n } ( R )$ . But $M _ { n } ( R )$ is an R-module, and so the scalars $^ { r , }$ s commute with the module elements $I _ { n }$ This means that we in fact have

$$
\begin{array} { r l } & { ( r I _ { n } ) ( s I _ { n } ) = ( r s ) I _ { n } ^ { 2 } = ( r s ) I _ { n } , } \\ & { ( s I _ { n } ) ( r I _ { n } ) = ( s r ) I _ { n } ^ { 2 } = ( s r ) I _ { n } } \\ & { \qquad \implies ( r s ) I _ { n } = ( s r ) I _ { n } } \\ & { \qquad \implies ( r s - s r ) I _ { n } = 0 _ { n } , } \end{array}
$$

the $n \times n$ zero matrix.

But then by equating (for example) the 1, 1 entry of the matrix $( r s - s r ) I _ { n }$ with the corresponding entry in $0 _ { n }$ , we find $r s - s r = 0 _ { R }$ , which means $r s = s r \in R$

Now since $s \in R$ was arbitrary, we find that $r \in Z ( R )$ as desired.

## 1.2 Part 2

Define a map

$$
\begin{array} { c } { { \phi : Z ( R )  Z ( M _ { n } ( R ) } } \\ { { r \mapsto r I _ { n } . } } \end{array}
$$

By part 1, this map is surjective.
To see that it is also injective, we can consider ker $\phi \ =$ $\{ r \in Z ( r ) \ \geqslant \ r I _ { n } = 0 _ { n } \}$ , which clearly forces $r \ = \ 0 _ { R }$ . It is also a homomorphism of R-modules, since $\phi ( r x + y ) = ( r x + y ) I _ { n } = r ( x I _ { n } ) + y I _ { n }$

Thus by the first isomorphism theorem, we have $Z ( R ) \cong Z ( M _ { n } ( R ) )$

## 2 Problem 2

## 2.1 Part 1

If A, B are (skew)-symmetric, then $A ^ { t } = \pm A$ and $B ^ { t } = \pm B$ respectively.
But then

$$
( A + B ) ^ { t } = A ^ { t } + B ^ { t } = \pm A + \pm B = \pm ( A + B ) ,
$$

which shows that $A + B$ is (skew)-symmetric.

## 2.2 Part 2

=⇒ : Suppose that whenever A, B are symmetric then AB is symmetric as well.

We then have $( A B ) ^ { t } = A B$ by assumption, and then by calculation we have $( A B ^ { t } ) = B ^ { t } A ^ { t } = B A$ so $A B = B A$

⇐= : Suppose that $A B = B A$ and A, B are symmetric.
We want to show that AB is also symmetric, so we compute

$$
( A B ) ^ { t } = B ^ { t } A ^ { t } = B A = B A .
$$

Now let $B \in M _ { n } ( R )$ be arbitrary.
We have

$( B B ^ { t } ) ^ { t } = ( B ^ { t } ) ^ { t } B ^ { t } = B B ^ { t }$ , so $B B ^ { t }$ is symmetric,

$( B + B ^ { t } ) ^ { t } = B ^ { t } + ( B ^ { t } ) ^ { t } = B ^ { t } + B = B + B ^ { t } ,$ so $B + B ^ { t }$ is symmetric,

$( B - B ^ { t } ) ^ { t } = B ^ { t } - B = - ( B + B ^ { t } )$ t), so $B - B ^ { t }$ is skew-symmetric

## 3 Problem 3

Definition: We say $A \sim B$ in $M _ { n } ( R )$ ⇐⇒ there exists an invertible P such that $B = P A P ^ { - 1 }$

• Reflexive, $A \sim A \cdot$

Take $P = I _ { n }$ the identity matrix.

• Symmetric, $A \sim B \implies B \sim A$

$B = P A P ^ { - 1 } \implies B P = P A \implies P ^ { - 1 } B P = A$ , so we can take $Q \ = \ P ^ { - 1 }$ to yield $A = Q B Q ^ { - 1 }$

$\mathrm { T r a n s i t i v e , } ~ A \sim B \& B \sim C \implies A \sim C ;$

If $B = P A P ^ { - 1 } , C = Q B Q ^ { - 1 }$ , then $C = Q ( P A P ^ { - 1 } ) Q ^ { - 1 } = ( Q P ) A ( Q P ) ^ { - 1 }$ , so take $L = Q P$ to yield $C = L A L ^ { - 1 }$

Definition: We say $A \sim B$ in $M ( n \times n , R ) \longleftrightarrow B = P A Q$ with $P \in \mathrm { G L } ( n , R ) , Q \in \mathrm { G L } ( m , R )$

• Reflexive, $A \sim A \cdot$

Take $P = I _ { m , n }$ the matrix with 1s on the diagonal and zeros elsewhere, and $Q = P ^ { t }$

• Symmetric, A ∼ B =⇒ B ∼ A:

$B = P A Q \implies B Q ^ { - 1 } = P A \implies P ^ { - 1 } B Q ^ { - 1 } = A$ , so we can take $S = P ^ { - 1 } , T = Q ^ { - 1 }$ to yield $A = Q B T$

• Transitive, $A \sim B \& B \sim C \implies A \sim C \mathrm { : }$

If $B = P A Q , C = R B S$ , then $C = R ( P A Q ) S = ( R P ) A ( Q S )$ , so take ${ \cal L } = { \cal R } { \cal P } , { \cal M } = { \cal Q } { \cal S }$ to yield $C = L A M$

## 4 Problem 4

Lemma: The rank-nullity theorem holds over division rings.

Proof: A linear map $\phi : D ^ { m } \to D ^ { n }$ induces a short exact sequence:

$$
0 \to \ker \phi \to D ^ { m } \overset { \phi } { \to } \operatorname { i m } \phi \to 0
$$

But every module over a division ring is free; in particular, im $\phi \le D ^ { n }$ is a module over D and is thus free.
So by a lemma in class, since the right-most term is a free module, this sequence splits and we have

$$
D ^ { m } \cong \ker \phi \oplus \operatorname { i m } \phi
$$

and taking dimensions yields

$$
m = \dim \ker ( \phi ) + \operatorname { r a n k } ( \phi ) .
$$

−

1. $A \in M ( n \times m , D )$ has a left inverse $B \iff \operatorname { r a n k } ( A ) = m !$

=⇒ : Suppose toward the contrapositive that ran $\mathfrak { c } ( A ) < m$ , so A has at least one pair of linearly dependent columns.
So wlog write

$$
A = [ \mathbf { a } _ { 1 } ^ { t } , \mathbf { a } _ { 2 } ^ { t } , \cdot \cdot \cdot , \mathbf { a } _ { m } ^ { t } ]
$$

$$
{ \bf a } _ { i }
$$

$$
\mathbf { a } _ { 1 } , \mathbf { a } _ { 2 }
$$

Now suppose such a left inverse B were to exist.
Write it in block form as

$$
B = [ { \bf b } _ { 1 } , { \bf b } _ { 2 } , \cdot \cdot \cdot , { \bf b } _ { n } ] ^ { t } ,
$$

so each $\mathbf { b } _ { i }$ is a row of B.

Now if $B A = I _ { m }$ is to hold, noting that $( B A ) _ { i j } = \langle \mathbf { b } _ { i } , \ \mathbf { a } _ { j } \rangle$ , we must have

$$
\begin{array} { r l } & { I _ { 1 , 1 } = \langle \mathbf { b } _ { 1 } , \mathbf { a } _ { 1 } \rangle = 1 } \\ & { I _ { 1 , 2 } = \langle \mathbf { b } _ { 1 } , \mathbf { a } _ { 2 } \rangle = 0 } \\ & { I _ { 1 , 3 } = \langle \mathbf { b } _ { 1 } , \mathbf { a } _ { 3 } \rangle = 0 } \\ & { \quad \vdots } \\ & { I _ { 2 , 1 } = \langle \mathbf { b } _ { 2 } , \mathbf { a } _ { 1 } \rangle = 0 } \\ & { I _ { 2 , 2 } = \langle \mathbf { b } _ { 2 } , \mathbf { a } _ { 2 } \rangle = 1 } \\ & { I _ { 2 , 3 } = \langle \mathbf { b } _ { 2 } , \mathbf { a } _ { 3 } \rangle = 0 } \\ & { \quad \vdots } \end{array}
$$

But the claim is that this can not happen if $\mathbf { a } _ { 1 } , \mathbf { a } _ { 2 }$ are linearly dependent.
To see why, note that the linear dependence supplies elements $d _ { 1 } , d _ { 2 } \ne 0 \in D$ such that $d _ { 1 } \mathbf { a } _ { 1 } + d _ { 2 } \mathbf { a } _ { 2 } = \mathbf { 0 }$ . But then taking inner products against, e.g. b1 (that is, applying $\langle \mathbf { b } _ { 1 } , \mathbf { \alpha } \cdot \mathbf { \alpha } \rangle$ to everything in sight), we obtain

$$
\begin{array} { r l r } & { } & { d _ { 1 } \mathbf { a } _ { 1 } + d _ { 2 } \mathbf { a } _ { 2 } = \mathbf { 0 } } \\ & { \implies } & { \langle \mathbf { b } _ { 1 } , ~ d _ { 1 } \mathbf { a } _ { 1 } \rangle + \langle \mathbf { b } _ { 1 } , ~ d _ { 2 } \mathbf { a } _ { 2 } \rangle = \langle \mathbf { b } _ { 1 } , ~ \mathbf { 0 } \rangle = 0 } \\ & { \implies d _ { 1 } \langle \mathbf { b } _ { 1 } , ~ \mathbf { a } _ { 1 } \rangle + d _ { 2 } \langle \mathbf { b } _ { 1 } , ~ \mathbf { a } _ { 2 } \rangle = \langle \mathbf { b } _ { 1 } , ~ \mathbf { 0 } \rangle = 0 } \\ & { } & { \implies d _ { 1 } \langle \mathbf { b } _ { 1 } , ~ \mathbf { a } _ { 1 } \rangle + d _ { 2 } \langle \mathbf { b } _ { 1 } , ~ \mathbf { a } _ { 2 } \rangle = 0 } \\ & { } & { \implies d _ { 1 } + d _ { 2 } \langle \mathbf { b } _ { 1 } , ~ \mathbf { a } _ { 2 } \rangle = 0 } \\ & { } & { \implies \langle \mathbf { b } _ { 1 } , ~ \mathbf { a } _ { 2 } \rangle = - \frac { d _ { 1 } } { d _ { 2 } } \neq 0 , } \end{array}
$$

which contradicts $\langle { \bf b } _ { 1 } , ~ { \bf a } _ { 2 } \rangle = 0$ as required by the previous equations.

⇐= : Suppose rank(A) = m, so A has m linearly independent columns – note that this is all of its columns.

Note: since row rank equals column rank, this also says that A has m linearly independent rows, so $n \geq m$

Viewing A as a representative of a map $\phi : D ^ { m } \to D ^ { n }$ , we find that dim im $\phi \ : = \ : m \ : \leq \ : n$ . In particular, from the rank nullity theorem, we have

$$
m = \dim \ker \phi + \operatorname { r a n k } ( \phi ) = \dim \ker \phi + m \implies \dim \ker \phi = 0 .
$$

So ker $A = \{ \mathbf { 0 } \}$ , and A represents an injective map $f _ { A } : D ^ { m } \to D ^ { n }$

But any injective set map $f : S _ { 1 }  S _ { 2 }$ has a left-inverse g such that $g \circ f = \operatorname { i d } _ { S _ { 1 } }$ . So $f _ { A } : D ^ { m } \to D ^ { n }$ as a set map has a left inverse $g _ { B } : D ^ { n }  D ^ { m }$ satisfying $g _ { B } \circ f _ { A } = \mathrm { i d } _ { D ^ { m } }$ . But then taking the matrix associated to gB yields a matrix $B \in M ( m \times n , D )$ such that $B A = I _ { m }$ as desired.

2. A has a right inverse $B \iff \operatorname { r a n k } ( A ) = n \colon$

=⇒ : By a similar argument, supposing that rank $A < n$ but $A B = I _ { n }$ for some B, we find that A has at least two linearly dependent rows this time, say $\mathbf { a } _ { 1 } , \mathbf { a } _ { 2 }$ , whereas we obtain a system of equations of the form $\langle a _ { i } , \ \mathbf { b } _ { k } \rangle = \delta _ { i k }$ where bi are now the columns of B.

In a similar manner, the linear dependence forces, say, $\left. \mathbf { a } _ { 2 } , ~ \mathbf { b } _ { 1 } \right. \neq 0$ , which is a contradiction.

⇐= : By another similar argument, we find that A represents a map $f _ { A } : D ^ { m } \to D ^ { n }$ , and since rank A = dim im $A = n$ , we find that A represents a surjective map $f _ { A }$ . Surjective set maps have $r i g h t$ inverses, so there is some $g _ { B } : D ^ { n }  D ^ { m }$ such that $f _ { A } \circ g _ { B } = \operatorname { i d } _ { D ^ { n } }$ , and when translated to matrices this yields $A B = I _ { n }$ . □

## 5 Problem 5

## 5.1 Part 1

⇐= : Suppose that Ax = b has a solution x.

Write $A = [ \mathbf { a } _ { 1 } , \mathbf { a } _ { 2 } , \cdot \cdot \cdot \mathbf { a } _ { m } ] ^ { t }$ in block form with each ai a row of A. By definition, a solution to this equation is $\mathrm { ~ a ~ } \mathbf { x } = \left( x _ { i } \right)$ such that for each i, we have $\langle \mathbf { a } _ { i } , \ \mathbf { x } \rangle = b _ { i }$ (by carrying out the matrix multiplication).

But

$$
\begin{array} { c } { { \langle { \bf { a } } _ { i } , { \bf { \sigma x } } \rangle = b _ { i } } } \\ { { \displaystyle \Longrightarrow \sum _ { j = 1 } ^ { m } a _ { i j } x _ { j } = b _ { i } , } } \end{array}
$$

which says that the collection $x _ { 1 } , \cdots , x _ { n }$ solves the equation

$$
a _ { i 1 } x _ { 1 } + a _ { i 2 } x _ { 2 } + \cdot \cdot \cdot a _ { i m } = b _ { i }
$$

for every i, which is exactly the statement that the $x _ { i }$ simultaneously solve the given system.

=⇒ : Suppose that the given system has a simultaneous solutions $x _ { 1 } , x _ { 2 } , \cdots , x _ { n }$ , and consider the matrix equation $A \mathbf { x } = \mathbf { b }$

Letting $\mathbf { x } = [ x _ { 1 } , x _ { 2 } , \cdots , x _ { n } ]$ , we can rewrite

$$
b _ { i } = a _ { i 1 } x _ { 1 } + a _ { i 2 } x _ { 2 } + \cdots + a _ { i m } x _ { m } = \langle { \bf a } _ { i } , { \bf x } \rangle ,
$$

where ${ \bf a } _ { i } = [ a _ { i 1 } , a _ { i 2 } , \cdots , a _ { i m } ]$

But then ${ \bf a } _ { i }$ is the ith row of A, and Ax = b has a solution iff there is a x such that $\langle \mathbf { a } _ { i } , \ \mathbf { x } \rangle = b _ { i }$ for all i, which is exactly what we’ve constructed.

## 5.2 Part 2

Noting that applying a row operation to A is the same as taking the product EA for some elementary matrix E, we can write $\begin{array} { r } { A _ { 1 } = \left( \prod _ { i = 1 } ^ { \ell } E _ { i } \right) } \end{array}$ A and $\begin{array} { r } { B _ { 1 } = \left( \prod _ { i = 1 } ^ { \ell } E _ { i } \right) B } \end{array}$ ;

thus

$$
\begin{array} { c } { A \mathbf { x } = \mathbf { b } } \\ { \implies E _ { \ell } A \mathbf { x } = E _ { \ell } \mathbf { b } } \\ { \implies E _ { \ell - 1 } E _ { \ell } A \mathbf { x } = E _ { \ell - 1 } E _ { \ell } \mathbf { b } } \\ { \vdots } \\ { \implies E _ { 1 } E _ { 2 } \cdot \cdot \cdot E _ { \ell } A \mathbf { x } = E _ { 1 } E _ { 2 } \cdot \cdot \cdot E _ { \ell } A \mathbf { b } } \\ { \implies E _ { \ell - 1 } \underset { + } { \longrightarrow } A _ { 1 } \mathbf { x } = B _ { 1 } } \end{array}
$$

## 5.3 Part 3

1. AX = B has a solution $\iff \operatorname { r a n k } ( A ) = \operatorname { r a n k } ( C )$

Note that we can only have rank $C \geq \operatorname { r a n k } A$

Suppose that $A X = B$ has a solution; then b is in the column space of A. But this says that

$$
\operatorname { s p a n } ( \{ \mathbf { a } _ { i } \} ) = \operatorname { s p a n } ( \{ \mathbf { a } _ { i } \} \bigcup \{ \mathbf { b } \} ) ,
$$

where ai are the columns of A. But then taking dimensions on both sides yields rank $A = \operatorname { r a n k } C ,$ since the rank of the dimension of the column space.

Suppose rank $A = \operatorname { r a n k } C ;$ then the

$$
\dim \operatorname { s p a n } ( \{ \mathbf { a } _ { i } \} ) = \dim \operatorname { s p a n } ( \{ \mathbf { a } _ { i } \} \bigcup \{ \mathbf { b } \} ) ,
$$

which says that $\mathbf { b } _ { i }$ is in the column space of A, and thus AX = B has a solution.

2. The solution is unique $\iff \operatorname { r a n k } ( A ) = m .$

$\Longrightarrow :$ To the contrapositive, Suppose rank $\mathsf { \Omega } _ { \mathsf { L } } ( A ) < m$ . Then by rank-nullity, dim ker $A > 0$ , so there is a vector $\mathbf v \neq 0$ such that $A \mathbf { v } = 0$ . But noting that $\mathbf { x } = \mathbf { 0 }$ is always a solution to $A \mathbf { x } = \mathbf { 0 }$ , this yields two distinct solutions.

Suppose that rank $( A ) = m$ . Then by rank-nullity, dim ker $A = 0$ , so ker $A = \{ \mathbf { 0 } \}$ . Now suppose $\mathbf { v } _ { 1 } , \mathbf { v } _ { 2 }$ are potentially distinct solutions to $A \mathbf { x } = \mathbf { b }$

Then,

$$
{ \begin{array} { r l } & { A \mathbf { v } _ { 1 } = A \mathbf { v } _ { 2 } = \mathbf { b } } \\ & { \qquad \implies A \mathbf { v } _ { 1 } - A \mathbf { v } _ { 2 } = \mathbf { b } - \mathbf { b } = \mathbf { 0 } } \\ & { \qquad \implies A ( \mathbf { v } _ { 1 } - \mathbf { v } _ { 2 } ) = \mathbf { 0 } } \\ & { \qquad \implies \mathbf { v } _ { 1 } - \mathbf { v } _ { 2 } \in \ker A } \\ & { \qquad \implies \mathbf { v } _ { 1 } - \mathbf { v } _ { 2 } = \mathbf { 0 } } \\ & { \qquad \implies \mathbf { v } _ { 1 } = \mathbf { v } _ { 2 } , } \end{array} }
$$

which shows that any solution is unique.

## 5.4 Part 4

We want to show that $A \mathbf { x } = \mathbf { 0 }$ has a nontrivial solution $\iff \operatorname { r a n k } ( A ) < m$

=⇒ : Suppose $A \mathbf { v } = \mathbf { 0 }$ for some $\mathbf { v } \neq 0$ . Then dim ker $A \geq 1$ , and by rank nullity we must have $m = \dim$ ker $A + \operatorname { r a n k } ( A )$ . But this immediately forces rank $( A ) \leq m - 1$

$\iff : { \mathrm { ~ S u p p o s e ~ r a n k } } ( A ) < m$ . Then again by rank nullity, this forces dim ker $A \geq 1$ , so A has a nontrivial kernel and thus there is a nontrivial solution to $A \mathbf { x } = 0$ .

## 6 Problem 6

## Proof following http://sierra.nmsu.edu/morandi/notes/SmithNormalForm.pdf

The goal is to show that any matrix $A \in M ( m \times n , R )$ is equivalent to a matrix D of the described form, so $A = P D Q$ for some matrices $P , Q .$ Since S is in fact the set of Smith Normal Forms for such matrices, it suffices to show that $S N F ( A )$ can be obtained by left and right multiplication by invertible matrices.
Moreover, since row operations can be performed by left-multiplication of elementary matrices, and column operations by right-multiplication.

We proceed by induction on $m + n$

For the base case $m + n = 2$ , this can only yield $\mathrm { ~ a ~ } 1 \times 1$ matrix, and the result holds vacuously.

For the inductive step, we will proceed by considering the top-left $2 \times 2$ block, say $M = { \left[ \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right] }$ , and showing it can be reduced to a block of the form $M ^ { \prime } = \left[ \begin{array} { c c } { { d _ { 1 } } } & { { 0 } } \\ { { 0 } } & { { d _ { 2 } } } \end{array} \right]$ where $d _ { 1 } \mid d _ { 2 }$ . Then the sub-matrix obtained by deleting the row and column containing $d _ { 1 }$ is a strictly smaller matrix, allowing the inductive hypothesis to be applied.

Moreover, note that if we are able to perform this reduction by a series of left and right multiplications, this will yields $A _ { 1 } = P _ { 1 } A Q _ { 1 }$ , and inductively we will have $A _ { r } = ( P _ { r } \cdot \cdot \cdot P _ { 2 } P _ { 1 } ) A ( Q _ { 1 } Q _ { 2 } \cdot \cdot \cdot Q _ { R } )$ , so each matrix will remain equivalent at every step.

Note: since R is a PID, it is also a Euclidean domain, so we can compute greatest common divisors.

We’ll first reduce the top-left entry and eliminate the bottom-left entry.

Let $d = \operatorname* { g c d } ( a , c )$ , so we can write $d = s a +$ tc for some $s , t \in R .$ . We would like to construct an operation that replaces a in M with d.

So let $\ell _ { 1 } , \ell _ { 2 }$ be parameters to be determined; we can then compute

$$
P _ { 1 } A = { \left[ \begin{array} { l l } { s } & { t } \\ { \ell _ { 1 } } & { \ell _ { 2 } } \end{array} \right] } { \left[ \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right] } = { \left[ \begin{array} { l l } { d } & { s b + t d } \\ { \ell _ { 1 } a + \ell _ { 2 } c } & { \ell _ { 1 } b + \ell _ { 1 } d } \end{array} \right] } ,
$$

where we now only have to choose $\ell _ { 1 } , \ell _ { 2 }$ so that $P _ { 1 }$ is invertible.

This lets us engineer an inverse matrix

$$
\begin{array} { r l } & { P _ { 1 } ^ { - 1 } : = \left[ \begin{array} { l l } { \ell _ { 2 } } & { - t } \\ { - \ell _ { 1 } } & { s } \end{array} \right] } \\ & { \qquad \implies P _ { 1 } P _ { 1 } ^ { - 1 } = \left[ \begin{array} { l l } { s } & { t } \\ { \ell _ { 1 } } & { \ell _ { 2 } } \end{array} \right] \left[ \begin{array} { l l } { \ell _ { 2 } } & { - t } \\ { - \ell _ { 1 } } & { s } \end{array} \right] } \\ & { \qquad = \left[ \begin{array} { l l } { s \ell _ { 2 } - t \ell _ { 1 } } & { - t s + s t } \\ { \ell _ { 1 } \ell _ { 2 } - \ell _ { 2 } \ell _ { 1 } } & { - t \ell _ { 1 } + s \ell _ { 2 } } \end{array} \right] , } \end{array}
$$

which just says that we need to pick $\ell _ { 1 } , \ell _ { 2 }$ such that $s \ell _ { 1 } - t \ell _ { 2 } = 1$ , since the off-diagonal entries vanish because R is commutative.

But this can be done by writing $a = d k _ { 1 }$ and $c = d k _ { 2 }$ , since d was their gcd, then

$$
d = s a + t c = s d k _ { 1 } + t d k _ { 2 } \implies 1 = s k _ { 1 } + t k _ { 2 } ,
$$

so just choose $\ell _ { 1 } = k _ { 1 } , \ell _ { 2 } = - k _ { 2 }$ to yield $P _ { 1 } P _ { 1 } ^ { - 1 } = I _ { 2 }$

We can observe that in the matrix $P _ { 1 } A$ , since d divides a and $^ { c , }$ d also divides $\ell _ { 1 } a + \ell _ { 2 } c$ . So write $k _ { 1 } d = \ell _ { 1 } a + \ell _ { 2 } c .$ , we can then perform a row operation by left-multiplying:

$$
Q _ { 1 } P _ { 1 } A : = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { - k } & { 1 } \end{array} \right] } { \left[ \begin{array} { l l } { d } & { s b + t d } \\ { \ell _ { 1 } a + \ell _ { 2 } c } & { \ell _ { 1 } b + \ell _ { 1 } d } \end{array} \right] } = { \left[ \begin{array} { l l } { d } & { s b + t d } \\ { 0 } & { - k ( s b + t d ) + \ell _ { 1 } b + \ell _ { 1 } d } \end{array} \right] } .
$$

We now carry out the same process with the top row instead of the first column.
This begins by computing $d _ { 1 } = \operatorname* { g c d } ( d , s b + t d )$ , where we can immediately note that $d _ { 1 }$ divides d.

We then write

$$
d _ { 1 } = d s ^ { \prime } + ( s b + t d ) t ^ { \prime } ,
$$

then perform column operations (i.e. right-multiplying by some $R _ { 1 } )$ to obtain a matrix of the form

$$
Q _ { 1 } P _ { 1 } A R _ { 1 } : = \left[ \begin{array} { c c } { { d } } & { { s b + t d } } \\ { { 0 } } & { { - k ( s b + t d ) + \ell _ { 1 } b + \ell _ { 1 } d } } \end{array} \right] \left[ \begin{array} { c c } { { s ^ { \prime } } } & { { \ell _ { 3 } } } \\ { { t ^ { \prime } } } & { { \ell _ { 4 } } } \end{array} \right] = \left[ \begin{array} { c c } { { d _ { 1 } } } & { { d \ell _ { 3 } + ( s b + t d ) \ell _ { 4 } } } \\ { { ? } } & { { ? } } \end{array} \right]
$$

where again $\ell _ { 3 } , \ell _ { 4 }$ are parameters that can be chosen to make $R _ { 1 }$ invertible.

We can again observe that $d _ { 1 }$ divides the top-left and (now) the top-right entry, which means we can find a $k ^ { \prime }$ such that

$$
Q _ { 1 } P _ { 1 } A R _ { 1 } S _ { 1 } : = \left[ \begin{array} { c c } { d _ { 1 } } & { d \ell _ { 3 } + ( s b + t d ) \ell _ { 4 } } \\ { \ ? } & { \ ? } \end{array} \right] \left[ \begin{array} { c c } { 1 } & { 0 } \\ { - k ^ { \prime } } & { 1 } \end{array} \right] = \left[ \begin{array} { c c } { d _ { 1 } } & { 0 } \\ { \ ? } & { \ ? } \end{array} \right] ,
$$

which puts us back in the original situation.

We can then continue by obtaining a $d _ { 2 }$ that divides $d _ { 1 }$ , doing row operations, and obtaining a matrix of the form

$$
P _ { 2 } Q _ { 1 } P _ { 1 } A R _ { 1 } S _ { 1 } : = \left[ \begin{array} { c c } { d _ { 2 } } & { \ ? } \\ { 0 } & { \ ? } \end{array} \right] ,
$$

and so on.

In a PID, “to divide is to contain” for ideals, so this generates a sequence of ideals

$$
( d ) \subseteq ( d _ { 1 } ) \subseteq ( d _ { 2 } ) \subseteq \cdot \cdot \cdot
$$

and since every PID is Noetherian, this increasing chain of ideals eventually stabilizes.

This means that after finitely many steps, we find $d _ { N + 1 } : = \operatorname* { g c d } ( d _ { N } , \cdot \cdot \cdot ) = d _ { N }$

obtain a matrix

$$
N : = \left( \prod _ { i } Q _ { i } P _ { i } \right) A \left( \prod _ { i } R _ { i } S _ { i } \right) = \left[ \begin{array} { c c } { { d _ { N } } } & { { x } } \\ { { y } } & { { z } } \end{array} \right]
$$

where either

$x = 0$ and y divides $d _ { N }$ N , or

$y = 0$ and x divides $d _ { N }$

Without loss of generality, supposing the first case holds, we can write $d _ { N } = \alpha y ;$ then

$$
E N : = \left[ \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 1 } } & { { - \alpha } } \end{array} \right] \left[ \begin{array} { c c } { { d _ { N } } } & { { 0 } } \\ { { y } } & { { z } } \end{array} \right] = \left[ \begin{array} { c c } { { d _ { N } } } & { { 0 } } \\ { { 0 } } & { { z } } \end{array} \right] ,
$$

where E is again invertible, yielding a diagonal matrix.

Note: in the general case of an m × n matrix, this eliminates entries 1, 2 and 2, 1. Eliminating the remaining entries in row 1 and column 1 proceed similarly, and never perturb entries that were made zero in a previous step.

Since it is not necessarily the case that $d _ { N }$ divides z here, a small additional modification is needed.
This is accomplished by a series of row operations, as described here:

Moreover, write $a = d \alpha$ and $b = d \beta$ for some $\alpha , \beta \in R$ We then perform the following row and column operations, yielding

$$
\begin{array} { c l c r } { { \left( \begin{array} { c } { { a 0 } } \\ { { 0 b } } \end{array} \right) \longrightarrow \left( \begin{array} { c } { { a 0 } } \\ { { a x b } } \end{array} \right) \longrightarrow \left( \begin{array} { c c } { { a } } & { { 0 } } \\ { { a x + b y b } } \end{array} \right) = \left( \begin{array} { c } { { a 0 } } \\ { { d b } } \end{array} \right) } } \\ { { \longrightarrow \left( \begin{array} { c } { { 0 - b \alpha } } \\ { { d } } & { { b } } \end{array} \right) \longrightarrow \left( \begin{array} { c c } { { 0 - b \alpha } } \\ { { d } } & { { 0 } } \end{array} \right) \longrightarrow \left( \begin{array} { c } { { d } } & { { 0 } } \\ { { 0 - b \alpha } } \end{array} \right) , } } \end{array}
$$

a diagonal matrix in Smith normal form since d divides bα.

This yields the desired form in the top-left $2 \times 2$ block, zeroing out the first column and row, so the inductive hypothesis applies to the remaining block.
