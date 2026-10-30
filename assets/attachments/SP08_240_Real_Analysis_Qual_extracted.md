MATH 240: Real Analysis Qualifying Exam. May 23, 2008

General instructions: 3 hours. No books or notes. Be sure to carefully motivate all (nontrivial) claims and statements. You may use without proof any result proved in the text. If you use a theorem from the text, refer to it either by name (if it has one) or explain what it says. Also verify explicitly all hypotheses in the theorem. You need to reprove any result given as an exercise.

Notation:

1. (50p) Determine if the statements below are True or False. If True, give a brief proof. If False, give a counterexample (or prove your assertion in another way, if you prefer). If you claim an assertion follows from a theorem in the text, name the theorem (or describe it otherwise) and explain carefully how the conclusion follows.

(a) (10p) Suppose $f \colon [ 0 , 1 ] \to \mathbb { C }$ is a continuous function that is differentiable a.e. with respect to Lebesgue measure. If $f ^ { \prime } \in L ^ { 1 } ( [ 0 , 1 ] )$ , then

<!-- image-->

$$
f ( 1 ) - f ( 0 ) = \int _ { 0 } ^ { 1 } f ^ { \prime } ( x ) d x .
$$

(b) (10p) Given any two points $a \neq b$ in a locally compact Hausdorff space, there is a real-valued continuous function f such that $f ( a ) \neq f ( b )$

(c) (10p) Let X be a Banach space and $\{ f _ { n } \} _ { n = 1 } ^ { \infty }$ a sequence in the dual $X ^ { \ast }$ such that $f _ { n } \neq 0$ for all n. Then, the set $\{ x \in X \colon f _ { n } ( x ) \neq 0 , \forall n = 1 , 2 , \ldots \}$ is dense in X.

(d) (10p) Let X be a measurable space. Let ν be a complex measure on X and µ a σ-finite positive measure on X. Suppose that there is a constant C such that for every $f \in L ^ { 1 } ( X , d \mu )$ , we have

$$
\left| \int _ { X } f d \nu \right| \leq C \left| \int _ { X } f d \mu \right| .
$$

Then, $d \nu = h d \mu$ for some $h \in L ^ { 1 } ( X , d \mu )$

2. Let $( X , \mu , )$ be a measure space and $f , f _ { n } \colon X \to \mathbb { R }$ measurable functions such that $f _ { 1 } \leq f _ { 2 } \leq . . . \leq f _ { n } \leq . . . \mathrm { a . e }$ and $\scriptstyle \operatorname* { l i m } _ { n \to \infty } f _ { n } = f$ a.e.

(a) (15p) For every $a \in \mathbb { R }$ , show that $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } \mu ( \{ x : f _ { n } ( x ) > a \} ) } \end{array}$ exists and

<!-- image-->

$$
\operatorname* { l i m } _ { n \to \infty } \mu ( \{ x \colon f _ { n } ( x ) > a \} ) = \mu ( \{ x \colon f ( x ) > a \} ) .
$$

2

(b) (15p) Assume that $\mu ( \mathrm { \boldsymbol { X } } ) < \infty$ Show that $\begin{array} { r } { \operatorname* { l i m } _ { n \longrightarrow \infty } \mu ( \{ x : f _ { n } ( x ) < a \} ) } \end{array}$ exists for every $a \in \mathbb { R }$ and

$$
\mu ( \{ x : f ( x ) < a \} ) \leq \operatorname* { l i m } _ { n \to \infty } \mu ( \{ x : f _ { n } ( x ) < a \} ) \leq \mu ( \{ x : f ( x ) < a \} ) + \mu ( \{ x : f ( x ) = a \} .
$$

Give an example where

$$
\mu ( \{ x : f ( x ) < a \} ) < \operatorname* { l i m } _ { n \to \infty } \mu ( \{ x : f _ { n } ( x ) < a \} )
$$

for some $a \in \mathbb { R }$

3. (30p) Show that, for measurable functions $f , g \colon [ 1 , \infty ] \to [ 0 , \infty ]$ , the following inequality holds:

$$
\left| \int _ { [ 1 , \infty ) ^ { 2 } } e ^ { - x y } f ( x ) g ( y ) d x d y \right| \leq \frac { 1 } { 2 \epsilon } \left( \int _ { 1 } ^ { \infty } | f ( x ) | ^ { 2 } d x \right) ^ { 1 / 2 } \left( \int _ { 1 } ^ { \infty } | g ( x ) | ^ { 2 } d x \right) ^ { 1 / 2 } ,
$$

whcre dx denotes the Lebesgue measure on $\{ 1 , \infty \}$ and dady denotes the Lebesgue measure on $[ 1 , \infty ) ^ { 2 } = [ 1 , \infty ] \times [ 1 , \infty )$

<!-- image-->

4. Let $\ell ^ { \infty }$ denote the Banach space of all bounded real-valued functions on the natural numbers N, and $f _ { n }$ the bounded linear functional

$$
f _ { n } ( x ) : = { \frac { x ( 1 ) + \ldots + x ( n ) } { n } } .
$$

Let $M \subset \ell ^ { \infty }$ be the subspace of all x such that lim $\mathfrak { i } _ { n \to \infty } f _ { n } ( x )$ exists, and f the linear functional $M \to \mathbb { R }$ given by $f ( x ) : = \textstyle \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x )$

(a) (10p) Let $\tau \colon \ell ^ { \infty }  \ell ^ { \infty }$ denote the shift operator given by $( \tau x ) ( n ) = x ( n + 1 )$ for $n = 1 , 2 , \ldots$ Show that T sends M to M and $f ( \tau x ) = f ( x )$ for all $x \in M$

(a) (20p) Show that there is a linear functional $F \colon \ell ^ { \infty }  \mathbb { R }$ such that $F | _ { M } = f$ and

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } x ( n ) \leq F ( x ) \leq \operatorname* { l i m } _ { n \to \infty } x ( n ) .
$$

5. (30p) Let $F \colon \mathbb { C } \to \mathbb { C }$ be a bounded Borel measurable function, and $y _ { 0 } \in \mathbb { C }$ Define a sequence of functions $f _ { n } \colon [ 0 , 1 ] \to \mathbb { C }$ by the recursion $f _ { 0 } ( x ) \equiv y _ { 0 }$ and

$$
f _ { n + 1 } ( x ) : = y _ { 0 } + \int _ { 0 } ^ { x } F ( f _ { n } ( t ) ) d t .
$$

<!-- image-->

Show that $f _ { n } \in C ( [ 0 , 1 ] )$ , and there are $f \in C ( [ 0 , 1 ] )$ and a subsequence $f _ { n _ { k } }$ such that $f _ { n _ { k } } \to f$ in $C ( [ 0 , 1 ] )$ .

6. (30p) For $f : \mathbb { R } \to \mathbb { C }$ and $h \in \mathbb R$ ,denote by $\tau _ { h } f : \mathbb { R } \to \mathbb { C }$ the function defined by $\tau _ { h } f ( x ) : = f ( x + h )$ for all $x \in \mathbb { R }$

(a) Show that if T is a distribution on $\mathbb { R }$ and $h \in \mathbb { R }$ then

$$
\tau _ { h } T ( \phi ) : = T ( \tau _ { - h } \phi ) , \qquad \phi \in C _ { 0 } ^ { \infty } ( \mathbb { R } ) ,
$$

defines a distribution $\tau _ { h } T$ on R.

(b) Show that the following holds in $\mathcal { D } ^ { \prime } ( \mathbb { R } )$

$$
\operatorname* { l i m } _ { h \longrightarrow 0 } { \frac { \tau _ { h } T - T } { h } } = T ^ { \prime } .
$$

(c) Show that if T is a tempered distribution then $\tau _ { h } T$ is also a tempered distribution. Find the Fourier transform of $\tau _ { h } T$ in terms of the Fourier transform of T.

7. (a) (15p) For $\phi \in C _ { 0 } ^ { \infty } (  { \mathbb { R } } )$ show that the expression

$$
T ( \phi ) : = \operatorname* { l i m } _ { \epsilon \to 0 ^ { + } } \big [ \int _ { \epsilon } ^ { \infty } \frac { \phi ( x ) } { x } d x + \phi ( 0 ) \log \epsilon \big ]
$$

<!-- image-->

defines a distribution on R.

(b) (15p) Show that the function $f ( x ) : = H ( x )$ log x is locally integrable on R (where H is the Heaviside function). Express the derivative of f in the sense of distributions in terms of the distribution T given in (a).