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

::: {.problem}
Given any map $f : S^n \to S^n$, let $\Gamma_f = \{(x, f(x)) : x \in S^n\} \subseteq S^n \times S^n$ be the graph of $f$.
By using the intersection theory of $S^n \times S^n$, calculate the intersection number $[\Gamma_{\operatorname{id}}] \cdot [\Gamma_f]$ and deduce that $f$ must have at least one fixed point provided $\deg f \neq (-1)^{n+1}$.
:::

::: {.solution}

::: pf

::: pf-step
Let
$$A=[S^n\times\{*\}],\qquad B=[\{*\}\times S^n]$$
be the standard basis of $H_n(S^n\times S^n;\mathbb Z)$.

::: pf-proof
Künneth gives $H_n(S^n\times S^n)\cong\mathbb Z\oplus\mathbb Z$ with these factor classes as generators.
:::

:::

::: pf-step
If $d=\deg f$, then
$$[\Gamma_f]=A+dB,\qquad [\Gamma_{\mathrm{id}}]=A+B.$$

::: pf-proof
The first projection restricts to a degree-$1$ map on every graph, while the second projection restricted to $\Gamma_f$ is $f$ and hence has degree $d$.
:::

:::

::: {.pf-step #intersection-pairing-formulas}
The middle-dimensional intersection pairing satisfies
$$A\cdot A=B\cdot B=0,\qquad A\cdot B=1,\qquad B\cdot A=(-1)^n.$$

::: pf-proof
The two factor cycles meet transversely in one point. Graded symmetry in an oriented $2n$-manifold gives $B\cdot A=(-1)^{n^2}A\cdot B=(-1)^n$.
:::

:::

::: {.pf-step #intersection-number-formula}
Therefore
$$\boxed{[\Gamma_{\mathrm{id}}]\cdot[\Gamma_f]=d+(-1)^n.}$$

::: pf-proof
Expand $(A+B)\cdot(A+dB)$ using step [](#intersection-pairing-formulas){.pf-ref}.
:::

:::

::: pf-step
If $d\ne(-1)^{n+1}$, then this intersection number is nonzero, so $\Gamma_f$ intersects $\Gamma_{\mathrm{id}}$.

::: pf-proof
Disjoint cycles have zero algebraic intersection number. The number in step [](#intersection-number-formula){.pf-ref} is nonzero exactly under the stated inequality.
:::

:::

::: pf-step
Any point of $\Gamma_f\cap\Gamma_{\mathrm{id}}$ has the form $(x,x)$ with $f(x)=x$. Hence $f$ has a fixed point.

::: pf-proof
This is immediate from the definitions of the two graphs.
:::

:::

:::

:::
