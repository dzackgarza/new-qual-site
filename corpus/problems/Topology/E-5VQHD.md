---
schema: qual/card@1
id: E-5VQHD
kind: problem
title: Heine–Cantor theorem
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Uniform Continuity
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: exercise
Show that if $f: A\to B$ is a continuous map between metric spaces and $K\subset A$ is compact, then $\restrictionof{f}{K}$ is uniformly continuous.
:::

::: solution
<1>1. Fix $\varepsilon>0$. For each $x\in K$, continuity of $f$ at $x$ gives $r_x>0$ such that
\[
d_A(z,x)<r_x\implies d_B(f(z),f(x))<\varepsilon/2.
\]
The balls $B_A(x,r_x/2)$ cover $K$.

<1>2. By compactness, choose $x_1,\dots,x_m\in K$ such that
\[
K\subseteq\bigcup_{i=1}^m B_A(x_i,r_{x_i}/2).
\]
Set
\[
\delta=\min_{1\le i\le m}r_{x_i}/2>0.
\]

<1>3. Let $x,y\in K$ with $d_A(x,y)<\delta$. Choose $i$ with $x\in B_A(x_i,r_{x_i}/2)$. Then
\[
d_A(x,x_i)<r_{x_i}/2<r_{x_i}
\]
and
\[
d_A(y,x_i)\le d_A(y,x)+d_A(x,x_i)
<\delta+r_{x_i}/2\le r_{x_i}.
\]
Therefore
\[
d_B(f(x),f(x_i))<\varepsilon/2,
\qquad
d_B(f(y),f(x_i))<\varepsilon/2.
\]
The triangle inequality gives
\[
d_B(f(x),f(y))<\varepsilon.
\]
Thus $f|_K$ is uniformly continuous.
:::
