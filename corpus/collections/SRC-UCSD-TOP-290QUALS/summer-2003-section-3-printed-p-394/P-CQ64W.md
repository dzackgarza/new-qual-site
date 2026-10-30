---
schema: qual/card@1
id: P-CQ64W
kind: problem
title: Universal cover of $(S^1\times S^1)\vee S^2$ and $\pi_2$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Homotopy
  - Homology
relations: []
review: draft
---

::: {.problem}
Describe the universal cover of $X = (S^1 \times S^1) \vee S^2$, and use it to compute the abelian group $\pi_2(X)$.
:::

::: {.solution}

::: pf

::: {.pf-step #cover}

The universal cover of $X$ is $\tilde X = \RR^2 \cup \bigcup_{(i,j)\in\ZZ^2} S^2_{i,j}$, the plane with one copy of $S^2$ wedged on at each lattice point.

::: pf-proof

$\pi_1(X) \cong \pi_1(T^2) \cong \ZZ^2$ by van Kampen, since $S^2$ is simply connected.
The space $\tilde X$ maps to $X$ by the covering $\RR^2 \to T^2$ on the plane and by the identity of each sphere onto $S^2$; this is a covering map because each sphere is attached at a lift of the wedge point.
$\tilde X$ is simply connected by van Kampen, since $\RR^2$ and every $S^2$ are simply connected.

:::

:::

::: {.pf-step #homotopy}

$\tilde X \simeq \bigvee_{\ZZ^2} S^2$.

::: pf-proof

Give $\RR^2$ the CW structure of the integer grid and let $A \subset \RR^2$ be the union of the $x$-axis and the vertical lines through integer points, a contractible subcomplex containing all lattice points.
Collapsing a contractible subcomplex is a homotopy equivalence, so $\tilde X \simeq \tilde X/A = (\RR^2/A)\vee\bigvee_{\ZZ^2}S^2$, and $\RR^2/A \simeq \RR^2$ is contractible by the same fact.

:::

:::

::: pf-qed

A covering map induces isomorphisms on $\pi_n$ for $n\ge 2$, and $\bigvee_{\ZZ^2}S^2$ is simply connected, so by Hurewicz and Step [](#homotopy){.pf-ref}
$$
\pi_2(X)\cong\pi_2(\tilde X)\cong H_2(\tilde X)\cong \bigoplus_{\ZZ^2}\ZZ,
$$
a free abelian group of countably infinite rank. As a $\ZZ[\pi_1 X]$-module it is free of rank one, $\ZZ[t_1^{\pm1}, t_2^{\pm1}]$.

:::

:::

:::
