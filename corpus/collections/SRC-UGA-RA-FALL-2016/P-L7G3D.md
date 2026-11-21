---
schema: qual/card@1
id: P-L7G3D
kind: problem
title: If $\mu(X\setminus E_n)\to 0$ then almost every point lies in infinitely many
  $E_n$
classification:
  areas:
  - real-analysis
  topics:
  - Borel-Cantelli
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 4 of the official UGA August 2016 real-analysis qualifying exam; repaired the legacy proof, whose final summability step was invalid.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the proof into Lamport steps and checked it: G is the countable union of the
    tail intersections F_N, hence measurable; F_N is contained in every E_m^c with m >= N, so
    mu(F_N) is bounded by a sequence tending to 0 and vanishes; countable subadditivity then
    gives mu(G) = 0. The prose's "letting m tend to infinity" is now the explicit argument that
    a constant bounded by a null sequence is zero.
---

::: {.problem}
Let $(X, \mathcal M, \mu)$ be a measure space and suppose $\theset{E_n} \subset \mathcal M$ satisfies
$$
\lim _{n \rightarrow \infty} \mu\left(X \backslash E_{n}\right)=0.
$$

Define
$$
G \coloneqq \theset{x\in X \suchthat x\in E_n \text{ for only finitely many  } n}.
$$

Show that $G \in \mathcal M$ and $\mu(G) = 0$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.
Put $F_N\coloneqq\bigcap_{n\ge N}E_n^{c}$ for $N\ge1$.

::: pf

::: {.pf-step #description}
$G=\bigcup_{N\ge1}F_N$, and each $F_N$ is measurable.

::: pf-proof
A point $x$ lies in $E_n$ for only finitely many $n$ exactly when there is an $N$ with $x\notin E_n$ for all $n\ge N$; that is $x\in F_N$. Each $E_n^c$ is measurable, so the countable intersection $F_N$ and the countable union $G$ are measurable.
:::

:::

::: {.pf-step #monotone}
For $m\ge N$, $F_N\subseteq E_m^c$ and hence $\mu(F_N)\le\mu(X\setminus E_m)$.

::: pf-proof
$F_N$ is the intersection of the sets $E_n^c$ over $n\ge N$, so it is contained in the factor indexed by $m$ whenever $m\ge N$; monotonicity of $\mu$ gives the inequality.
:::

:::

::: {.pf-step}
$\mu(F_N)=0$ for every $N$.

::: pf-proof
By step [](#monotone){.pf-ref}, $0\le\mu(F_N)\le\mu(X\setminus E_m)$ for every $m\ge N$. The hypothesis says $\mu(X\setminus E_m)\to0$, so the right side tends to $0$ along $m\to\infty$, and a nonnegative constant bounded by a sequence tending to $0$ is $0$.
:::

:::

::: {.pf-step}
$G\in\mathcal M$ and $\mu(G)=0$.

::: pf-proof
Measurability is step [](#description){.pf-ref}. By countable subadditivity and the vanishing of each $\mu(F_N)$,
$$
\mu(G)=\mu\left(\bigcup_N F_N\right)\le\sum_{N\ge1}\mu(F_N)=0,
$$
so $\mu(G)=0$. No summability hypothesis on $\mu(X\setminus E_n)$ is used: it suffices that each $F_N$ is caught by a single tail set.
:::

:::

:::
:::
