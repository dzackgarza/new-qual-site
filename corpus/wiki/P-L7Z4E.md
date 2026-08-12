---
schema: qual/card@1
id: P-L7Z4E
kind: problem
title: "Show there is no homeomorphism $\\CP^2 \\mapsvia{f} \\CP^2$ such that $f(\\CP^1)$ is disjoint from $\\CP_1 \\subset \\CP_2$."
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---

Show there is no homeomorphism $\CP^2 \mapsvia{f} \CP^2$ such that $f(\CP^1)$ is disjoint from $\CP_1 \subset \CP_2$.

::: {.solution}

\envlist
::: {.concept}
\envlist

1. Every homeomorphism induces isomorphisms on homotopy/homology/cohomology.

2. $H^*(\CP^2) = \ZZ[\alpha] / (\alpha^2)$ where $\deg \alpha = 2$.

3. $[f(X)] = f_*([X])$

4. $a\capprod b = 0 \implies a=0~\text{or}~b=0$ (nondegeneracy).
:::

Supposing such a homeomorphism exists, we would have $[\CP^1] \capprod [f(\CP^1)] = 0$ by the definition of these submanifolds being disjoint.
But $[\CP^1]\capprod[f(\CP^1)] = [\CP^1]\capprod f_*([\CP^1])$, where
\[
f_*: H^*(\CP^2) \to H^*(\CP^2)
\]
is the induced map on cohomology.
Since the intersection pairing is nondegenerate, either $[\CP^1] = 0$ or $f_*([\CP^1]) = 0$.
We know that $H^*(\CP^2) = \ZZ[\alpha] / \alpha^2$ where $\alpha = [\CP^1]$, however, so this forces $f_*([\CP^1]) = 0$.
But since this was a generator of $H^*$, we have $f_*(H^*(\CP^2)) = 0$, so $f$ is not an isomorphism on cohomology.
:::
