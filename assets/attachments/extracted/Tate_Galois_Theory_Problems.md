# Homework problems given by Prof. J. Tate in a course on Algebra $\mathbf { 2 5 0 ( a ) }$ at Harvard in the Fall of 1985.

## October 22, 1985

(1) Suppose $f ( X )$ is irreducible and $G _ { f }$ is abelian. Prove that the order of $G _ { f }$ is the degree of f .

(2) Suppose $K / F$ is a finite Galois extension. Let $G = \operatorname { G a l } ( K / F )$

(a) Suppose G acts transitively on a set I. Show that there exists a family $( \alpha _ { i } ) _ { i \in I }$ of elements of K such that $\sigma ( \alpha _ { i } ) = \alpha _ { \sigma i }$ for all $\sigma \in G$

(b) Let n be an integer $\geq 0$ and suppose $h : G \hookrightarrow { \mathcal { S } } _ { n }$ is an injective group homomorphism. Show that if F has at least n elements, then there is a polynomial $f ( X ) \in F [ X ]$ with distinct roots such that K is a splitting field for f over F and such that $G _ { f } = h ( G ) \subset S _ { n }$

(3) Let $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { n }$ be “variables” and

$$
f ( X ) = \prod _ { i = 1 } ^ { n } ( X - \alpha _ { i } ) = X ^ { n } - a _ { 1 } X ^ { n - 1 } + \dots .
$$

Put :

$$
\beta = \sum _ { \pi \in { \mathcal A } _ { n } } \alpha _ { \pi ( 2 ) } \alpha _ { \pi ( 3 ) } ^ { 2 } \ldots \alpha _ { \pi ( n ) } ^ { n - 1 } , { \mathrm { ~ a n d ~ } } \gamma = \sum _ { \pi \in { \mathcal S } _ { n } \setminus { \mathcal A } _ { n } } \alpha _ { \pi ( 2 ) } \alpha _ { \pi ( 3 ) } ^ { 2 } \ldots \alpha _ { \pi ( n ) } ^ { n - 1 } .
$$

(a) Show that $( \beta - \gamma ) ^ { 2 } = d _ { f }$ (the discriminant of $f )$

(b) Let $b = \beta + \gamma$ and $c = \beta \gamma$ . How do you know b and c are in $\mathbb { Z } [ a _ { 1 } , a _ { 2 } , \ldots ]$

(c) For $n \ = \ 2$ and 3, give b and c explicitly as elements of $\mathbb { Z } [ a _ { 1 } , a _ { 2 } ]$ , and of $\mathbb { Z } [ a _ { 1 } , a _ { 2 } , a _ { 3 } ]$ (Recall : $\bar { f } ( X ) = X ^ { n } - a _ { 1 } X ^ { n - 1 } + a _ { 2 } X ^ { n - 2 } - \dots )$

(d) Now drop the assumption that the $\alpha _ { i }$ are “variables”. Let F be a field, $a _ { i } \in$ $F , \ 1 \leq \ i \ \leq \ n$ , and suppose $d _ { f } \ne 0$ . Let K be a splitting field for f over $F , { \mathrm { ~ i . e . , ~ } } K = F ( \alpha _ { 1 } , \ldots , \alpha _ { n } )$ and $G = \operatorname { G a l } ( K / F )$ Show that the fixed field of $G _ { f } \cap { \mathcal { A } } _ { n }$ is the splitting field of the quadratic polynomial $X ^ { 2 } - b X + c .$ regardless of the characteristic.

(e) Let $F = \mathbb { F } _ { 2 } ( t )$ , t transcendental. Find $G _ { f }$ in the following cases :

(i) $f ( X ) = X ^ { 3 } + t X + 1 ;$

(ii) $f ( X ) = X ^ { 3 } + t ^ { 3 } X + t ^ { 2 } ;$

(iii) $f ( X ) = X ^ { 3 } + t ^ { 2 } X + ( t + 1 ) { \mathrm { { ' } } }$

(f) Show that if the $a _ { i } \in \mathbb { Z }$ , then $d _ { f } \equiv 0$ or 1 (mod 4) (just express $d _ { f }$ in terms of b and c).

(4) Let

$$
f ( X ) = X ^ { 4 } - a _ { 1 } X ^ { 3 } + a _ { 2 } X ^ { 2 } - a _ { 3 } X + a _ { 4 } = \prod _ { i = 1 } ^ { 4 } ( X - \alpha _ { i } )
$$

with $a _ { i } \in F$ , F a field, $\alpha _ { i } \in K = F ( \alpha _ { 1 } , . . . , \alpha _ { 4 } )$ , the splitting field. Put

$$
\beta _ { 1 } = \alpha _ { 1 } \alpha _ { 2 } + \alpha _ { 3 } \alpha _ { 4 } , \beta _ { 2 } = \alpha _ { 1 } \alpha _ { 3 } + \alpha _ { 2 } \alpha _ { 4 } , \beta _ { 3 } = \alpha _ { 1 } \alpha _ { 4 } + \alpha _ { 2 } \alpha _ { 3 } ,
$$

and let :

$$
\begin{array} { l c l } { { g ( X ) } } & { { = } } & { { ( X - \beta _ { 1 } ) ( X - \beta _ { 2 } ) ( X - \beta _ { 3 } ) } } \\ { { } } & { { = } } & { { X ^ { 3 } - a _ { 2 } X ^ { 2 } + ( a _ { 1 } a _ { 3 } - 4 a _ { 4 } ) X + ( a _ { 1 } ^ { 2 } a _ { 4 } + a _ { 3 } ^ { 2 } - 4 a _ { 2 } a _ { 4 } ) } } \end{array}
$$

be the “cubic resolvent” of $f .$ . Prove that $d _ { f } = d _ { g }$ (discriminants). Suppose $d _ { f } \neq 0$ and char $F \neq 2$ when necessary. Assume also that $f ( X )$ has no root in $F .$

(a) Show that f has a quadratic factor in $F [ X ]$ if and only if, for some $i ,$

$\beta _ { i } \in F$ and both $a _ { 1 } ^ { 2 } - 4 a _ { 2 } + 4 \beta _ { i }$ and $\beta _ { i } ^ { 2 } - 4 a _ { 4 }$ are squares in F .

(b) $G _ { f } = S _ { 4 } \iff g$ has no root in F and $d _ { f }$ not a square in $F ; G _ { f } = A _ { 4 } \iff g$ has no root in $F$ and $d _ { f }$ is a square in $F _ { \mathbf { \alpha } }$

Suppose from now $o n ,$ that $f$ is irreducible in $F [ X ]$ and $g$ has a root, say $\beta _ { 1 }$ , in $F$ .

(c) Show that $G _ { f }$ is a group of order a power of 2, so is contained in a 2-Sylow subgroup of $S _ { 4 }$

(d) Show $G _ { f } = V \stackrel { \mathrm { d e f n } } { = } \{ ( 1 ) , ( 1 2 ) ( 3 4 ) , ( 1 3 ) ( 2 4 ) , ( 1 4 ) ( 2 3 ) \}$ if and only if $g$ has three roots in $f ,$ if and only if $d _ { f }$ is a square in $F .$

(e) Suppose $G _ { f }$ has exactly one root in F . Show that $G _ { f }$ is cyclic of order 4, or is dihedral of order 8, and give a criterion to decide which.

(f) Find $G _ { f } \mathrm { ^ { * } s }$ for the following five quartic $f \mathrm { ^ { \prime } s }$

(i) $x ^ { \dot { 4 } } + x ^ { 3 } + x ^ { 2 } + x + 1 ;$

(ii) $x ^ { 4 } + x + 1 ;$

(iii) $x ^ { 4 } + 2 ;$

(iv) $x ^ { 4 } + 8 x + 1 2 ;$

(v) $x ^ { 4 } - 2 x ^ { 2 } + 9 .$

## October 29, 1985

(1) Let $f ( X ) \in \mathbb { Z } [ X ]$ be an irreducible quintic. We have seen in class that its group, $G _ { f }$ , has order 120, 60, 20, 10 or 5, being isomorphic to $S _ { 5 } , A _ { 5 } .$ , or to the group of permutations of $\mathbb { F } _ { 5 }$ of the form $x \mapsto a x + b$ for $b \in \mathbb { F } _ { 5 }$ and for $a \in \mathbb { F } _ { 5 } ^ { \times }$ , or $a = \pm 1$ , or $a = 1$ . For $i = { 0 , 1 , 2 , 3 , 5 }$ , let $\mathcal { P } _ { i }$ denote the set of prime numbers p such that the congruence $f ( X ) \equiv 0 { \bmod { p } }$ has exactly i incongruent solutions mod p. Assuming the Tschebotaroff density theorem, make a table giving, for each of the five possible $\boldsymbol { G } _ { f } { } ^ { \prime } \mathrm { s }$ , the density of $\mathcal { P } _ { i }$ in that case. For example, the density of $\mathcal { P } _ { 5 } \mathrm { i s } \frac { 1 } { 1 2 0 } , \frac { 1 } { 6 0 } , \frac { 1 } { 2 0 } ,$ ${ \frac { 1 } { 1 0 } } \ \mathrm { { o r } } \ { \frac { 1 } { 5 } } ,$ i.e., is $| G _ { f } | ^ { - 1 }$ in each case.

(2) Consider the polynomials $A ( X ) = X ^ { 5 } - X ^ { 3 } - 2 X ^ { 2 } - 2 X - 1 , B ( X ) = X ^ { 5 } - X + 3 .$ $C ( X ) = X ^ { 5 } + X ^ { 4 } - 4 X ^ { 3 } - 3 X ^ { 2 } + 3 X + 1 , D ( X ) = X ^ { 5 } - 5 , E ( X ) = X ^ { 5 } + 1 0 X ^ { 3 } - 1 0 X + 1 1 , C ( X ) = X ^ { 5 } - 5 , E ( X ) = X ^ { 5 }$ $1 0 X ^ { 2 } + 3 5 X - 1 8$ . Each of these five is irreducible. Their discriminants are : $d _ { A } = 4 7 ^ { 2 } , d _ { B } = 2 5 2 8 6 9 \ ( \mathrm { p r i m e } ) , d _ { C } = 1 1 ^ { 4 } , d _ { D } = 5 ^ { 9 } , d _ { E } = 2 ^ { 6 } 5 ^ { 8 } 1 1 ^ { 1 2 }$ . The following is a table, produced in about 25 hours of running time by my Macintosh, giving for each polynomial the number of primes in $\mathcal { P } _ { i }$ (cf. Problem 1) among the first 360 primes. (Thus, the sum of each row is 360).

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0 roots</td><td rowspan=1 colspan=1>1 root</td><td rowspan=1 colspan=1>2 roots</td><td rowspan=1 colspan=1>3 roots</td><td rowspan=1 colspan=1>5 roots</td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>147</td><td rowspan=1 colspan=1>180</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1> $\overline { { 1  p = 4 7 } }$ </td><td rowspan=1 colspan=1>32</td></tr><tr><td rowspan=1 colspan=1>B</td><td rowspan=1 colspan=1>143</td><td rowspan=1 colspan=1>131</td><td rowspan=1 colspan=1>58</td><td rowspan=1 colspan=1>27</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>288</td><td rowspan=1 colspan=1>1 $\overline { { ( p = 1 1 ) } }$ </td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>71</td></tr><tr><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>78</td><td rowspan=1 colspan=1>272</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=1>142</td><td rowspan=1 colspan=1>88</td><td rowspan=1 colspan=1>128</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>2</td></tr></table>

The primes among the first 360 which are in ${ \mathcal { P } } _ { 5 } .$ , i.e., for which f (X ) splits in $\mathbb { F } _ { p }$ are in each case as follows :

A : p = 83, 191, 197, 269, 439, 487, 523, 619, 761, 823, 907, 947,

977, 1193, 1277, 1319, 1447, 1481, 1499, 1579, 1693, 1709, 1741,

1811, 1861, 1867, 2053, 2213, 2221, 2273, 2339, 2351.

B : just p = 1609.

C : all primes p ≡ ±1( mod 11), i.e., p = 23, 43, 67, 89, . . . ,

2287, 2309, 2311, 2333, 2377, 2399.

D : p = 31, 191, 251, 271, 601, 641, 761, 1091, 1861, 2381.

E : just p = 2063 and 2213.

Armed with all this information (you don’t really need much of it), and using the simple form of $D ( X )$ , determine the groups $G _ { B } , G _ { E }$ and $G _ { D }$ . What are the only possibilities for $G _ { A }$ and $G _ { C } ?$ Which of these possibilities do you guess is the correct one?

(3) Guess what the splitting field of $G _ { C }$ is. Try to prove your guess by guessing the element α in that field whose minimal polynomial is $C ( X )$

(4) To prove your guess for $G _ { A }$ is not so easy without a clue. To show it by brute force, let α be a root of $A ( X )$ and check that in $\mathbb { Z } [ \alpha ] [ X ]$ , we have :

$$
A ( X ) = ( X - \alpha ) ( X ^ { 2 } - c _ { 1 } X + c _ { 2 } ) ( X ^ { 2 } - d _ { 1 } X + d _ { 2 } ) ,
$$

where

$$
\begin{array} { c } { { c _ { 1 } = 2 \alpha ^ { 4 } - \alpha ^ { 3 } - 2 \alpha ^ { 2 } - 3 \alpha - 2 , d _ { 1 } = - 2 \alpha ^ { 4 } + \alpha ^ { 3 } + 2 \alpha ^ { 2 } + 2 \alpha + 2 , } } \\ { { { } } } \\ { { c _ { 2 } = - \alpha ^ { 4 } + \alpha ^ { 3 } + \alpha ^ { 2 } + \alpha , d _ { 2 } = - \alpha ^ { 4 } + \alpha ^ { 3 } + 2 \alpha + 1 . } } \end{array}
$$

Please don’t hand in your verification of this. But answer the following : What is the quadratic field contained in the splitting field of $A ( X ) ?$

(1) Let $F \subset K$ be finite fields. Prove that $N _ { K / F } : K ^ { \times } \to F ^ { \times }$ is surjective.

(2) Let F be the fraction field of an integral domain A. Prove that A is integrally closed (in $F ) \iff A$ has the following property : if $f ( X )$ and $g ( X ) \in F [ X ]$ are monic and $f ( X ) \cdot g ( X ) \in A [ X ]$ , then $f ( X )$ and $g ( X ) \in A [ X ]$

(3) Let $F = \mathbb { Q } ( i )$ and $K = F ( 2 ^ { \frac { 1 } { 4 } } , i ^ { \frac { 1 } { 4 } } )$ , where $2 ^ { \frac { 1 } { 4 } }$ is the positive fourth root of 2 and $i ^ { \frac { 1 } { 4 } } ~ = ~ e ^ { \frac { 2 \pi i } { 1 6 } }$ Determine $\operatorname { G a l } ( K / F )$ . Is $K / \mathbb { Q }$ Galois, and if so, what is its Galois group?

(4) (a) A ring of the form $\mathbb { Z } [ \alpha ]$ has at most two homomorphisms into √ $\mathbb { F } _ { 2 }$ . Why?

(b) Let A be the integral closure of $\mathbb { Z }$ in the field $\mathbb { Q } ( { \sqrt { - 7 } } , { \sqrt { 1 7 } } )$ . Find a Z-base for A (cf. class discussion on October 31).

(c) Show that A has four distinct homomorphisms into $\mathbb { F } _ { 2 }$ (and consequently there does not exist $\alpha \in A$ such that $A = \mathbb { Z } [ \alpha ] )$

(5) Find three integers $a , b , c$ such that $\mathbb { Q } ( e ^ { \frac { 2 \pi i } { 4 } } ) = \mathbb { Q } ( { \sqrt { a } } , { \sqrt { b } } , { \sqrt { c } } )$

(6) (a) Prove that R has no non-trivial automorphism (hint : show that an automorphism of R is order-preserving automatically).

(b) Show that the only automorphisms of C which commute with complex conjugation are the identity and complex conjugation.√ √ √ √ √

(7) Let $\alpha = ( 2 + { \sqrt { 2 } } ) ( 3 + { \sqrt { 3 } } ) = - { \sqrt { 6 } } ( 1 + { \sqrt { 2 } } ) ( 1 + { \sqrt { 3 } } )$ and let $\theta = \sqrt { - \alpha } = i \sqrt { \alpha }$ . Show $\mathbb { Q } ( \theta ) / \mathbb { Q }$ is Galois of degree 8. Determine the structure of $G = { \mathrm { G a l } } ( \mathbb { Q } ( \theta ) / \mathbb { Q } )$ , and explain why $\mathbb { Q } ( \theta )$ is not the splitting field of any polynomial of degree $< 8$

(8) Suppose $\left[ F : \mathbb { Q } \right]$ is odd. Prove that −1 is not a sum of squares of elements of $F _ { \mathbf { \alpha } }$

(9) Suppose F is a field of characteristic $p > 0$ . The map $x \mapsto x ^ { p } - x$ is a homomorphism of the additive group of F into itself with kernel $\mathbb { F } _ { p } .$ Suppose $a \in F$ is not in the image, i.e., suppose the polynomial $f ( X ) = X ^ { p } - \dot { X } - a$ has no root in F . Show that the splitting field of $f ( X )$ is cyclic of degree p over $F$

(1) Let e be an idempotent $( e ^ { 2 } = e )$ in a local ring A (a ring with a unique maximal ideal). Show that $e = 0$ or 1.

(2) Suppose A is integrally closed in its fraction field F . Prove that the same is true for A[X] (polynomial ring). (Suggestion : $F [ X ]$ is integrally closed, being a PID).

(3) (a) Show that an order B in a quadratic extension of Q is of the form $B = \mathbb { Z } [ \alpha ] =$ $\mathbb { Z } + \mathbb { Z } \alpha$ , where α is a root of an irreducible monic quadratic polynomial $f ( X ) =$ $X ^ { 2 } + r X + s \in \mathbb { Z } [ X ]$

(b) For each such polynomial f, let $d _ { f } = r ^ { 2 } - 4$ s and $B _ { f } = \mathbb { Z } [ \alpha ] = \mathbb { Z } [ \alpha , \beta ]$ where α and β are the complex (or real) roots of f. Let g be another irreducible monic quadratic polynomial in $\mathbb { Z } [ X ]$ . Show

$$
B _ { g } \subset B _ { f } \iff d _ { f } \boxed { \vphantom { \boxplus } } d _ { g } ,
$$

where a  b means by definition that $b = m ^ { 2 } a$ , for some $m \in \mathbb { Z } ,$ , and when that is the case, show that the additive group $B _ { f } / B _ { g }$ is cyclic of order $m .$ , where $d _ { q } = m ^ { 2 } d _ { f }$

(c) Thus, $B _ { g } = B _ { f } \iff d _ { f } = d _ { g }$ Show that the integers d which occur as discriminants of quadaratic orders, i.e., the integers d of the form $d _ { f }$ for some $f$ as above, are those $d \equiv 0 \ \mathrm { { o r } \ 1 }$ (mod 4) such that d is not a perfect square.

(d) Show that $B _ { f }$ is integrally closed if and only if

$$
d \mathbb { D } d _ { f } , d \equiv 0 \mathrm { ~ o r ~ } 1 \mathrm { ~ m o d ~ } 4 \Rightarrow d = d _ { f } ,
$$

and then the other orders in $\mathbb { Q } ( B _ { f } )$ are the $B _ { g } \mathrm { ^ { * } s }$ such that $d _ { f } \boxed { \parallel } d _ { g }$ (e) Suppose f and g are as in (d), say $d _ { g } = m ^ { 2 } d _ { f }$ . Show for each prime number p such that $p \mid d _ { g }$ that there is a unique prime ideal P of $B _ { g }$ such that $p \in P .$ , and that $\begin{array} { r } { B _ { g } = \mathbf { \check { P } } + \mathbf { \check { Z } } } \end{array}$ , i.e., $B _ { g } / P \cong \mathbb { F } _ { p }$ . Show $P ^ { 2 } = p B _ { g } { \mathrm { ~ i f ~ } } { p } { \mathrm { ~ / ~ } } m , P ^ { 2 } = p P$ if $p \mid m$

(1) Let k be a field, $\mathbb { M } _ { 2 } ( k )$ the ring of $2 \times 2$ matrices $\left[ \begin{array} { l l } { a } & { b } \\ { c } & { d } \end{array} \right]$ with $a , b , c , d \in k$ , and let A be the subring of all such matrices with $c = 0$ . The maps $\varphi _ { 1 } : { \bigg [ } { a b } { \bigg ] } \mapsto a$ and $\varphi _ { 2 } : \left\lceil { a b \atop c d } \right\rceil \mapsto $ d are homomorphisms of A onto k. Let $P _ { j } = \mathrm { K e r } \varphi _ { j }$ for $j = 1 , 2$ Since dim $\overset { \vartriangle } { \boldsymbol { k } } \boldsymbol { A } = 3 < \infty$ , A is of finite length as a left A-module.

(a) Show that $A / P _ { 1 }$ and $A / P _ { 2 }$ are the only simple A-modules (up to isomorphism).

(b) Compute $P _ { 1 } ^ { 2 } , P _ { 1 } P _ { 2 } , P _ { 2 } P _ { 1 } , P _ { 2 } ^ { 2 }$ and $P _ { 1 } \cap P _ { 2 }$ . Are these the only two sided ideals of A (besides (0) and A)? What are the left ideals?

(c) What are the multiplicities of $A / P _ { 1 }$ and $A / P _ { 2 }$ in the left A-module A?

(d) Show that A is not isomorphic to the direct product of two non-zero rings.

<table><tr><td> $f _ { 1 } ( X ) = X ^ { 3 } + X ^ { 2 } + 7 X - 8 ,$   $\equiv ( X - 6 ) ( X + 5 ) ( X + 2 ) { \pmod { 1 3 } }$  and is irreducible mod 17, 19 and 29</td><td> ${ \overline { { f _ { 2 } ( X ) = X ^ { 3 } - 8 X + 1 5 } } }$   $\equiv ( X + 4 ) ( X + 6 ) ( X + 7 ) { \pmod { 1 7 } }$  irred. mod 13, 29, 29</td></tr><tr><td> $\overline { { f _ { 3 } ( X ) = X ^ { 3 } + X ^ { 2 } - 7 X + 1 2 } }$   $\equiv ( X - 8 ) ( X + 8 ) ( X + 1 ) { \pmod { 1 9 } }$  irred. mod 13, 17, 29</td><td> $\overline { { f _ { 4 } ( X ) = X ^ { 3 } + 1 0 X + 1 } }$   $\equiv ( X - 2 ) ( X - 3 ) ( X - 5 ) { \pmod { 2 9 } }$  irred. mod 13, 17, 19</td></tr></table>

Each of the four polynomials has discriminant −4027, a prime. Nevertheless, the fields $\mathbb { Q } ( \alpha _ { i } )$ , αi a root of $f _ { i } ( X )$ , are pairwise non-isomorphic. Why?

(3) Suppose $f ( X )$ is a monic cubic with coefficients in a finite field k, and suppose the discriminant of $f$ is not a square in k. Prove that $f ( X )$ is the product of a linear polynomial and an irreducible quadratic polynomial in $k [ X ]$ . Now explain why we didn’t give congruences mod $p = 2 , 3 , 5 , 7$ , 11 and 23 in problem 2 (there is an arrow to the ‘Why?’ question of problem 2).

(4) Let k be a field (C or R if you wish) and let $f ( X , Y )$ be an irreducible polynomial in two variables over k, i.e., a prime element in the U. F. D. $k [ X , Y ]$ Let $A =$ $k [ X , Y ] / ( f )$ Then A is Noetherian (Tate writes ‘noetherian’), and the nonzero prime ideals of A are maximal. Can you show this? Anyway, taking that for granted, let $( x _ { 0 } , y _ { 0 } ) \in k \times k$ be a point on the curve $f ( X , Y ) = 0 .$ , i.e., be such that $f ( x _ { 0 } , y _ { 0 } ) = 0$ and let P be the corresponding maximal ideal of $A ,$ consisting of the polynomials $p ( X , Y )$ such that $p ( x _ { 0 } , y _ { 0 } ) = 0$ , modulo $( f )$ . Prove that $P$ is an invertible ideal in A if and only if the point $( x _ { 0 } , y _ { 0 } )$ is a “non-singular” point of the curve, in the sense that not both partial derivatives $\frac { \partial f } { \partial x }$ and $\frac { \breve { \partial } f } { \partial y }$ vanish at $( x _ { 0 } , y _ { 0 } )$ . (Suggestion : Note that the translation $( X , Y ) \mapsto ( X - x _ { 0 } , Y - y _ { 0 } )$ , which is an automorphism of $k [ X , Y ]$ , allows you to assume $( x _ { 0 } , y _ { 0 } ) = ( 0 , 0 )$ without loss of generality).

(5) Let a and b be positive integers such that ab is square free $> 1$ , and let $E = \mathbb { Q } ( { \sqrt [ { 3 } ] { a b ^ { 2 } } } )$ Let $\alpha = \sqrt [ 3 ] { a b ^ { 2 } }$ , and $\beta = \sqrt [ 3 ] { a ^ { 2 } b } = a b / \alpha$ Show that if $a ^ { 2 } \not = b ^ { 2 }$ (mod 9), then the integral closure of Z in E is $\mathbb { Z } + \mathbb { Z } \alpha + \mathbb { Z } \beta$ , and the discriminant of the field E is $- 2 7 a ^ { 2 } b ^ { 2 }$ . What if $a ^ { 2 } \equiv b ^ { 2 } ( { \mathrm { m o d } } \ 9 ) ?$

## X7 − 7X + 3

(I) Suppose $f ( X ) \in \mathbb { Z } [ X ]$ is monic irreducible of degree 7, has a square discriminant, and has exactly three real roots. Prove that $G _ { f }$ is isomorphic either to $\boldsymbol { A } _ { 7 }$ or to the group $G _ { 1 6 8 } = \mathrm { G L } ( 3 , \mathbb { F } _ { 2 } ) \approx \mathrm { P S L } ( 2 , \mathbb { F } _ { 7 } )$ . Note that $G _ { 1 6 8 }$ is isomorphic to a subgroup of ${ \cal S } _ { 7 } ,$ in fact of $\boldsymbol { A } _ { 7 }$ , via the action of $G _ { 1 6 8 } = \mathrm { G L _ { 3 } ( F _ { 2 } ) }$ on the 7 non-zero vectors in $\mathbb { F } _ { 2 } ^ { 3 }$

(By considering Sylow subgroups, especially the ones for 7, this can be done from scratch without too much trouble. But it is even easier if you know that the only non-abelian simple groups of order $< 1 0 0 0$ are $A _ { 5 }$ of order $6 0 = 2 ^ { 2 } \cdot 3 \cdot 5 , G _ { 1 6 8 }$ of order $1 6 8 = 2 ^ { 3 } \cdot 3 \cdot 7 , \mathcal { A } _ { 6 }$ of order $3 6 0 = 2 ^ { 3 } \cdot 3 ^ { 2 } \cdot 5$ 7 $\mathrm { P S L } ( 2 , \mathbb { F } _ { 8 } )$ of order $5 0 4 = 2 ^ { 3 } \cdot 3 ^ { 2 } \cdot 7 .$ PSL $( 2 , \mathbb { F } _ { 1 1 } )$ of order $6 6 0 = 2 ^ { 2 } \cdot 3 \cdot 5 \cdot 1 1 )$

(II) Let $f ( X ) = X ^ { 7 } - 7 X + 3$ (shown me by Mr. Elkies). It is easy to check that $f ( X )$ satisfies the conditions of (I). For example, $d _ { f } = 3 ^ { 8 } \cdot 7 ^ { 8 }$ . Moreover, out of the first 360 primes :

$$
p = 2 , 3 , 5 , 7 , . . . , 2 4 2 3 :
$$

• f (X) has no root (mod p) for 104 $p \mathrm { { ^ { \circ } s } ; }$

• f (X) has 1 root (mod p) for 214 p’s;

• f (X) has 3 roots (mod p) for 41 p’s;

$f ( X )$ has 7 roots (mod p) for 1 p (namely $p = 1 8 7 9 )$ ;

Is $G _ { f } = G _ { 1 6 8 } , \mathrm { o r } \ A _ { 7 } { \mathrm { ? } }$

Newton Formulas, Discriminant

$$
f ( X ) = X ^ { n } - a _ { 1 } X ^ { n - 1 } + a _ { 2 } X ^ { n - 2 } - \cdots + ( - 1 ) ^ { n } a _ { n } = ( X - \alpha _ { 1 } ) ( X - \alpha _ { 2 } ) \dots ( X - \alpha _ { n } ) .
$$

Here $a _ { \nu } = \sum \alpha _ { i _ { 1 } } \alpha _ { i _ { 2 } } \ldots \alpha _ { i _ { \nu } }$ . Put $S _ { \nu } = \sum _ { i } \alpha _ { i } ^ { \nu } .$ i1<i2<···<iν

Then :

$$
S _ { 1 } - a _ { 1 } = 0 .
$$

$$
\begin{array} { r } { S _ { 2 } - a _ { 1 } S _ { 1 } + 2 a _ { 2 } = 0 . } \end{array}
$$

$$
\begin{array} { r } { S _ { 3 } - a _ { 1 } S _ { 2 } + a _ { 2 } S _ { 1 } - 3 a _ { 3 } = 0 . } \end{array}
$$

$$
S _ { n } - a _ { 1 } S _ { n - 1 } + \cdot \cdot \cdot \pm a _ { n } S _ { 0 } = 0 .
$$

$$
S _ { m } - a _ { 1 } S _ { m - 1 } + \cdot \cdot \cdot \pm a _ { n } S _ { m - n } = 0 , m \geq n .
$$

Proof. Write :

$$
\prod _ { i = 1 } ^ { n } ( 1 - \alpha _ { i } t ) = 1 - a _ { 1 } t + a _ { 2 } t ^ { 2 } - \cdot \cdot \cdot = \sum _ { \nu \geq 0 } ( - 1 ) ^ { \nu } a _ { \nu } t ^ { \nu } .
$$

Take the logarithmic derivative formally :

$$
\sum _ { i } { \frac { - \alpha _ { i } } { 1 - \alpha _ { i } t } } = - \sum _ { i , \nu } \alpha _ { i } ^ { \nu + 1 } t ^ { \nu } = - \sum _ { \nu } S _ { \nu + 1 } t ^ { \nu } = { \frac { - a _ { 1 } + 2 a _ { 2 } t - 3 a _ { 3 } t ^ { 2 } + \dots } { 1 - a _ { 1 } t + a _ { 2 } t ^ { 2 } - a _ { 3 } t ^ { 3 } + \dots } } ,
$$

cross-multiply and compare coefficients of $t ^ { \nu }$

Solving for $S _ { n }$ we get for $n \leq 4$

$$
S _ { 4 } = a _ { 1 } ^ { 4 } - 4 a _ { 1 } ^ { 2 } a _ { 2 } + 2 a _ { 2 } ^ { 2 } + 4 a _ { 1 } a _ { 3 } - 4 a _ { 4 } .
$$

$$
S _ { 3 } = a _ { 1 } ^ { 3 } - 3 a _ { 1 } a _ { 2 } + 3 a _ { 3 } .
$$

$$
S _ { 2 } = a _ { 1 } ^ { 2 } - 2 a _ { 2 } .
$$

$$
S _ { 1 } = a _ { 1 } .
$$

$$
S _ { 0 } = n .
$$

Further, the discriminant $d _ { f }$ of $f ( X )$ is

$$
\begin{array} { r l } & { - d _ { j } - \prod ( | \partial _ { x } \boldsymbol { \sigma } _ { j }   } \\ & {   - \partial _ { j } \boldsymbol { \hat { \sigma } } _ { j } ) ^ { 2 } - ( - 1 ) ^ { \frac { 1 } { 2 } \frac { \partial \sigma _ { j } } { 2 } } | \prod ( \partial _ { x } \boldsymbol { \sigma } _ { j } - \partial _ { z } ) - ( - 1 ) ^ { \frac { 1 } { 2 } \frac { \partial \sigma _ { j } } { 2 } } | \prod ^ { j } ( \partial _ { z } \boldsymbol { \sigma } _ { j } ) } \\ & { + d _ { j } ^ { - 1 } } \\ & { = \operatorname { l i d t } ^ { 2 } [ \begin{array} { l l l l l } { 1 } & { \hat { \sigma } _ { j } } & { \hat { \sigma } _ { j } ^ { 1 } } & { \cdots } & {  \partial _ { z } ^ { 1 - n } | } \\ { 1 } & { \hat { \sigma } _ { j } } & { \hat { \sigma } _ { j } ^ { 2 } } & { \cdots } & {  \partial _ { z } ^ { 1 - n } | } \\ { 1 } & { \hat { \sigma } _ { j } } & { \cdots } & {  \partial _ { z } ^ { 1 } } & { \cdots } \\ { 1 } & { \hat { \sigma } _ { j } } & { \cdots } & {  \partial _ { z } ^ { 1 } } & { \cdots } \end{array} ] } \\ &  = \operatorname { l i d t } ( [ \begin{array} { l l l l l } { 1 } & { 1 } & { 1 } & { - \sigma _ { j } } & { 1 } \\ { \sigma _ { j } ^ { 2 } } & { \sigma _ { j } ^ { 2 } } & { \cdots } & { \sigma _ { j } ^ { 2 } } & { 1 } \\ { \sigma _ { j } ^ { 2 } } & { \sigma _ { j } ^ { 2 } } & { \cdots } & { \sigma _ { j } ^ { 2 - n } } & { 1 } \\ { \sigma _ { j } ^ { 2 } } & { \sigma _ { j } ^ { 2 } } & { \cdots } &  \sigma _ { j } ^   \end{array} \end{array}
$$

This last can also be written :

$$
d _ { f } = ( - 1 ) ^ { \frac { n ( n - 1 ) } { 2 } } R ( f , f ^ { \prime } ) ,
$$

where R is the resultant; cf. Lang page 211 (Ch $\mathrm { V } , \{ 1 0 \}$

Example : For $f ( X ) = X ^ { n } + p X + q$ , we have $( - 1 ) ^ { \frac { n ( n - 1 ) } { 2 } } d _ { f } = n ^ { n } q ^ { n - 1 } + ( 1 - n ) ^ { n - 1 } p ^ { n }$ , as can be seen by writing $- \alpha _ { j } f ^ { \prime } ( \alpha _ { j } ) = n q - ( 1 - n ) p \alpha _ { j }$ and multiplying over $j$ .

## Examples of prime ideals

(1) Let A be a u.f.d. (unique factorization domain, e.g., $A = \mathbb { Z } [ x _ { 1 } , \dots , x _ { n } ]$ or $A =$ $K [ x _ { 1 } , \ldots , x _ { n } ]$ , K a field) and let π be a prime element in A. Show :

(a) The principal ideal $\pi A$ is a prime ideal.

(b) Every nonzero prime ideal contains one of the form $\pi A$

(c) The ideals of the form $\pi A$ are the minimal elements in the set of nonzero prime ideals, ordered by inclusion, and they are the only nonzero principal prime ideals.

(2) Let A be a p.i.d. (principal ideal domain, e.g., $A = \mathbb { Z }$ or $A = K [ X ]$ , K a field). Then the ideals of the form $\pi A$ are maximal, and are the only non-zero prime ideals of A.

(3) Let B be an integral domain with field of fractions K. Let $A = B [ X ]$ and let P be a prime ideal of A; then $P \cap B$ is a prime ideal in B.

<!-- image-->

(a) If $P \cap B = ( 0 )$ , show :

(i) $P K = P ( K [ X ] )$ is a prime ideal in $A K = K [ X ]$

(ii) $P = P K \cap A$

(iii) If B is a u.f.d., then either $P = ( 0 )$ , or $P = f ( X ) A$ , where $f ( X )$ is a polynomial with coefficients in B, these coefficients having $^ { 6 } \mathrm { n o } ^ { \prime }$ common divisor (i.e., none except units in B), and $f ( X )$ being irreducible in K[X]. Moreover f is determined by P up to a unit (invertible element) of B.

(b) If $P \cap B = M$ , a maximal ideal of B, then, making the identification $A / M A =$ $B [ X ] / M B [ X ] \approx ( B / M ) [ X ] = k [ X ]$ , where $k = B / M$ , we see that P/M A is a prime ideal in $k [ X ]$ . Hence show : either $P = M A$ , or $P = M A + g ( x ) A$ , where $g ( X )$ is a polynomial with coefficients in B such that the polynomial ${ \overline { { g } } } ( X )$ which we obtain by reducing the coefficients of g (mod M) is an irreducible polynomial in $k [ X ]$ . Moreover g is determined by P up to multiplication by an element of B not in M and addition of a polynomial whose coefficients are in M .

(4) Apply (3) to the case where B is a p.i.d., and show that the prime ideals P of A are of the following distinct types :

(I) $P = ( 0 )$

(II) $P = f ( X ) A$ , where f is as in 3.a.iii.

(III) $P = \pi A , \pi \mathrm { ~ a ~ }$ prime element of B.

(IV) $P = \pi ^ { * } A + g ( X ) , \pi ^ { * }$ a prime element of B, and g as in 3b, with $M = \pi B$ The ideals of type IV are maximal and are not principal. The ideals of type IV which contain a given πA of type III are those for which $\pi ^ { * } \sim \pi$ , i.e., $\pi ^ { * } B = \pi B$

The ideals of type IV which contain a given $f ( X ) A$ of type II are those for which ${ \overline { { g } } } ( X )$ divides ${ \overline { { f } } } ( X )$ in $k [ X ]$ , where $k = B / \pi ^ { * } B$ and where $\overline { { g } }$ and $\overline { { f } }$ denote the polynomials obtained from $g$ and f by reducing their coeffients $( \mathrm { m o d } \ \pi ^ { * } )$ ; hence no ideal of type II is maximal unless B has only a finite number of maximal ideals, say $\pi _ { 1 } B , \pi _ { 2 } B , \dots , \pi _ { m } B$ , in which case, the ideals of type II generated by $f ( X )$ of the form $f ( X ) = 1 + \pi _ { 1 } \pi _ { 2 } \dots \pi _ { m } X h ( X )$ , with $h ( X ) \in B ( X )$ are maximal (because for every $\pi _ { i }$ we have $\bar { f } = f ( \mathrm { m o d } ~ \pi _ { i } ) - 1 !$

(5) If C is the field of complex numbers (or any algebraically closed field), apply (4) to $B = \mathbb { C } [ Y ]$ to show that the prime ideals $P$ in the ring $A = \mathbb { C } [ X , Y ]$ are of three distinct types :

(I) $P = ( 0 )$

(II) and (III) $P = f ( X , Y ) A$ where $f ( X , Y )$ is an irreducible polynomial in two variables with complex coefficients, uniquely determined by $P$ up to a nonzero constant factor.

(IV) $P = ( X - x _ { 0 } ) A + ( Y - y _ { 0 } ) A$ , where $x _ { 0 }$ and $y _ { 0 }$ are complex numbers uniquely determined by $P .$

The only maximal ideals are those of type IV, and the ideals of type IV containing a given $f ( X , Y ) A$ are those for which $f ( x _ { 0 } , y _ { 0 } ) = 0$

(6) Let $A = \mathbb { C } [ X , Y , Z ]$ . What are the minimal non-zero prime ideals of A? Try to prove that the only maximal ideals of A are those of the form $( X - x _ { 0 } , Y - y _ { 0 } , Z - z _ { 0 } )$ (special case of Hilbert’s Nullstellensatz). The prime ideals of A which are neither maximal nor minimal nonzero are harder to describe. One such is $P = ( X , Y )$ . But not all of them can be generated by two elements. For example, let $\varphi : A \to \mathbb { C } [ T ]$ be the homomorphism defined by $\bar { \varphi } ( f ( X , Y , Z ) ) = f ( T ^ { 3 } , T ^ { 4 } , \bar { T } ^ { 5 } )$ , and let $P$ be the kernel of $\varphi .$ . Try to show that $P$ is generated by the three elements $Y ^ { 2 } - X Z , X ^ { 3 } -$ $Y Z , Z ^ { 2 } - X ^ { 2 } Y$ , but on the other hand, P cannot be generated by two elements.

(7) Let M be a maximal ideal in a ring B and let $A = B / M ^ { n }$ for some integer $n > 0$ Show that the only prime ideal of A is $M / M ^ { n }$

Examples: $A = \mathbb { Z } / 1 0 2 4 \mathbb { Z } , A = \mathbb { C } [ X ] / X ^ { n } \mathbb { C } [ X ]$

(8) Let A be the ring of power series $c _ { 0 } + c _ { 1 } z + c _ { 2 } z ^ { 2 } + . .$ . with complex coefficients $c _ { i }$ which have a nonzero radius of convergence (ring of germs of analytic functions at the origin $z = 0$ in the complex z-plane). Discuss the prime ideals in $A .$ . Do the same for the ring of formal power series $\dot { \boldsymbol { A } } = \boldsymbol { K } [ [ \boldsymbol { z } ] ]$ in one variable z over any field.

(9) Let E be a compact Hausdorff topological space. Let A be the ring of all continuous real valued functions on $E .$ . For each $x \in E$ , let $M ( x )$ be the maximal ideal of $A$ consisting of the functions $f \in A$ such that $f ( x ) = 0 \ ( \mathrm { i . e . , } \ M ( x ) \ =$ Kernel of the homomorphism $f \ \sim \ f ( x ) )$ . Prove that the map $x \ \sim \ M ( x )$ is a homeomorphism of $E$ onto the maximal ideal spectrum of $A .$ (You may use the well-known lemma which states that, given two disjoint closed subsets of $E$ (in particular two distinct points of $E )$ , there exists a continuous real valued function on $E$ taking the value 0 on one of the sets and the value 1 on the other - if you don’t like too much abstraction, take E to be the closed interval [0, 1] on the real line.) (Hint : the only hard part is to show that every maximal ideal M of A is of the form $M ( x )$ for some $x \in E$ . To do this, suppose the contrary. Then for every $x \in E$ there exists a function $f _ { x } \in \mathcal { M }$ , but with $f _ { x } ( x ) \neq 0$ . Show that if you replace $f _ { x }$ by $g _ { x } f _ { x }$ with a suitable $g _ { x } ,$ , you can assume $f _ { x } \in \mathcal { M }$ , and $f _ { x } ( y ) = 1$ for all y in some neighborhood $U _ { x }$ of x. Now these $U _ { x }$ cover E, so already a finite number $U _ { x _ { 1 } } , U _ { x _ { 2 } } , \dotsc , U _ { x _ { n } }$ cover E etc.).