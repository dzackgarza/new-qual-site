---
schema: qual/card@1
id: P-24CMJ
kind: problem
title: $\pi_1(S^1\vee S^1)$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Compute the fundamental group $\pi_1(S^1 \vee S^1, x_0)$ of the wedge sum of two circles (the figure eight space).
:::

::: {.solution}

Let $X=S^1_a\vee S^1_b$ with wedge point $x_0$. Choose $p_a\in S^1_a\setminus\{x_0\}$ and $p_b\in S^1_b\setminus\{x_0\}$, and put $U=X\setminus\{p_b\}$ and $V=X\setminus\{p_a\}$.

::: pf

::: {.pf-step #pieces}

$U$ and $V$ are open path-connected sets containing $x_0$ with $\pi_1(U,x_0)\cong\ZZ$, $\pi_1(V,x_0)\cong\ZZ$, and $\pi_1(U\cap V,x_0)=1$.

::: pf-proof

$S^1_b\setminus\{p_b\}$ is an open arc through $x_0$, which deformation retracts to $x_0$; so $U$ deformation retracts onto $S^1_a$, and likewise $V$ onto $S^1_b$. The set $U\cap V$ is the union of two open arcs meeting at $x_0$, which deformation retracts to $x_0$.

:::

:::

::: pf-step

$\pi_1(S^1\vee S^1,x_0)\cong\boxed{\ZZ*\ZZ\cong F_2}$, free on the loops around the two circles.

::: pf-proof

$X=U\cup V$, so the Seifert--van Kampen theorem and step [](#pieces){.pf-ref} give $\pi_1(X,x_0)\cong\pi_1(U,x_0)*\pi_1(V,x_0)$, with generators the loops around $S^1_a$ and $S^1_b$.

:::

:::

:::

:::
