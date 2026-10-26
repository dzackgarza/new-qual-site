---
schema: qual/card@1
id: P-UCLAB02F-03
kind: problem
title: A subset of $\mathbb R$ that is not a $G_\delta$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 of the retained UCLA Basic Examination, Fall 2002 PDF.
---

::: {.problem}
Show that there is a subset of the real numbers that is not the intersection of a countable collection of open subsets of $\mathbb R$.
:::

Take
\[
S=\mathbb Q.
\]

::: pf

::: pf-step

Suppose, for contradiction, that
\[
\mathbb Q=\bigcap_{n=1}^{\infty}U_n
\]
for open sets $U_n\subseteq\mathbb R$.


::: pf-proof

This is the negation of the desired claim for the proposed example $S=\mathbb Q$.

:::

:::

::: pf-step

Every $U_n$ is dense in $\mathbb R$.


::: pf-proof

Since
\[
\mathbb Q\subseteq U_n
\]
for every $n$ and $\mathbb Q$ is dense in $\mathbb R$, the closure of $U_n$ contains
\[
\overline{\mathbb Q}=\mathbb R.
\]
Hence $U_n$ is dense.

:::

:::

::: pf-step

If
\[
\mathbb Q=\{q_1,q_2,\ldots\},
\]
then every set
\[
V_m=\mathbb R\setminus\{q_m\}
\]
is open and dense in $\mathbb R$.


::: pf-proof

Each singleton $\{q_m\}$ is closed and has empty interior. Therefore its complement $V_m$ is open and dense.

:::

:::

::: pf-step

The intersection
\[
\bigcap_{n=1}^{\infty}U_n
\cap
\bigcap_{m=1}^{\infty}V_m
\]
is nonempty.


::: pf-proof

By steps <1>2--<1>3, all sets appearing in the two countable families are open and dense in $\mathbb R$. Since $\mathbb R$ is a complete metric space, the Baire category theorem implies that the intersection of these countably many open dense sets is dense, hence nonempty.

:::

:::

::: pf-step

The intersection in step <1>4 is empty.


::: pf-proof

By step <1>1,
\[
\bigcap_{n=1}^{\infty}U_n=\mathbb Q.
\]
By the definition of the sets $V_m$,
\[
\bigcap_{m=1}^{\infty}V_m
=
\mathbb R\setminus\mathbb Q.
\]
Their intersection is therefore empty.

:::

:::

::: pf-step

The set $\mathbb Q$ is not a countable intersection of open subsets of $\mathbb R$.


::: pf-proof

Steps <1>4 and <1>5 contradict the assumption in step <1>1. Hence no such family $(U_n)$ exists.

:::

:::

::: pf-qed

Step <1>6 supplies the required subset of $\mathbb R$.

:::

:::
