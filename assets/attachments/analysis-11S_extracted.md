# Analysis Qualifying Examination, Spring 2011

26pm, Wednesday, March 23, 2011

Instructions: Solve no more than 10 problems. All problems are worth ten points; parts of a problem do not carry equal weight. You must demonstrate adequate knowledge of both real analysis (problems 16) and complex analysis (problems 712).

Problem 1. (a) Define what it means to say that $f _ { n }  f$ weakly in $L ^ { 2 } ( [ 0 , 1 ] )$

(b) Suppose $f _ { \mathscr { n } } \in L ^ { 2 } ( [ 0 , 1 ] )$ converge weakly to $f \in L ^ { 2 } ( [ 0 , 1 ] )$ and define 'primitive' functions:

$$
F _ { n } ( x ) : = \int _ { 0 } ^ { x } f _ { n } ( t ) d t \quad { \mathrm { a n d } } \quad F ( x ) : = \int _ { 0 } ^ { x } f ( t ) d t .
$$

Show that $F _ { \eta } , F \in C ( [ 0 , 1 ] )$ and that $F _ { \pi } \to F$ uniformly on [0, 1].

Problem 2. Let $f \in L ^ { 3 } ( \mathbb { R } )$ and

$$
\phi ( x ) = { \left\{ \begin{array} { l l } { \sin ( \pi x ) } & { : | x | \leq 1 } \\ { 0 } & { : { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

Show that

$$
f _ { n } ( x ) : = n \int f ( x - y ) \phi ( n y ) d y \longrightarrow 0
$$

Lebesgue almost everywhere.

Problem 3. Let $\mu$ be a Borel probability measure on R and define $\begin{array} { r } { f ( t ) = \int e ^ { i t x } \mu ( d x ) } \end{array}$ Suppose that

$$
\operatorname* { l i m } _ { t \to 0 } { \frac { f ( 0 ) - f ( t ) } { t ^ { 2 } } } = 0 .
$$

Show that $\mu$ is supported at {0}.

Problem 4. Let $f _ { n } : [ 0 , 1 ] \to [ 0 , \infty )$ be Borel functions with

$$
\operatorname* { s u p } _ { n } \int _ { 0 } ^ { 1 } f _ { n } ( x ) \log \bigl ( 2 + f _ { n } ( x ) \bigr ) d x < \infty
$$

Suppose $f _ { n }  f$ Lebesgue almost everywhere. Show that $f \in L ^ { I }$ and $f _ { n }  f$ in $L ^ { I }$ sense. Hint: Consider $g _ { n } ( x ) = \operatorname* { m a x } ( f _ { n } ( x ) , \lambda )$ for certain choices of $\lambda .$

Problem 5. (a) Show that ${ \ell ^ { \infty } ( \mathbb { Z } ) }$ contains continuum many functions $x _ { \alpha } : \mathbb { Z } \to \mathbb { R }$ obeying

$$
\| x _ { \alpha } \| _ { \ell ^ { \infty } } = 1 \quad { \mathrm { a n d } } \quad \| x _ { \alpha } - x _ { \beta } \| _ { \ell ^ { \infty } } \geq 1 \quad { \mathrm { w h e n e v e r ~ } } \alpha \neq \beta .
$$

(b) Deduce (assuming the axiom of choice) that the Banach space dual of ${ \ell ^ { \infty } ( \mathbb { Z } ) }$ cannot contain a countable dense subset.

c) Deduce that $\ell ^ { 1 } ( \mathbb { Z } )$ is not reflexive.

Problem 6. Suppose $\mu$ and v are finite positive (regular) Borel measures on $\mathbb { R } ^ { n }$ .Prove the existence and uniqueness of the Lebesgue decomposition: There are a unique pair of positive Borel measures $\mu _ { a }$ and $\mu _ { s }$ so that

$$
\mu = \mu _ { a } + \mu _ { s } , \mu _ { a } \ll \nu , \mathrm { a . n d } \mu _ { s } \perp \nu
$$

That is, $\mu _ { a }$ is absolutely continuous to $\nu ,$ while $\mu _ { s }$ is mutually singular to $V .$

Problem 7. Prove Gorsat's theorem: If $f : \mathbb { C } \to \mathbb { C }$ is complex differentiable (and so continuous), then for every triangle $\Delta \subset \mathbb { C }$

$$
\oint _ { \partial \triangle } f ( z ) d z = 0
$$

where line integral is over the three sides of the triangle.

Problem 8. (a) Define upper-semicontinuous for functions $f : \mathbb { C } \to [ - \infty , \infty )$

(b) Define what it means for such an upper-semicontinuous function to be subharmonic.

(c) Prove or refute (with a counterexample) each of the following:

The pointwise supremum of a bounded family of subharmonic functions is subharmonic.

The pointwise infimum of a family of subharmonic functions is subharmonic.

)Let $A ( z )$ be a $2 \times 2$ matrix-valued holomorphic function (i.e., the entries are holomorphic). Show that

$$
z \mapsto \log \left( \left| | A ( z ) \right| \right) \qquad { \mathrm { i s ~ s u b h a r m o n i c } }
$$

where $\left\| \mathcal { A } ( z ) \right\|$ is the norm as an operator on the Hilbert space $\mathbb { C } ^ { 2 }$

Problem 9. Let $E \subseteq [ 0 , 1 ]$ denote the Cantor 'middle thirds' set; namely, the set $\sum \ m$ $\textstyle \{ \sum _ { i > 1 } b _ { i } 3 ^ { - i } : b _ { i } = 0 , 2 \}$ . Embedding $[ 0 , 1 ]$ naturally into $\mathbb { C } ,$ we regard E as a subset of C. Suppose $f \colon \mathbb { C } \backslash E  \mathbb { C }$ is holomorphic and (uniformly) bounded. Show that f is constant.

Problem 10. Let $\mathbb { D } = \{ z : | z | < 1 \}$ and let $\Omega = \{ z \in \mathbb { D } : \operatorname { I m } z > 0 \}$ . Evaluate sup $\Big \{ \mathrm { R e } f ^ { \prime } \big ( \frac { \cdot i } { 2 } \big ) \Big | f : \Omega $ D is holomorphic

Problem 11. Consider the function defined for $s \in ( 1 , \infty )$ by

$$
f ( s ) : = \int _ { 0 } ^ { \infty } { \frac { x ^ { s - 1 } } { e ^ { x } - 1 } } d x .
$$

Show that $f$ has an analytic continuation to $\{ s \in \mathbb { C } \colon \mathrm { R e } s > 0 , s \neq 1 \}$ with a simple pole at $s = 1$ . Compute the residue at $s \stackrel { \cdot } { = } \mathfrak { I }$

Problem 12. Let $\Omega = \mathbb { C } \setminus \left( - \infty , 0 \right]$ and let $\log ( z )$ be the branch of the complex logarithm on Ω that is real on the positive real axis (and analytic throughout Ω). Show that for $0 < t < \infty .$ ,the number of solutions $z \in \Omega$ to

$$
\log ( z ) = \frac { t } { z }
$$

is finite and independent of t.