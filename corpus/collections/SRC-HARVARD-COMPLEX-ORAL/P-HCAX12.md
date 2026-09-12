---
schema: qual/card@1
id: P-HCAX12
kind: problem
title: Zeros and poles of a doubly periodic function
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Functions
relations: []
review: draft
---

::: problem
Show that a nonconstant doubly periodic meromorphic function has equally many zeros and poles, counted with multiplicity, in a fundamental parallelogram.
:::

::: solution
Let $\omega_1,\omega_2$ be periods of $f$ which are linearly independent over $\mathbb R$. Translate a fundamental parallelogram if necessary so that its boundary contains no zero or pole of $f$; this is possible because the zeros and poles are discrete.

Let $P$ be such a parallelogram, positively oriented. By the argument principle,
\[
N_0-N_\infty
=\frac{1}{2\pi i}\int_{\partial P}\frac{f'(z)}{f(z)}\,dz,
\]
where $N_0$ and $N_\infty$ are respectively the numbers of zeros and poles of $f$ in $P$, counted with multiplicity.

Since $f(z+\omega_j)=f(z)$, differentiation gives $f'(z+\omega_j)=f'(z)$, so $f'/f$ is doubly periodic with the same periods. The two edges of $\partial P$ parallel to $\omega_1$ differ by translation by $\omega_2$ and are traversed in opposite directions; therefore their integrals of $f'/f$ cancel. The same holds for the two edges parallel to $\omega_2$. Hence
\[
\int_{\partial P}\frac{f'(z)}{f(z)}\,dz=0.
\]
Thus $N_0-N_\infty=0$, so $f$ has equally many zeros and poles in a fundamental parallelogram, counted with multiplicity.
:::
