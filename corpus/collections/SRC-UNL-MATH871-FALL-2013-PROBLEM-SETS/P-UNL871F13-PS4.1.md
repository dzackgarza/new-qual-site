---
schema: qual/card@1
id: P-UNL871F13-PS4.1
kind: problem
title: Continuity into the included-point topology
classification:
  areas: [topology]
  topics: [Continuity]
relations: []
review: draft
---

::: {.problem}
Let $X=\mathbb R$ with the Euclidean topology and let $Y=\mathbb R$ with the included-point topology whose included point is $0$.
Define
\[
f:X\to Y,\qquad f(t)=t-1.
\]
Determine whether $f$ is continuous, and prove your answer.
:::

::: pf

::: pf-step

In the included-point topology on $Y$, the singleton
\[
\{0\}
\]
is open.


::: pf-proof

By definition, every nonempty subset of $Y$ containing the distinguished
point
\[
0
\]
is open.
Therefore
\[
\{0\}
\]
is open.

:::

:::

::: pf-step

The preimage of this open set is
\[
f^{-1}(\{0\})
=
\{1\}.
\]


::: pf-proof

One has
\[
f(t)=0
\quad\Longleftrightarrow\quad
t-1=0
\quad\Longleftrightarrow\quad
t=1.
\]

:::

:::

::: pf-step

The set
\[
\{1\}
\]
is not open in the Euclidean topology on $X=\mathbb R$.


::: pf-proof

Every Euclidean neighborhood of
\[
1
\]
contains points other than $1$.
Thus no open interval about $1$ is contained in the singleton.

:::

:::

::: pf-step

Therefore
\[
\boxed{
f\text{ is not continuous}.
}
\]


::: pf-proof

Continuity would require the preimage of every open subset of $Y$ to be
open in $X$.
Steps <1>1--<1>3 give an open set
\[
\{0\}\subseteq Y
\]
whose preimage
\[
\{1\}
\]
is not open in $X$.

:::

:::

::: pf-qed

Step <1>4 is the required conclusion.

:::

:::
