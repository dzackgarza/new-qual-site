---
schema: qual/card@1
id: P-UCLAB03F-02
kind: problem
title: A uniform finite derivative order on a compact interval
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 of the official UCLA Basic Exam Fall 2003 PDF.
---

::: {.problem}
Let $f:\RR\to\RR$ be infinitely differentiable.
Assume that for each $x\in[0,1]$ there is a positive integer $m$ such that
\[
f^{(m)}(x)\ne0.
\]
Prove that there exists an integer $M$ such that, for every $x\in[0,1]$, there is a positive integer $m\leq M$ for which
\[
f^{(m)}(x)\ne0.
\]
:::

::: {.solution}

For each positive integer $m$, define
\[
U_m=\{x\in[0,1]:f^{(m)}(x)\ne0\}.
\]

::: pf

::: pf-step

Each $U_m$ is open in the subspace $[0,1]$.


::: pf-proof

The derivative $f^{(m)}$ is continuous because $f$ is infinitely differentiable. Hence
\[
U_m=(f^{(m)})^{-1}(\RR\setminus\{0\})\cap[0,1]
\]
is open in the subspace topology on $[0,1]$.

:::

:::

::: {.pf-step #s1-2}

The family
\[
\{U_m:m\ge1\}
\]
is an open cover of $[0,1]$.


::: pf-proof

By hypothesis, for every $x\in[0,1]$ there is a positive integer $m$ with
\[
f^{(m)}(x)\ne0.
\]
Equivalently, every $x$ belongs to at least one $U_m$.

:::

:::

::: {.pf-step #s1-3}

There are positive integers
\[
m_1,\ldots,m_r
\]
such that
\[
[0,1]=U_{m_1}\cup\cdots\cup U_{m_r}.
\]


::: pf-proof

The interval $[0,1]$ is compact. By step [](#s1-2){.pf-ref}, the sets $U_m$ form an open cover, so compactness gives a finite subcover.

:::

:::

::: {.pf-step #s1-4}

Let
\[
M=\max\{m_1,\ldots,m_r\}.
\]
Then for every $x\in[0,1]$ there is a positive integer $m\le M$ such that
\[
f^{(m)}(x)\ne0.
\]


::: pf-proof

Fix $x\in[0,1]$. By step [](#s1-3){.pf-ref}, $x\in U_{m_i}$ for some $i$. By the definition of $U_{m_i}$,
\[
f^{(m_i)}(x)\ne0.
\]
Since $m_i\le M$, taking $m=m_i$ proves the claim.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is exactly the required uniform finite bound on the derivative order.

:::

:::

:::
