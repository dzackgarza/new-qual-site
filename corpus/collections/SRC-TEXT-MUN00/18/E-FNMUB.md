---
schema: qual/card@1
id: E-FNMUB
kind: problem
title: Uniqueness of continuous extensions into Hausdorff spaces
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Let $A \subset X$; let $f: A \to Y$ be continuous; let $Y$ be Hausdorff.
Show that if $f$ may be extended to a continuous function $g: \overline{A} \to Y$, then $g$ is uniquely determined by $f$.
:::

::: {.solution}
Let $g_1,g_2\colon\overline A\to Y$ be continuous with $g_1|_A=g_2|_A=f$, and put $E=\{x\in\overline A:g_1(x)=g_2(x)\}$.

<1>1. $E$ is closed in $\overline A$ and contains $A$.

::: {.proof}
The map $h\colon\overline A\to Y\times Y$, $h(x)=(g_1(x),g_2(x))$, is continuous because its coordinates are.
Since $Y$ is Hausdorff, the diagonal $\Delta\subseteq Y\times Y$ is closed by [[E-6A0RO]], so $E=h^{-1}(\Delta)$ is closed in $\overline A$.
For $a\in A$, $g_1(a)=f(a)=g_2(a)$, so $A\subseteq E$.
:::

<1>2. Q.E.D.

::: {.proof}
The closure of $A$ in the subspace $\overline A$ is $\overline A\cap\overline A=\overline A$.
By step <1>1, $E$ is a closed subset of $\overline A$ containing $A$, so $\overline A\subseteq E$.
Hence $g_1=g_2$ on $\overline A$.
:::
:::
