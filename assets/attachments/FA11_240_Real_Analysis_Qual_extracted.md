## MATH 240 QUALIFYING EXAM: FALL 2011

Instructions: Please answer all 5 questions. Partial credit will be given, so you should attempt all problems. You may quote any standard proposition/theorem from Folland or Lieb-Loss, but not the homeworks. If you use a major result like MCT etc, you need to state the theorem you are using explicitly. In this exam dx is integration with respect to Lebesgue measure, and |E| denotes the Lebesgue measure of E.

I) a) (10 pts) Let $E \subseteq [ 0 , 1 ]$ be Lebesgue measurable. Suppose there exists a fixed $\epsilon > 0$ such that $| E \cap ( a , b ) | \geqslant \epsilon | a - b |$ for all intervals $( a , b ) \subseteq [ 0 , 1 ]$ . Show that one must have $| E | = 1$

b) (10 pts) Give an example of a Lebesgue measurable set $E \subseteq [ 0 , 1 ]$ with $0 < | E | < 1$ and $| E \cap ( a , b ) | > 0$ for all nontrivial intervals $( a , b ) \subseteq [ 0 , 1 ]$ . Explain why this example does not contradict part a) above.

II) a) (10 pts) Let X be an infinite dimensional Banach space. Prove that X endowed with the the weak topology is not a complete metric space. (Hint: Begin by showing that any norm bounded set in X is nowhere dense in the weak topology.)

b) (10 pts) Let X be a Banach space and $X ^ { * }$ its dual. Suppose that there exists countably many linear functionals $L _ { n } \in X ^ { * }$ with the following property: Any sequence $x _ { j } , x \in X$ converges weakly $x _ { j } \to x$ iff $L _ { n } ( x _ { j } )  L _ { n } ( x )$ for all n. Show that X must be finite dimensional. (Hint: Consider the function $\begin{array} { r } { d ( x , y ) = \sum _ { n } 2 ^ { - n } \frac { | L _ { n } ( x - y ) | } { 1 + | L _ { n } ( x - y ) | } . \ d ) \ d y } \end{array}$

III) a) $( 1 5 \ \mathrm { p t s } )$ Let $( X , { \mathcal { M } } , \mu )$ be a finite measure space. Suppose that $f _ { n } ~ \in ~ L ^ { 1 } ( d \mu )$ is a sequence of functions with the property that for every $\epsilon > 0$ there exists a $\delta > 0$ such that for all $E \in { \mathcal { M } } \colon$

$$
| E | ~ < ~ \delta ~ \Longrightarrow ~ \operatorname* { s u p } _ { n } \int _ { E } | f _ { n } | d \mu ~ < ~ \epsilon ~ .
$$

Suppose in addition that there exists f with $f _ { n } \to f \mu { \mathrm { - a . e . } }$ .. Show that $f _ { n }  f$ in $L ^ { 1 } ( d \mu )$

b) (5 pts) Give a simple example to show that if one drops the finite measure assumption but keeps all the other hypotheses above, the conclusion can fail.

IV) (20 pts) Let $K \in L ^ { 1 } ( \mathbb { R } ^ { d } )$ with Lebesgue measure. Suppose that $\psi _ { n } \in L ^ { 2 } ( \mathbb { R } ^ { d } )$ is a sequence of functions such that $\psi _ { n }  \psi$ (weak $L ^ { 2 }$ convergence), and also with the property that $\psi _ { n } \equiv 0$ in $| x | > 1$ . Show that $\begin{array} { r } { f _ { n } ( x ) = \int _ { \mathbb { R } ^ { d } } K ( x - y ) \psi _ { n } ( y ) d y } \end{array}$ converges to $\begin{array} { r } { f ( x ) = \int _ { \mathbb { R } ^ { d } } K ( x - y ) \psi ( y ) d y } \end{array}$ strongly in $L ^ { 2 } ( \mathbb { R } ^ { d } )$

V) (20 pts) Let $f : \mathbb { R } \to \mathbb { R }$ be a 2π periodic function, i.e. $f ( x ) = f ( x + 2 \pi )$ , such that there exists $C > 0$ (possibly large) and $\epsilon > 0$ (possibly small) with $| f ( x ) - f ( y ) | \leqslant C | x - y | ^ { \frac { 1 } { 2 } + \epsilon }$ Show that the Fourier series of f converges uniformly. (Hint: Half credit will be given for the special case $\begin{array} { r } { \epsilon = \frac { 1 } { 2 } } \end{array}$ , which can be treated more directly. For the general case try computing $\begin{array} { r } { \int _ { 0 } ^ { 2 \pi } | f ( x + h ) - f ( x ) | ^ { 2 } d x } \end{array}$ two different ways.)