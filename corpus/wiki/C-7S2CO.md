---
schema: qual/card@1
id: C-7S2CO
kind: corollary
title: "Formula for Laurent coefficients"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.corollary title="Formula for Laurent coefficients"}
Differentiating under the integral above yields
\[
c_k = \frac{f^{(k)}(p)}{k !}=\frac{1}{2 \pi i} \int_{\partial U} \frac{f(z) }{(z-p)^{k+1}} \dz
= {1 \over 2\pi R^n}\int_0^{2\pi} f(z_0 + Re^{i\theta})e^{-in\theta} \dtheta
.\]
For $R \da d(p, \bd U)$,
this yields a bound
\[
f(z) = \sum c_kz_k \implies \abs{c_k} \leq {\sup_{z\in \bd U}f(z) \cdot \length(\bd U) \over 2\pi R^{k+1}}
,\]
so $\limsup \abs{c_k}^{1\over k} < R\inv$, showing that $\sum c_k (z-p)^k$ has radius of convergence at least $R$ and is represented by its power series in $D_R(p)$.
This implies that $f$ is smooth at $p\in U$, and thus can only have poles on $\bd U$.
:::
