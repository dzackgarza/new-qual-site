---
schema: qual/card@1
id: P-ALGF06F
kind: problem
title: "Structure and module-theoretic properties of Z[X]/(2X + 1)"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Module Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 3.2 of the official UCSD Algebra Qualifying Examination, Fall 2006. The source has Z[X]/(2X+1); the card had incorrectly transcribed this as Z[X]/(2^X+1), which has been corrected.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the explicit localization isomorphism, flatness of the localization, nonprojectivity via freeness over Z, and noninjectivity from failure of 3-divisibility.
---

::: {.problem}
Consider the $\mathbb{Z}$-algebra $R := \mathbb{Z}[X]/(2X + 1)$.

(a) Show that there is a ring isomorphism $R \simeq S^{-1}\mathbb{Z}$ where $S$ is the multiplicatively closed subset of $\mathbb{Z}$ consisting of all the non-negative integral powers of 2, i.e.\ $S := \{1, 2, 2^2, 2^3, \ldots\}$.

(b) Is $R$ a flat $\mathbb{Z}$-module?
Justify your answer.

(c) Is $R$ a projective $\mathbb{Z}$-module?
Justify your answer.

(d) Is $R$ an injective $\mathbb{Z}$-module?
Justify your answer.
:::

::: {.solution}
Write $\bar X$ for the image of $X$ in $R$.

<1>1. There is an isomorphism
\[
R\cong \mathbb Z[1/2]=S^{-1}\mathbb Z.
\]
::: {.proof}
In $R$ the relation $2\bar X+1=0$ gives
\[
2(-\bar X)=1,
\]
so $2$ is a unit with inverse $-\bar X$.
By the universal property of localization, the inclusion $\mathbb Z\to R$ therefore extends uniquely to a homomorphism
\[
\psi:\mathbb Z[1/2]\longrightarrow R,
\qquad
\psi(1/2)=-\bar X.
\]

Conversely, evaluation at $-1/2$ defines a homomorphism
\[
\mathbb Z[X]\longrightarrow \mathbb Z[1/2],
\qquad
X\longmapsto -1/2.
\]
Since $2(-1/2)+1=0$, it factors through a homomorphism
\[
\phi:R\longrightarrow\mathbb Z[1/2],
\qquad
\phi(\bar X)=-1/2.
\]
The composite $\phi\psi$ fixes $\mathbb Z$ and $1/2$, hence is the identity on $\mathbb Z[1/2]$.
The composite $\psi\phi$ fixes $\mathbb Z$ and $\bar X$, hence is the identity on $R$.
Thus $\phi$ and $\psi$ are inverse isomorphisms.
:::

<1>2. The $\mathbb Z$-module $R$ is flat.
::: {.proof}
By <1>1 it suffices to consider $S^{-1}\mathbb Z$.
For every exact sequence of $\mathbb Z$-modules
\[
0\longrightarrow M'\longrightarrow M\longrightarrow M''\longrightarrow0,
\]
localization is exact:
\[
0\longrightarrow S^{-1}M'\longrightarrow S^{-1}M\longrightarrow S^{-1}M''\longrightarrow0.
\]
Indeed, surjectivity is immediate by lifting numerators, while if $m/s$ maps to zero in $S^{-1}M''$, then some $t\in S$ annihilates the image of $m$ in $M''$, so $tm$ lies in $M'$ and
\[
\frac{m}{s}=\frac{tm}{ts}
\]
lies in the image of $S^{-1}M'$.
Since
\[
S^{-1}M\cong M\otimes_{\mathbb Z}S^{-1}\mathbb Z,
\]
tensoring with $R\cong S^{-1}\mathbb Z$ is exact.
Therefore $R$ is flat over $\mathbb Z$.
:::

<1>3. The $\mathbb Z$-module $R$ is not projective.
::: {.proof}
Every projective module over the principal ideal domain $\mathbb Z$ is free: a projective module is a direct summand of a free module, hence a submodule of a free $\mathbb Z$-module, and every submodule of a free module over a PID is free.

Suppose $R$ were projective.
Then, by <1>1, $\mathbb Z[1/2]$ would be a nonzero free $\mathbb Z$-module.
But multiplication by $2$ is surjective on $\mathbb Z[1/2]$, since
\[
\frac{a}{2^k}=2\frac{a}{2^{k+1}}.
\]
Multiplication by $2$ is not surjective on any nonzero free $\mathbb Z$-module: if $e$ is a basis element, there is no vector $v$ with $2v=e$, because all coordinates of $2v$ are even.
This contradiction shows that $R$ is not projective over $\mathbb Z$.
:::

<1>4. The $\mathbb Z$-module $R$ is not injective.
::: {.proof}
Let
\[
i:3\mathbb Z\hookrightarrow\mathbb Z
\]
be the inclusion and define
\[
f:3\mathbb Z\longrightarrow\mathbb Z[1/2],
\qquad
f(3k)=k.
\]
If $\mathbb Z[1/2]$ were injective, $f$ would extend along $i$ to a homomorphism
\[
F:\mathbb Z\longrightarrow\mathbb Z[1/2].
\]
Writing $u=F(1)$, we would obtain
\[
3u=F(3)=f(3)=1.
\]
But no element of $\mathbb Z[1/2]$ satisfies $3u=1$: if $u=a/2^k$, then $3a=2^k$, impossible because the left side is divisible by $3$ and the right side is not.
Therefore the required extension does not exist, so $R$ is not injective.
:::
:::
