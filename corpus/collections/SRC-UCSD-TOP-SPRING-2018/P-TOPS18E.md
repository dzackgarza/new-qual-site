---
schema: qual/card@1
id: P-TOPS18E
kind: problem
title: "Intersection number of the graph of a self-map of S^n with the diagonal"
classification:
  areas:
  - topology
  topics:
  - Intersection Theory
  - Fixed Point Theory
  - Spheres
relations: []
review: draft
---

::: problem
Given any map $f : S^n \to S^n$, let $\Gamma_f = \{(x, f(x)) : x \in S^n\} \subseteq S^n \times S^n$ be the graph of $f$.
By using the intersection theory of $S^n \times S^n$, calculate the intersection number $[\Gamma_{\operatorname{id}}] \cdot [\Gamma_f]$ and deduce that $f$ must have at least one fixed point provided $\deg f \neq (-1)^{n+1}$.
:::

::: {.solution}
<1>1. Let
$$A=[S^n\times\{*\}],\qquad B=[\{*\}\times S^n]$$
be the standard basis of $H_n(S^n\times S^n;\mathbb Z)$.
::: {.proof}
Künneth gives $H_n(S^n\times S^n)\cong\mathbb Z\oplus\mathbb Z$ with these factor classes as generators.
:::

<1>2. If $d=\deg f$, then
$$[\Gamma_f]=A+dB,\qquad [\Gamma_{\mathrm{id}}]=A+B.$$
::: {.proof}
The first projection restricts to a degree-$1$ map on every graph, while the second projection restricted to $\Gamma_f$ is $f$ and hence has degree $d$.
:::

<1>3. The middle-dimensional intersection pairing satisfies
$$A\cdot A=B\cdot B=0,\qquad A\cdot B=1,\qquad B\cdot A=(-1)^n.$$
::: {.proof}
The two factor cycles meet transversely in one point. Graded symmetry in an oriented $2n$-manifold gives $B\cdot A=(-1)^{n^2}A\cdot B=(-1)^n$.
:::

<1>4. Therefore
$$\boxed{[\Gamma_{\mathrm{id}}]\cdot[\Gamma_f]=d+(-1)^n.}$$
::: {.proof}
Expand $(A+B)\cdot(A+dB)$ using <1>3.
:::

<1>5. If $d\ne(-1)^{n+1}$, then this intersection number is nonzero, so $\Gamma_f$ intersects $\Gamma_{\mathrm{id}}$.
::: {.proof}
Disjoint cycles have zero algebraic intersection number. The number in <1>4 is nonzero exactly under the stated inequality.
:::

<1>6. Any point of $\Gamma_f\cap\Gamma_{\mathrm{id}}$ has the form $(x,x)$ with $f(x)=x$. Hence $f$ has a fixed point.
::: {.proof}
This is immediate from the definitions of the two graphs.
:::
:::
