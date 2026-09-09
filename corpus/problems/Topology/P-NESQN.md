---
schema: qual/card@1
id: P-NESQN
kind: problem
title: $\pi_1(S^n)$ by van Kampen on the complements of the north and south poles
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
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
Compute the fundamental group $\pi_1(S^n, x_0)$ for $n \ge 2$ using the **Seifert–van Kampen Theorem** by decomposing the $n$-sphere $S^n$ into the complements of the north and south poles.
:::

::: solution
<1>1. Let $N,S\in S^n$ be the north and south poles and set
\[
U=S^n\setminus\{S\},\qquad V=S^n\setminus\{N\}.
\]
By stereographic projection, both $U$ and $V$ are homeomorphic to $\mathbb R^n$, hence
\[
\pi_1(U)=\pi_1(V)=1.
\]

<1>2. Their intersection is
\[
U\cap V=S^n\setminus\{N,S\}\cong\mathbb R^n\setminus\{0\}.
\]
This deformation retracts onto $S^{n-1}$, which is path-connected for $n\ge2$. Thus $U\cap V$ is path-connected.

<1>3. Choose $x_0\in U\cap V$. Seifert--van Kampen identifies $\pi_1(S^n,x_0)$ with the pushout
\[
\pi_1(U,x_0)*_{\pi_1(U\cap V,x_0)}\pi_1(V,x_0).
\]
Both maps from $\pi_1(U\cap V,x_0)$ land in the trivial group, so this pushout is trivial. Therefore
\[
\pi_1(S^n,x_0)=1
\qquad(n\ge2).
\]
:::
