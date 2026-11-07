---
schema: qual/card@1
id: E-HAT-2.2-6
kind: problem
title: Every map $S^n \to S^n$ can be homotoped to have a fixed point
classification:
  areas:
  - topology
  topics:
  - Degree
  - Fixed Point Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 6; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof reviewed using degree theory and orthogonal-group homotopies.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: $SO(n+1)$ acts transitively on $S^n$ and is path connected for $n\ge1$, so
    $R_t\circ f$ runs from $f$ to a map carrying $f(x_0)$ to $x_0$.
---

::: {.problem}
Show that every map $S^n \to S^n$ can be homotoped to have a fixed point if $n > 0$.
:::

::: {.solution}
Let $f:S^n\to S^n$ with $n>0$, and choose a point $x_0\in S^n$.

::: pf

::: {.pf-step #s1}

There is a continuous path of orthogonal transformations $R_t$ of $\RR^{n+1}$, $t\in[0,1]$, with $R_0=\id$ and $R_1(f(x_0))=x_0$.

::: pf-proof

If $f(x_0)=x_0$ take $R_t=\id$. Otherwise put $e_1=f(x_0)$. If $f(x_0)\neq -x_0$, let $e_2$ be the normalization of $x_0-\langle x_0,e_1\rangle e_1$, so that $e_1,e_2$ are orthonormal and $x_0=\cos\theta\,e_1+\sin\theta\,e_2$ with $\theta\in(0,\pi)$; if $f(x_0)=-x_0$, let $e_2$ be any unit vector orthogonal to $e_1$ and set $\theta=\pi$, which is possible because $n+1\ge2$. Let $V$ be the plane spanned by $e_1,e_2$ and let $R_t$ rotate $V$ by the angle $t\theta$, carrying $e_1$ to $\cos t\theta\,e_1+\sin t\theta\,e_2$, and fix $V^\perp$ pointwise. Each $R_t$ is orthogonal and depends continuously on $t$, $R_0=\id$, and $R_1(e_1)=x_0$, that is $R_1(f(x_0))=x_0$.

:::

:::

::: {.pf-step #s2}

The maps $f_t=R_t\circ f$ form a homotopy from $f$ to a map having $x_0$ as a fixed point.

::: pf-proof

A homotopy is a continuous family of maps indexed by $t\in[0,1]$ with the stated endpoints (Hatcher p. 3), and $R_t\circ f$ is such a family. At $t=0$ it is $f$, and at $t=1$ it sends $x_0$ to $R_1(f(x_0))=x_0$.

:::

:::

:::

Hence every map $S^n\to S^n$ with $n>0$ is homotopic to a map with a fixed point.
:::
