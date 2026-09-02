## Problem Set 10

## D. Zack Garza

## December 3, 2019

Contents\
1 Problem 1 1\
2 Problem 2 2\
3 Problem 3 2\
4 Problem 4 2\
5 Problem 5 3\
5.1 Part 1 3\
5.2 Part 2 5\
6 Problem 6 7\
7 Problem 7 7\
7.1 Part 1 7\
7.2 Part 2 7

## 1 Problem 1

Let ϕ be an n-form.
If suffices to show these statements for $n = 2$

=⇒ : Suppose $\phi$ is alternating, then $\phi ( b , b ) = 0$ for all $b \in B$

Letting $a , b \in B$ be arbitrary, we then have

$$
\begin{array} { r c l } { { } } & { { } } & { { 0 = \phi ( a + b , a + b ) } } \\ { { } } & { { } } & { { = \phi ( a , a + b ) + \phi ( b , a + b ) } } \\ { { } } & { { } } & { { = \phi ( a , a ) + \phi ( a , b ) + \phi ( b , a ) + \phi ( b , b ) } } \\ { { } } & { { } } & { { = \phi ( a , b ) + \phi ( b , a ) } } \\ { { } } & { { } } & { { \Longrightarrow \phi ( a , b ) = - \phi ( b , a ) , } } \end{array}
$$

which shows that $\phi$ is skew-symmetric.

⇐= Suppose $\phi$ is skew-symmetric, so $\phi ( a , b ) = - \phi ( b , a )$ for all $a , b \in B$ . Then $\phi ( b , b ) = - \phi ( b , b )$ by transposing the terms, which says that $\phi ( b , b ) = 0$ for all $b \in B$ and thus $\phi$ is alternating.

## 2 Problem 2

Let $f ( x ) = \operatorname* { d e t } ( P + x Q ) \in R [ x ]$ , then f is a polynomial in x which is not identically zero.

To see that $f \not \equiv 0$ , we can use that fact that P is invertible to evaluate $f ( 0 ) = \operatorname* { d e t } ( P ) \neq 0$

We can now note that f has finite degree, and thus finitely many zeroes in R.

## 3 Problem 3

Letting $k [ x ] \cap _ { \phi }$ E to yield a $k [ x ] .$ -module structure on E and take an invariant factor decomposition,

$$
E = E _ { 1 } \oplus E _ { 2 } \oplus \cdots \oplus E _ { t } , \quad E _ { i } = \frac { k [ x ] } { ( q _ { i } ) } , \quad q _ { 1 } \mid q _ { 2 } \mid \cdots \mid q _ { t }
$$

where $E _ { i } = k [ x ] / ( q _ { i } )$ . Then $q _ { t } = q .$ the minimal polynomial of $E .$ .

In particular, $E _ { t }$ is a ϕ-invariant subspace of E, and if deg $q _ { t } = m$ , then $E _ { t }$ is in fact an m-dimensional cyclic module with basis $\{ \mathbf { v } , \phi ( \mathbf { v } ) , \phi ^ { 2 } ( \mathbf { v } ) , \cdot \cdot \cdot , \phi ^ { m - 1 } ( \mathbf { v } ) \}$ for some $\mathbf { v } \in E _ { t }$

But since $E _ { t } \leq E$ is a subspace, we have

$$
m = \deg q ( x ) = \deg q _ { t } ( x ) = \dim E _ { t } \leq \dim E .
$$

## 4 Problem 4

=⇒ : Suppose $A \sim D$ where D is diagonal.
Then $J C F ( A ) = J C F ( D ) = D$ , which means that every Jordan block of A has size exactly 1.

Since the elementary divisors of A are precisely the minimal polynomials of the Jordan blocks of $A _ { i }$ and the minimal polynomial of any $1 \times 1$ matrix $[ a _ { i j } ]$ is given by the linear polynomial $x - a _ { i j }$ , every elementary divisor of A must be linear.

⇐= : Suppose all of the elementary divisors of A are linear.
Every elementary divisor is the minimal polynomial of a Jordan block of $A ,$ and so if we write $J C F ( A ) = \oplus M _ { i }$ , then the minimal polynomial of each $M _ { i }$ is linear.

Supposing that $M _ { i }$ has minimal polynomial $p _ { i } ( x ) = x - c$ for some scalar c, we have

$$
p _ { i } ( M _ { i } ) = 0 \implies M _ { i } - c I _ { n } = 0 \implies M _ { i } = c I _ { n } ,
$$

which shows that $M _ { i }$ is a diagonal matrix with only c on its diagonal.

But if every Jordan block of A is diagonal, then $J C F ( A ) = D$ is diagonal and $A \sim D$

## 5 Problem 5

## 5.1 Part 1

We’ll use the fact that the minimal polynomial q is the invariant factor of highest degree, and so every other invariant factor must divide q.

Moreover, $R C F ( A ) = C _ { 1 } \oplus C _ { 2 } \oplus \cdots \oplus C _ { k }$ where each $C _ { i }$ is the companion matrix of the ith invariant factor if we write $V \cong \oplus _ { i = 1 } ^ { k } k [ x ] / ( a _ { i } )$ . So it suffices to determine all of the possible distinct combinations of invariant factors.

We can restrict this list by noting that the characteristic polynomial satisfies $\chi _ { A } ( x ) = \prod a _ { i }$ , and in particular, deg $\chi _ { A } ( x ) = 6$ . Noting that $\deg q ( x ) = 3$ , the degrees of the remaining invariant factors must sum to 3.

So the possibilities are:

$$
\begin{array} { r l r l r l r l } & { R _ { 1 } : a _ { 1 } = ( x - 2 ) , } & & { \quad \quad a _ { 2 } = ( x - 2 ) ^ { 2 } , } & & { \quad \quad a _ { 3 } = q ( x ) , } \\ & { R _ { 2 } : a _ { 1 } = ( x - 2 ) , } & & { \quad a _ { 2 } = ( x - 2 ) ( x + 3 ) , } & & { \quad \quad a _ { 3 } = q ( x ) , } \\ & { R _ { 3 } : a _ { 1 } = ( x + 3 ) , } & & { \quad a _ { 2 } = ( x - 2 ) ( x + 3 ) , } & & { \quad \quad a _ { 3 } = q ( x ) , } \\ & { R _ { 4 } : a _ { 1 } = ( x - 2 ) , } & & { \quad \quad a _ { 2 } = ( x - 2 ) , } & & { \quad \quad a _ { 3 } = ( x - 2 ) } & & { \quad a _ { 4 } = q ( x ) , } \\ & { R _ { 5 } : a _ { 1 } = ( x + 3 ) , } & & { \quad \quad a _ { 2 } = ( x + 3 ) , } & & { \quad \quad a _ { 3 } = ( x + 3 ) } & & { \quad a _ { 4 } = q ( x ) . } \end{array}
$$

This exhausts all possibilities, because the degrees of ai must be a weakly increasing integer partitions of 3, namely (1, 2) or (1, 1, 1). A (1, 2) partition can only yield a quadratic factor for $a _ { 2 } .$ , and since $a _ { 2 } \ \bigg | \ a _ { 3 }$ there are only two choices.
If a repeated factor is chosen like $( x - 2 ) ^ { 2 }$ then $a _ { 1 } \ \bigg | \ a _ { 2 }$ forces $a _ { 1 } = x - 2$ ,yielding $R _ { 1 }$ Otherwise, we can pick either distinct factor of $a _ { 2 }$ as a choice for $a _ { 1 } .$ yielding $R _ { 2 } , R _ { 3 }$ . Any (1, 1, 1) partition can only be a repeated linear factor, since we must have $a _ { 1 } \mid a _ { 2 } \mid a _ { 3 } ,$ , and there are only two choices.
This yields $R _ { 4 } , R _ { 5 }$

Noting that

$$
\begin{array} { c } { { ( x - 2 ) ^ { 2 } = x ^ { 2 } - 4 x + 4 } } \\ { { ( x - 2 ) ( x + 3 ) = x ^ { 2 } + x - 6 } } \\ { { q ( x ) = x ^ { 3 } - x ^ { 2 } - 8 x + 1 2 , } } \end{array}
$$

these choices correspond to the matrices

$$
R _ { 1 } = [ { \begin{array} { l l l l l } { { \frac { 2 } { 0 } } | { \begin{array} { l l l l l } { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { - 4 } \\ { 0 } & { 1 } & { 4 } \end{array} } | 0 } & { 0 } & { 0 } \\ { { \frac { 0 } { 0 } } | { \begin{array} { l l l l l } { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { - 1 2 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { 1 } \end{array} } | } , \qquad R _ { 2 } = [ { \frac { 2 } { 0 } } | { \begin{array} { l l l l l } { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 6 } & { 0 } & { 0 } \\ { 1 } & { - 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { - 1 2 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 8 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { 1 } \end{array} } ] } , R _ { 3 } = [ { \frac { 3 } { 0 } } | { \begin{array} { l l l l l } { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 6 } & { 6 } & { 0 } & { 0 } & { 0 } \\ { 1 } & { - 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { - 1 2 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { 0 } & { 8 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { 1 } \end{array} } |  ] \end{array}
$$

$$
R _ { 4 } = \left[ \begin{array} { c } { \displaystyle \frac { 2 \ | \ 0 \ | \ 0 \ | \ 0 \ 0 } { 0 \ | \ 2 \ | \ 0 \ 0 } 0 } \\ { \displaystyle \frac { 0 \ | \ 2 \ | \ 0 \ | \ 0 \ 0 } { 0 \ | \ 0 \ 2 \ | \ 0 \ 0 } 0 } \\ { \displaystyle \frac { 0 \ | \ 0 \ | \ 0 \ | \ 0 \ 0 } { 0 \ | \ 0 \ 0 } 0 0 } \\ { \displaystyle 0 \ | \ 0 \ | \ 0 \ | \ 1 \ 0 \ 8 } \\ { \displaystyle 0 \ | \ 0 \ | \ 0 \ | \ 0 \ 1 \ 1 } \end{array} \right] \qquad R _ { 5 } = \left[ \frac { - 3 \ | \ 0 \ | \ 0 \ | \ 0 \ 0 \ 0 } { 0 \ 0 \ - 3 \ | \ 0 \ 0 0 } 0 \right]
$$

Note: these are perhaps transposed from Hungerford’s notation.

Since none of the associated polynomials were irreducible over Q, $R C F ( A )$ takes these forms over C as well.

To obtain the possible Jordan Canonical forms, we’ll instead need to consider elementary divisors.
These can be obtained from the invariant factors above, yielding the possibilities:

$$
\begin{array} { r l } & { R _ { 1 } : ( x - 2 ) , ~ ( x - 2 ) , ~ ( x - 2 ) ^ { 2 } ~ ( x + 3 ) } \\ & { R _ { 2 } : ( x - 2 ) , ~ ( x - 2 ) , ~ ( x - 2 ) ^ { 2 } , ~ ( x + 3 ) , ~ ( x + 3 ) } \\ & { R _ { 3 } : ( x - 2 ) , ~ ( x - 2 ) ^ { 2 } , ~ ( x + 3 ) , ~ ( x + 3 ) , ~ ( x + 3 ) } \\ & { R _ { 4 } : ( x - 2 ) , ~ ( x - 2 ) , ~ ( x - 2 ) , ~ ( x - 2 ) ^ { 2 } , ~ ( x + 3 ) } \\ & { R _ { 5 } : ( x + 3 ) , ~ ( x + 3 ) , ~ ( x + 3 ) , ~ ( x + 3 ) , ~ ( x - 2 ) ^ { 2 } } \end{array}
$$

For the sake of notation, write $J _ { \lambda } ^ { k }$ for a $k \times k$ Jordan block with λ on the diagonal and $0 _ { k }$ for the $k \times k$ zero matrix.
We then have

$$
{ \cal R } _ { 1 } : 0 _ { 2 } \oplus J _ { 2 } ^ { 1 } \oplus J _ { 2 } ^ { 1 } \oplus J _ { 2 } ^ { 2 } \oplus J _ { 3 } ^ { 1 }
$$

$$
R _ { 2 } : J _ { 2 } ^ { 1 } \oplus J _ { 2 } ^ { 1 } \oplus J _ { 2 } ^ { 2 } \oplus J _ { 3 } ^ { 1 } \oplus J _ { 3 } ^ { 1 }
$$

$$
{ R _ { 3 } } : { J _ { 2 } ^ { 1 } } \oplus J _ { 2 } ^ { 2 } \oplus J _ { 3 } ^ { 1 } \oplus J _ { 3 } ^ { 1 } \oplus J _ { 3 } ^ { 1 }
$$

$$
{ R _ { 4 } } : { J _ { 2 } ^ { 1 } } \oplus J _ { 2 } ^ { 1 } \oplus J _ { 2 } ^ { 1 } \oplus J _ { 2 } ^ { 2 } \oplus J _ { 3 }
$$

$$
R _ { 5 } : J _ { 2 } ^ { 2 } \oplus J _ { 3 } ^ { 1 } \oplus J _ { 3 } ^ { 1 } \oplus J _ { 3 } ^ { 1 } \oplus J _ { 3 } ^ { 1 }
$$

## 5.2 Part 2

We’ll first exhibit the possibilities over C, then show what subset can be obtained over $\mathbb { Q } .$

Over C, we have $x ^ { 2 } + 1 = ( x - i ) ( x + i )$ . By the same argument used in Part 1, we know that $q ( x )$ is the largest invariant factor, and since deg $q = 3$ , the degrees of the remaining factors must sum to 4 (since the degree $\chi _ { A }$ will be 7, and it’s the product of these factors).

We also know that the degrees must forma weakly decreasing partition of 4, which are

$( 1 , 1 , 1 , 1 )$

– This can only be $a _ { 1 } = a _ { 2 } = a _ { 3 } = a _ { 4 }$ , a repeated linear factor, so there are 3 possibilities $( 1 , 1 , 2 )$

– This must satisfy $a _ { 1 } = a _ { 2 }$ , so there are 3 possibilities for $a _ { 1 } = a _ { 2 }$ and 2 for $a _ { 3 }$ , for 6 total.
• (2, 2)

– This also must satisfy $a _ { 1 } = a _ { 2 }$ , so there are ${ \binom { 3 } { 2 } } / 2 = 3$ possibilities

The possibilities are thus

$$
R _ { 1 } : a _ { 1 } = ( x - i ) a _ { 2 } = ( x - i ) a _ { 3 } = ( x - i ) a _ { 4 } = ( x - i ) a _ { 5 } = q ( x )
$$

$$
R _ { 2 } : a _ { 1 } = ( x + i ) a _ { 2 } = ( x + i ) a _ { 3 } = ( x + i ) a _ { 4 } = ( x + i ) a _ { 5 } = q ( x )
$$

$$
R _ { 3 } : a _ { 1 } = ( x - 7 ) a _ { 2 } = ( x - 7 ) a _ { 3 } = ( x - 7 ) a _ { 4 } = ( x - 7 ) a _ { 5 } = q ( x )
$$

$$
R _ { 4 } : a _ { 1 } = ( x + i ) \quad \quad \quad \quad a _ { 2 } = ( x + i ) \quad a _ { 3 } = ( x + i ) ( x - i ) \quad \quad a _ { 4 } = q ( x )
$$

$$
R _ { 5 } : a _ { 1 } = ( x + i ) \quad \quad \quad \quad a _ { 2 } = ( x + i ) \quad a _ { 3 } = ( x + i ) ( x - 7 ) \quad \quad a _ { 4 } = q ( x )
$$

$$
R _ { 6 } : a _ { 1 } = ( x - i ) \quad \quad \quad \quad a _ { 2 } = ( x - i ) \quad a _ { 3 } = ( x - i ) ( x + i ) \quad \quad a _ { 4 } = q ( x )
$$

$$
R _ { 7 } : a _ { 1 } = ( x - i ) a _ { 2 } = ( x - i ) a _ { 3 } = ( x - i ) ( x - 7 ) a _ { 4 } = q ( x )
$$

$$
R _ { 8 } : a _ { 1 } = ( x - 7 ) \qquad \quad a _ { 2 } = ( x - 7 ) \quad a _ { 3 } = ( x - 7 ) ( x + i ) \qquad \quad a _ { 4 } = q ( x )
$$

$$
R 9 : a _ { 1 } = ( x - 7 ) a _ { 2 } = ( x - 7 ) a _ { 3 } = ( x - 7 ) ( x - i ) a _ { 4 } = q ( x )
$$

$$
R _ { 1 0 } : a _ { 1 } = ( x + i ) ( x - i ) \quad a _ { 2 } = ( x + i ) ( x - i ) \qquad \quad a _ { 3 } = q ( x )
$$

$$
R _ { 1 2 } : a _ { 1 } = ( x - i ) ( x - 7 ) \quad a _ { 2 } = ( x - i ) ( x - 7 ) \qquad \quad a _ { 3 } = q ( x )
$$

The corresponding Rational Canonical Forms for each $R _ { j }$ can be obtained by writing the companion matrix for the blocks $a _ { i }$ and taking their direct sum.

It is then easy to see that if A is taken over Q instead, only form $R _ { 3 }$ is possible (since $x ^ { 2 } + 1$ does not split over Q).

Let $n J _ { \lambda } ^ { k }$ denote $J _ { \lambda } ^ { k } \oplus J _ { \lambda } ^ { k } \oplus \cdot \cdot \cdot \oplus J _ { \lambda } ^ { k }$ , where n copies appear in the direct sum corresponding to n Jordan blocks.
We can immediately obtain the corresponding Jordan forms:

$$
R _ { 1 } : 5 J _ { i } ^ { 1 } \oplus J _ { - i } ^ { 1 } \oplus J _ { 7 } ^ { 1 }
$$

$$
{ \cal R } _ { 2 } : 5 J _ { - i } ^ { 1 } \oplus J _ { i } ^ { 1 } \oplus J _ { 7 } ^ { 1 }
$$

$$
{ \cal R } _ { 3 } : 5 J _ { 7 } ^ { 1 } \oplus J _ { i } ^ { 1 } \oplus J _ { - i } ^ { 1 }
$$

$$
{ \cal R } _ { 4 } : 4 J _ { - i } ^ { 1 } \oplus 2 J _ { i } ^ { 1 } \oplus J _ { 7 } ^ { 1 }
$$

$$
R _ { 5 } : 4 J _ { - i } ^ { 1 } \oplus J _ { i } ^ { 1 } \oplus 2 J _ { 7 } ^ { 1 }
$$

$$
{ R _ { 6 } } : 4 J _ { i } ^ { 1 } \oplus 2 J _ { - i } ^ { 1 } \oplus J _ { 7 } ^ { 1 }
$$

$$
R _ { 7 } : 4 J _ { i } ^ { 1 } \oplus J _ { - i } ^ { 1 } \oplus 2 J _ { 7 } ^ { 1 }
$$

$$
{ \cal R } _ { 8 } : 2 J _ { - i } ^ { 1 } \oplus J _ { i } ^ { 1 } \oplus 2 J _ { 7 } ^ { 1 }
$$

$$
{ \cal R } _ { 9 } : 2 J _ { i } ^ { 1 } \oplus J _ { - i } ^ { 1 } \oplus 4 J _ { 7 } ^ { 1 }
$$

$$
{ \cal R } _ { 1 0 } : 3 J _ { i } ^ { 1 } \oplus 3 J _ { - i } ^ { 1 } \oplus J _ { 7 } ^ { 1 }
$$

$$
R _ { 1 1 } : J _ { i } ^ { 1 } \oplus 3 J _ { - i } ^ { 1 } \oplus 3 J _ { 7 } ^ { 1 }
$$

$$
R _ { 1 2 } : 3 J _ { i } ^ { 1 } \oplus J _ { - i } ^ { 1 } \oplus 3 J _ { 7 } ^ { 1 } .
$$

## 6 Problem 6

Let $\phi \in \operatorname { E n d } ( V )$ , then following a different proof than what is suggested in Hungerford, define an action

$$
\begin{array} { c } { k [ x ] \curvearrowright V } \\ { p ( x ) \curvearrowright \langle \left( x \right) ( \left( x \right) ( \left( \mathbf { v } \right) ) , } \end{array}
$$

which induces an invariant factor decomposition

$$
V \cong \bigoplus _ { i = 1 } ^ { n } { \frac { k [ x ] } { ( f _ { i } ) } } , \quad f _ { i } \in k [ x ] , \quad f _ { 1 } \ { \Big | } \ f _ { 2 } \ { \Big | } \ \cdots \ { \Big | } \ f _ { n } .
$$

Then $f _ { n } ( x )$ is the minimal polynomial of $\phi ,$ and the characteristic polynomial is given by $p _ { \phi } ( x ) =$ $\scriptstyle \prod _ { i = 1 } ^ { n } f _ { i } ( x )$ . In particular, $f _ { n } ( x ) \mid p _ { \phi } ( x )$ and $f _ { n } ( \phi ) = 0$ by definition, so $p _ { \phi } ( \phi ) = 0$ as well.

## 7 Problem 7

## 7.1 Part 1

Suppose $\phi \psi = \psi \phi$ and both $\phi , \psi$ have bases of eigenvectors.

Letting $\lambda _ { i }$ denote the eigenvalues of $\phi ,$ , write

$$
V = \bigoplus _ { i } V _ { \lambda _ { i } } .
$$

Now let v be an eigenvector corresponding to $\lambda _ { i }$ . We have $\phi ( \mathbf { v } ) = \lambda _ { i } \mathbf { v }$ , and

$$
\phi \psi ( \mathbf { v } ) = \psi \phi ( \mathbf { v } ) = \psi ( \lambda _ { i } \mathbf { v } ) = \lambda _ { i } \psi ( \mathbf { v } ) ,
$$

which demonstrates that $\psi ( \mathbf { v } )$ is also an eigenvector for $\phi ,$ and moreover $\psi ( V _ { \lambda _ { i } } ) \subseteq V _ { \lambda _ { i } }$ , so it only sends $\lambda _ { i }$ eigenvectors to other $\lambda _ { i }$ eigenvectors.

Now consider $\psi | _ { V _ { \lambda _ { i } } }$ , the restriction of $\psi$ this eigenspace.
Since $\psi$ had an eigenbasis on $V _ { : }$ this restricts to an eigenbasis $B _ { i } = \left\{ \mathbf { w } _ { i } \right\}$ of $V _ { \lambda _ { i } }$ . But then every element of $\mathbf { w } _ { i }$ is an eigenvector of $\psi$ by definition, and we also have $\mathbf { w } _ { i } \in V _ { \lambda _ { i } }$ , so the $\mathbf { w } _ { i }$ are also eigenvectors for $\phi .$

Doing this for every $i ,$ we obtain $\begin{array} { r } { B = \amalg _ { i } B _ { i } } \end{array}$ where $\operatorname { s p a n } ( B ) = E$ , which yields a simultaneous eigenbasis of E for both $\psi$ and $\phi .$

## 7.2 Part 2

Writing $B = \left\{ \mathbf { v } _ { i } \mid 1 \leq i \leq n \right\}$ , this means we can form an invertible matrix $P = [ \mathbf { v } _ { 1 } ^ { t } , \cdots , \mathbf { v } _ { n } ^ { t } ]$ . Then if A is the matrix of $\phi$ in the standard basis and B is the matrix of $\psi ,$ we have

$$
P A P ^ { - 1 } = D _ { 1 } \quad { \mathrm { a n d } } \quad P B P ^ { - 1 } = D _ { 2 }
$$

where $D _ { 1 } , D _ { 2 }$ are diagonal.
In other words, P simultaneously diagonalizes both A and $B .$
