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

::: {.solution}
<1>1. In the included-point topology on $Y$, the singleton
\[
\{0\}
\]
is open.

::: {.proof}
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

<1>2. The preimage of this open set is
\[
f^{-1}(\{0\})
=
\{1\}.
\]

::: {.proof}
One has
\[
f(t)=0
\quad\Longleftrightarrow\quad
t-1=0
\quad\Longleftrightarrow\quad
t=1.
\]
:::

<1>3. The set
\[
\{1\}
\]
is not open in the Euclidean topology on $X=\mathbb R$.

::: {.proof}
Every Euclidean neighborhood of
\[
1
\]
contains points other than $1$.
Thus no open interval about $1$ is contained in the singleton.
:::

<1>4. Therefore
\[
\boxed{
f\text{ is not continuous}.
}
\]

::: {.proof}
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

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
