---
schema: qual/card@1
id: D-ZVY6X
kind: definition
title: Local degree
classification:
  areas:
  - topology
  topics:
  - Degree
  - Homology
relations: []
review: draft
---

::: {.definition}
Let $n\geq 1$, let $f\colon S^n\to S^n$ be a continuous map, and let $y\in S^n$ be a point whose preimage $f\inv(y) = \ts{x_1, \ldots, x_m}$ is finite.
Homology is taken with coefficients in $\ZZ$.
Choose an open neighborhood $V$ of $y$ and disjoint open neighborhoods $U_i$ of $x_i$ with $f(U_i)\subseteq V$, and fix a generator of $H_n(S^n)$.
Then $f$ restricts to maps of pairs $f_i\colon (U_i, U_i\sm\ts{x_i})\to (V, V\sm\ts{y})$, and under the isomorphisms
$$
H_n(U_i, U_i\sm\ts{x_i})\cong H_n(S^n, S^n\sm\ts{x_i})\cong H_n(S^n)\cong\ZZ, \qquad H_n(V, V\sm\ts{y})\cong H_n(S^n, S^n\sm\ts{y})\cong H_n(S^n)\cong\ZZ
$$
given by excision and the long exact sequence of the pair, the induced homomorphism $f_{i*}$ is multiplication by an integer.
This integer is the \dfn{local degree} $\deg f\vert_{x_i}$ of $f$ at $x_i$.
:::

::: {.proposition}
In the setting of the definition, $\deg f = \sum_{i=1}^m \deg f\vert_{x_i}$, where $\deg f$ is the [[D-XC53X|degree]] of $f$.
:::

::: {.concept}
[@Hat02, §2.2, Proposition 2.30].
:::
