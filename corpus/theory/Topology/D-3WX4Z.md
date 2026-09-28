---
schema: qual/card@1
id: D-3WX4Z
kind: definition
title: Split short exact sequence
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Groups
relations: []
review: draft
---

::: {.definition}
Let
$$
1 \to A \mapsvia{f} B \mapsvia{g} C \to 1
$$
be a [[D-SIUWU|short exact sequence]] of groups.
The sequence \dfn{splits} if there exists a homomorphism $s\colon C\to B$ with $g\circ s = \id_C$.
:::

::: {.remark}
For a short exact sequence $0\to A\mapsvia{f} B\mapsvia{g} C\to 0$ of abelian groups, or more generally of modules over a ring, the following are equivalent: the sequence splits; there exists a homomorphism $r\colon B\to A$ with $r\circ f = \id_A$; there exists an isomorphism $B\cong A\oplus C$ under which $f$ is the inclusion of $A$ and $g$ is the projection onto $C$.
For groups, if $s$ splits the sequence, then $B \cong A\rtimes_\varphi C$, where $\varphi\colon C\to\Aut(A)$ is given by $f(\varphi(c)(a)) = s(c)\,f(a)\,s(c)^{-1}$.
:::

::: {.concept}
[@DF04].
:::
