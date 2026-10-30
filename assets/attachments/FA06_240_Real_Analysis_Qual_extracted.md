MATH 240: Real Analysis Qualifying Exam. September 8, 2006

General instructions: 3 hours. No books or notes. Be sure to motivate all (nontrivial) claims and statements. You may use without proof any result prcved in the text. You need to reprove any result given as an exercise.

Notation: m = dx denotes the Lebesgue measure. $\left( X , { \mathcal { M } } , \mu \right)$ is a measure space.

1. (50p) Determine if the statements below are True or False. If True, give a brief proof. If False, give a counterexample (or prove your assertion in another way, if you prefer). If you claim an assertion follows from a theorem in the text, name the theorem (or describe it otherwise) and explain carefully how the conclusion follows.

(a) (10p) Let μ be a Borel measure on R (i.e. a measure defined on the Borel algebra of R) such that $\mu ( B ) < \infty$ for every bounded Borel set B. Let E be a Borel set and assume that $\mu ( K ^ { \prime } ) = 0$ for every compact set $\smash {  { F _ { \perp } } ^ { - } \subseteq E _ { \perp } ^ { } }$ Then $\mu ( E ) = 0$

(b) (10p) Let $f : \{ - 1 , 1 \} \pmod \mathbb { E }$ be continuous with $f ( 0 ) = 0$ For every $\epsilon > 0$ , there exists an integer n $\geq 1$ and continuous functions $u _ { j } \colon [ - 1 , 1 ] \longrightarrow \mathbb { E } , j = 1 , \ldots , n .$ such that $u _ { j } \{ x \} = 0$ only at $x = 0$ and

$$
\operatorname* { s u p } _ { x \in [ - 1 , 1 ) } | f ( x ) - \sum _ { j = 1 } ^ { n } u _ { j } ( x ) | < \epsilon .
$$

(c) (10p) Let v be a complex measure and µ a (positive) measure on $( X , { \mathcal { M } } )$ Suppose that $X ^ { \prime } = A \cup B$ with $A \cap B = \emptyset$ and $\nu ( A ) = 0$ Moreover, assume that there is a measurable function $f \colon B \to \mathbb { C }$ such that $\textstyle \nu ( E ) = \int _ { E } f d \mu$ for every measurable $E \subset B$ . Then there is a measurable function ${ \tilde { f } } \colon X \to \complement$ such that $\nu = \tilde { f } d \mu$

(d) (10p) Let $\left\{ f _ { \mathfrak { n } } \right\}$ be a sequence in $\tilde { L } ^ { 4 } ( \mathcal { X } , \mu )$ . Suppose that $\begin{array} { r } { \operatorname* { l i m } _ { \tau _ { \iota } \longrightarrow \infty } \int _ { X } f _ { n } g d \mu } \end{array}$ exists (as a complex number) for every $g \in \mathcal { L } ^ { 4 / 3 } ( . X , \mu )$ . Then there is $M > 0$ such that $| { \dot { | f _ { \pi } } } | { \dot { | } } _ { 4 } \leq M$ for every n = 1. 2.. . ..

(e) (10p) Let {fn} be a sequence in $\tilde { L } ^ { 4 } ( \tilde { \lambda _ { 3 } } , \mu )$ . Suppose that there is $M > 0$ such that $| | f _ { \pi } | | _ { 4 } \leq M$ for every $n = 1 . 2 \dots .$ Then there is a subsequence $\{ f _ { n _ { k } } \}$ such that $\begin{array} { r } { \operatorname* { l i m } _ { k \to \infty } \int _ { X } f _ { n _ { k } } g d \mu } \end{array}$ exists (as a complex number) for every $g \in \ L ^ { 4 / 5 } ( \ddot { X } , \mu )$

2. (30p) Recall that $f _ { n } \to f$ in measure if. for every $\epsilon > 0 , \mu ( \{ x : | f ( x ) - f _ { n } ( x ) | \geq$ }→0asn-x.Let $1 \leq p < \infty$

(a) (10p) Suppose $f _ { \pi }  f$ in $L ^ { \mathcal { P } } ( \boldsymbol { X } , \mu )$ . Show that $\hat { \bar { \rho } } _ { n }  \hat { f }$ in measure. (b) (20p) Suppose $f _ { n } \longrightarrow f$ in measure and $\lvert f _ { \pi } \rvert \leq g \mathrm { ~ a . } \Theta$ with $g \in [ \bar { \mathcal { P } } ( \bar { \mathcal { X } } , \bar { \mathcal { P } } )$ . Show that $f \in \mathcal { L } ^ { \mathfrak { p } } ( X , \mu )$ and $f _ { r _ { i } } \longrightarrow f$ in $\tilde { L } ^ { \mathcal { P } } ( \mathcal { X } , \mu )$

3. Let H be a Hilbert space. $T \colon { \mathcal { H } } \to { \mathcal { H } } ~ { \mathsf { a } }$ bounded linear operator. $T ^ { \star } \colon { \mathcal { H } } \longrightarrow { \mathcal { H } }$ its adjoint (i.e. $( T x , y ) = ( x , T ^ { \star } y )$ for all $x , y \in \mathcal { H } )$ , and $\mathcal { R } ( T ) , \mathcal { N } ( T )$ its range and nullspace, respectively.

(a) (15p) Show that $\mathcal { N } ( T ^ { \star } ) = \mathcal { R } ( T ) ^ { \bot }$ and $\overline { { \mathscr { R } ( T ^ { \star } ) } } = \mathcal { N } ( \underline { { T } } ) ^ { \perp }$

(b) (15p) Show that $\mathcal { R } ( T ^ { \star } )$ is closed if $\mathcal { R } ( T )$ is closed.

Hint for (b): Show that. for every $y \in { \mathcal { N } } ( T ) ^ { \downarrow }$ , there is a bounded linear functional $\Lambda \colon { \mathcal { R } } ( T ) \to \mathbb { C }$ with the property that $\Lambda T x \ = \ ( x , y )$ Use this to show that $\mathcal { N } ( T ) ^ { \perp } \subset \mathcal { R } ( T ^ { * } )$

4. Recall that a function $f \colon ( a , b ) \longrightarrow \mathbb { R } { \mathrm { ~ ( w i t h ~ } } - \infty \leq a < b \leq \infty { \mathrm { ) } }$ is called convex if

$$
\begin{array} { r l } { ( 1 ) \quad } & { f \big ( ( 1 - \lambda ) x + \lambda y \big ) \leq ( 1 - \lambda ) f ( x ) + \lambda f ( y ) , \quad \forall \lambda \in ( 0 , 1 ) , \ x , y \in ( a , b ) . } \end{array}
$$

(a) (15p) Show that f is convex if and only if for all $x , y , x ^ { \prime } , y ^ { \prime } \ \triangleq \ ( a , b )$ with $x \leq x ^ { \prime } < y ^ { \prime }$ and $x < y \le y ^ { \prime }$ 5

$$
\frac { f ( y ) - f ( x ) } { y - x } \leq \frac { f ( y ^ { \prime } ) - f ( x ^ { \prime } ) } { y ^ { \prime } - x ^ { \prime } } .\tag{2}
$$

(b) (15p) Show that f is convex if and only if f is absolutely continuous on every compact subinterval $\{ c , d \}$ of (a.b) and $f ^ { \prime }$ is increasing a.e.

Hint for (a): Interpret the two conditions (1) and (2) geometrically. Treat the two cases $x ^ { \prime } \leq y$ and $\mathcal { Y } < \mathfrak { x ^ { \prime } }$ separately when showing $\left( 1 \right) \Longrightarrow \left( 2 \right)$

## 5Consider the linear operator

$$
( T f ) ( y ) : = \int _ { 0 } ^ { \infty } \epsilon ^ { - x y } f ( x ) d x , \quad y > 0 .
$$

(a) (15p) Let $1 < p < \infty , 1 / p \div 1 / q = 1$ , and show that for nonnegative measurable functions $f , g \colon ( 0 , \infty ) \to \{ 0 , \infty )$

$$
\int _ { 0 } ^ { \infty } \int _ { 0 } ^ { \infty } \epsilon ^ { - x y } f ( x ) g ( y ) d x d y \leq C _ { p } \bigg ( \int _ { 0 } ^ { \infty } f ( x ) ^ { \varepsilon } x ^ { \nu - 2 } d x \bigg ) ^ { 1 / p } \bigg ( \int _ { 0 } ^ { \infty } g ( x ) ^ { q } d x \bigg ) ^ { 1 / q } ,
$$

where

$$
C _ { p } : = \int _ { 0 } ^ { \infty } \epsilon ^ { - z } x ^ { ( 1 - p ) / p } d x .
$$

(b) (15p) Show that the operator $\varup T$ is bounded on $\mathcal { L } ^ { 2 } ( ( 0 , \infty ) , \eta _ { \lambda } )$ and $\vdots \uparrow f \vdots \vdots 2 \leq$ $C _ { 2 } \} \} \} \{ \ f \} _ { 2 }$ where $C _ { 2 }$ is the constant in (a) with ${ \mathfrak { P } } = { \mathfrak { Z } } .$