Do the following exercises from Chapter 3 of the text (Pages 174–181): 8, 9, 17, 29, 43, 47

8. Show that $\mathbb { Q }$ is a torsion-free Z-module that is not free.

I Solution. $\mathbb { Q }$ is torsion free as a Z module since $\mathbb { Q }$ is a field that contains $\mathbb { Z }$ as a submodule. Specifically, if m $\neq 0 \in \mathbb { Z }$ and $r \in \mathbb { Q }$ with $m r = 0$ , then $m \neq 0$ as an element of $\mathbb { Q }$ and $r = ( 1 / m ) ( m r ) = 0$ . Thus $\mathbb { Q }$ is torsion-free as a Z-module.

To see that $\mathbb { Q }$ is not free as a Z-module, simply note that if $S \subseteq \mathbb { Q }$ is any subset consisting of more than one element, then S is not Z-linearly independent. To see this, suppose that $r / s$ and $t / u$ are two distinct elements of S. Then

$$
( s t ) \frac { r } { s } - ( u r ) \frac { t } { u } = 0
$$

is a nontrivial Z-linear dependence relation between $r / s$ and $t / u ,$ so $S$ is not Z-linearly independent if it contains at least 2 elements. If $S = \{ r / s \}$ is a subset of $\mathbb { Q }$ containing exactly one element, then S does not generate $\mathbb { Q }$ as a $\mathbb { Z }$ -module. To see this, observe that $1 / 2 s$ cannot be written as an integer multiple of $r / s .$ , since, if this were possible then we would have $1 / 2 s = m ( r / s )$ for some $m \in \mathbb { Z }$ which would give the equation in integers $1 = 2 m r$ , which is not possible. J

9. (a) Let R be an integral domain, let M be a torsion R-module, and let N be a torsion-free R-module. Show that Hom $\iota _ { R } ( M , N ) = \langle 0 \rangle$

I Solution. Let $f \in { \mathrm { H o m } } _ { R } ( M , N )$ and let $m \in M$ . Since M is a torsion module, there is an $r \ne 0 \in R$ with $r m = 0$ . Then $0 = f ( 0 ) = f ( r m ) = r f ( m )$ . Since $r \neq 0$ and N is torsion-free, this implies that $f ( m ) = 0$ . Since $m \in M$ is arbitrary, this gives $f = 0$ , as required. J

(b) If $n = k m$ , then show that Hom $\mathbb { Z } _ { n } ( \mathbb { Z } _ { m } , \mathbb { Z } _ { n } ) \cong \mathbb { Z } _ { m }$

I Solution. Define a map $\varphi : \operatorname { H o m } _ { \mathbb { Z } _ { n } } ( \mathbb { Z } _ { m } , \mathbb { Z } _ { n } ) \to \mathbb { Z } _ { n } { \mathrm { ~ b y ~ } } \varphi ( f ) = f ( 1 )$ . This is a $\mathbb { Z } _ { n ^ { - } } { \bmod { \mathrm { u l e } } }$ homomorphism from the definition of sum and scalar multiplication of functions. If $f ( 1 ) = 0$ then $f ( r ) = r f ( 1 ) = 0$ for all $r \in \mathbb { Z } _ { m }$ so $\operatorname { K e r } ( \varphi ) = \langle 0 \rangle$ If $t \in \mathbb { Z } _ { n }$ is in the image of $\varphi _ { ; }$ then $t = f ( 1 )$ for some $f \in { \mathrm { { H o m } } } _ { \mathbb { Z } _ { n } } ( \mathbb { Z } _ { m } , \mathbb { Z } _ { n } )$ Then $m t = m f ( 1 ) = f ( m ) = f ( 0 ) = 0$ , so the order of t divides m. Conversely, any element of $\mathbb { Z } _ { n }$ whose order divides m is $f ( 1 )$ for some $f \in { \mathrm { H o m } } _ { \mathbb { Z } _ { n } } ( \mathbb { Z } _ { m } , \mathbb { Z } _ { n } )$ Thus, the image of $\varphi$ consists of all elements of $\mathbb { Z } _ { n }$ whose order divides m, i.e., Im $. ( \varphi ) = \langle k \rangle \cong \mathbb { Z } _ { m }$ J

17. Give examples of short exact sequences of R-modules

$$
0 \longrightarrow M _ { 1 } \longrightarrow M \longrightarrow M \longrightarrow M _ { 2 } \longrightarrow 0
$$

and

$$
0 \xrightarrow [ ] { } N _ { 1 } \xrightarrow [ ] { \psi } N \xrightarrow [ ] { \psi ^ { \prime } } N _ { 2 } \xrightarrow [ ] { } 0
$$

such that

(a) $M _ { 1 } \cong N _ { 1 } , M \cong N , M _ { 2 } \cong N _ { 2 }$

I Solution. For $n \in \mathbb { N }$ , consider the short exact sequence

$$
\left( * _ { n } \right)
$$

$$
0 \longrightarrow \mathbb { Z } \xrightarrow { \phi _ { n } } \mathbb { Z } \xrightarrow { \pi } \mathbb { Z } _ { n } \xrightarrow { } 0
$$

where $\phi _ { n } ( x ) = n x$ and $\pi$ is the standard projection map. Then choosing any two natural numbers n 6= m will give two short exact sequences $\left( * _ { n } \right)$ and $\left( * _ { m } \right)$ with the first two terms equal in each sequence, the third terms $\mathbb { Z } _ { n } \not \cong \mathbb { Z } _ { m }$ J

(b) $M _ { 1 } \cong N _ { 1 } , M \not \cong N , M _ { 2 } \cong N _ { 2 } ;$

I Solution. For this part, you can use the two short exact sequences from Example 3.8, Page 122:

$$
0 \xrightarrow [ ] { } \mathbb { Z } _ { p } \xrightarrow [ ] { \phi } \mathbb { Z } _ { p q } \xrightarrow [ ] { \psi } \mathbb { Z } _ { p } \xrightarrow [ ] { } 0
$$

and

$$
0 \xrightarrow [ ] { } \mathbb { Z } _ { p } \xrightarrow [ ] { f } \mathbb { Z } _ { p ^ { 2 } } \xrightarrow [ ] { g } \mathbb { Z } _ { p } \xrightarrow [ ] { } 0 ,
$$

where p and q are distinct primes, $\phi ( m ) = q m \in \mathbb { Z } _ { p q } , \ f ( m ) = p m \in \mathbb { Z } _ { p ^ { 2 } }$ and ψ and g are the canonical projection maps. J

(c) $M _ { 1 } \cong N _ { 1 } , M \cong N , M _ { 2 } \cong N _ { 2 } .$

I Solution. Let M be the Z-module consisting of sequences of elements from the field $\mathbb { Z } _ { 2 }$ . That is,

$$
M = \left\{ \left( a _ { 0 } , a _ { 1 } , a _ { 2 } , \ldots \right) : a _ { j } \in \mathbb { Z } _ { 2 } \right\} .
$$

For each natural number $n \in \mathbb { N }$ define a map $\psi _ { n } : M \to M$ by

$$
\psi _ { n } ( a _ { 0 } , a _ { 1 } , a _ { 2 } , . . . ) = ( a _ { n } , a _ { n + 1 } , a _ { n + 2 } , . . . ) .
$$

It is clear that $\psi _ { n }$ is a Z-module homomorphism and that it is surjective. Moreover, if $n \geq 1$ b,

$$
\mathrm { K e r } ( \psi _ { n } ) = \{ ( a _ { 0 } , a _ { 1 } , \ldots , a _ { n - 1 } , 0 , \ldots ) : a _ { j } \in \mathbb { Z } _ { 2 } \} \cong \mathbb { Z } _ { 2 } ^ { n } .
$$

Thus, for each $n \in \mathbb { N }$ there is a short exact sequence

$$
0 \xrightarrow [ ] { } \mathbb { Z } _ { 2 } ^ { n } \xrightarrow [ ] { \phi _ { n } } M \xrightarrow [ ] { \psi _ { n } } M \xrightarrow [ ] { } 0\tag{∗n}
$$

where

$$
\phi _ { n } ( a _ { 0 } , \ldots , a _ { n - 1 } ) = ( a _ { 0 } , a _ { 1 } , \ldots , a _ { n - 1 } , 0 , \ldots ) .
$$

Since $\mathbb { Z } _ { 2 } ^ { n } \not \cong \mathbb { Z } _ { 2 } ^ { m }$ if $m \neq n$ , the short exact sequences $\left( * _ { n } \right)$ and $\left( * _ { m } \right)$ for $m \neq n$ give the required example. J

29. Let $R = \mathbb { Z } _ { 3 0 }$ and let $A \in M _ { 2 , 3 } ( R )$ be the matrix

$$
A = { \left[ \begin{array} { l l l } { 1 } & { 1 } & { - 1 } \\ { 0 } & { 2 } & { 3 } \end{array} \right] } .
$$

Show that the two rows of A are linearly independent over $R ,$ but that any two of the three columns are linearly dependent over R.

I Solution. As far as the rows are concerned, suppose there is an R-linear dependence relation

$$
r \left[ 1 \quad 1 \quad - 1 \right] + s \left[ 0 \quad 2 \quad 3 \right] = \left[ 0 \quad 0 \quad 0 \right] .
$$

This implies that $r = 0$ which then says that $2 s = 0$ and $3 s = 0$ so that $s = 3 s - 2 s = 0$ Thus the rows are linearly independent over R. As for the columns, note that

$$
1 5 \left[ 0 \right] + 1 5 \left[ 1 ^ { 1 } \right] = \left[ 0 \right] ; \quad 1 0 \left[ 1 ^ { 1 } \right] + 1 0 \left[ { - 1 } ^ { 1 } \right] = \left[ 0 \right] ; { \mathrm { ~ a n d ~ } } 6 \left[ 1 ^ { 1 } \right] + 6 \left[ { - 1 } ^ { - 1 } \right] = \left[ 0 \right] .
$$

Thus, any two of the three columns are R-linearly dependent.

43. Suppose R is a PID and $M = R \langle x \rangle$ is a cyclic R-module with $\mathrm { A n n } ( x ) = \langle a \rangle \neq \langle 0 \rangle$ Show that if N is a submodule of M , then N is cylic with Ann $N = \left. b \right.$ where b is a divisor of a. Conversely, show that M has a unique submodule N with annihilator hbi for each divisor b of a.

I Solution. Define an R-module homomorphism $\varphi : R  M$ by $\varphi ( r ) = r x$ . Since M is cyclic with generator x, $\varphi$ is surjective and $\operatorname { K e r } ( \varphi ) = \operatorname { A n n } ( x ) = \langle a \rangle$ . By the first isomorphism theorem for R-modules, there is an isomorphism $\overline { { \varphi } } : R / \langle a \rangle \to M$ and by the correspondence theorem, $\varphi$ provides a one-to-one correspondence between the submodules of M and the submodules of R containing hai, with the submodule N corresponding to $\varphi ^ { - 1 } ( N )$ . But R is a PID so R-submodules of R are just principal ideals. Thus $\varphi ^ { - 1 } ( N ) = \langle c \rangle \supseteq \langle a \rangle$ , so that $N = \varphi ( \langle c \rangle ) = \{ r ( c x ) : r \in R \}$ . Then the annihilator of N is

$$
\mathrm { A n n } ( N ) = \{ r \in R : r ( c x ) = 0 \} = \{ r \in R : a | r c \} = \langle \frac { a } { c } \rangle .
$$

Thus, the annihilator of N is generated by the divisor $b = a / c$ of $a .$ . Conversely, if b is any divisor of a, then the submodule $N \ = \ \langle ( a / b ) x \rangle \ \subset \ M$ is a submodule with $\mathrm { A n n } ( N ) = \langle b \rangle$ Therefore, the pairing $b \longleftrightarrow \langle ( a / b ) x \rangle$ sets up a one-to-one correspondence between divisors of a and submodules of N. J

47. Let $u = ( a , b ) \in \mathbb { Z } ^ { 2 }$

(a) Show that there is a basis of $\mathbb { Z } ^ { 2 }$ containing u if and only if a and b are relatively prime.

I Solution. Suppose that $v = ( c , d )$ and that the two vectors u and v form a basis of $\mathbb { Z } ^ { 2 }$ . Then there are integers k, l, m and n such that

$$
\begin{array} { r c l } { { k u + l v } } & { { = } } & { { ( 1 , 0 ) } } \\ { { m u + n v } } & { { = } } & { { ( 0 , 1 ) , } } \end{array}
$$

which gives the matrix equation

$$
{ \left[ \begin{array} { l l } { a } & { c } \\ { b } & { d } \end{array} \right] } { \left[ \begin{array} { l l } { k } & { m } \\ { l } & { n } \end{array} \right] } = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] } .
$$

Taking determinants then gives $( a d - b c ) ( k n - m l ) = 1$ . Since this is an equation in integers, it follows that $a d - b c = \pm 1$ so that a and b are relatively prime.

Conversely, if a and b are relatively prime, then we can write $r a + s b = 1$ and we claim that $u = ( a , b )$ and $v = ( - s , r )$ form a basis of $\mathbb { Z } ^ { 2 }$ . Consider the linear equation

$$
x u + y v = ( \alpha , \beta )
$$

in integers. This is equivalent to the matrix equation

$$
{ \left[ \begin{array} { l l } { a } & { - s } \\ { b } & { r } \end{array} \right] } { \left[ \begin{array} { l } { x } \\ { y } \end{array} \right] } = { \left[ \begin{array} { l } { \alpha } \\ { \beta } \end{array} \right] } .
$$

Multiplying this equation on the left by the matrix $\left[ \begin{array} { l l } { r } & { s } \\ { - b } & { a } \end{array} \right]$ gives

$$
\left[ x \atop y \right] = \left[ { r \atop b } s \right] \left[ { \alpha \atop \beta } \right] = \left[ { r \alpha + s \beta \atop - b \alpha + a \beta } \right] .
$$

This equation shows that u and v is a linearly independent generating set for $\mathbb { Z } ^ { 2 } .$ i.e., a basis. J

(b) Suppose that $u = ( 5 , 1 2 )$ . Find $\mathrm { ~ a ~ } v \in \mathbb { Z } ^ { 2 }$ such that $\{ u , u \}$ is a basis of $\mathbb { Z } ^ { 2 }$

I Solution. Since $5 \cdot 5 + ( - 2 ) \cdot 1 2 = 1$ , the calculation done in part (a) shows that we can take $v = ( 2 , 5 )$ J