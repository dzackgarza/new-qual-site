---
schema: qual/card@1
id: P-AGH26HOMDIM
kind: problem
title: The homogeneous coordinate ring satisfies $\dim S(Y) = \dim Y + 1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dimension
  - Coordinate Rings
  - Transcendence Degree
relations: []
review: draft
---

::: {.problem}
Let $Y$ be a projective variety with homogeneous coordinate ring $S(Y)$.
Show that $\dim S(Y) = \dim Y + 1$.
:::

::: {.hint}
Let $\phi_i : U_i \to \AA^n$ be the homeomorphism
$$
\thevector{a_0 : \cdots : a_n} \mapsto \qty{ \frac{a_0}{a_i}, \ldots, \widehat{\frac{a_i}{a_i}}, \ldots, \frac{a_n}{a_i} }
$$
from the open set $U_i = \PP^n \sm Z(x_i)$, let $Y_i$ be the affine variety $\phi_i(Y \intersect U_i)$, and let $A(Y_i)$ be its affine coordinate ring.
Show that $A(Y_i)$ can be identified with the subring of elements of degree $0$ of the localized ring $S(Y)_{x_i}$.
Then show that $S(Y)_{x_i} \cong A(Y_i)[x_i, \inverseof{x_i}]$.
Now use Proposition I.1.7, Theorem I.1.8A and Ex. I.1.10, and look at transcendence degrees.
Conclude also that $\dim Y = \dim Y_i$ whenever $Y_i$ is nonempty.
:::

::: {.solution}
Let $Y \subseteq \PP^n$, put $S = k[x_0,\ldots,x_n]$, and write $\bar x_j$ for the image of $x_j$ in $S(Y) = S/I(Y)$.
The ring $S(Y)$ is a graded domain by [[P-AGH24CORRESPONDENCE]].
Fix $i$ with $Y_i \neq \emptyset$.
Then $x_i \notin I(Y)$, so $\bar x_i \neq 0$.

**The chart ring.** The substitution $y_j \mapsto x_j/x_i$ for $j \neq i$ is an isomorphism $k[y_1,\ldots,y_n] \to S_{(x_i)}$; its inverse sends $F/x_i^d$, with $F$ homogeneous of degree $d$, to $F$ with $x_i = 1$.
For such $F$, the function $F/x_i^d$ vanishes on $Y_i$ exactly when $F$ vanishes on $Y \intersect U_i$, that is, when $x_i F$ vanishes on $Y$.
So this isomorphism carries $I(Y_i)$ onto $I(Y) S_{(x_i)}$, because $F/x_i^d = x_i F / x_i^{d+1}$.
Passing to quotients, and using that localization and taking degree-zero parts are exact,
$$
A(Y_i) \cong S_{(x_i)} / I(Y) S_{(x_i)} \cong S(Y)_{(\bar x_i)} .
$$

**The localization.** A homogeneous element $g/\bar x_i^m$ of $S(Y)_{\bar x_i}$ of degree $e$ equals $(g/\bar x_i^{m+e}) \cdot \bar x_i^e$, so $S(Y)_{\bar x_i} = S(Y)_{(\bar x_i)}[\bar x_i, \inverseof{\bar x_i}]$.
The element $\bar x_i$ is transcendental over $S(Y)_{(\bar x_i)}$: in a relation $\sum_j c_j \bar x_i^j = 0$ with $c_j$ of degree $0$, the term $c_j \bar x_i^j$ is the degree-$j$ part, so each $c_j \bar x_i^j = 0$ and $c_j = 0$.
Hence
$$
S(Y)_{\bar x_i} \cong A(Y_i)[t, \inverseof{t}] .
$$

**Transcendence degrees.** The fraction field of $S(Y)$ equals that of $S(Y)_{\bar x_i}$, which is $K(Y_i)(t)$ with $t$ transcendental.
For a finitely generated $k$-domain the dimension equals the transcendence degree of its fraction field [@Har77, Theorem I.1.8A].
Applying this to $S(Y)$ and to $A(Y_i)$, and using Proposition I.1.7 for $Y_i$,
$$
\dim S(Y) = \trdeg_k K(Y_i) + 1 = \dim Y_i + 1 .
$$

**Conclusion.** The sets $Y \intersect U_i$ form an open cover of $Y$, and $\phi_i$ maps $Y \intersect U_i$ homeomorphically onto $Y_i$.
By Ex. I.1.10(b), $\dim Y = \sup_i \dim Y_i$, the supremum over the $i$ with $Y_i \neq \emptyset$.
Every such $Y_i$ has $\dim Y_i = \dim S(Y) - 1$ by the previous paragraph.
So $\dim Y = \dim S(Y) - 1$, and $\dim Y_i = \dim Y$ whenever $Y_i$ is nonempty.
:::
