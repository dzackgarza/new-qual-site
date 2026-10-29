---
schema: qual/card@1
id: P-UCLAB08S-07
kind: problem
title: A summable family on an arbitrary set has countable support
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 7 of the retained UCLA Basic Examination, Spring 2008.
---

::: {.problem}
Let $a\colon\RR\to[0,\infty)$ satisfy the following bounded-finite-sum condition: there exists $M<\infty$ such that
\[
\sum_{x\in F}a(x)\le M
\]
for every finite set $F\subset\RR$.
Prove that
\[
\{x\in\RR:a(x)>0\}
\]
is countable.
:::

::: {.solution}

For each positive integer $n$, define
\[
E_n
=
\left\{
x\in\RR:
a(x)\ge\frac1n
\right\}.
\]

::: pf

::: {.pf-step #s1-1}

Each set $E_n$ is finite.


::: pf-proof

Suppose some $E_n$ were infinite.
Then for every positive integer $N$, one could choose a finite subset
\[
F\subseteq E_n
\]
with
\[
|F|=N.
\]
For such an $F$,
\[
\sum_{x\in F}a(x)
\ge
\sum_{x\in F}\frac1n
=
\frac{N}{n}.
\]
Choose
\[
N>nM.
\]
Then
\[
\frac{N}{n}>M,
\]
contradicting the hypothesis that every finite sum is at most $M$.
Therefore $E_n$ must be finite.

:::

:::

::: {.pf-step #s1-2}

Every point $x$ with
\[
a(x)>0
\]
belongs to some $E_n$.


::: pf-proof

Fix $x$ with
\[
a(x)>0.
\]
Choose a positive integer $n$ satisfying
\[
n\ge \frac1{a(x)}.
\]
Then
\[
\frac1n\le a(x),
\]
so
\[
x\in E_n.
\]

:::

:::

::: {.pf-step #s1-3}

One has
\[
\{x\in\RR:a(x)>0\}
=
\bigcup_{n=1}^{\infty}E_n.
\]


::: pf-proof

If $x\in E_n$, then
\[
a(x)\ge\frac1n>0,
\]
so
\[
x
\]
belongs to the set on the left.
Conversely, step [](#s1-2){.pf-ref} shows that every point on the left belongs to at least one $E_n$.
Thus the sets are equal.

:::

:::

::: {.pf-step #s1-4}

Therefore
\[
\boxed{
\{x\in\RR:a(x)>0\}
\text{ is countable}.
}
\]


::: pf-proof

By step [](#s1-1){.pf-ref}, each $E_n$ is finite.
By step [](#s1-3){.pf-ref}, the support of $a$ is a countable union of finite sets.
Every countable union of finite sets is countable.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
