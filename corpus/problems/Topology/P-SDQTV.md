---
schema: qual/card@1
id: P-SDQTV
kind: problem
title: Covering spaces and deck transformations of the Klein bottle, Möbius band,
  and $\RP^2\times S^1$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Group Actions
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
a. Give the definitions of **covering space** and **deck transformation** (or covering transformation).

b. Describe the universal cover of the Klein bottle and its group of deck transformations.

c. Explicitly give a collection of deck transformations on $\{(x, y) \mid -1 \leq x \leq 1, -\infty < y < \infty\}$ such that the quotient is a Möbius band.

d. Find the universal cover of $\mathbb{RP}^2 \times S^1$ and explicitly describe its group of deck transformations.
:::

::: solution
<1>1. A covering map is a surjective continuous map $p:\widetilde X\to X$ such that every $x\in X$ has an open neighborhood $U$ for which
\[
p^{-1}(U)=\bigsqcup_{\alpha}U_\alpha
\]
and every restriction $p|_{U_\alpha}:U_\alpha\to U$ is a homeomorphism. A deck transformation is a homeomorphism $h:\widetilde X\to\widetilde X$ satisfying $p\circ h=p$.

<1>2. For the Klein bottle, take $\widetilde K=\mathbb R^2$ and let
\[
T(x,y)=(x,y+1),\qquad R(x,y)=(x+1,-y).
\]
<2>1. The group $\Gamma=\langle R,T\rangle$ acts freely and properly discontinuously on $\mathbb R^2$, and a fundamental rectangle has the standard Klein-bottle edge identifications.
<2>2. Moreover
\[
RTR^{-1}=T^{-1},
\]
so
\[
\Gamma\cong\langle R,T\mid RTR^{-1}=T^{-1}\rangle\cong\pi_1(K).
\]
Hence $\mathbb R^2\to\mathbb R^2/\Gamma\cong K$ is the universal covering and $\Gamma$ is its deck group.

<1>3. On $[-1,1]\times\mathbb R$, define
\[
\tau(x,y)=(-x,y+1).
\]
Then
\[
\tau^m(x,y)=((-1)^m x,y+m),
\]
and $\langle\tau\rangle\cong\mathbb Z$ acts freely and properly discontinuously. A fundamental domain is $[-1,1]\times[0,1]$, with
\[
(x,0)\sim(-x,1),
\]
so the quotient is a Möbius band.

<1>4. The universal cover of $\mathbb{RP}^2\times S^1$ is
\[
S^2\times\mathbb R\longrightarrow\mathbb{RP}^2\times S^1,
\qquad
(v,t)\longmapsto([v],e^{2\pi i t}).
\]
Its deck transformations are
\[
(v,t)\longmapsto((-1)^\varepsilon v,t+m),
\qquad
(\varepsilon,m)\in\mathbb Z/2\times\mathbb Z.
\]
Therefore
\[
\operatorname{Deck}(S^2\times\mathbb R/\mathbb{RP}^2\times S^1)
\cong\mathbb Z/2\times\mathbb Z.
\]
:::
