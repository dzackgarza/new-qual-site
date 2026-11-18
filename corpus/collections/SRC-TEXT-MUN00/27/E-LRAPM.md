---
schema: qual/card@1
id: E-LRAPM
kind: problem
title: Compact closed intervals imply the least upper bound property
classification:
  areas:
  - topology
  topics:
  - Order Topology
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §27 Exercise 1, printed p. 177, with Theorem 27.4
    and Theorem 26.2; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 27.1, PDF pp. 15-16. The closure of a bounded set
    is compact, the identity attains a maximum there, and that maximum is the least upper
    bound. (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Prove that if $X$ is an ordered set in which every closed interval is compact, then $X$ has the least upper bound property.
:::

::: {.solution}

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 27.1, PDF pp. 15--16** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the extremal-point argument is theirs. Their last paragraph uses intervals $(c-\varepsilon,c+\varepsilon)$, which a general ordered set does not have; the open ray $(c,\infty)$ replaces it below, and that is the whole of the change.

Let $X$ be an ordered set in the order topology in which every closed interval is compact, let $A\subseteq X$ be nonempty and let $u$ be an upper bound of $A$.

::: pf

::: {.pf-step #compact-closure}
For $a\in A$ the closure $\overline A$ is a closed subset of the compact interval $[a,u]$, hence compact.

::: pf-proof
$A\subseteq[a,u]$, so $\overline A\subseteq\overline{[a,u]}=[a,u]$, the interval being closed in the order topology; $[a,u]$ is compact by hypothesis, and a closed subset of a compact space is compact (Theorem 26.2, printed p. 165).
:::

:::

::: {.pf-step #max}
The inclusion $\overline A\to X$, $x\mapsto x$, attains a maximum at some $b\in\overline A$.

::: pf-proof
The inclusion is continuous (Theorem 18.2(b), printed p. 107), $\overline A$ is compact by step [](#compact-closure){.pf-ref}, and $X$ is an ordered set in the order topology; so the extreme value theorem (Theorem 27.4, printed p. 174) gives $b\in\overline A$ with $x\le b$ for all $x\in\overline A$. In particular $a\le b$ for all $a\in A$, so $b$ is an upper bound of $A$.
:::

:::

::: {.pf-step #least}
$b$ is the least upper bound of $A$.

::: pf-proof
Let $c<b$ be any upper bound of $A$. Then $(c,\infty)$ is an open set of $X$ containing $b$, and it contains no point of $A$, since every $a\in A$ satisfies $a\le c$. So $X\setminus(c,\infty)$ is a closed set containing $A$ and missing $b$, contradicting $b\in\overline A$. Hence no $c<b$ bounds $A$ above, and $b$, an upper bound by step [](#max){.pf-ref}, is the least one.
:::

:::

::: {.pf-qed}
Every nonempty subset of $X$ with an upper bound has a least upper bound, by steps [](#max){.pf-ref} and [](#least){.pf-ref}: $X$ has the least upper bound property.
:::

:::

:::
