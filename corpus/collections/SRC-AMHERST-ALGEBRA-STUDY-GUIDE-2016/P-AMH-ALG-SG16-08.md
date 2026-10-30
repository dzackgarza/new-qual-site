---
schema: qual/card@1
id: P-AMH-ALG-SG16-08
kind: problem
title: $x^{42}\in N$ for a normal subgroup $N$ of index 42
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
Let $G$ be a group, let $N\subseteq G$ be a normal subgroup, and suppose that $[G:N]=42$, where $[G:N]$ denotes the index of $N$ in $G$.
Prove that $x^{42}\in N$ for every $x\in G$.
(Suggestion: Consider the quotient group $G/N$.)
:::

::: {.solution}

::: pf

::: pf-step
The quotient group $G/N$ has order $42$.

::: pf-proof
Since $N\trianglelefteq G$ and
$$
[G:N]=42,
$$
the quotient is defined and satisfies
$$
\cardinality{G/N}=[G:N]=42.
$$
:::

:::

::: {.pf-step #s1-2}
For every $x\in G$,
$$
(xN)^{42}=N
$$
in $G/N$.

::: pf-proof
By Lagrange's theorem, the order of the element $xN\in G/N$ divides
$$
\cardinality{G/N}=42.
$$
Hence its $42$-nd power is the identity coset $N$.
:::

:::

::: pf-step
Therefore
$$
\boxed{x^{42}\in N}
$$
for every $x\in G$.

::: pf-proof
By the quotient-group multiplication law,
$$
(xN)^{42}=x^{42}N.
$$
Step [](#s1-2){.pf-ref} gives
$$
x^{42}N=N,
$$
which is equivalent to $x^{42}\in N$.
:::

:::

:::

:::
