## Midterm

## D. Zack Garza

## October 31, 2019

## Contents

1 Problem 1 1   
1.1 Case 1: p = q. . 2   
1.2 Case 2: $p > q .$ 2   
1.3 Case 3: $q > p .$ 2   
2 Problem 2 3   
3 Problem 3 3   
4 Problem 4 3   
5 Problem 5 4   
6 Problem 6 5   
7 Problem 7 5   
7.1 = 5   
7.2 ⇐= 6   
8 Problem 8 7   
9 Problem 9 8   
10 Problem 10 8   
10.1 Part 1 8   
10.2 Part 2 9

## 1 Problem 1

Note that if either $p = 1$ or $q = 1$ , G is a p-group, which is a nontrivial center that is always normal. So assume $p \neq 1$ and $q \neq 1$

We want to show that G has a non-trivial normal subgroup. Noting that $\# G = p ^ { 2 } q$ , we will proceed by showing that either $n _ { p }$ or $n _ { q }$ must be 1.

We immediately note that

$$
\begin{array} { r l r } { n _ { p } \equiv 1 \pmod p \quad \quad } & { } & { n _ { q } \equiv 1 \pmod p } \\ & { } & { n _ { p } \enspace \middle | \ q \qquad \quad } & { } & { n _ { q } \enspace \middle | p ^ { 2 } , } \end{array}
$$

which forces

$$
n _ { p } \in \left\{ 1 , q \right\} , \quad n _ { 1 } \in \left\{ 1 , p , p ^ { 2 } \right\} .
$$

If either $n _ { p } = 1 \mathrm { o r } n _ { q } = 1$ , we are done, so suppose $n _ { p } \neq 1$ and $n _ { 1 } \neq 1$ . This forces $n _ { p } = q$ , and we proceed by cases:

## 1.1 Case 1: $p = q .$

Then $\# G = p ^ { 3 }$ and G is a p-group. But every p-group has a non-trivial center $Z ( G ) \leq G ,$ and the center is always a normal subgroup.

## 1.2 Case 2: $p > q$

Here, since $n _ { p } \ \middle | \ q$ , we must have $n _ { p } < q$ . But if $n _ { p } < q < p$ and $n _ { p } = 1$ mod p, then $n _ { p } = 1$

## 1.3 Case 3: $q > p .$

Since $n _ { p } \neq 1$ by assumption, we must have $n _ { p } = q$ . Now consider sub-cases for $n _ { q } \mathrm { . }$

$n _ { q } = p \colon \mathrm { H } \ n _ { q } = p = 1$ mod q and $p < q ,$ this forces $p = 1$

$n _ { q } = p ^ { 2 }$ : We will reach a contradiction by showing that this forces

$$
\left| P : = \bigcup _ { S _ { p } \in \mathrm { S y l } ( p , G ) } S _ { p } \setminus \{ e \} \right| + \left| Q : = \bigcup _ { S _ { q } \in \mathrm { S y l } ( q , G ) } S _ { q } \setminus \{ e \} \right| + | \{ e \} | > | G | .
$$

We have

$$
\begin{array} { r l r l } & { | P | + | Q | + | \{ e \} | = n _ { p } ( q - 1 ) + n _ { q } ( p ^ { 2 } - 1 ) + 1 } \\ & { \quad \quad = p ^ { 2 } ( q - 1 ) + q ( p ^ { 2 } - 1 ) + 1 } \\ & { \quad \quad = p ^ { 2 } ( q - 1 ) + 1 ( p ^ { 2 } - 1 ) + ( q - 1 ) ( p ^ { 2 } - 1 ) + 1 } & & { ( \mathrm { s i n c e ~ } q > 1 ) } \\ & { \quad \quad = ( p ^ { 2 } q - p ^ { 2 } ) + ( p ^ { 2 } - 1 ) + ( q - 1 ) ( p ^ { 2 } - 1 ) + 1 } \\ & { \quad \quad = p ^ { 2 } q + ( q - 1 ) ( p ^ { 2 } - 1 ) } \\ & { \quad \quad \geq p ^ { 2 } q + ( 2 - 1 ) ( 2 ^ { 2 } - 1 ) } & & { ( \mathrm { s i n c e ~ } p , q \geq 2 ) } \\ & { \quad \quad = p ^ { 2 } q + 3 } \\ & { \quad \quad \quad > p ^ { 2 } q = | G | , } \end{array}
$$

which is a contradiction.

## 2 Problem 2

We’ll use the fact that $H \leq N ( H )$ for any subgroup H (following directly from the closure axioms for a subgroup), and thus

$$
P \triangleleft N ( P ) \quad { \mathrm { a n d } } \quad N ( P ) \triangleleft N ^ { 2 } ( P ) .
$$

Since it is then clear that $N ( P ) \subseteq N ^ { 2 } ( P )$ , it remains to show that $N ^ { 2 } ( P ) \subseteq N ( P )$

So if we let $x \in N ^ { 2 } ( P )$ , so x normalizes $N ( P )$ , we need to show that x normalizes P as well, i.e. $x P x ^ { - 1 } = P .$

However, supposing that $| G | = p ^ { k } m$ where $( p , m ) = 1$ , we have

$$
P \leq N ( P ) \leq G \implies p ^ { k } \ \Big | \ | N ( P ) | \ \Big | \ p ^ { k } m ,
$$

so in fact $P \in \mathrm { S y l } ( p , N ( P ) )$ since it is a maximal p-subgroup.

Then $P ^ { \prime } : = x P x ^ { - 1 } \in \mathrm { S y l } ( p , N ( P ) )$ ) as well, since all conjugates of Sylow p-subgroups are also Sylow p-subgroups.

But since $P \triangleleft { N ( P ) }$ , there is only one Sylow p- subgroup of $N ( P )$ , namely P . This forces $P = P ^ { \prime }$ i.e. ${ \cal P } = x { \cal P } x ^ { - 1 }$ , which says that $x \in N ( P )$ as desired.

## 3 Problem 3

By definition, G is simple iff it has no non-trivial subgroups, so we will show that if $| G | = 1 4 8$ then it must contain a normal subgroup.

Noting that $2 4 8 = p ^ { 2 } q$ where $p = 2 , q = 3 7$ , we find that (for example) $n _ { 2 } \ \big | \ 3 7$ but $n \equiv 1$ mod 2; but the only odd divisor of 7 is 1, forcing $n _ { 2 } = 1$ . So G has a normal Sylow 2-subgroup and we are done.

## 4 Problem 4

Let $\tau : = ( t _ { 1 } , t _ { 2 } )$ denote the transposition and $\sigma = ( s _ { 1 } , s _ { 2 } \dots s _ { p } )$ denote the p-cycle, and let $S =$ $\langle \sigma , \tau \rangle$ . We would like to show that $S = S _ { p }$ , and since $S \subseteq S _ { p }$ is clear, we just need to show that $S _ { p } \subseteq S$

We first note that because p is prime, $\sigma ^ { k }$ is a p-cycle for every $1 \leq k \leq p .$ and $\langle \sigma \rangle = \langle \sigma ^ { k } \rangle$ for any such k.

Then note that $t _ { 1 } = s _ { i }$ for some i and $t _ { 2 } = s _ { j }$ for some $j ,$ so we can take $k = j - i$ to get a cycle $\sigma ^ { k }$ that sends $t _ { 1 }$ to $t _ { 2 }$ . So without loss of generality, we can replace σ with

$$
\sigma = ( t _ { 1 } , t _ { 2 } , \cdots )
$$

But now, we can relabel all of the elements of $S _ { p }$ simultaneously (i.e. replace $\langle \sigma , \tau \rangle$ with another subgroup in the same conjugacy class) in such a way that $t _ { 1 }$ becomes 1 and $t _ { 2 }$ becomes 2. We can

then assume wlog that

$$
\tau = ( 1 , 2 ) , \quad \sigma = ( 1 , 2 , \cdots , p )
$$

We can then get all adjacent transpositions: noting that

$$
\sigma ^ { - 1 } \tau \sigma = ( 2 , 3 )
$$

$$
\sigma ^ { - 2 } \tau \sigma ^ { 2 } = ( 3 , 4 )
$$

$$
\sigma ^ { - k } \tau \sigma ^ { k } = ( k + 1 \mod p , k + 2 \mod p ) \quad \forall 1 \leq k \leq p ,
$$

where we use the fact that for any $\gamma \in S _ { p }$ , we have $\gamma \tau \gamma = ( \gamma ( 1 ) , \ \gamma ( 2 ) )$

But this also gives us all transpositions of the form $( 1 , j )$ for each $2 \leq j \leq p \colon$

$$
( 2 , 3 ) ^ { - 1 } ( 1 , 2 ) ( 2 , 3 ) = ( 1 , 3 )
$$

$$
( 3 , 4 ) ^ { - 1 } ( 1 , 3 ) ( 3 , 4 ) = ( 1 , 4 )
$$

$$
( j - 1 , j ) ^ { - 1 } ( 1 , j - 1 ) ( j - 1 , j ) = ( 1 , j ) \quad \forall 1 \leq j \leq p .
$$

Thus we have $J : = \langle \{ ( 1 , j ) \mid 2 \leq j \leq p \} \rangle \subseteq S .$

But now if $\gamma = ( g _ { 1 } , g _ { 2 } , \cdot \cdot \cdot , g _ { k } ) \in S _ { p }$ is an arbitrary cycle, we can write

$$
\gamma = ( g _ { 1 } , g _ { 2 } , \cdot \cdot \cdot , g _ { k } ) = ( 1 , g _ { 1 } ) ( 1 , g _ { 2 } ) , \cdot \cdot \cdot ( 1 , g _ { k } ) ,
$$

so $\gamma \in J$ . Then writing any arbitrary permutation as a product of disjoint cycles, we find that $S _ { p } \subseteq J \subseteq S$ , and so $S _ { p } \subseteq S$ as desired.

## 5 Problem 5

Since G is a p-group, it has a nontrivial center. Since p is prime and $Z ( G )$ is a subgroup, this forces $\# Z ( G ) \in \{ p , p ^ { 2 } \}$ , where $p ^ { 3 }$ is ruled out because this would make G abelian.

Supposing that $\# Z ( G ) = p ^ { 2 }$ ,we would have $[ G : Z ( G ) ] = p ,$ and since $Z ( G ) \leq G$ , we can take the quotient and # $( G / Z ( G ) ) = p$ . But this means $G / Z ( G )$ is cyclic, which implies that G is abelian, a contradiction.

So we must have # $Z ( G ) = p ,$ and $\# \left( G / Z ( G ) \right) = p ^ { 2 }$

But any group of $p ^ { 2 }$ is abelian, and we can characterize $G ^ { \prime } : = [ G , G ]$ in the following way:

$G ^ { \prime } \leq G$ is the unique subgroup of G such that if $N \leq G$ and $G / N$ is abelian, then $N \leq G ^ { \prime } .$

We can thus conclude that $G ^ { \prime } \leq Z ( G )$ . It can not be the case that $G ^ { \prime } = \{ e \}$ , since this would make G abelian. This forces $G ^ { \prime } = Z ( G )$ as desired.

## 6 Problem 6

Writing $\begin{array} { r } { f ( { \boldsymbol x } ) = x ^ { 3 } - 3 { \boldsymbol x } - 3 = \sum a _ { i } x _ { i } \in \mathbb { Q } [ { \boldsymbol x } ] } \end{array}$ , we can conclude that f is irreducible over $\mathbb { Q }$ by Eisenstein with the prime $p = 3 .$ , since $\textit { p } \big | \ a _ { 0 } = - 3 , a _ { 1 } = 3 , a _ { 2 } = 0$ , but $p ^ { 2 } \nmid a _ { 3 } = 1$ •

We can check that $f ( 0 ) < 0$ and $f ( 1 0 ) > 0$ , so f has at least one real root. By the 1st derivative test, we can find that f is increasing on $( - \infty , - 1 )$ and less than zero, decreasing on $( - 1 , 1 )$ and less than zero, and increasing on $( 1 , \infty )$ , where it it attains its root. This root has multiplicity one, since gcd $( f , f ^ { \prime } ) = 1$ , which means that f has exactly one real root $r _ { 0 }$ , and thus a complex conjugate pair of roots $r _ { 1 } , \bar { r } _ { 1 }$ as well.

This means that complex conjugation is a nontrivial element τ of the Galois group $G \leq S _ { 3 }$ , and thus G contains a 2-cycle.

The Galois group must be a transitive subgroup of $S _ { 3 }$ , which restricts the possibilities to $S _ { 3 } , A _ { 3 }$

Since $A _ { 3 }$ only contains 3-cycles, this possibility is ruled out. Thus the Galois group must be $S _ { 3 }$

## 7 Problem 7

Definition: A field F is perfect if every irreducible polynomial $f ( x ) \in F [ x ]$ is separable in ${ \overline { { F } } } [ x ]$

Note that since F is a finite field, p must be a prime.

$$
{ \bf 7 . 1 } \implies :
$$

Suppose all irreducible polynomials in $F [ x ]$ are separable. Then let $a \in K$ be arbitrary, we will show that there exists some $\beta \in K$ such that $\beta ^ { p } = a$ .

Given such an $^ { a , }$ define the polynomial

$$
f ( x ) = x ^ { p } - a \in F [ x ] .
$$

Note that f is not separable, since $f ^ { \prime } ( x ) \ = \ p x ^ { p - 1 } \ = \ 0$ since $\operatorname { c h a r } ( F ) = p _ { \mathrm { : } }$ , which means (by assumption) that f must be reducible.

Thus we can write $f ( x ) = g ( x ) h ( x )$ where $g \in F [ x ]$ is some irreducible factor that divides $f .$

Noting that if $\beta \in { \overline { { F } } }$ is a any root of $f ,$ then

$$
f ( \beta ) = 0 \implies \beta ^ { p } = a \implies f ( x ) = x ^ { p } - a = x ^ { p } - \beta ^ { p } = ( x - \beta ) ^ { p } ,
$$

and so $\beta$ is necessarily a multiple root.

Moreover, since $g \mid f ,$ we must have $g ( x ) = ( x - \beta ) ^ { \ell }$ for some $1 \leq \ell \leq p$

But then we can expand g using the binomial formula:

$$
g ( x ) = ( x - \beta ) ^ { \ell } = \sum _ { k = 1 } ^ { \ell } { \binom { \ell } { k } } x ^ { \ell - k } ( - \beta ) ^ { k } = x ^ { \ell } + \cdot \cdot \cdot + ( - \beta ) ^ { \ell } \in F [ x ] .
$$

But since every coefficient must be in $F ,$ we must have $\beta ^ { \ell } \in F$ . We know that $\beta ^ { p } = a \in F$ as well, but since p is prime, $\operatorname* { g c d } ( p , \ell ) = 1$ .

We can thus find $s , t \in \mathbb { Z }$ such that $p s + t \ell = 1$ . But then

$$
\beta = \beta ^ { 1 } = \beta ^ { p s + t \ell } = \beta ^ { s t } \beta ^ { t \ell } = ( \beta ^ { \ell } ) ^ { s } ( \beta ^ { p } ) ^ { t } ,
$$

where since $\beta ^ { \ell } , \beta ^ { p } \in F$ , the entire RHS is in F , and thus the LHS $\beta \in F$ as well.

But then $\alpha = \beta ^ { p }$ where $\beta \in F$ , which is exactly what we wanted to show.

## 7.2 ⇐= :

Suppose every element in F admits a pth root in F , and suppose $f \in F [ x ]$ is an irreducible polynomial which is not separable, so it has a repeated root in ${ \overline { { F } } } .$

Supposing that $\operatorname* { g c d } ( f , f ^ { \prime } ) = g ( x )$ for any polynomial $g ( x )$ , this would imply that $g \ \big | \ f .$ But $f$ was assumed irreducible, so the only possibility is that in fact $g = f$

But if gcd $( f , f ^ { \prime } ) = f ;$ , since deg $f ^ { \prime } < f$ , we can not have $f \mid f ^ { \prime }$ unless $f ^ { \prime }$ is identically zero.

If we thus write

$$
\begin{array} { l } { f ( x ) = \displaystyle \sum _ { k = 0 } ^ { n } c _ { k } x ^ { k } , } \\ { f ^ { \prime } ( x ) = \displaystyle \sum _ { k = 1 } ^ { n } k c _ { k } x ^ { k - 1 } } \\ { \equiv 0 , } \end{array}
$$

then for each k we must have $c _ { k } = 0$ or k = 0 in F , i.e. $c _ { k } = 0$ or p  k .

Thus the only possible nonzero terms in f must come from coefficients of $x ^ { k p }$ for each k such that $1 \leq k p \leq n$ , i.e.

$$
f ( x ) = c _ { 0 } + c _ { p } x ^ { p } + c _ { 2 p } x ^ { 2 p } + \cdot \cdot \cdot
$$

But this says we can write $f ( x ) : = g ( x ^ { p } )$ , where

$$
g ( x ) = c _ { 0 } + c _ { p } x + c _ { 2 p } x ^ { 2 } + \cdot \cdot \cdot
$$

and furthermore, we can now use the assumption that $F$ is perfect to write $c _ { i } = b _ { i } ^ { p }$ for each $i ,$ yielding

$$
g ( x ) = b _ { 0 } ^ { p } + b _ { p } ^ { p } x ^ { 2 } + b _ { 2 p } ^ { p } x ^ { 2 } + \cdot \cdot \cdot
$$

and thus

$$
\begin{array} { r l } & { f ( x ) = g ( x ^ { p } ) } \\ & { \qquad = b _ { 0 } ^ { p } + b _ { p } ^ { p } x ^ { p } + b _ { 2 p } ^ { p } x ^ { 2 p } + \cdot \cdot \cdot } \\ & { \qquad = ( b _ { 0 } + b _ { p } x + b _ { 2 p } x ^ { 2 } ) ^ { p } } \\ & { \qquad : = ( j ( x ) ) ^ { p } , } \end{array}
$$

from which it follows that $j \ \vert \ f$ in $F [ x ]$ . But since f was irreducible, this is a contradiction, and so $f$ could not have had a repeated root. Thus every irreducible polynomial is separable, which is what we wanted to show.

## 8 Problem 8

Let $f ( x ) \in F [ x ]$ be irreducible, then since $p ( x ) : = \operatorname* { g c d } ( f , f ^ { \prime } )$ must divide f and f is irreducible, the only possibilities are $p ( x ) = 1$ or $p ( x ) = f ( x )$

If $p ( x ) = 1$ , then f is separable, so every root is distinct and f itself is of the form $f ( x ^ { p ^ { e } } )$ where each $e = 0$

Otherwise, $p ( x ) = f ( x )$ , which forces $f ^ { \prime } ( x ) = 0$ in $K [ x ]$ . If we write

$$
f ( x ) = \sum _ { k = 0 } ^ { n } a _ { k } a ^ { k }
$$

$$
f ^ { \prime } ( x ) = \sum _ { k = 1 } ^ { n } k a _ { k } a ^ { k - 1 }
$$

then $f ^ { \prime } ( x ) \equiv 0$ forces either $a _ { k } = 0$ 0, or $k = 0$ in $F \left( \mathrm { s o } p \mid k \right)$

We can thus rewrite f by leaving out all terms where $a _ { k } = 0$ to obtain

$$
f ( x ) = a _ { p } x ^ { p } + a _ { 2 p } x ^ { 2 p } + \cdot \cdot \cdot
$$

and we thus define

$$
g ( x ) : = a _ { p } x + a _ { 2 p } x ^ { 2 } + \cdot \cdot \cdot
$$

and we recover $f ( x ) = g ( x ^ { p } )$ . Moreover, $g$ is irreducible; otherwise if $h ( x ) \mid g ( x )$ then $h ( x ^ { p } ) \mid g ( x ^ { p } ) =$ $f ,$ where $f$ was assumed irreducible. If $g$ is separable we are done; otherwise $g$ fulfills the same hypotheses of that applied to $f ,$ so we can inductively continue this process to write $g ( x ) = g _ { 1 } ( x ^ { p } )$ 2 and thus $f ( x ) = g ( x ^ { p } ) = g _ { 1 } ( x ^ { p ^ { 2 } } )$ , and so on.

To see that every root of f has multiplicity $p ^ { e }$ , note that if $f ( \alpha ) = 0$ then $g ( \alpha ^ { p ^ { e } } ) = 0$ . But $g$ is separable, so $( x - \alpha ^ { p ^ { e } } ) \mid g ( x )$ in $K [ x ]$ and thus $( x ^ { p ^ { e } } - \alpha ^ { p ^ { e } } ) \mid g ( x ^ { p ^ { e } } ) = f$ in $\overline { { K } } [ x ]$ where K is an algebraic closure of K. But then $x ^ { p ^ { e } } - \alpha ^ { p ^ { e } } = ( x - \alpha ) ^ { p ^ { e } } \mid f ( x )$ , which precisely says that α is a root of multiplicity $p ^ { e }$

## 9 Problem 9

Let $x = [ \mathbb { Q } ( \zeta + \zeta ^ { - 1 } ) : \mathbb { Q } ]$

Noting that

$$
\zeta ( \zeta + \zeta ^ { - 1 } ) = \zeta ^ { 2 } + 1 ,
$$

if we let

$$
f ( x ) = x ^ { 2 } - ( \zeta + \zeta ^ { - 1 } ) x + 1 \in \mathbb { Q } ( \zeta + \zeta ^ { - 1 } ) [ x ] ,
$$

then $f ( \zeta ) = 0$

Since $\mathbb { Q } ( \zeta + \zeta ^ { - 1 } ) \subset \mathbb { R } , \mathbb { Q } ( \zeta )$ is a proper extension over this field, so if $d : = [ \mathbb { Q } ( \zeta ) : \mathbb { Q } ( \zeta + \zeta ^ { - 1 } ) ]$ then $d > 1$ . The fact that $\zeta$ is a root of f shows that $d \leq 2 ,$ so $d = 2$ . We also know that $[ \mathbb { Q } ( \zeta ) : \mathbb { Q } ] = \phi ( n )$

We thus have

$$
[ \mathbb { Q } ( \zeta ) : \mathbb { Q } ] = [ \mathbb { Q } ( \zeta ) : \mathbb { Q } ( \zeta + \zeta ^ { - 1 } ) ] [ \mathbb { Q } ( \zeta + \zeta ^ { - 1 } ) : \mathbb { Q } ] \quad \implies \quad \phi ( n ) = 2 x ,
$$

and so $\begin{array} { r } { x = \frac { \phi ( n ) } { 2 } } \end{array}$ as desired.

## 10 Problem 10

Suppose $K / F$ is a finite, normal, Galois extension.

## 10.1 Part 1

We have $F \leq E \leq K$ . Suppose that

$K / F$ is cyclic, so Gal $( K / F )$ is a cyclic group,

$E / F$ is normal

We then want to show that

1. $E / F$ is cyclic, i.e. $\operatorname { G a l } ( E / F )$ is cyclic, and

2. $K / E$ is cyclic, i.e. Ga $\scriptstyle { | ( K / E ) }$ is cyclic.

By the fundamental theorem of Galois theory, $E / F$ is normal if and only if

a. $\operatorname { G a l } ( K / E ) \triangleleft \operatorname { G a l } ( K / F )$ ), and

b. $\operatorname { G a l } ( E / F ) \cong \operatorname { G a l } ( K / F ) / \operatorname { G a l } ( K / E )$

Since $\operatorname { G a l } ( K / F )$ is a cyclic group and every subgroup of a cyclic group is itself cyclic, (a) lets us conclude that (1) holds.

Similarly, since $\operatorname { G a l } ( K / F )$ is a cyclic group and every quotient of a cyclic group is cyclic, (b) lets us conclude (2).

## 10.2 Part 2

By the Galois correspondence, all intermediate fields will correspond to subgroups of $\operatorname { G a l } ( K / F )$ Since this group is cyclic, we are reduced to analyzing the subgroup lattice of a generic cyclic group.

But if $G = \langle x \mid x ^ { n } = e \rangle$ where $\# G = n$ , then there is one and only one subgroup of index d and order $\textstyle { \frac { n } { d } }$ for every d dividing n, given by $H _ { d } : = \langle x ^ { d } \rangle$

So we have $[ G : H _ { d } ] = d ;$ so $H _ { d }$ corresponds to a field $E _ { d } / F$ of degree d where $F \leq E _ { d } \leq K$ . This can be done for every d dividing n, and since $K / F$ is a Galois extension, $n = | \mathrm { G a l } ( K / F ) | = [ K : F ]$ and this can be done for every divisor of $[ K : F ]$ as desired.