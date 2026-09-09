---
schema: qual/card@1
id: E-DXXL4
kind: problem
title: Uniform limit theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Continuity
  - Continuity
  - Compactness
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

::: {.exercise}
Prove the Heine–Cantor Theorem: let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces. If $X$ is compact and $f: X \to Y$ is continuous, then $f$ is uniformly continuous.
:::

::: solution
Fix $\varepsilon>0$. For each $p\in X$, continuity gives $r_p>0$ such that
\[
d_X(x,p)<r_p
\quad\Longrightarrow\quad
d_Y(f(x),f(p))<\frac\varepsilon2.
\]
The balls $B(p,r_p/2)$ cover $X$. By compactness, choose a finite subcover
\[
B(p_1,r_1/2),\dots,B(p_N,r_N/2).
\]
Set
\[
\delta=\frac12\min_{1\le j\le N}r_j>0.
\]

If $d_X(x,y)<\delta$, choose $j$ with $x\in B(p_j,r_j/2)$. Then
\[
d_X(y,p_j)\le d_X(y,x)+d_X(x,p_j)
<\delta+\frac{r_j}{2}\le r_j.
\]
Thus
\[
d_Y(f(x),f(p_j))<\frac\varepsilon2,
\qquad
d_Y(f(y),f(p_j))<\frac\varepsilon2.
\]
By the triangle inequality,
\[
d_Y(f(x),f(y))<\varepsilon.
\]
Hence $f$ is uniformly continuous.
:::
