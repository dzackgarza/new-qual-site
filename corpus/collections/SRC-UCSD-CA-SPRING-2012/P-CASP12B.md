---
schema: qual/card@1
id: P-CASP12B
kind: problem
title: "Normal families characterized by coefficient bounds"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $\mathcal{F} \subseteq H(\mathbb{D})$.
Prove that $\mathcal{F}$ is normal if and only if there exists a sequence of nonnegative constants $\{M_n\}$ such that $\lim_{n \to \infty} M_n^{1/n} \leq 1$ and $\sup_{f \in \mathcal{F}} \left|\frac{f^{(n)}(0)}{n!}\right| \leq M_n$ for each $n \geq 0$.
:::

::: solution
Write
\[
f(z)=\sum_{n=0}^\infty a_n(f)z^n,
\qquad a_n(f)=\frac{f^{(n)}(0)}{n!}.
\]

Suppose first that numbers $M_n$ as stated exist. Fix $0<r<1$. Choose
$\rho$ with $r<\rho<1$. Since $\limsup M_n^{1/n}\le1$, for all sufficiently
large $n$ we have $M_n\le \rho^{-n}$. Hence
\[
\sup_{f\in\mathcal F}\sup_{|z|\le r}|f(z)|
\le \sum_{n=0}^\infty M_nr^n<\infty.
\]
Thus $\mathcal F$ is locally bounded, and Montel's theorem says that it is
normal.

Conversely suppose $\mathcal F$ is normal. A normal family of holomorphic
functions is locally bounded: otherwise there would be a compact set $K$ and
$f_j\in\mathcal F$ with $\sup_K|f_j|\to\infty$; a locally uniformly
convergent subsequence would then be bounded on $K$, a contradiction. For
each $0<r<1$ put
\[
C_r=\sup_{f\in\mathcal F}\max_{|z|=r}|f(z)|<\infty.
\]
Cauchy's estimate gives
\[
|a_n(f)|\le C_r r^{-n}.
\]
Define
\[
M_n=\sup_{f\in\mathcal F}|a_n(f)|.
\]
Then $M_n<\infty$, and for every $r<1$,
\[
\limsup_{n\to\infty}M_n^{1/n}\le r^{-1}.
\]
Letting $r\uparrow1$ yields
\[
\limsup_{n\to\infty}M_n^{1/n}\le1.
\]
This is the required coefficient characterization.
:::
