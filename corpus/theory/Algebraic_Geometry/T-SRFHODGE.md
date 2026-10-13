---
schema: qual/card@1
id: T-SRFHODGE
kind: theorem
title: The Hodge index theorem
slogan: 'On a smooth projective surface, an ample class gives the unique positive direction and its orthogonal complement is negative definite.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Hodge Index Theorem
  - Intersection Theory
  - Neron-Severi Group
relations:
- kind: uses
  target: D-SRFNS
review: draft
prompts:
- State the Hodge index theorem.
- What is the signature of the intersection form on a surface?
---

::: {.theorem}
Let $X$ be a smooth projective surface over an algebraically closed field, and let $H$ be an ample divisor.
If $D \cdot H = 0$ and $D \not\equiv 0$, then $D^2 < 0$.
Equivalently, the intersection form on $\NS(X) \otimes \RR$ has signature $(1, \rho - 1)$.
:::

::: {.remark}
Since $H^2>0$, the line $\RR H$ is a positive direction and
$$
H^\perp\subseteq\NS(X)_\RR
$$
is negative definite. Thus the numerical Néron--Severi space is a real quadratic space of signature $(1,\rho-1)$.

If $D^2>0$, then $D\cdot H\ne0$ for every ample $H$. After replacing $D$ by $-D$, one may therefore assume $D\cdot H>0$. Riemann--Roch then shows that $nD$ is effective for all sufficiently large $n$: the quadratic term in $\chi(\OO_X(nD))$ is positive, while $K_X-nD$ has negative intersection with $H$ and hence no effective representative for $n\gg0$.

For any $D,E\in\NS(X)_\RR$ with $D^2>0$,
$$
(D\cdot E)^2\geq D^2E^2,
$$
with equality exactly when $E$ is numerically proportional to $D$.

Over $\CC$ this is the Hodge--Riemann bilinear relation on $H^{1,1}$ specialised to the algebraic classes, which is where the name comes from.
:::
