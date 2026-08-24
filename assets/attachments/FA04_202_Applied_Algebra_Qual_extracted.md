# Algebra/Applied Aigebra Qualifying Exam

Part 1

September 10, 2004

(15) 1. State and prove the Cayley-Hamilton Theorem. (You may use the Schur Decomposition Theorem.)

(10) 2. (a) Showthat $a _ { 1 } , \cdots , a _ { n } \in \mathbb { R } ^ { m }$ are linearly independent over C iff they are linearly independent over R.

(b) Show that if $A \in M _ { \mathfrak { n } } ( \mathbb { R } )$ , then an eigenvalue λ of A is real iff it has a real corresponding eigenvector.

(15) 3. Let i be a least squares solution to $A x = b ;$ where $A \in M _ { m , n }$ and $m \geq n$ Let $A ^ { \dagger }$ be the pseudo-inverse of A. Use the Singular Value Decomposition to show that $\tilde { z } = A ^ { \dagger } b$ is the min 2- norm least squares solution to $A x = b , \mathrm { i . e . }$ , show

(a)i is a least squares solution,

(b) if  is a least square solution then $\| \hat { x } \| _ { 2 } \geq \| \tilde { x } \| _ { 2 }$ , and

c)i is unique.

Notation: $M _ { \pi , \pi } \equiv$ set of $m \times n$ complex matrices.

$M _ { \pi } \equiv { \sf s e t }$ of $\textstyle n \times n$ complex matrices.

$M _ { n } ( \mathbb { R } ) \equiv { \sf s e t }$ of $\pi \times \pi$ real matrices.

# Applied Algebra Qualifying Exam: Part III Fall 2004. September 10, 2004

as many problems as you can, but y o must atempt at least 1 problem from probiems 1-3, one probiem from  n  st  ps omThe poin val i au  hs pr  them Your final score will be scaled so that this part of the exam will represent 60% of your point total.

Let $N = \{ 0 , 1 , 2 , . . . \} , Z = \{ 0 , \pm 1 , \pm 2 , . . . \}$ , Q equal the rationals and C denote the complex numbers.

If $\lambda = ( \lambda _ { 1 } \geq \lambda _ { 2 } \geq . . . \geq \lambda _ { k } )$ is a partition of n, let $\ . \dot { - } \dot { } ^ { \lambda }$ denote the irreducible representation of the symmetric group $S _ { n }$ such that the Frobenius image of $\chi ^ { \dot { \mathbf { \varphi } } ^ { \dot { \mathbf { \varphi } } ^ { \dot { \mathbf { \varphi } } ^ { \dot { \mathbf { \varphi } } } } } } = \chi ^ { \dot { \mathbf { \varphi } } }$ is the Schur function $S _ { \lambda } ( x _ { 1 } , \dots , x _ { N } )$ where $\smash { \mathrm { ~ \textit ~ { ~ N ~ } ~ } > \pi }$

(20 pts.) (a) Prove that f G is fnite group and λ(x) is a lnear characerof G, then for any reducible character $\chi$ of $G ,$ the function $\chi ^ { \bullet }$ defined by $\chi ^ { \bullet } ( \sigma ) = \lambda ( \sigma ) \chi ( \sigma )$ for all $\sigma \in G$ is aiso an irreducible character of G.

(b) Let $A : G \to G L _ { n } ( \mathbf { C } )$ and ${ \cal B } : { \cal G }  { \cal G } L _ { n } ( { \bf C } )$ be two representations of a finite group G. Show that if for all $\sigma \in G$ , there exists a matrix $P ( \sigma )$ such that

$$
( P ( \sigma ) ) ^ { - 1 } A ( \sigma ) P ( \sigma ) = B ( \sigma ) ,
$$

then there exist a nonsingular matrix $T$ such that for all $\sigma ,$

$$
T ^ { - 1 } A ( \sigma ) T = B ( \sigma ) .
$$

40 pts.) Let $G = \{ g _ { 1 } , \dots , g _ { k } \}$ be a finite group. Introduce variables $x _ { g _ { 1 } } , \ldots , x _ { g _ { k } }$ and consider the $k \times k$ matrix

$$
\ X ^ { \prime } = \{ \pmb { x } _ { g _ { i } g _ { 2 } ^ { - 1 } } \} .
$$

Let $\begin{array} { r } { X = \sum _ { i = 1 } ^ { k } A ( g _ { i } ) x _ { g _ { i } } } \end{array}$ so that we can define a map $g _ { i }  A ( g _ { i } )$

(a) Show that A is the left regular representation of G.

(b) Show that

$$
d e t ( X ) = \prod _ { \nu = 1 } ^ { h } d e t ( \sum _ { g \in G } A ^ { ( \nu ) } ( g ) x _ { g } ) ^ { n _ { \nu } }
$$

where $A ^ { ( 1 ) } , \ldots , A ^ { ( h ) }$ are a complete set of representatives of the irreducible representations of G and $n _ { \nu } =$ $d i m ( A ^ { ( \nu ) } )$ for $\nu = 1 , \ldots , h$

cUse part (b) to show that

$$
d e t \left[ \begin{array} { c c c c c c } { x _ { 0 } } & { x _ { 1 } } & { x _ { 2 } } & { \dots } & { x _ { n - 1 } } \\ { x _ { n - 1 } } & { x _ { 0 } } & { x _ { 1 } } & { \dots } & { x _ { n - 2 } } \\ { x _ { n - 2 } } & { x _ { n - 1 } } & { x _ { 0 } } & { \dots } & { x _ { n - 3 } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots \ddots } & { \vdots } \\ { x _ { 1 } } & { x _ { 2 } } & { x _ { 3 } } & { \dots } & { x _ { 0 } } \end{array} \right] = \prod _ { \tau = 0 } ^ { n - 1 } ( x _ { 0 } + \epsilon ^ { \tau } x _ { 1 } + \epsilon ^ { 2 \tau } x _ { 2 } + \dots \epsilon ^ { ( n - 1 ) \tau } x _ { n - 1 } )
$$

where $\epsilon = e ^ { 2 \pi i / n }$

(3) $( 2 0 \ p \mathtt { t s . } )$ Given a partition λ of n, let l(λ) denote the number of parts of λ and $\lambda ^ { \prime }$ denote its conjugate partition. Let $\chi _ { \mu } ^ { \lambda }$ denote the value of the character of the irreducible representation $A ^ { \lambda }$ of $S _ { n }$ at the conjugacy class indexed by the partition µ. Show that $\chi _ { \mu } ^ { \lambda ^ { \prime } } = ( - 1 ) ^ { n - l ( \mu ) } \chi _ { \mu } ^ { \lambda }$