---
schema: qual/card@1
id: P-UUYPV
kind: problem
title: An elliptic function has equally many zeros and poles in a period square
classification:
  areas:
  - real-analysis
  topics:
  - Meromorphic Functions
  - Argument Principle
relations: []
review: draft
---

::: {.problem}
Let $F(z)$ be a non-constant meromorphic function on the complex plane $\mathbb{C}$ such that $F(z+1)=F(z)=F(z+i)$ for all $z$.
Let $Q$ be a square with vertices $z, z+1, z+i,$ and $z+1+i$ such that $F$ has no zeros and no poles on $\partial Q$.
Prove that inside $Q$ the function $F$ has the same number of zeros as poles (counting multiplicities).
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Let $F$ be a non-constant meromorphic function on $\CC$ with periods $1$ and $i$, and let $Q$ be a period square with no zeros or poles of $F$ on $\bd Q$.
Prove $F$ has the same number of zeros as poles inside $Q$ (counting multiplicities).

<1>1. Setup: let $G = F'/F$; $G$ is meromorphic with periods $1$ and $i$ wherever $F \ne 0, \infty$.
Proof: $F(z+1) = F(z)$ and $F(z+i) = F(z)$; differentiating, $F'(z+1) = F'(z)$, $F'(z+i) = F'(z)$, so $G$ is doubly periodic on its domain.

<1>2. By the argument principle, $N - P = \frac{1}{2\pi i}\oint_{\bd Q} G(z)\, dz$ where $N, P$ are the numbers of zeros and poles of $F$ inside $Q$.
Proof: the argument principle for meromorphic functions.

<1>3. $\oint_{\bd Q} G\, dz = 0$.
<2>1. Write $Q = \{z_0 + s + it : 0 \le s, t \le 1\}$ and $\bd Q$ as the four sides $\gamma_1, \gamma_2, \gamma_3, \gamma_4$ (bottom, right, top, left, counterclockwise).
Proof: parametrization.
<2>2. The integrals over opposite sides cancel: $\int_{\gamma_1} G + \int_{\gamma_3} G = 0$ and $\int_{\gamma_2} G + \int_{\gamma_4} G = 0$.
Proof: $\int_{\gamma_3} G = \int_1^0 G(z_0 + s + i)\, ds = -\int_0^1 G(z_0 + s)\, ds = -\int_{\gamma_1} G$ by the period $i$ (and similarly the vertical sides cancel by the period $1$); no zeros or poles on $\bd Q$ makes $G$ continuous there, so the integrals are well defined.
<2>3. Total integral is 0. Proof: sum over the four sides: <2>2 gives pairwise cancellation.

<1>4. $N = P$.
Proof: <1>2 and <1>3 give $N - P = 0$.

<1>5. Q.E.D. Proof: <1>1–<1>4 prove the claim.
:::
