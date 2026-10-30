## Analysis Qualifying Exam, Spring 2013

Instructions: Work on any 10 problems and therefore at least 4 from Problems 1-6 and at least 4 from Problems 7-12. All problems are worth ten points. Full credit on one problem will be better than part credit on two problems. If you attempt more than 10 problems, indicate which 10 are to be graded.

1: Suppose $f : \mathbb { R } \to \mathbb { R }$ is bounded, Lebesgue measurable, and

$$
\operatorname* { l i m } _ { h \to 0 } \int _ { 0 } ^ { 1 } { \frac { | f ( x + h ) - f ( x ) | } { h } } d x = 0 .
$$

Show that $f$ is a.e. constant on the interval [0, 1].

2: Consider the Hilbert space $\ell ^ { 2 } ( \mathbb { Z } )$ . Show that the Borel $\sigma \cdot$ -algebra $\mathcal { N }$ on $\ell ^ { 2 } ( \mathbb { Z } )$ associated to the norm topology agrees with the Borel σ-algebra W on $\ell ^ { 2 } ( \mathbb { Z } )$ associated to the weak topology.

3: Given $f : \mathbb { R } ^ { 2 } \to \mathbb { R }$ , continuous, we define

$$
[ A _ { r } f ] ( x , y ) : = { \frac { 1 } { 2 \pi } } \int _ { - \pi } ^ { \pi } f ( x + r \cos \theta , y + r \sin \theta ) d \theta \quad { \mathrm { a n d } } \quad [ M f ] ( x , y ) : = \operatorname* { s u p } _ { 0 < r < 1 } [ A _ { r } f ] ( x , y ) .
$$

By a theorem of Bourgain, there is an absolute constant C so that

$$
\| M f \| _ { L ^ { 3 } ( \mathbb { R } ^ { 2 } ) } \leq C \| f \| _ { L ^ { 3 } ( \mathbb { R } ^ { 2 } ) } \quad { \mathrm { f o r ~ a l l } } \quad f \in C _ { c } ( \mathbb { R } ^ { 2 } ) .
$$

Here $C _ { c } ( \mathbb { R } )$ denotes the set of continuous functions of compact support.

Use this to show the following: If $K \subset \mathbb { R } ^ { 2 }$ is compact, then $[ A _ { r } \chi _ { K } ] ( x , y )  1$ as $r  0$ at almost every point $( x , y )$ in K (with respect to Lebesgue measure). Here $\chi _ { K }$ denotes the characteristic function of $K$

4: Let K be a non-empty compact subset of $\mathbb { R } ^ { 3 }$ . For any Borel probability measure $\mu$ on $K$ , define the Newtonian energy $I ( \mu ) \in ( 0 , + \infty ]$ by

$$
I ( \mu ) : = \int _ { K } \int _ { K } { \frac { 1 } { | x - y | } } \ d \mu ( x ) d \mu ( y )
$$

and let $R _ { K }$ be the infimum of $I ( \mu )$ over all Borel probability measures $\mu$ on $K$ . Show that there exists a Borel probability measure $\mu$ such that $I ( \mu ) = R _ { K }$

5: Let $\mathbb { D } = \{ ( x , y ) : x ^ { 2 } + y ^ { 2 } < 1 \}$ and let us define a Hilbert space

$H : = \{ u : \mathbb { D }  \mathbb { R } \ |$ u is harmonic and $\int _ { D } | f ( x , y ) | ^ { 2 } d x d y < \infty \}$

with inner product $\begin{array} { r } { \langle f , g \rangle : = \int _ { D } } \end{array}$ fg dx dy.

(a) Show that $\textstyle f \mapsto { \frac { \partial f } { \partial x } } ( 0 , 0 )$ is a bounded linear functional on H.

(b) Compute the norm of this linear functional.

6: Let $C _ { 0 } ( \mathbb { R } ) : = \{ F : \mathbb { R } \to \mathbb { C } | F$ is continuous and $F ( \xi ) \to 0 { \mathrm { ~ a s ~ } } \xi \to \pm \infty \}$ ; this is Banach space under the supremum norm. Additionally, let

$$
X : = { \Bigl \{ } \xi \mapsto \int _ { \mathbb { R } } e ^ { i \xi x } f ( x ) d x ~ { \Big | } ~ f \in L ^ { 1 } ( \mathbb { R } ) { \Bigr \} } . 
$$

Show the following three properties of $X { \mathrm { i } }$

(a) X is a subset of $C _ { 0 } ( \mathbb { R } )$

(b) X is a dense subset of $C _ { 0 } ( \mathbb { R } )$

(c) $X \neq C _ { 0 } ( \mathbb { R } )$

7: Let $f : \mathbb { C } \to \mathbb { C }$ be an entire function such that log $| f |$ is absolutely integrable with respect to planar Lebesgue measure. Show that f is constant.

8: Let A and B be positive definite $n \times n$ real symmetric matrices with the property

$$
\left\| B A ^ { - 1 } x \right\| \leq \left\| x \right\| \quad { \mathrm { f o r ~ a l l } } \quad x \in \mathbb { R } ^ { n }
$$

where $\lVert x \rVert$ denotes the usual Euclidean norm: $\textstyle \| x \| ^ { 2 } = \sum _ { i = 1 } ^ { n } | x _ { i } | ^ { 2 }$

(a) Show that for each pair $x , y \in \mathbb { R } ^ { n }$

$$
z \mapsto \langle y , B ^ { z } A ^ { - z } x \rangle
$$

admits an analytic continuation from $0 < z < 1$ to the whole complex plane. Here $\langle \cdot , \cdot \rangle$ denotes the usual Euclidean inner product on $\mathbb { R } ^ { n }$

(b) Show that

$$
\| B ^ { \theta } A ^ { - \theta } x \| \leq \| x \|
$$

for all $0 \leq \theta \leq 1$

9: Let $P ( z )$ be a non-constant complex polynomial, all of whose zeroes lie in a halfplane $\{ z \in \mathbb { C } : \operatorname { R e } ( z ) < \sigma \}$ . Show that all the zeroes of $P ^ { \prime } ( z )$ also lie in the same half-plane $\{ z \in \mathbb { C } : \operatorname { R e } ( z ) < \sigma \}$ . (Hint: compute the log-derivative $P ^ { \prime } ( z ) / P ( z )$ of P .)

10: Let $f : \mathbb { C } \to \mathbb { C }$ be a non-constant entire function. Without using either of the Picard theorems, show that there exist arbitrarily large complex numbers z for which $f ( z )$ is a positive real.

11: Let $f ( z ) : = - \pi z \cot ( \pi z )$ as a meromorphic function on the whole of $\mathbb { C } .$

(a) Locate all poles of $f$ and determine their residues.

(b) Show that for each $n \geq 1$ the coefficient of $z ^ { 2 n }$ in the Taylor expansion of $f ( z )$ about $z = 0$ coincides with

$$
a _ { n } : = \sum _ { k = 1 } ^ { \infty } { \frac { 2 } { k ^ { 2 n } } }
$$

12: Let $\mathbf { \mathcal { I } } : = \{ z \in \mathbb { C } : \operatorname { I m } z > 0 \}$ be the upper half-plane. Let $f : \mathbf { H }  \mathbf { H }$ be a holomorphic function obeying

$$
\operatorname* { l i m } _ { y \to \infty } y f ( i y ) = i \quad { \mathrm { a n d } } \quad | f ( z ) | \leq { \frac { 1 } { \operatorname { I m } ( z ) } } \quad { \mathrm { f o r ~ a l l ~ } } z \in \mathbf { H } .
$$

(a) For $\varepsilon > 0$ , write $\textstyle g _ { \varepsilon } ( x ) : = { \frac { 1 } { \pi } }$ Im $f ( x + i \varepsilon )$ . Show that

$$
f ( z + i \varepsilon ) = \int _ { \mathbb { R } } { \frac { g _ { \varepsilon } ( x ) } { x - z } } \ d x .
$$

(b) Show that there exists a Borel probability measure $\mu$ on $\mathbb { R }$ such that

$$
f ( z ) = \int _ { \mathbb { R } } \frac { d \mu ( x ) } { x - z } .
$$