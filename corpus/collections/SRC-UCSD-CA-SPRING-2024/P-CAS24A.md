---
schema: qual/card@1
id: P-CAS24A
kind: problem
title: $|f|^2+|f|$ harmonic implies $f$ constant
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $f$ be a holomorphic function on a region $G$ such that $|f|^2 + |f|$ is harmonic on $G$.
Prove $f$ is constant.
:::

::: {.solution}
On the open set where $f\ne0$, the function $|f|$ is smooth and the standard
Laplacian identities for a holomorphic function give
\[
\Delta |f|^2=4|f'|^2,
\qquad
\Delta |f|=\frac{|f'|^2}{|f|}.
\]
Hence on $\{f\ne0\}$,
\[
0=\Delta(|f|^2+|f|)
=|f'|^2\left(4+\frac1{|f|}\right).
\]
Thus $f'=0$ at every point where $f\ne0$.

If $f\equiv0$ there is nothing to prove. Otherwise choose a point where
$f\ne0$. In a neighborhood of that point, $f'=0$, so $f$ is constant there.
The identity theorem then makes $f$ constant on the connected region $G$.
:::
