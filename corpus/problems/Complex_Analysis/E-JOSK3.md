---
schema: qual/card@1
id: E-JOSK3
kind: problem
title: Orders of the poles of $\frac{1}{z\sin z}$ and $\frac{e^{z^2}-1}{z^4}$ at $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Laurent Series
  - Singularities
relations: []
review: draft
---

::: {.exercise}
Determine the order of the pole of

(a) ${1\over z\sin(z)}$ at $z_0 = 0$.

(b) ${e^{z^2}-1\over z^4}$ at $z_0=0$.

:::

::: {.solution}
A function $f$ has a pole of order $m$ at $0$ exactly when $\lim_{z\to0}z^mf(z)$ exists and is nonzero.

::: pf

::: pf-step
(a) $\frac{1}{z\sin z}$ has a pole of order $\boxed{2}$ at $0$.

::: pf-proof
$z^2\cdot\frac{1}{z\sin z}=\frac{z}{\sin z}\to1$ as $z\to0$, since $\sin z=z+\bigo(z^3)$.
:::

:::

::: pf-step
(b) $\frac{e^{z^2}-1}{z^4}$ has a pole of order $\boxed{2}$ at $0$.

::: pf-proof
From $e^{w}=1+w+\frac{w^2}{2!}+\frac{w^3}{3!}+\bigo(w^4)$ with $w=z^2$,
$$
\frac{e^{z^2}-1}{z^4}=z^{-4}\qty{z^2+\frac{z^4}{2!}+\frac{z^6}{3!}+\bigo(z^8)}=z^{-2}+\frac1{2}+\frac{z^2}{6}+\bigo(z^4).
$$
The principal part is $z^{-2}$.
:::

:::

:::

:::
