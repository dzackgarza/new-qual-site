---
schema: qual/card@1
id: P-JHUFA08ANG
kind: problem
title: "Holomorphic bijections onto a simply connected domain agreeing at 0"
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Mapping Theorem
  - Disc Automorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both bijections and their common value at zero with Fall 2008 problem 7 in the retained JHU extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the direction of composition, holomorphy of both inverses, the two Schwarz inequalities, and uniqueness and sufficiency of the rotation parameter."
---

::: {.problem}
7) (10 points) Let $D \subset \mathbb { C }$ be the unit disk and $\Omega \subset \mathbb { C }$ a bounded, simply connected domain. If $f _ { 1 } : D \to \Omega$ and $f _ { 2 } : D \to \Omega$ are holomorphic bijections so that $f _ { 1 } ( 0 ) = f _ { 2 } ( 0 )$ ， then how are $f _ { 1 }$ and $f _ { 2 }$ related to each other?
:::

::: {.solution}
They differ by precomposition with a unique rotation:
$$
\boxed{f_2(z)=f_1(\lambda z)\quad(z\in D),\qquad |\lambda|=1.}
$$
Moreover $\lambda=f_2'(0)/f_1'(0)$.

<1>1. Their composition is an automorphism of the disk fixing zero.

::: {.proof}
An injective holomorphic function has nonzero derivative;
the holomorphic inverse function theorem consequently makes
the inverse of each $f_j$ holomorphic on $\Omega$ [@SS03].
Thus $H=f_1^{-1}\circ f_2$ is a holomorphic bijection
$D\to D$, its inverse is $f_2^{-1}\circ f_1$, and
$H(0)=0=H^{-1}(0)$ by the common-value assumption.
Schwarz's lemma applied to both maps gives
$$
|H(z)|\leq|z|=|H^{-1}(H(z))|\leq|H(z)|.
$$
Hence $|H(z)|=|z|$ throughout $D$ [@SS03].
:::

<1>2. The equality forces precisely the stated rotation freedom.

::: {.proof}
The quotient $Q(z)=H(z)/z$ extends holomorphically to
zero with value $H'(0)$, by the Taylor expansion of $H$.
It has modulus one at each nonzero point and modulus
at most one everywhere by continuity. The maximum
modulus principle therefore makes $Q$ a constant
$\lambda$ with $|\lambda|=1$ [@SS03]. This gives
$H(z)=\lambda z$ and $f_2(z)=f_1(\lambda z)$.
Differentiating at zero gives
$f_2'(0)=\lambda f_1'(0)$. Since $f_1'(0)\ne0$,
this also proves uniqueness of $\lambda$.

Conversely, for every $|\lambda|=1$, precomposition of
$f_1$ with $z\mapsto\lambda z$ is a holomorphic bijection
onto the same domain and has the same value at zero.
Thus every stated rotation is possible, and there is
no further freedom.
:::
:::
