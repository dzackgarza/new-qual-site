# ANALYSIS QUALIFYING EXAM: FALL 2017

Ten of the twelve problems will be counted for the total score, at least four from Problems 1–6, and at least four from Problems $_ { 7 - 1 2 }$ . To pass the exam, you have to show sufficient competence in both real and complex analysis. Please indicate on the front of your exam which ten problems you wish to have graded.

Throughout the exam the notation $\mathbb { D } = \left\{ z \in \mathbb { C } : | z | < 1 \right\}$ is used.

Problem 1. Suppose $f \colon  { \mathbb { R } } \to  { \mathbb { R } }$ is non-decreasing; specifically, for $x , y \in \mathbb { R }$ we have the implication

$$
x \leq y \implies f ( x ) \leq f ( y ) .
$$

Show that if $A \subset \mathbb { R }$ is a Borel set, then so is $f ( A ) = \{ f ( x ) : x \in A \}$

Problem 2. Let $\left\{ f _ { n } \right\}$ denote a bounded sequence in $L ^ { 2 } ( [ 0 , 1 ] )$ . Suppose the sequence $\{ f _ { n } \}$ also converges almost everywhere. Show that then $\{ f _ { n } \}$ converges in the weak topology on $L ^ { 2 } ( [ 0 , 1 ] )$

Problem 3. Let $\{ \mu _ { n } \}$ denote a sequence of Borel probability measures on R. For $n \in \mathbb { N }$ and $x \in \mathbb { R }$ we define

$$
F _ { n } ( x ) : = \mu _ { n } { \big ( } ( - \infty , x ] { \big ) } .
$$

Suppose the sequence $\{ F _ { n } \}$ converges uniformly on R. Show that then for every bounded continuous function $f : \mathbb { R } \to$ R the numbers

$$
\int _ { \mathbb { R } } f ( x ) d \mu _ { n } ( x )
$$

converge as $n \to \infty$

Problem 4. Consider the Banach space $V = C ( [ - 1 , 1 ] )$ of all real-valued continuous functions on $[ - 1 , 1 ]$ equipped with the supremum norm defined as

$$
\| f \| = \operatorname* { s u p } \{ | f ( x ) | : x \in [ - 1 , 1 ] \} \quad { \mathrm { f o r ~ } } f \in V .
$$

Let $B = \{ f \in V : \| f \| \leq 1 \}$ be the closed unit ball in V .

Show that there exists a bounded linear functional $\Lambda \colon V  \mathbb { R }$ such that $\Lambda ( B )$ is an open subset of R.

Problem 5. Suppose $f \colon  { \mathbb { R } } \to  { \mathbb { R } }$ is a bounded and measurable function satisfying $f ( x + 1 ) = f ( x )$ and $f ( 2 x ) = f ( x )$ for almost every $x \in$ R. Show that then there exists a constant $c \in \mathbb { R }$ such that $f ( x ) = c$ for almost every $x \in \mathbb { R }$

Problem 6. Let $f \in L ^ { 2 } ( \mathbb { C } )$ . For $z \in \mathbb { C }$ we define

$$
g ( z ) = \int _ { \{ w \in \mathbb { C } : | w - z | \leq 1 \} } { \frac { | f ( w ) | } { | w - z | } } d A ( w ) ,
$$

where dA denotes integration with respect to Lebesgue measure on $\mathbb { C } \cong \mathbb { R } ^ { 2 }$ . Show that then $| g ( z ) | < \infty$ for almost every $z \in \mathbb { C }$ and that $g \in L ^ { 2 } ( \mathbb { C } )$

Problem 7. Prove that there exists a meromorphic function f on C with the following three properties:

(i) $f ( z ) = 0$ if and only ${ \mathrm { i f ~ } } z \in \mathbb { Z } ,$

(ii) $f ( z ) = \infty$ if and only if $z - { \frac { 1 } { 3 } } \in \mathbb { Z } ,$

(iii) $| f ( x + i y ) | \leq 1$ for all $x \in \mathbb { R }$ and all $y \in \mathbb R$ with $| y | \geq 1$

Problem 8. Show that a harmonic function $u : \mathbb { D }  \mathbb { R }$ is uniformly continuous if and only if it admits the representation

$$
u ( z ) = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \mathrm { R e } \Big ( \frac { e ^ { i \theta } + z } { e ^ { i \theta } - z } \Big ) f ( e ^ { i \theta } ) d \theta , \quad z \in \mathbb { D } ,
$$

with $f \colon \partial \mathbb { D } \to \mathbb { R }$ continuous.

Problem 9. Consider a map $F \colon \mathbb { C } \times \mathbb { C } \to \mathbb { C }$ with the following properties:

(i) For each fixed $z \in \mathbb { C }$ the map $w \mapsto F ( z , w )$ is injective.

(ii) For each fixed $w \in \mathbb { C }$ the map $z \mapsto F ( z , w )$ is holomorphic.

(iii) $F ( 0 , w ) = w$ for $w \in \mathbb { C }$

Show that then

$$
F ( z , w ) = a ( z ) w + b ( z )
$$

for $z , w \in \mathbb { C }$ , where a and b are entire functions with $a ( 0 ) = 1 , b ( 0 ) = 0$ , and $a ( z ) \neq 0$ for $z \in \mathbb { C } .$

Hint: Consider ${ \frac { F ( z , w ) - F ( z , 0 ) } { F ( z , 1 ) - F ( z , 0 ) } } .$

Problem 10. Let $\{ f _ { n } \}$ be a sequence of holomorphic functions on D with the property that

$$
F ( z ) : = \sum _ { n = 1 } ^ { \infty } | f _ { n } ( z ) | ^ { 2 } \leq 1
$$

for all $z \in \mathbb { D }$ . Show that the series defining $F ( z )$ converges uniformly on compact subsets of D and that F is subharmonic.

Problem 11. Let $f \colon \mathbb { D }  \mathbb { C }$ be an injective and holomorphic function with $f ( 0 ) =$ 0 and $f ^ { \prime } ( 0 ) = 1$ . Show that then

$$
\operatorname* { i n f } \{ | w | : w \notin f ( \mathbb { D } ) \} \leq 1
$$

with equality if and only if $f ( z ) = z { \mathrm { ~ f o r ~ a l l ~ } } z \in \mathbb { D } .$

Problem 12. Let $f , g ,$ and h be complex-valued functions defined on C with

$$
f = g \circ h .
$$

Show that if h is continuous, and both $f$ and $g$ are non-constant and holomorphic, then h is holomorphic as well.