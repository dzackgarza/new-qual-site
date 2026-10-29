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
$$
\lim_{R\to \infty} \int_{\abs z = R} {f(z) \over (z-a)(z-b)} \,dz
.$$

Use this to show that $f(z)$ must be constant.
:::

::: {.solution}
Let $\abs{f(z)}\le M$ on $\CC$, and write $I(R)$ for the integral over $\abs z = R$.

::: pf

::: {.pf-step #limit-zero}
$\lim_{R\to\infty} I(R) = 0$; in particular the limit exists.

::: pf-proof
For $R>\max\theset{\abs a,\abs b}$, on $\abs z = R$ we have $\abs{z-a}\geq R-\abs a$ and $\abs{z-b}\geq R-\abs b$, so
$$
\abs{I(R)} \le 2\pi R\frac{M}{(R-\abs a)(R-\abs b)},
$$
and the right-hand side tends to $0$ as $R\to\infty$.
:::

:::

::: {.pf-step #residues}
For $R>\max\theset{\abs a,\abs b}$, $I(R) = 2\pi i\,\dfrac{f(a)-f(b)}{a-b}$.

::: pf-proof
The integrand is holomorphic on $\CC$ except for simple poles at $a$ and $b$, with residues $f(a)/(a-b)$ and $f(b)/(b-a)$. Both poles lie inside $\abs z = R$, so the residue theorem gives
$$
I(R) = 2\pi i\left(\frac{f(a)}{a-b}+\frac{f(b)}{b-a}\right) = 2\pi i\,\frac{f(a)-f(b)}{a-b}.
$$
:::

:::

::: pf-step
$f$ is constant.

::: pf-proof
By step [](#residues){.pf-ref}, $I(R)$ is independent of $R$ for large $R$, and by step [](#limit-zero){.pf-ref} it tends to $0$. Hence $f(a) = f(b)$.
The argument applies to every pair $a\neq b$ in $\CC$, so $f$ is constant.
:::

:::

:::

:::
