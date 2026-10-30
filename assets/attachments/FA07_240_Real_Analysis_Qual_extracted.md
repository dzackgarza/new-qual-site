September 11, 2007

## Qualifying Exam in Real Analysis

Instructions. You may use without proof anything which is proved in the text by Folland or in the notes on distributions, unless otherwise stated. Either state the theorem by name, if it has one, or say what the theorem says. However, you must reprove items which were given as exercises. Unless indicated otherwise, $( . \mathrm { { Y } } , \mathcal { M } , \mu )$ is a measure space. Also, m denotes Lebesgue measure.

1. (70 pts.) True or false. For each part, determine if it is always true or sometines false. If true give a brief proof. If false give a counterexample or disprove it. No credit if reason is missing or incorrect. It's OK to be brief here.

(a) If $f : \mathbb { R } \to \mathbb { R }$ is continuous with $f \in L ^ { 1 } ( \mathbb { R } , m )$ , then $\scriptstyle \operatorname* { l i m } _ { x \to \infty } f ( x ) = 0$ (b) If $f : \mathbb { R } \to \mathbb { R }$ is a continuously differentiable function with $f , f ^ { \prime } \in L ^ { 1 } ( \mathbb { R } , m )$ , then $\begin{array} { r } { \operatorname* { l i m } _ { x \to \infty } f ( x ) = 0 . } \end{array}$

(c) If $\left\{ f _ { n } \right\}$ is a sequence of Lebesgue integrable functions on $[ 0 , 1 ]$ such that $f _ { n }$ converges to 0 in $L ^ { 1 } ( [ 0 , 1 ] , m )$ , then there exists a Lebesgue measurable set $E \subset \{ 0 , 1 \}$ with $m ( E ) > 0$ such that $\scriptstyle \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x ) = 0$ for all $x \in E$

(d) If X and y are Banach spaces and $T : \mathcal { X }  \mathcal { Y }$ is a linear mapping for which $f \circ T \in { \mathcal { X } } ^ { \ast }$ for all $f \in \mathcal { V } ^ { * }$ , then T is bounded.

() If $\alpha > 0$ and $\left\{ f _ { n } \right\}$ a sequence of functions on [0, 1] for which

$$
| f _ { n } ( x ) - f _ { n } ( y ) | \leq | x - y | ^ { \alpha } { \mathrm { ~ a n d ~ } } f _ { n } ( 0 ) = 0 \forall n , \forall x , y \in [ 0 , 1 ] ,
$$

then there exists a subsequence $\{ f _ { n _ { j } } \}$ that converges uniformly on [0, 1].

2. (20 pts.) Recall that a measure µ is semifinite if for any $E \in { \mathcal { M } }$ with $\mu ( E ) = \infty$ , there exists $F \in { \mathcal { M } }$ with $F \subset E$ and $0 < \mu ( F ) < \infty$ . Show that $\operatorname { i f } \mu$ is semifinite, then for any $E \in { \mathcal { M } }$

$$
\mu ( E ) = \operatorname* { s u p } \{ \mu ( F ) : F \in { \mathcal { M } } , \ F \subset E , \ \mu ( F ) < \infty \} .
$$

3. (30 pts.) Let $f \in L ^ { 1 } ( \mathbb { R } )$ and put

$$
g ( \xi ) : = \int _ { \mathbb { R } } e ^ { i \xi \cos x } f ( x ) d x , \quad \xi \in \mathbb { R } .
$$

(a) Show that g is continuous on R.

(b) Show that g is infinitely differentiable on R (i.e. $g \in C ^ { \infty } ( \mathbb { R } ) )$

(c) Show that the sequence $\{ g ^ { ( n ) } ( \xi ) \}$ converges uniformly to 0 on R, where $g ^ { ( n ) } ( \xi )$ denotes the nth derivative of g.

4. (30 pts.) Let X be a normed space and $\mathcal { X } ^ { \ast }$ its dual space.

(a) Define the weak topology and the weak\* topology on $\mathcal { X } ^ { \ast }$

(b) State and prove Alaoglu's Theorem.

5. (25 pts.) For $a \in \mathbb { R }$ , let $f _ { a }$ be the function on R defined by $f _ { a } ( x ) : = e ^ { i a x }$ (a) Show that $f _ { a }$ is a tempered distribution on R.

(b) Find the Fourier transform of $f _ { a }$

6. (25 pts.) Let C be a coilection of open balls in $\mathbb { R } ^ { n }$ , and let $U = \textstyle \bigcup _ { B \in { \mathcal { C } } } B$ Prove that if $c < \eta \eta ( U )$ , then there exist disjoint balls $B _ { 1 } , \ldots , B _ { k }$ in C such that ${ \textstyle \sum _ { 1 } ^ { k } m ( B _ { k } ) > 3 ^ { - n } c }$ . [This statement is proved in Folland, but you are being asked to give a proof here.]