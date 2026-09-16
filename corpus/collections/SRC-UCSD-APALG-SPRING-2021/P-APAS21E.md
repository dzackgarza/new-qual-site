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
Let $G$ be a group (possibly infinite) and let $V$ be a finite-dimensional $G$-module over $\mathbb{C}$.
Assume that $V$ admits a $G$-invariant inner product $\langle -, - \rangle$.
Prove that $V$ is completely reducible.
:::

::: {.solution}
Let $W\subseteq V$ be a $G$-submodule. We claim that its orthogonal complement
\[
W^\perp=\{v\in V: \langle v,w\rangle=0\text{ for every }w\in W\}
\]
is also $G$-stable. Indeed, let $g\in G$, $v\in W^\perp$, and $w\in W$. Since the inner product is $G$-invariant,
\[
\langle gv,w\rangle
=\langle gv,g(g^{-1}w)\rangle
=\langle v,g^{-1}w\rangle.
\]
Because $W$ is $G$-stable, $g^{-1}w\in W$, so the last inner product is zero. Hence $gv\in W^\perp$.

Since the inner product is positive definite and $V$ is finite-dimensional,
\[
V=W\oplus W^\perp.
\]
Thus every $G$-submodule of $V$ has a $G$-stable complement.

We now prove complete reducibility by induction on $\dim V$. If $V=0$ there is nothing to prove. If $V\neq0$ is irreducible, we are done. Otherwise choose a nonzero proper $G$-submodule $W$. Then
\[
V=W\oplus W^\perp,
\]
and both summands have smaller dimension than $V$. By induction, each is a direct sum of irreducible $G$-modules. Therefore $V$ is a direct sum of irreducible $G$-modules. Hence $V$ is completely reducible.
:::
