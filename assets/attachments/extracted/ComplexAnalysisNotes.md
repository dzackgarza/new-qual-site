## COMPLEX ANALYSIS THEOREMS AND RESULTS JAMES BROOMFIELD

Theorem. (Cauchy-Riemann Equations) A function $f : \mathbb { C } \to \mathbb { C }$ given by $f ( z ) = u ( x , y ) + i \cdot v ( x , y )$ , where u and v are differentiable real functions, is holomorphic on a domain Ω $i f$ and only if the following equations are satisfied on Ω

$$
{ \frac { \partial u } { \partial x } } = { \frac { \partial v } { \partial y } }
$$

(1)

$$
{ \frac { \partial u } { \partial y } } = - { \frac { \partial v } { \partial x } }
$$

Theorem. (Cauchy-Goursat Theorem) $I f f : \mathbb { C } \to \mathbb { C }$ is holomorphic on a simply connected open subset U of C, then for any closed rectifiable path $\gamma \in U$ ,

$$
\oint _ { \gamma } f ( z ) d z = 0
$$

Theorem. (Cauchy’s Integral Formula) Let U be a simply connected open subset $o f \mathbb { C } ,$ let $\gamma \in U$ be a closed rectifiable path containing a, and let γ have winding number one about the point a. If $f : U \to \mathbb { C }$ is holomorphic, then

$$
f ^ { ( n ) } ( a ) = \frac { n ! } { 2 \pi i } \oint _ { \gamma } \frac { f ( z ) } { ( z - a ) ^ { n + 1 } }
$$

This also formula holds for n < m if f is only m-times differentiable.

Theorem. (Residue Theorem) Let D be an open set, E a discrete subset of $D ,$ and $\gamma \textit { a }$ null-homotopic piecewise smooth closed curve in D which doesn’t intersect E and has winding number one with respect to each $a \in E$ Under these conditions, if $f : D \setminus E \to \mathbb { C }$ is holomorphic, then

$$
\oint _ { \gamma } f ( z ) d z = 2 \pi i \sum _ { a \in E } R e s \left( f , a \right)
$$

Definition. (Line integrals) Let $\gamma$ be a smooth path parameterized by $\gamma ( t )$ , for $a \leq t \leq b$ . If f is a complex function on $\gamma _ { ; }$ , then the line integral of f over γ is

$$
\int _ { \gamma } f ( z ) d z = \int _ { a } ^ { b } f ( \gamma ( t ) ) \gamma ^ { \prime } d t .
$$

Result. (Trivial estimation for line integrals) Let $\gamma$ be a smooth path parameterized by $\gamma ( t )$ , for $a \leq t \leq b$ . If f is a complex function on $\gamma ,$ then the line integral of f over γ is

$$
\left| \int _ { \gamma } f ( z ) d z \right| \leq \operatorname* { s u p } _ { z \in \gamma } | f ( z ) | \cdot l e n g t h \left( \gamma \right) .
$$

Theorem. (Morera’s Theorem) If D is a connected open set and $f :$ $D \to \mathbb { C }$ is a continuous function such that $\textstyle \int _ { T } f d z = 0$ for each triangular path T in D, then f is analytic.

Theorem. (Open Mapping Theorem) If D is a domain in the complex plane, and $f : D \to \mathbb { C }$ is a non-constant holomorphic function, then f is an open map. That is, f maps open subsets of D to open subsets of C.

Theorem. (Louiville’s Theorem) A bounded entire function is constant.

Theorem. (Maximum Modulus Principle) An analytic function on a region D which attains its maximum on the interior of D is constant.

Theorem. (Schwarz’s Lemma) Let f map the open unit disk to itself with the origin fixed. Then $| f ( z ) | \leq | z |$ for all z in the disk, and $| f ^ { \prime } ( 0 ) | \leq 1$ . Further, if either $| f ( z ) | = z \ o r \ | f ^ { \prime } ( z ) | = 1$ , then $f ( z ) = c \cdot z$ for some c of modulus 1, i.e. f is a rotation.

Theorem. (Schwarz Reflection Principle) Let D be a region of the complex plane that is symmetric with respect to the real axis. Denote the $D _ { + } , D _ { 0 }$ , and $D _ { - }$ to be the intersection of D with the upper half plane, the real axis, and the lower half plane respectively.

If $f : D _ { + } \cup D _ { 0 }  \mathbb { C }$ is a continuous function which is analytic on $D _ { + }$ then f admits a unique extension to an analytic function. This extension is defined by $f ( z ) = \overline { { f ( \overline { { z } } ) } } \ f o r \ z \in D _ { - }$

Theorem. (Argument Principle) Let D be an open set, let f be a meromorphic function on D, and let γ be a null-homotopic piecewise smooth closed curve in D which doesn’t intersect either set of zeros of f or the set of poles of f . Then

$$
{ \frac { 1 } { 2 \pi i } } \int _ { \gamma } { \frac { f ^ { \prime } ( z ) } { f ( z ) } } d z = N - P
$$

Where N is the number of zeros of f in γ and P is the number of poles of $f$ in γ.

Theorem. (Roch´e’s Theorem) Let f be holomorphic on an open set U containing D, where ∂D is a simple closed path. Suppose that f does not vanish on ∂D. If another holomorphic function g on U satisfies

$$
| f ( z ) - g ( z ) | < | f ( z ) | ,
$$

for all $z \in \partial D$ , then f and g have the same number of zeros inside of f.

Theorem. (Great Picard’s Theorem) Every nonconstant entire function attains every comple value with at most one exception. Furthermore, every analytic function assumes every complex value, with possibly one exception, infinitely often in any neighborhood of an essential singularity.

If f is an analytic function from C to the extended complex plane, then f assumes every complex value, with possibly two exceptions, infinitely often in any neighborhood of an essential singularity.

Theorem. (Identity Theorem) Let f and g be holomorphic functions on a connected open set D. If $f = g$ on a subset S having an accumulation point in D, then $f = g$ on D.

Definition. (M¨obius Transformation) A function

$$
f ( z ) = { \frac { a z + b } { c z + d } }
$$

with $a , b , c , d \in \mathbb { C }$ and ad − bc 6= 0 is called a M¨obius transformation.

Result. (Conformality of M¨obius transformation) A M¨obius transformation

$$
f ( z ) = { \frac { a z + b } { c z + d } }
$$

is conformal except at $\frac { - d } { c }$ . When vied as an extended complex-valued function, f is conformal everywhere.

Result. (M¨obius transformation of bigons) M¨obius transformations send bigons to bigons.

Result. (Inverse of M¨obius transformations) Let

$$
f ( z ) = { \frac { a z + b } { c z + d } }
$$

be a M¨obius transformation. Then

$$
f ^ { - 1 } ( z ) = { \frac { d z - b } { - c z + a } }
$$

is an inverse for restriction of f $t o \mathbb { C } \setminus \{ \frac { - d } { c } \}$

Definition. (Cayley Transformations) A M¨obius transformation taking the upper half plane to the unit disk is called a Caley transformation. An example of such a map is

$$
f ( z ) = { \frac { z - i } { z + i } } .
$$

The inverse for this example is

$$
f ^ { - 1 } ( z ) = i { \biggl ( } { \frac { z + 1 } { - z + 1 } } { \biggr ) }
$$

Theorem. (Riemann Mapping Theorem) Let $D \subsetneq \mathbb { C }$ be simply-connected.   
Then D is conformally equivalent to the open disk.