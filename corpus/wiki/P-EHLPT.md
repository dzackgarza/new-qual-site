---
schema: qual/card@1
id: P-EHLPT
kind: problem
title: "Let $f(z)$ be bounded and analytic in $\\mathbb C$. Let $a \\neq b$ be a\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Let $f(z)$ be bounded and analytic in $\mathbb C$. Let $a \neq b$ be any fixed complex numbers. Show that the following limit exists:
$$
\lim_{R \rightarrow \infty} \int_{|z|=R} \frac{f(z)}{(z-a)(z-b)} dz
.$$

Use this to show that $f(z)$ must be a constant (Liouville's theorem).
:::


:::{.solution}
Apply PFD and use that $f$ is holomorphic to apply Cauchy's formula over a curve of radius $R$ enclosing $a$ and $b$:
\[
\int_\gamma {f(z) \over (z-a)(z-b)}\dz
&= \int_\gamma f(z)\qty{{a-b \over z-a} + {b-a\over z-b} } \dz\\
&= (a-b)\inv \int_\gamma {f(z) \over z-a} \dz + (b-a)\inv \int_\gamma {f(z) \over z-b}\dz \\ 
&= (a-b)\inv \cdot 2\pi i f(a) + (b-a)\cdot 2\pi i f(b)\\
&= 2\pi i\qty{f(a) - f(b) \over a-b }
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
