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
Let $S\subseteq\RR^n$, equipped with the Euclidean distance restricted to $S$.
Fix $y\in S$ and $r\in\RR$.

(a) Is $E=\{x\in S:d(x,y)\ge r\}$ closed in $S$?

(b) Is $E$ contained in the closure in $S$ of $\{x\in S:d(x,y)>r\}$?

Prove your answers.
:::

::: {.solution}

Let
\[
\delta_y:S\to\RR,
\qquad
\delta_y(x)=d(x,y).
\]

::: pf

::: {.pf-step #s1-1}

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

::: {.pf-step #s1-2}

The set
\[
E=\{x\in S:d(x,y)\ge r\}
\]
is closed in $S$.


::: pf-proof

By step [](#s1-1){.pf-ref},
\[
E=\delta_y^{-1}([r,\infty)).
\]
The interval $[r,\infty)$ is closed in $\RR$, and the inverse image of a closed set under a continuous map is closed. Hence
\[
\boxed{E\text{ is closed in }S}.
\]

:::

:::

::: {.pf-step #s1-3}

In general,
\[
E\not\subseteq
\overline{\{x\in S:d(x,y)>r\}}^{\,S}.
\]


::: pf-proof

Take
\[
S=\{0,1\}\subseteq\RR,
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

Step [](#s1-2){.pf-ref} answers part (a) affirmatively, and step [](#s1-3){.pf-ref} gives a counterexample to part (b).

:::

:::

:::
