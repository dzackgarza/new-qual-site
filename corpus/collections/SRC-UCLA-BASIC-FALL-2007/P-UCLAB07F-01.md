---
schema: qual/card@1
id: P-UCLAB07F-01
kind: problem
title: Closed distance superlevel sets and their strict superlevel closures
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Fall 2007 PDF.
---

::: {.problem}
Let $S\subseteq\mathbb R^n$, equipped with the Euclidean distance restricted to $S$.
Fix $y\in S$ and $r\in\mathbb R$.

(a) Is $E=\{x\in S:d(x,y)\ge r\}$ closed in $S$?

(b) Is $E$ contained in the closure in $S$ of $\{x\in S:d(x,y)>r\}$?

Prove your answers.
:::

Let
\[
\delta_y:S\to\mathbb R,
\qquad
\delta_y(x)=d(x,y).
\]

::: pf

::: pf-step

The function $\delta_y$ is continuous.


::: pf-proof

For all $x,z\in S$, the triangle inequality gives
\[
d(x,y)\le d(x,z)+d(z,y)
\]
and
\[
d(z,y)\le d(z,x)+d(x,y).
\]
Hence
\[
|d(x,y)-d(z,y)|\le d(x,z).
\]
Thus $\delta_y$ is $1$-Lipschitz, and therefore continuous.

:::

:::

::: pf-step

The set
\[
E=\{x\in S:d(x,y)\ge r\}
\]
is closed in $S$.


::: pf-proof

By step <1>1,
\[
E=\delta_y^{-1}([r,\infty)).
\]
The interval $[r,\infty)$ is closed in $\mathbb R$, and the inverse image of a closed set under a continuous map is closed. Hence
\[
\boxed{E\text{ is closed in }S}.
\]

:::

:::

::: pf-step

In general,
\[
E\not\subseteq
\overline{\{x\in S:d(x,y)>r\}}^{\,S}.
\]


::: pf-proof

Take
\[
S=\{0,1\}\subseteq\mathbb R,
\qquad
y=0,
\qquad
r=1.
\]
Then
\[
E
=
\{x\in S:|x|\ge1\}
=
\{1\}.
\]
But
\[
\{x\in S:|x|>1\}
=
\varnothing,
\]
whose closure in $S$ is still empty. Therefore
\[
E=\{1\}
\not\subseteq
\varnothing
=
\overline{\{x\in S:d(x,y)>1\}}^{\,S}.
\]
Thus the answer to part (b) is no in general.

:::

:::

::: pf-qed

Step <1>2 answers part (a) affirmatively, and step <1>3 gives a counterexample to part (b).

:::

:::
