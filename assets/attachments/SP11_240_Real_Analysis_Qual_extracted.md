# MATH 240 QUALIFYING EXAM: SPRING 2011

Instructions: Please answer all 5 questions. Partial credit will be given, so you should attempt all problems. You may quote any standard proposition/theorem from Folland or Lieb-Loss, but not the homeworks. If you use a major result like MCT etc, you need to state the theorem you are using explicitly. In this exam dx is integration with respect to Lebesgue measure, and $| E |$ denotes the Lebesgue measure of E.

I) True/False, Short Answer: Please answer True or False. You must support your claim with a short explanation or counterexample, but you need not give an entire proof:

a) (5 pts) If $T _ { n } \in { \mathcal { L } } ( X , Y )$ is a sequence of bounded linear operators with $X , Y$ are Banach spaces, then if $T x : = \operatorname* { l i m } _ { n } T _ { n } x$ exists in the Y norm for all $x \in X$ , one has $T \in { \mathcal { L } } ( X , Y )$

b) (5 pts) Let $( X , { \mathcal { M } } , \mu )$ be any measure space. If $f _ { n } , f \in L ^ { 1 } ( d \mu )$ are measurable functions such that $f _ { n } \to f \mu { \mathrm { - a . e . } }$ . and lim $\textstyle \int f _ { n } \to \int f ,$ then $f _ { n }  f$ in $L ^ { 1 } ( d \mu )$

c) (5 pts) If $\{ X _ { \alpha } \} _ { \alpha \in A }$ is any collection of compact Hausdorff topological spaces, then $E \subset \Pi _ { \alpha \in A } X _ { \alpha }$ with the product topology is compact iff it is closed.

d) (5 pts) If $f _ { n } \in L ^ { 2 } ( [ 0 , 1 ] )$ (Lebesgue measure) converge weakly to $f \in L ^ { 2 } ( [ 0 , 1 ] )$ , then there is a subsequence such that $f _ { n _ { k } }  f$ pointwise a.e. with respect to Lebesgue measure.

e) (5 pts) If µ is positive and finite Borel measure on $\mathbb { R } ^ { n }$ which is a.c. with respect to Lebesgue measure, then lim $_ { r  0 } \frac { \mu ( B _ { r } ( x ) ) } { | B _ { r } ( x ) | }  0$ for $\mathrm { a . e . ~ } x \in \mathbb { R } ^ { n }$ implies $\mu \equiv 0$ . Here $B _ { r } ( x )$ is the ball of radius r at x.

II) For each integer $k > 0$ denote by $\Delta _ { k } ( j ) = [ j 2 ^ { - k } , ( j + 1 ) 2 ^ { - k } ]$ where $j \in \mathbb Z$ , the dyadic rational interval of length $2 ^ { - k }$ starting at $j 2 ^ { - k }$ . Let $f \in L ^ { 1 } ( \mathbb { R } )$ , and define:

$$
A _ { k } ( f ) ( x ) = \sum _ { j } a _ { k } ( j ) { \bf 1 } _ { \Delta _ { k } ( j ) } ( x ) , \qquad a _ { k } ( j ) = \frac { 1 } { | \Delta _ { k } ( j ) | } \int _ { \Delta _ { k } ( j ) } f ( y ) d y .
$$

a) (5 pts) Prove that $\| A _ { k } f \| _ { L ^ { 1 } ( \mathbb { R } ) } \leqslant \| f \| _ { L ^ { 1 } ( \mathbb { R } ) }$ for all $k > 0 , f \in L ^ { 1 } ( \mathbb R )$

b) (10 pts) Show that if $f \in L ^ { 1 } ( \mathbb { R } )$ then $A _ { k } ( f ) \to f$ in $L ^ { 1 } ( \mathbb { R } )$ as $k \to \infty$ . (Hint: First try to show this when f is continuous and compactly supported).

III) (15 pts) Let $1 \leqslant p , p ^ { \prime } \leqslant \infty$ be fixed, with $p , p ^ { \prime }$ dual indices. Suppose $K ( x , y ) \geqslant 0$ is a Lebesgue measurable function on $\mathbb { R } ^ { n } \times \mathbb { R } ^ { n }$ such that there exists a constant $0 \leqslant K _ { 0 } < \infty$ with:

$$
\iint g ( x ) K ( x , y ) f ( y ) d x d y \leqslant K _ { 0 } \| g \| _ { L ^ { p ^ { \prime } } ( { \mathbb R } ^ { n } ) } \| f \| _ { L ^ { p } ( { \mathbb R } ^ { n } ) } ~ ,
$$

for all measurable $f , g \geqslant 0 \mathrm { o n } \mathbb { R } ^ { n }$ . Show that if $f \in L ^ { p } ( \mathbb { R } ^ { n } )$ , then the function $\begin{array} { r } { K f ( x ) : = \int _ { { \mathbb R } ^ { n } } K ( x , y ) f ( y ) d y } \end{array}$ is well defined for (Lebesgue) a.e. x ∈ Rn, and one has $\| K f \| _ { L ^ { p } ( d x ) } \leqslant K _ { 0 } \| f \| _ { L ^ { p } ( d x ) }$

IV) Let $( X , { \mathcal { M } } , \mu )$ be a finite measure space.

a) (10 pts) Let $1 \leqslant p \leqslant \infty$ Show that for fixed $M > 0$ the ball $\| f \| _ { L ^ { p } ( d \mu ) } \leqslant M$ is closed in $L ^ { 1 } ( d \mu )$ b) (10 pts) Show that the whole of $L ^ { p } ( d \mu )$ is closed in $L ^ { 1 } ( d \mu )$ iff there exists $C \ > \ 0$ such that $\| f \| _ { L ^ { p } ( d \mu ) } \leqslant C \| f \| _ { L ^ { 1 } ( d \mu ) }$ for all $f \in L ^ { p } ( d \mu )$

c) (10 pts) Now let $1 < p \leqslant \infty$ Show that the assumptions of part b) above holds iff both $L ^ { p } ( d \mu )$ and $L ^ { 1 } ( d \mu )$ are finite dimensional. (Hint: Show that if $( X , { \mathcal { M } } , \mu )$ is any measure space where there exists $0 < c , C < \infty$ such that $c \leqslant \mu ( E ) \leqslant C$ for every set $E \in { \mathcal { M } }$ of nonzero measure, then $L ^ { 1 } ( d \mu )$ is finite dimensional).

V) (15 pts) Let $f \in L ^ { 2 } ( [ 0 , 2 \pi ] )$ , and set $\begin{array} { r } { S _ { N } f ( x ) = \sum _ { n = - N } ^ { N } \hat { f } ( n ) e ^ { i n x } } \end{array}$ to be the $N ^ { t h }$ symmetric partial sum of its Fourier series. Here we are defining $\begin{array} { r } { \hat { f } ( n ) = ( 2 \pi ) ^ { - 1 } \int _ { 0 } ^ { 2 \pi } e ^ { - i n x } f ( x ) d x } \end{array}$ . Show that there exists a subsequence $N _ { k } \to \infty$ so that $S _ { N _ { k } } f  f$ a.e. with respect to Lebesgue measure in [0, 2π].