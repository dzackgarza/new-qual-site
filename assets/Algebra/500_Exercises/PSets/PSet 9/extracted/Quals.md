# Problem Set 9 Qual Problems

D. Zack Garza

November 30, 2019

## Contents

1 Problem 1 1   
1.1 Part 1 1   
1.2 Part 2 1   
1.3 Part 3 2   
2 Problem 2 2   
2.1 Lemma 1 2   
2.2 Lemma 2 3   
2.3 Main Result . 3   
3 Problem 3 5   
3.1 Part 1 5   
3.2 Part 2 5   
3.3 Part 3 5

## 1 Problem 1

## 1.1 Part 1

Definition: An element $r \in R$ is irreducible if whenever $r = s t$ , then either s or t is a unit.

Definition: Two elements $r , s \in R$ are associates if $r = \ell s$ for some unit ℓ.

A ring R is a unique factorization domain iff for every $r \in R$ , there exists a set $\left\{ p _ { i } \mid 1 \leq i \leq n \right\}$ such that $\textstyle r = u \prod _ { i = 1 } ^ { n } p _ { i }$ where u is a unit and each $p _ { i }$ is irreducible.

Moreover, this factorization is unique in the sense that if $\textstyle r = w \prod _ { i = 1 } ^ { n } q _ { i }$ for some w a unit and $q _ { i }$ irreducible elements, then each $q _ { i }$ is an associate of some $p _ { i }$

## 1.2 Part 2

A ring R is a principal ideal domain iff whenever $I \leq R$ is an ideal of R, there is a single element $r _ { i } \in R$ such that $I = ( r _ { i } )$ .

## 1.3 Part 3

An example of a UFD that is not a PID is given by $R = k [ x , y ]$ for k a field.

That R is a UFD follows from the fact that if k is a field, then k has no prime elements since every non-zero element is a unit. So the factorization condition holds vacuously for k, and k is a UFD. But then we can use the following result:

Theorem: If R is a UFD, then $R [ x ]$ is a UFD.

Since k is a UFD, the theorem implies that $k [ x ]$ is a UFD, from which it follows that $k [ x ] [ y ] = k [ x , y ]$ is also a UFD.

To see that R is not a PID, consider the ideal $I = ( x , y )$ , and suppose $\boldsymbol { I } = \boldsymbol { \mathit { g } } )$ for some single $g \in k [ x , y ]$

Note that $I \neq R ,$ , since I contains no degree zero polynomials. Moreover, since $( x ) \subset I = ( g )$ (and similarly for y), we have g  x and ${ \boldsymbol { g } } \mid { \boldsymbol { y } } ,$ which forces deg $g = 0$

So in fact $g \in k$ and thus g is invertible, but then $( g ) = g ^ { - 1 } ( g ) = ( 1 ) = k \ /$ , so this forces $I =$ $k \triangleleft k [ x , y ]$ . However, x $\not \in k \ ( \mathrm { n o r } \ y )$ , which is a contradiction.

## 2 Problem 2

## 2.1 Lemma 1

A has n distinct eigenvalues $\iff m _ { A } ( x ) = \chi _ { A } ( x )$

Proof:

The eigenvalues are always root of both $m _ { A } ( x )$ and $\chi _ { A } ( x )$ (potentially with differing multiplicities), so we can write

$$
m _ { A } ( x ) = \prod _ { i } ( x - \lambda _ { i } ) ^ { p _ { i } }
$$

$$
\chi _ { A } ( x ) = \prod _ { i } ( x - \lambda _ { i } ) ^ { q _ { i } }
$$

where $1 \leq p _ { i } \leq q _ { i }$ for every i.

=⇒ : If A has n distinct eigenvalues, then $\begin{array} { r } { \chi _ { A } ( x ) = \prod _ { i = 1 } ^ { n } ( x - \lambda _ { i } ) } \end{array}$ in ${ \overline { { k } } } [ x ]$ . Noting that every exponent is 1, we have $q _ { i } = 1$ for all i, which forces $p _ { i } = 1$ and thus $m _ { A } ( x ) = \chi _ { A } ( x )$

$\iff : \operatorname { I f } m _ { A } ( x ) = \chi _ { A } ( x )$ , then $p _ { i } = q _ { i }$ for all i. If we then consider $J C F ( A )$ , we have

• The number of Jordan block $J _ { \lambda _ { i } }$ is the dimension of the eigenspace $E _ { \lambda _ { i } }$ ,

$q _ { i } =$ the sum of the sizes of all Jordan blocks $J _ { \lambda _ { i } }$ , and

$p _ { i } =$ the size of the largest Jordan block $J _ { \lambda _ { i } }$

Thus $p _ { i } = q _ { i }$ for every $i \longleftrightarrow$ there is one Jordan block for every $\lambda _ { i } \iff$ dim $E _ { \lambda _ { i } } = 1$ for every i.

But dim $E _ { \lambda _ { i } }$ is precisely the multiplicity of $\lambda _ { i }$ in $\chi _ { A } ( x )$ , which means that $\begin{array} { r } { \chi _ { A } ( x ) = \prod _ { i } ( x - \lambda _ { i } ) } \end{array}$ Since $\chi _ { A } ( \boldsymbol { x } )$ is a degree n polynomial, this says that $\chi _ { A }$ has n distinct linear factors, corresponding to n distinct eigenvalues of A.

□

## 2.2 Lemma 2

Let $k [ x ] \cap V$ in the usual way with A to obtain an invariant factor decomposition

$$
V = \frac { k [ x ] } { ( f _ { 1 } ) } \oplus \frac { k [ x ] } { ( f _ { 2 } ) } \oplus \cdots \oplus \frac { k [ x ] } { ( f _ { k } ) } , \quad f _ { 1 } \mid f _ { 2 } \mid \cdots \mid f _ { k } .
$$

Then it is always the case that

$m _ { A } ( x ) = f _ { k } ( x )$ , i.e. the minimal polynomial is the invariant factor of largest degree,

$\begin{array} { r } { \chi _ { A } ( x ) = \prod _ { i = 1 } ^ { k } f _ { i } ( x ) } \end{array}$ , i.e. the characteristic polynomial is the product of all of the invariant factors.

## 2.3 Main Result

(1) =⇒ (2):

Suppose

$$
V = \operatorname { s p a n } _ { k } \left\{ \mathbf { v } , A \mathbf { v } , A ^ { 2 } \mathbf { v } , \cdot \cdot \cdot A ^ { n - 1 } \mathbf { v } \right\} : = \operatorname { s p a n } _ { k } B
$$

where dim $k V = n$

Then $A ^ { n } \mathbf { v }$ is necessarily a linear combination of these basis elements, and in particular, there are coefficients $c _ { i }$ (not all zero) such that

$$
A ^ { n } \mathbf { v } = \sum _ { i = 0 } ^ { n - 1 } c _ { i } A ^ { i } \mathbf { v } .
$$

The consider computing the matrix of A in B by considering the images of all basis elements under A.

Letting $B = \left\{ \mathbf w _ { i } : = A ^ { i } \mathbf v \Bigm | 0 \leq i \leq n - 1 \right\}$ , we have

$$
\begin{array} { r } { \mathbf { w } _ { 0 } : = \mathbf { v } \mapsto A \mathbf { v } : = \mathbf { w } _ { 1 } } \\ { \mathbf { w } _ { 1 } : = A \mathbf { v } \mapsto A ^ { 2 } \mathbf { v } : = \mathbf { w } _ { 2 } } \\ { \mathbf { w } _ { 2 } : = A ^ { 2 } \mathbf { v } \mapsto A ^ { 3 } \mathbf { v } : = \mathbf { w } _ { 3 } } \end{array}
$$

$$
\vdots \vdots
$$

$$
\mathbf { w } _ { n - 2 } : = A ^ { n - 2 } \mathbf { v } \mapsto A ^ { n - 1 } \mathbf { v } : = \mathbf { w } _ { n - 1 }
$$

$$
\mathbf { w } _ { n - 1 } : = A ^ { n - 1 } \mathbf { v } \mapsto A ^ { n } \mathbf { v } = \sum _ { i = 0 } ^ { n - 1 } c _ { i } A ^ { i } \mathbf { v } _ { i } : = \sum _ { i = 0 } ^ { n - 1 } c _ { i } \mathbf { w } _ { i } .
$$

This means that with respect to the basis B, A has the following matrix representation:

$$
[ A ] _ { B } = { \left[ \begin{array} { l l l l l } { 0 } & { 0 } & { \ldots } & { 0 } & { c _ { 0 } } \\ { 1 } & { 0 } & { \ldots } & { 0 } & { c _ { 1 } } \\ { 0 } & { 1 } & { \ldots } & { 0 } & { c _ { 2 } } \\ & & { \ddots } & & { \vdots } \\ { 0 } & { 0 } & { \ldots } & { 1 } & { c _ { n - 1 } } \end{array} \right] }
$$

But this is the companion matrix for $\textstyle p ( x ) = \sum _ { i = 0 } ^ { n - 1 } c _ { i } x ^ { i }$ , which always satisfy the property that $p ( x )$ equals both their characteristic and their minimal polynomial.

Thus by lemma 1, the matrix $[ A ] _ { B }$ has distinct eigenvalues, and thus so does A.

(2) =⇒ (1):

Suppose A has distinct eigenvalues. By Lemma 1, $\chi _ { A } ( x ) = m _ { A } ( x )$ , and so we have

$$
\chi _ { A } ( x ) = f _ { k } ( x ) = \prod _ { i = 1 } ^ { k } f _ { i } ( x ) = m _ { A } ( x ) ,
$$

which can only happen if $f _ { 1 } ( x ) = f _ { 2 } ( x ) = \cdot \cdot \cdot = f _ { n - 1 } ( x ) = 1$ , in which case there is only one nontrivial invariant factor.

So we have

$$
V \cong { \frac { k [ x ] } { ( f _ { k } ) } } , \quad \operatorname { A n n } ( V ) = ( f _ { k } ) , \quad \deg f _ { k } = n .
$$

If we now take the Rational Canonical Form of A, it follows that $R C F ( A )$ has only a single block in a suitable ordered basis $\boldsymbol { B } = \left\{ \mathbf { w } _ { 0 } , \cdots , \mathbf { w } _ { n - 1 } \right\}$

So write $\textstyle f _ { k } ( x ) = \sum _ { i = 0 } ^ { n } c _ { i } x ^ { i }$ ; then $[ A ] _ { B }$ is the companion matrix to $f _ { k } ( x )$ in the basis B, which by construction satisfies

$$
A = { \left[ \begin{array} { l l l l } { 0 } & { 0 } & { \ldots } & { 0 } & { c _ { 0 } } \\ { 1 } & { 0 } & { \ldots } & { 0 } & { c _ { 1 } } \\ { 0 } & { 1 } & { \ldots } & { 0 } & { c _ { 2 } } \\ & & { \ddots } & & { \vdots } \\ { 0 } & { 0 } & { \ldots } & { 1 } & { c _ { n - 1 } } \end{array} \right] } \Longrightarrow \ A \mathbf { w } _ { i } = { \left\{ \begin{array} { l l l } { \mathbf { w } _ { i + 1 } } & { 0 \leq i < n - 2 } \\ { \sum _ { i = 0 } ^ { n - 1 } c _ { i } \mathbf { w } _ { i } } & { i = n - 1 , } \end{array} \right. }
$$

and thus we have

$$
V \cong \operatorname { s p a n } _ { k } { \mathcal { B } } = \operatorname { s p a n } _ { k } \left\{ \mathbf { w } _ { 0 } , \cdot \cdot \cdot \mathbf { w } _ { n - 1 } \right\} \cong \operatorname { s p a n } _ { k } \left\{ \mathbf { w } _ { 0 } , A \mathbf { w } _ { 0 } , A ^ { 2 } \mathbf { w } _ { 0 } , \cdot \cdot \cdot , A ^ { n - 1 } \mathbf { w } _ { 0 } \right\} .
$$

−

## 3 Problem 3

## 3.1 Part 1

Let $\mathbf { v } = [ 0 , 1 , 0 ] ^ { t }$ , We compute

$$
M \mathbf { v } = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { x } \\ { 0 } & { 1 } & { 0 } \\ { y } & { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { 0 } \\ { 1 } \\ { 0 } \end{array} \right] } = { \left[ \begin{array} { l l l } { 1 ( 0 ) + 0 ( 1 ) + x ( 0 ) } \\ { 0 ( 0 ) + 1 ( 1 ) + 0 ( 0 ) } \\ { y ( 0 ) + 0 ( 1 ) + 1 ( 0 ) } \end{array} \right] } = { \left[ \begin{array} { l } { 0 } \\ { 1 } \\ { 0 } \end{array} \right] } = 1 { \left[ \begin{array} { l } { 0 } \\ { 1 } \\ { 0 } \end{array} \right] } ,
$$

which shows that v is an eigenvector of M with eigenvalue $\lambda = 1$

## 3.2 Part 2

Noting that the rank is the dimension of the column space, we find that

$\operatorname { r a n k } ( M ) \geq 1$ , since it is not the zero matrix,

$\operatorname { r a n k } ( M ) \geq 2$ , since neither $[ 1 , 0 , y ] ^ { t }$ or $[ x , 0 , 1 ] ^ { t }$ can be in the span of $[ 0 , 1 , 0 ] ^ { t }$ , and

$$
\operatorname { r a n k } ( M ) = 3 \iff \operatorname* { d e t } ( M ) \neq 0
$$

So we compute

$$
\operatorname* { d e t } ( x , y ) = { \left| \begin{array} { l l l } { 1 } & { 0 } & { x } \\ { 0 } & { 1 } & { 0 } \\ { y } & { 0 } & { 1 } \end{array} \right| } = 1 ( 1 - 0 ) - 0 ( 1 - x y ) + x ( - y ) = 1 - x y ,
$$

and so det $_ M ( x , y ) = 0 \iff x y = 1$ . Thus

$$
\operatorname { r a n k } ( M ) = { \left\{ \begin{array} { l l } { 3 } & { x y = 1 } \\ { 2 } & { \operatorname { e l s e } . } \end{array} \right. }
$$

## 3.3 Part 3

Since M is diagonalizable $\iff M$ is full rank, which in this case means $\operatorname { r a n k } ( M ) = 3$ , we have

$$
S = \left\{ ( x , y ) \in \mathbb { R } ^ { 2 } \ \middle \vert \ M \mathrm { { \ i s \ d i a g o n a l i z a b l e } } \ \right\} = \left\{ \left( x , { \frac { 1 } { x } } \right) \ \middle \vert \ x \in \mathbb { R } \setminus \{ 0 \} \right\} \subset \mathbb { R } ^ { 2 } .
$$