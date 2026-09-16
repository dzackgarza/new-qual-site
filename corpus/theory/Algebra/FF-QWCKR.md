---
schema: qual/card@1
id: FF-QWCKR
kind: fact
title: Quasiregular elements and the Jacobson radical
prompts:
- What is a quasiregular element in a ring?
classification:
  areas:
  - algebra
  topics:
  - Jacobson Radical
  - Rings
relations: []
review: draft
---

::: {.fact}
Let $R$ be a commutative ring.
An element $a\in R$ is \dfn{quasiregular} if $1-a$ is a [[D-QQIQZ|unit]] of $R$.
The [[D-2IO6Q|Jacobson radical]] $J(R)$ is the largest ideal of $R$ all of whose elements are quasiregular: every element of $J(R)$ is quasiregular, and every ideal consisting of quasiregular elements is contained in $J(R)$.
:::

::: {.proof}
Let $x\in J(R)$.
If $1-x$ were not a unit, it would lie in a maximal ideal $\mfm$ by [[FF-QELG7]], and so would $x$, giving $1\in\mfm$.

Let $I$ be an ideal consisting of quasiregular elements, let $x\in I$, and suppose $x\notin\mfm$ for a maximal ideal $\mfm$.
Then $\mfm+(x)=R$, so $1=y+rx$ with $y\in\mfm$ and $r\in R$.
Since $rx\in I$, the element $y=1-rx$ is a unit, contradicting $y\in\mfm$.
So $I\subseteq\mfm$ for every maximal ideal $\mfm$, that is, $I\subseteq J(R)$.
:::
