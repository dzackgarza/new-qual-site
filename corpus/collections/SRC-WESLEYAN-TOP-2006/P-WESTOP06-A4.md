---
schema: qual/card@1
id: P-WESTOP06-A4
kind: problem
title: The interval is injective among compact Hausdorff spaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $C$ be the class of compact Hausdorff spaces. Call $I\in C$ *injective in $C$* if whenever $X,Y\in C$, $X\subseteq Y$, and $f:X\to I$ is continuous, there is a continuous extension
\[
\overline f:Y\to I.
\]
Explain why $[0,1]$ is injective in $C$.
:::

::: {.solution}
<1>1. The subspace \(X\) is closed in \(Y\).

::: {.proof}
The space \(X\) is compact because \(X\in C\), and \(Y\) is Hausdorff because \(Y\in C\). Every compact subset of a Hausdorff space is closed, so \(X\subseteq Y\) is closed.
:::

<1>2. The space \(Y\) is normal.

::: {.proof}
Every compact Hausdorff space is normal, and \(Y\in C\).
:::

<1>3. The map \(f:X\to[0,1]\) has a continuous extension
\[
\boxed{\overline f:Y\to[0,1].}
\]

::: {.proof}
By steps <1>1 and <1>2, \(X\) is a closed subspace of the normal space \(Y\). The bounded form of the Tietze extension theorem therefore extends the continuous map \(f:X\to[0,1]\subset\mathbb R\) to a continuous map \(\overline f:Y\to[0,1]\).
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 supplies the required extension for arbitrary \(X,Y\in C\) with \(X\subseteq Y\) and arbitrary continuous \(f:X\to[0,1]\). Hence \([0,1]\) is injective in \(C\).
:::
:::
