---
schema: qual/card@1
id: P-APAS21E
kind: problem
title: $G$-invariant inner product implies complete reducibility
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
---

::: {.problem}
Let $G$ be a group (possibly infinite) and let $V$ be a finite-dimensional $G$-module over $\CC$.
Assume that $V$ admits a $G$-invariant inner product $\langle -, - \rangle$.
Prove that $V$ is completely reducible.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the invariance computation, the complement and the decomposition as separate steps.

Let $V$ be a finite-dimensional $\CC G$-module with a $G$-invariant inner product $\langle-,-\rangle$, and let $W\subseteq V$ be a $G$-submodule.

::: pf

::: {.pf-step #stable}
$W^{\perp}$ is a $G$-submodule.

::: pf-proof
For $g\in G$, $v\in W^{\perp}$ and $w\in W$: $\langle gv,w\rangle=\langle gv,g(g^{-1}w)\rangle=\langle v,g^{-1}w\rangle$ by invariance of the inner product, and $g^{-1}w\in W$ because $W$ is a submodule, so the last term is $0$. Hence $\langle gv,w\rangle=0$ for all $w\in W$, that is $gv\in W^{\perp}$.
:::

:::

::: {.pf-step #decompose}
$V=W\oplus W^{\perp}$.

::: pf-proof
The inner product is positive definite, so $W\cap W^{\perp}=\{0\}$: a vector of $W$ orthogonal to every element of $W$, in particular to itself, is $0$. In finite dimension $\dim W+\dim W^{\perp}=\dim V$, so the sum is all of $V$; equivalently every $v$ is $v=w+(v-w)$ with $w$ the orthogonal projection of $v$ onto $W$ and $v-w\in W^{\perp}$.
:::

:::

::: {.pf-step #induction}
Every $G$-submodule of $V$ has a $G$-stable complement, hence $V$ is completely reducible.

::: pf-proof
Given a submodule $W$, step [](#stable){.pf-ref} shows $W^{\perp}$ is a submodule and step [](#decompose){.pf-ref} shows $V=W\oplus W^{\perp}$; iterating on $W$ and on $W^{\perp}$ (both of smaller dimension, so the process terminates) writes $V$ as a direct sum of irreducible submodules.
:::

:::

::: {.pf-qed}
Every submodule has a $G$-stable complement by step [](#induction){.pf-ref}, which is precisely complete reducibility of $V$.
:::

:::

:::
