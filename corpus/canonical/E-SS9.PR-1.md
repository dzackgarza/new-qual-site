---
schema: qual/card@1
id: E-SS9.PR-1
kind: exercise
title: "Besides the approach in Section 1"
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Uniform Convergence
relations: []
review: draft
---

::: exercise
1. Besides the approach in Section 1.2, there are several alternate ways of dealing with the sum $\textstyle \sum { 1 } / ( z + \omega ) ^ { 2 }$ , where $\omega = n + m \tau$ . For example, one may sum either (a) circularly, (b) first in n then in m, (c) or first in m then in n.

(a) Prove that ${ \mathrm { i f ~ } } z \notin \Lambda$ , then

$$

\lim _ {R \to \infty} \sum_ {n ^ {2} + m ^ {2} \leq R ^ {2}} \frac {1}{(z + n + m \tau) ^ {2}} = S _ {1} (z)

$$

exists and $S _ { 1 } ( z ) = \wp ( z ) + c _ { 1 }$

(b) Similarly,

$$

\sum_ {m} \left(\sum_ {n} \frac {1}{(z + n + m \tau) ^ {2}}\right) = S _ {2} (z)

$$

exists and $S _ { 2 } ( z ) = \wp ( z ) + c _ { 2 } , { \mathrm { w h e r e ~ } } c _ { 2 } = F ( \tau )$ , and F is the forbidden Eisenstein series.

(c) Also

$$

\sum_ {n} \left(\sum_ {m} \frac {1}{(z + n + m \tau) ^ {2}}\right) = S _ {3} (z)

$$

exists with $S _ { 3 } ( z ) = \wp ( z ) + c _ { 3 }$ , and $c _ { 3 } = \tilde { F } ( \tau )$ , the reverse of $F ,$

[Hint: To prove (a), it sufices to show that lim $. R { \longrightarrow } \infty$ $\sum { \begin{array} { r l } \end{array} } \quad 1 / ( n + m \tau ) ^ { 2 } = c _ { 1 }$ $1 \leq n ^ { 2 } + m ^ { 2 } \leq R ^ { 2 }$ exists. This is proved by a comparision with $\begin{array} { r } { \int _ { 1 \leq x ^ { 2 } + y ^ { 2 } \leq R ^ { 2 } } \frac { d x } { ( x + y \tau ) ^ { 2 } } = I ( R ) } \end{array}$ . It can be shown that $I ( R ) = 0$ , which follows because $( \overline { { x } } + y \tau ) ^ { - 2 } = - ( \partial / \partial x ) ( x + y \tau ) ^ { - 1 } . ]$
:::
