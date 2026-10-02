---
schema: qual/card@1
id: D-CRVHYP
kind: definition
title: Hyperelliptic curves, and what the canonical map does to them
classification:
  areas:
  - algebraic-geometry
  topics:
  - Hyperelliptic Curves
  - Canonical Divisor
  - Linear Systems
relations:
- kind: uses
  target: T-D8TUX
- kind: uses
  target: D-CRVGON
review: draft
prompts:
- What is a hyperelliptic curve?
- What does the canonical map do on a hyperelliptic curve?
- Is the $g^1_2$ on a hyperelliptic curve unique?
---

::: {.definition}
Let $C$ be a smooth projective curve of genus $g\geq2$ over an algebraically closed field $k$.
The curve $C$ is \dfn{hyperelliptic} if it admits a finite morphism $C \to \PP^1_k$ of degree $2$, equivalently a $g^1_2$.
:::

::: {.proposition}
A hyperelliptic curve has exactly one $g^1_2$.
The canonical system $\abs{K}$ is base-point free for every $g \geq 2$, so it always defines a morphism $C \to \PP^{g-1}$; on a hyperelliptic curve that morphism factors as
$$
C \to \PP^1 \to \PP^{g-1} ,
$$
the degree-two map followed by the $(g-1)$-uple embedding, whose image is a rational normal curve of degree $g-1$.
Equivalently $\abs{K} = (g-1)\, g^1_2$.
:::

::: {.remark}
For a hyperelliptic curve, the canonical map is two-to-one onto a rational normal curve instead of an embedding.

For every $p\in C$, one has $\ell(p)=1$: otherwise a nonconstant function with polar divisor bounded by $p$ would define a degree-one morphism $C\to\PP^1$, forcing $C\cong\PP^1$. Riemann--Roch therefore gives $\ell(K-p)=g-1$, so $\abs K$ is base-point free.
Similarly, Riemann--Roch gives
$$
\ell(K-p-q)=g-3+\ell(p+q).
$$
Thus the canonical system fails to separate some pair of points or tangent direction exactly when $\ell(p+q)=2$, equivalently when $p+q$ belongs to a $g^1_2$.

Every curve of genus $2$ is hyperelliptic, since $\abs{K}$ is then a $g^1_2$ outright.
If $\operatorname{char}k\ne2$, the degree-two map is tamely ramified at $2g+2$ points by Riemann--Hurwitz. Hence the hyperelliptic locus has dimension
$$
(2g+2)-\dim\PGL_2=2g-1;
$$
it is all of $\mathcal M_2$ and is a proper locus in $\mathcal M_g$ for $g\geq3$.
:::
