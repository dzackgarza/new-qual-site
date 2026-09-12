---
schema: qual/card@1
id: P-CH10A-6
kind: problem
title: Chapter 10A exercise 6
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
Let G be the group of all polynomials with real coefficients under addition.
For each f in G let R f denote the antiderivative of f that passes through the point (0, 0). Show that the mapping $f \mapsto \textstyle \int f$ from G to G is a homomorphism.
What is the kernel of this mapping?
Is this mapping a homomorphism if $\textstyle \int f$ denotes the antiderivative of f that passes through (0, 1)?
:::

::: {.solution}
Let $\phi : \mathbb { R } [ x ] \to \mathbb { R } [ x ]$ be defined by $f \mapsto \int f$ Then $\phi ( f + g ) = \textstyle \int ( f + g ) + c$ where $c = - ( f + g ) ( 0 )$ and $\textstyle \int ( f + g )$ is the polynomial that is the antiderivative without a constant term.
Now, $\begin{array} { r } { \phi ( f ) + \phi ( g ) = \int f + \int g + c _ { 1 } + c _ { 2 } } \end{array}$ where $c _ { 1 } = - f ( 0 )$ and $c _ { 2 } = - g ( 0 )$ . Hence $\phi ( f + g ) = \phi ( f ) + \phi ( g )$ for all $f , g \in \mathbb { R } [ x ]$ so $\phi$ is a homomorphism.

Now, the kernel of $\phi$ are the set of things that map to the identity, 0. So $K e r \phi = \{ f \vert \int f = 0 \} = \{ a _ { 0 } + a _ { 1 } x + \dotsc + a _ { n } x ^ { n } \vert a _ { 0 } x + \frac { a _ { 1 } } { 2 } x ^ { 2 } + \dotsc + \frac { a _ { n } } { n + 1 } x ^ { n + 1 } = 0 \} = \{ a _ { 0 } = a _ { 1 } = \dotsc = a _ { n } = 0 \} = \{ 0 \}$

If the function $\textstyle \int f$ goes through (0,1) instead, it is not a homomorphism.
This is because $\phi ( f + g ) ( 0 ) = 1$ but $( \phi ( f ) + \phi ( g ) ) ( 0 ) = \phi ( f ) ( 0 ) + \phi ( g ) ( 0 ) = 1 + 1 = 2$ , so the functions are not the same.
:::
