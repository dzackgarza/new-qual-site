---
schema: qual/card@1
id: P-HCAX25
kind: problem
title: A mild growth bound makes a puncture removable
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
relations: []
review: draft
---

::: {.problem}
Let $f$ be holomorphic on the punctured unit disk and suppose
$$
\abs{f(z)}\leq \frac1{\sqrt{\abs{z}}}.
$$
Show that the singularity at the origin is removable.
:::

::: {.solution}
Write the Laurent expansion
$$
f(z)=\sum_{n=-\infty}^{\infty}a_nz^n
$$
on $0<\abs{z}<1$. For $m\ge1$, Cauchy's formula on the circle $\abs{z}=r$ gives
$$
a_{-m}
=\frac1{2\pi i}\int_{\abs{z}=r}f(z)z^{m-1}\,dz.
$$
Hence
$$
\abs{a_{-m}}
\le r^m\max_{\abs{z}=r}\abs{f(z)}
\le r^{m-1/2}.
$$
Since $m-1/2>0$, letting $r\downarrow0$ yields
$$
a_{-m}=0
$$
for every $m\ge1$.

Thus the Laurent series has no principal part:
$$
f(z)=\sum_{n=0}^{\infty}a_nz^n.
$$
The right-hand side is holomorphic at $0$, so it gives the required holomorphic extension. Therefore the singularity at the origin is removable.
:::
