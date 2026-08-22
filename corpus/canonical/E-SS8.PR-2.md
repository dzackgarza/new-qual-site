---
schema: qual/card@1
id: E-SS8.PR-2
kind: exercise
title: "The angle between two non-zero complex numbers z and  (taken in that order) is s"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
solved: false
---

::: exercise
2. The angle between two non-zero complex numbers z and $w$ (taken in that order) is simply the oriented angle, in $( - \pi , \pi ]$ , that is formed between the two vectors in $\mathbb { R } ^ { 2 }$ corresponding to the points z and w. This oriented angle, say $\alpha ,$ is uniquely determined by the two quantities

$$

\frac {(z , w)}{| z | | w |} \quad \mathrm{and} \quad \frac {(z , - i w)}{| z | | w |}

$$

which are simply the cosine and sine of $\alpha ,$ respectively. Here, the notation $( \cdot , \cdot )$ corresponds to the usual Euclidian inner product in $\mathbb { R } ^ { 2 }$ , which in terms of complex numbers takes the form $( z , w ) = \operatorname { R e } ( z { \overline { { w } } } )$

In particular, we may now consider two smooth curves $\gamma : [ a , b ]  \mathbb { C }$ and $\eta :$ $[ a , b ] \to \mathbb { C }$ that intersect at $z _ { 0 }$ , say $\gamma ( t _ { 0 } ) = \eta ( t _ { 0 } ) = z _ { 0 }$ , for some $t _ { 0 } \in ( a , b )$ . If the quantities $\gamma ^ { \prime } ( t _ { 0 } )$ and $\eta ^ { \prime } ( t _ { 0 } )$ are non-zero, then they represent the tangents to the curves $\gamma$ and $\eta$ at the point $z _ { 0 }$ , and we say that the two curves intersect at $z _ { 0 }$ at the angle formed by the two vectors $\gamma ^ { \prime } ( t _ { 0 } )$ and $\eta ^ { \prime } ( t _ { 0 } )$

A holomorphic function $f$ defined near $z _ { 0 }$ is said to preserve angles at $z _ { 0 }$ if for any two smooth curves $\gamma$ and $\eta$ intersecting at $z _ { 0 }$ , the angle formed between the curves $\gamma$ and $\eta$ at $z _ { \mathrm { 0 } }$ equals the angle formed between the curves $f \circ \gamma$ and $f \circ \eta$ at $f ( z _ { 0 } )$ . (See Figure 12 for an illustration.) In particular, we assume that the tangents to the curves $\gamma , \eta , f \circ \gamma$ , and $f \circ \eta$ at the point $z _ { 0 }$ and $f ( z _ { 0 } )$ are all non-zero.

Figure 12. Preservation of angles at $z _ { \mathrm { 0 } }$

(a) Prove that if $f : \Omega \to \mathbb { C }$ is holomorphic, and $f ^ { \prime } ( z _ { 0 } ) \neq 0$ , then $f$ preserves angles at $z _ { \mathrm { 0 } }$ . [Hint: Observe that

$$

(f ^ {\prime} (z _ {0}) \gamma^ {\prime} (t _ {0}), f ^ {\prime} (z _ {0}) \eta^ {\prime} (t _ {0})) = | f ^ {\prime} (z _ {0}) | ^ {2} (\gamma^ {\prime} (t _ {0}), \eta^ {\prime} (t _ {0})). ]

$$

(b) Conversely, prove the following: suppose $f : \Omega \to \mathbb { C }$ is a complex-valued function, that is real-diferentiable at $z _ { 0 } \in \Omega$ , and $J _ { f } ( z _ { 0 } ) \ne 0$ . If f preserves angles at $z _ { \mathrm { 0 } }$ , then $f$ is holomorphic at $z _ { \mathrm { 0 } }$ with $f ^ { \prime } ( z _ { 0 } ) \neq 0$

$\mathbf { 3 . ^ { * } }$ The Schwarz-Pick lemma (see Exercise 13) is the infinitesimal version of an important observation in complex analysis and geometry.

For complex numbers $w \in \mathbb { C }$ and $z \in \mathbb { D }$ we define the hyperbolic length of $w$ at $z$ by

$$

\| w \| _ {z} = \frac {| w |}{1 - | z | ^ {2}},

$$

where $| w |$ and $| z |$ denote the usual absolute values. This length is sometimes referred to as the Poincar´e metric, and as a Riemann metric it is written as

$$

d s ^ {2} = \frac {| d z | ^ {2}}{(1 - | z | ^ {2}) ^ {2}}.

$$

The idea is to think of $w$ as a vector lying in the tangent space at $z .$ . Observe that for a fixed $w ,$ its hyperbolic length grows to infinity as z approaches the boundary of the disc. We pass from the infinitesimal hyperbolic length of tangent vectors to the global hyperbolic distance between two points by integration.

(a) Given two complex numbers $z _ { 1 }$ and $z _ { 2 }$ in the disc, we define the hyperbolic distance between them by
:::
