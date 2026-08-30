---
schema: qual/card@1
id: P-YDJE6
kind: problem
title: $\frac{1}{2\pi i}\int_{|z|=2}\frac{z^n}{1-3z\cos\theta+z^2}\,dz=\frac{\sin(n\theta)}{\sin\theta}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Trigonometry
  - Poles
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

:::{.problem}
Let $n\in \ZZ^{\geq 1}$ and $0<\theta<\pi$ and show that
\[
{1\over 2\pi i} \int_{\abs z = 2} {z^n \over 1 -3z\cos(\theta) + z^2} \,dz = {\sin(n\theta) \over \sin(\theta)}
.\]
:::

::: {.solution}
<1>1. Factorization of the quadratic denominator $P(z) = z^2 - 2z\cos\theta + 1$:
<2>1. For $0 < \theta < \pi$, the quadratic $z^2 - 2z\cos\theta + 1$ factors over $\mathbb{C}$ as:
\[
z^2 - 2z\cos\theta + 1 = (z - e^{i\theta})(z - e^{-i\theta}).
\]
Proof: $(z - e^{i\theta})(z - e^{-i\theta}) = z^2 - (e^{i\theta} + e^{-i\theta})z + 1 = z^2 - 2z\cos\theta + 1$.
<2>2. The roots are $z_1 = e^{i\theta}$ and $z_2 = e^{-i\theta}$.
Since $|z_1| = |z_2| = 1 < 2$, both poles lie strictly inside the circular contour $\gamma: |z| = 2$.
Since $0 < \theta < \pi$, $\sin\theta \neq 0$, so $z_1 \neq z_2$, and both poles are simple poles.
Proof: modulus of complex exponentials and $e^{i\theta} \neq e^{-i\theta}$ for $\theta \in (0, \pi)$.

<1>2. Residue computation:
<2>1. Let $g(z) = \frac{z^n}{(z - e^{i\theta})(z - e^{-i\theta})}$.
At the simple pole $z_1 = e^{i\theta}$:
\[
\operatorname{Res}(g, e^{i\theta}) = \lim_{z \to e^{i\theta}} (z - e^{i\theta}) g(z) = \frac{(e^{i\theta})^n}{e^{i\theta} - e^{-i\theta}} = \frac{e^{in\theta}}{2i\sin\theta}.
\]
Proof: standard residue formula for simple poles and Euler's formula $e^{i\theta} - e^{-i\theta} = 2i\sin\theta$.
<2>2. At the simple pole $z_2 = e^{-i\theta}$:
\[
\operatorname{Res}(g, e^{-i\theta}) = \lim_{z \to e^{-i\theta}} (z - e^{-i\theta}) g(z) = \frac{(e^{-i\theta})^n}{e^{-i\theta} - e^{i\theta}} = -\frac{e^{-in\theta}}{2i\sin\theta}.
\]
Proof: residue formula for simple poles.
<2>3. Summing the residues:
\[
\operatorname{Res}(g, e^{i\theta}) + \operatorname{Res}(g, e^{-i\theta}) = \frac{e^{in\theta} - e^{-in\theta}}{2i\sin\theta} = \frac{2i\sin(n\theta)}{2i\sin\theta} = \frac{\sin(n\theta)}{\sin\theta}.
\]
Proof: Euler's formula $\sin(n\theta) = \frac{e^{in\theta} - e^{-in\theta}}{2i}$.

<1>3. Evaluation of the contour integral:
<2>1. By the Cauchy Residue Theorem:
\[
\frac{1}{2\pi i} \oint_{|z|=2} \frac{z^n}{z^2 - 2z\cos\theta + 1} \, dz = \sum_{j=1}^2 \operatorname{Res}(g, z_j) = \frac{\sin(n\theta)}{\sin\theta}.
\]
Proof: Cauchy Residue Theorem.

<1>4. Conclusion:
$\frac{1}{2\pi i} \int_{|z|=2} \frac{z^n}{1 - 2z\cos\theta + z^2} \, dz = \frac{\sin(n\theta)}{\sin\theta}$. Q.E.D.
Proof: <1>1 through <1>3.
:::
