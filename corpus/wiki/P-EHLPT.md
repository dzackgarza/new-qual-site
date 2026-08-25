---
schema: qual/card@1
id: P-EHLPT
kind: problem
title: Liouville's theorem via $\lim_{R\to\infty}\int_{|z|=R}\frac{f(z)}{(z-a)(z-b)}\,dz$
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

:::{.problem}
Let $f(z)$ be bounded and analytic in $\mathbb C$. Let $a \neq b$ be any fixed complex numbers. Show that the following limit exists:
$$
\lim_{R \rightarrow \infty} \int_{|z|=R} \frac{f(z)}{(z-a)(z-b)} dz
.$$

Use this to show that $f(z)$ must be a constant (Liouville's theorem).
:::


:::{.solution}
Apply PFD and use that $f$ is holomorphic to apply Cauchy's formula over a curve of radius $R$ enclosing $a$ and $b$:
\[
{1 \over (z-a)(z-b)} = {1 \over a-b}\qty{{1 \over z-a} - {1 \over z-b}},
\]
so
\[
\int_\gamma {f(z) \over (z-a)(z-b)}\dz
&= {1 \over a-b}\qty{\int_\gamma {f(z) \over z-a}\dz - \int_\gamma {f(z) \over z-b}\dz} \\
&= {2\pi i \over a-b}\qty{f(a) - f(b)}
.\]
Since $f$ is bounded, this number is finite and independent of $R$, so taking $R\to\infty$ preserves this equality.
On the other hand, if $\abs{f(z)}\leq M$, then we can estimate this integral directly as 
\[
I \leq 
\int_{\abs z = R} {M \over \abs{R-a} \cdot \abs{R-b} } 
= {M\cdot 2\pi R \over \abs{R-a} \cdot \abs{R-b}} \asymptotic {1\over R} \to 0
,\]
which forces $f(a) =f(b)$.
Since $a, b$ were arbitrary, $f$ must be constant.
:::
