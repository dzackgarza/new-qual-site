---
schema: qual/card@1
id: P-FL5SY
kind: problem
title: Liouville's theorem via $\lim_{R\to\infty}\int_{|z|=R}\frac{f(z)}{(z-a)(z-b)}\,dz$
  for bounded entire $f$
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Cauchy Integral Formula
  - Residues
  - Entire Functions
relations: []
review: draft
---

::: {.problem}
Let $f(z)$ be bounded and analytic in $\CC$.
Let $a\neq b$ be any fixed complex numbers.
Show that the following limit exists:
\[
\lim_{R\to \infty} \int_{\abs z = R} {f(z) \over (z-a)(z-b)} \,dz
.\]

Use this to show that $f(z)$ must be constant.
:::

::: {.solution}
Let $|f(z)|\le M$ on $\mathbb C$. For $R>2\max\{|a|,|b|\}$,
\[
\left|
\int_{|z|=R}\frac{f(z)}{(z-a)(z-b)}\,dz
\right|
\le
2\pi R\frac{M}{(R-|a|)(R-|b|)}.
\]
The right-hand side tends to $0$ as $R\to\infty$, so the requested limit
exists and equals $0$.

For such $R$, the residue theorem gives
\[
\int_{|z|=R}\frac{f(z)}{(z-a)(z-b)}\,dz
=2\pi i\left(
\frac{f(a)}{a-b}+\frac{f(b)}{b-a}
\right)
=2\pi i\frac{f(a)-f(b)}{a-b}.
\]
The left-hand side tends to $0$, while the right-hand side is independent of
$R$. Hence
\[
f(a)=f(b).
\]
Because $a\ne b$ were arbitrary, $f$ is constant.
:::
