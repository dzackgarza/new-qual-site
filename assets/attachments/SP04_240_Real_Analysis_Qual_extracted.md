## 1. ANALYSIS QUALIFYING EXAM, SPRING 2004

Instructions: Clearly explain and justify your answers. You may cite theorems from textbooks or that were proved in class as lorg as they are not what the problem explicitly asks you to prove. You may also use the results of prior problems or prior parts of the same problem when solving a problem - this is allowed even if you were unable to prove the previous results. Make sure to state the results that you are using and be sure to verify their hypotheses. All problems have equal value.

Notation: Let m denote Lebesgue measure on $( \mathbb { R } , \mathbb { S } _ { \Xi } )$ and $( \xi , \mathcal { M } , \mu )$ denote a finite measure space. Also for a bounded measurable function, $f : \mathcal { X } \longrightarrow \mathbb { C } .$ let $M _ { f } : \bar { L } ^ { 2 } \left( \mu \right) \to \bar { L } ^ { 2 } \left( \mu \right)$ denote the multiplication operator, $M _ { f } h : = f h$ for all $h \in \bar { \mathcal { L } } ^ { 2 } \left( \mu \right)$

Exercise 1.1. In this problem $\left( { \cal { X } } , \| \cdot \| \right)$ is an infinite dimensional normed space. Determine which of the following statements are true. For the true statements give a brief reason and for the false statements give a counter example.

(a) If $A = \mathbb { R } \setminus E$ and $m ( { \cal E } ) = 0$ , then $\bar { \mathcal { A } } = \mathbb { R }$

(b) Every m - null set $\mathcal { E } \in \mathcal { B } _ { \mathbb { R } }$ is nowhere dense in R.

(c) Every proper subspace $E \subset X$ is nowhere dense.

(d) If E is a subspace of X with non-empty interior, then ${ \mathcal { E } } = { \mathcal { X } } .$

Exercise 1.2. Compute the values of the following two expressions. (You must justify your answers.).

(a)

$$
\sum _ { \pi = 0 } ^ { \infty } \int _ { 0 } ^ { \infty } { e ^ { - z x } \frac { ( - 1 ) ^ { n } } { ( 2 n + 1 ) ! } x ^ { 2 n + 1 } } \dot { a } x\tag{b}
$$

$$
\int _ { 0 } ^ { \infty } \left( \int _ { 0 } ^ { \infty } x ^ { 2 } e ^ { - z ^ { 2 } } \sin \left( x ^ { 2 } \right) e ^ { - y z } \dot { d } x \right) d y .
$$

You may find the following integration formula useful;

$$
\int e ^ { - a z } \sin { x } d x = - { \frac { 1 } { a ^ { 2 } + 1 } } e ^ { - a x } \left[ \cos { x } + a \sin { x } \right] + C .
$$

Exercise 1.3. Suppose that $\left\{ u _ { n } \right\} _ { n = 1 } ^ { \infty }$ is an orthonormal subset of Hilbert space, H, and S is a dense subset of H. Show $\left\{ u _ { n } \right\} _ { n = 1 } ^ { \infty }$ is an orthonormal basis for H if

$$
\left\| { \boldsymbol f } \right\| _ { H } ^ { 2 } = \sum _ { n = 1 } ^ { \infty } \left| \langle { \boldsymbol f } | u _ { n } \rangle \right| ^ { 2 } ~ \mathrm { f o r ~ a l l } ~ f \in \mathcal { S } .\tag{1.1}
$$

Exercise 1.4. Let $\varphi \in C _ { c } ^ { \infty } ( \overrightarrow { \mathbb { F } } _ { \circ } )$ and $f : \mathbb { F } \longrightarrow \mathbb { R }$ be an absolutely continuous function with compact support and $\varphi * \ j$ be the convolution of $\varphi$ and $\hat { j } ;$

$$
\varphi * f \left( x \right) : = \int _ { \mathbb { E } } \varphi \left( x - y \right) \widehat { \mathscr { I } } \left( y \right) \dot { \alpha } y .
$$

a) Show $\begin{array} { r } { \frac { c } { \dot { a } \tau } \left( \underline { { c } } \ast \hat { f } \right) ( x ) = ( \varphi ^ { \prime } \ast \hat { f } ) ( x ) } \end{array}$ for all $x \in \mathbb { R } .$

(b) Show $\left( \varphi ^ { \prime } \ast \bar { f } \right) ( x ) = \left( \varphi \ast \bar { f } ^ { \prime } \right) ( x )$ for all $z \in \mathbb { R } .$

(c) Explain why there exists ${ \bar { f } } _ { n } \in C _ { c } ^ { \infty } : ( \mathbb { R } )$ such that

$$
\operatorname* { l i m } _ { \pi \to \infty } \| \widehat { j } _ { n } - f \| _ { L ^ { \infty } ( \mathbb { R } , m ) } = 0 = \operatorname* { l i m } _ { \pi \to \infty } \| f ^ { \prime } - f _ { n } ^ { \prime } \| _ { L ^ { 1 } ( \mathbb { R } , m ) } .
$$

Exercise 1.5. Suppose that $\{ f _ { n } \} _ { n = 1 } ^ { \infty } = I ^ { 3 } \left( \mu \right)$ such that $\begin{array} { r } { \operatorname* { l i m } _ { \pi  \infty } \int _ { X } f _ { n } \omega d \mu , } \end{array}$ exists in C for all $\varphi \in { \mathcal { L } } ^ { 3 / 2 } \left( \mu \right)$ . Show $M : = \operatorname* { s u p } \| f _ { n } \| _ { L ^ { 3 } ( \mu ) } < \infty$

Exercise 1.6. Suppose $f : X \longrightarrow [ - 1 , 1 ]$ is a measurable function and $\varphi : [ - 1 , 1 ] \to \mathbb { R }$ is a bounded Borel measurable function. Show:

(a) $\Vert M _ { \varphi \circ f } \Vert _ { B ( L ^ { 2 } ( \mu ) ) } \leq \Vert \varphi \Vert _ { u } : = \operatorname { s u p } _ { | x | \leq 1 } | \varphi \left( x \right) |$ where $\left. M _ { \geqslant \circ f } \right. _ { B ( L ^ { 2 } ( \mu ) ) } = \operatorname* { s u p } _ { \{ \| \dot { h } \| _ { L ^ { 2 } ( \mu ) } = 1 } \atop { }  \left. M _ { \varphi \circ f } \dot { h } \right. _ { L ^ { 2 } ( \mu ) }$ is the operator norm of $M _ { \varphi \circ f }$

) Suppose $\varphi _ { n } : [ - 1 , 1 ] \to \mathbb { R }$ are bounded Borel measurable functions converging boundedly to $\varphi ,$ then, for all $h \in \mathcal { L } ^ { 2 } \left( \mu \right)$ ;

$$
L ^ { 2 } \left( \mu \right) \cdot \operatorname* { l i m } _ { \pi \to \infty } M _ { \varphi _ { \pi } \circ f } h = M _ { \varphi \circ f } \dot { n } .
$$

(c) Show by example that it is possible that $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } \| M _ { \varphi _ { n } \circ f } \| _ { B ( L ^ { 2 } ( \mu ) ) } \neq 0 } \end{array}$ even though $\varphi _ { \mathscr { n } }  0$ boundedly.

Exercise 1.7. Let $f , g : X \longrightarrow [ - 1 , 1 ]$ be measurable functions and $U : { \mathbb { Z } } ^ { 2 } \left( X , \mu \right) \longrightarrow { \mathbb { Z } } ^ { 2 } \left( X , \mu \right)$ be a unitary map such that $U M _ { f } U ^ { - 1 } = M _ { g }$ . Let H denote the collection of bounded Borel measurable functions, $\varphi : [ - 1 , 1 ] \to { \mathbb R }$ such that $U M _ { \varphi \circ f } U ^ { - 1 } = M _ { \varphi \circ g }$ .Show:

(a) $\begin{array} { r } { \varphi \in \mathcal { H } \mathrm { ~ i f ~ } \varphi \left( x \right) = \sum _ { n = 0 } ^ { N } \alpha _ { n } x ^ { n } } \end{array}$ is a polynomial with $\qquad \alpha _ { n } \in \mathbb { R } .$

) Show $C \left( \left\{ - 1 , 1 \right\} , \mathbb { R } \right) \subset \mathcal { H } .$

(c) Show H contains all bounded real measurable functions.

Hints: 1. The results of Exercise 1.6 are useful. 2. For (a) show $\varphi ( M _ { f } ) = M _ { \varphi \circ f } . \ 3$ For (c), notice that $\it U M _ { \varphi \circ f } U ^ { - 1 } = M _ { \varphi \circ \underline { { { \theta } } } }$ iff

$$
U M _ { \varphi \circ f } U ^ { - 1 } \hbar = M _ { \varphi \circ g } \hbar \ { \mathrm { ~ f o r ~ a l l ~ } } \hbar \in { \cal L } ^ { 2 } \left( \mu \right) .
$$

4. You do not have to prove (b) if you can prove (c).