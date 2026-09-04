---
schema: qual/card@1
id: E-YFBH5
kind: problem
title: Analytic self-maps of the disc with a zero of order $k$ at $0$ and $|f|\to
  1$ at the boundary
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Schwarz Lemma
  - Zeros
  - Maximum Modulus Principle
relations: []
review: draft
---

::: {.problem}
Suppose $f:\DD\to\DD$ is analytic, has a single zero of order $k$ at $z=0$, and satisfies $\lim_{\abs z \to 1} \abs{f(z)} = 1$.
Give with proof a formula for $f(z)$.
:::

::: {.solution}
Since $f$ has a zero of order $k$ at $0$, the quotient
\[
g(z)={f(z)\over z^k}
\]
extends holomorphically across $0$.
Because $0$ is the only zero of $f$, this extension is nowhere zero on $\DD$.

Moreover,
\[
|g(z)|={|f(z)|\over |z|^k}\longrightarrow1
\qquad (|z|\to1).
\]
We claim $|g|\le1$ on $\DD$.
Fix $z_0\in\DD$ and $\varepsilon>0$.
By the boundary limit there is $r_0<1$ such that
\[
|g(z)|<1+\varepsilon
\qquad(r_0<|z|<1).
\]
Choose $r$ with $\max\{r_0,|z_0|\}<r<1$.
The maximum modulus principle on $|z|\le r$ gives
\[
|g(z_0)|\le \max_{|z|=r}|g(z)|<1+\varepsilon.
\]
Since $\varepsilon$ is arbitrary, $|g(z_0)|\le1$.

Apply the same argument to the holomorphic function $1/g$.
Since
\[
|1/g(z)|\longrightarrow1
\qquad(|z|\to1),
\]
we get $|1/g|\le1$, hence $|g|\ge1$.
Therefore $|g|\equiv1$ on $\DD$.

By the open mapping theorem, a holomorphic function with image contained in $S^1$ is constant.
Thus
\[
g(z)=\lambda,
\qquad |\lambda|=1,
\]
and consequently
\[
f(z)=\lambda z^k.
\]
:::
