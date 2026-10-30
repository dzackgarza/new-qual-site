---
schema: qual/card@1
id: P-UCTOP-SU11-6
kind: problem
title: Space with free fundamental group and no higher homotopy is a bouquet of circles
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source states the result for any topological space X, which is false (the Warsaw circle is weakly contractible but not contractible). The statement now assumes X is a CW complex.
---

::: {.problem}
Let $X$ be a path-connected space with $\pi_{\geq 2}(X) = 0$ and whose fundamental group is a free group on a set $S$.
Show that there is a homotopy equivalence between a bouquet of circles, indexed by $S$, and $X$.
:::

::: {.solution}

::: pf

::: pf-step
There is a map $f:\bigvee_{s\in S}S^1_s\to X$ sending the $s$-th circle to a loop representing the free generator $s$.

::: pf-proof
Let
$$B=\bigvee_{s\in S}S^1_s.$$
Choose for each free generator $s\in\pi_1(X)$ a based loop $\gamma_s:S^1\to X$, and let
$$f:B\to X$$
be the map whose restriction to the $s$-th circle is $\gamma_s$.
:::

:::

::: {.pf-step #f-weak-equivalence}
The map $f$ induces an isomorphism on every homotopy group.

::: pf-proof
By construction,
$$f_*:\pi_1(B)\cong F(S)\longrightarrow\pi_1(X)\cong F(S)$$
is the isomorphism sending each standard free generator to the chosen generator with the same name. The universal cover of a graph is a tree, so $\pi_n(B)=0$ for every $n\ge2$. These groups agree with the assumed groups $\pi_n(X)=0$ for $n\ge2$. Both spaces are path connected, so $f$ is a weak homotopy equivalence.
:::

:::

::: pf-step
Therefore
$$\boxed{X\simeq\bigvee_{s\in S}S^1}.$$

::: pf-proof
Whitehead's theorem upgrades the weak homotopy equivalence $f$ from step [](#f-weak-equivalence){.pf-ref} to a homotopy equivalence when $X$ has the homotopy type of a CW complex, which is the setting of the question: $B$ is a CW complex, and a weak equivalence between spaces of CW homotopy type is a homotopy equivalence. For an arbitrary path-connected space, $f$ is a weak homotopy equivalence, and a CW approximation of $X$ is homotopy equivalent to $B$.
:::

:::

:::

:::
