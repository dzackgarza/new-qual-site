---
schema: qual/card@1
id: P-BKF18-9A
kind: problem
title: Cauchy's theorem for elements of prime order
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Suppose a prime $p$ divides the order of a finite group $G$.
Prove that there exists an element $g\in G$ of order $p$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $X=\{(g_1,\dots,g_p)\in G^p: g_1\cdots g_p=e\}$. Then $\abs{X}=\abs{G}^{p-1}$, and $\ZZ/p\ZZ$ acts on $X$ by cyclic shift $(g_1,\dots,g_p)\mapsto(g_p,g_1,\dots,g_{p-1})$.

::: pf-proof

The first $p-1$ entries are arbitrary and determine $g_p=(g_1\cdots g_{p-1})^{-1}$. If $g_1\cdots g_p=e$, then $g_p(g_1\cdots g_{p-1})=g_p\,g_p^{-1}=e$, so the shift preserves $X$; applying it $p$ times is the identity.

:::

:::

::: {.pf-step #s2}

The number of fixed points of the action is divisible by $p$, and the fixed points are the tuples $(g,\dots,g)$ with $g^p=e$.

::: pf-proof

Every orbit of a group of order $p$ has size $1$ or $p$, so $\abs{X}\equiv\#\{\text{fixed points}\}\pmod p$, and $p\mid\abs{G}^{p-1}$ because $p\mid\abs{G}$ and $p-1\ge1$. A tuple fixed by the shift has all entries equal.

:::

:::

::: pf-qed

The tuple $(e,\dots,e)$ is fixed, so by step [](#s2){.pf-ref} there are at least $p\ge2$ fixed points, hence some $(g,\dots,g)$ with $g\ne e$ and $g^p=e$. Since $p$ is prime, $g$ has order $p$.

:::

:::

:::
