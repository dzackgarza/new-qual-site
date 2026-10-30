---
schema: qual/card@1
id: P-PJA4A
kind: problem
title: Unique quadratic subfield of a Galois extension of degree $14$, and two distinct
  degree-$7$ subfields imply a nonabelian Galois group
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Suppose that $F\subset E$ are fields such that $E/F$ is Galois and $\abs{\gal(E/F)} = 14$.

a. Show that there exists a unique intermediate field $K$ with $F\subset K \subset E$ such that $[K: F] = 2$.

b. Assume that there are at least two distinct intermediate subfields $F \subset L_1, L_2 \subset E$ with $[L_i: F]= 7$.
Prove that $\gal(E/F)$ is nonabelian.
:::

::: {.solution}

Let $G=\operatorname{Gal}(E/F)$, with $\cardinality{G}=14$.

::: pf

::: {.pf-step #s1-1}

There exists exactly one intermediate field of degree two over $F$.


::: pf-proof

By the Galois correspondence, a field $K$ with $[K:F]=2$ corresponds to a subgroup $\operatorname{Gal}(E/K)$ of order $[E:K]=7$. The Sylow number $n_7$ satisfies $n_7\mid2$ and $n_7\equiv1\pmod7$, forcing $n_7=1$. Thus there is exactly one subgroup of order seven and exactly one corresponding quadratic intermediate field.

:::

:::

::: {.pf-step #s1-2}

If there exist two distinct intermediate fields of degree seven over $F$, then $G$ is nonabelian.


::: pf-proof

The two fields correspond to distinct subgroups $H_1,H_2\leq G$ of order two by the Galois correspondence. Both are Sylow $2$-subgroups. If $G$ were abelian, all subgroups would be normal, and Sylow conjugacy would force all Sylow $2$-subgroups to coincide, contrary to $H_1\neq H_2$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} prove parts (a) and (b), respectively.

:::

:::

:::
