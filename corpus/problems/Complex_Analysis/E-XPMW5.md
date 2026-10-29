---
schema: qual/card@1
id: E-XPMW5
kind: problem
title: Singularities at $0$ of $\Log(1+z)\sin(z)/z^2$, $e^{\sin(1/z)}$, and $(1+z)/(e^z-1)$
classification:
  areas:
  - complex-analysis
  topics:
  - Singularities
  - Laurent Series
  - Removable Singularities
  - Essential Singularities
  - Poles
relations: []
review: draft
---

::: {.exercise}
Classify the singularities at $z=0$ of the following
$$
\begin{aligned}
f_1(z) &= \frac{\Log(1+z) \sin(z)}{z^2} \\
f_2(z) &= e^{\sin\qty{1/z}} \\
f_3(z) &= \frac{1+z}{e^z-1}.
\end{aligned}
$$
:::

::: {.solution}

::: pf

::: pf-step
$f_1$ has a $\boxed{\text{removable singularity}}$ at $0$.

::: pf-proof
Near $0$, $\Log(1+z) = z - \frac{z^2}{2} + O(z^3)$ and $\sin z = z + O(z^3)$, so $\Log(1+z)\sin z = z^2 - \frac{z^3}{2} + O(z^4)$ and
$$
f_1(z) = 1 - \frac z2 + O(z^2),
$$
which has no negative powers of $z$.
:::

:::

::: pf-step
$f_2$ has an $\boxed{\text{essential singularity}}$ at $0$.

::: pf-proof
Along $z_k \coloneqq \frac{1}{2\pi k}\to0$, $\sin(1/z_k) = 0$ and $f_2(z_k) = 1$; along $w_k \coloneqq \frac{1}{\pi/2 + 2\pi k}\to0$, $\sin(1/w_k)=1$ and $f_2(w_k) = e$.
So $\lim_{z\to0}f_2(z)$ does not exist, and the singularity is not removable; and $\abs{f_2(z_k)}=1$ does not tend to $\infty$, so it is not a pole.
:::

:::

::: pf-step
$f_3$ has a $\boxed{\text{simple pole with residue } 1}$ at $0$.

::: pf-proof
$e^z - 1 = z\,u(z)$ with $u(z) = 1 + \frac z2 + \cdots$ entire and $u(0)=1$, so $f_3(z) = \frac1z\cdot\frac{1+z}{u(z)}$ where $\frac{1+z}{u(z)}$ is holomorphic near $0$ with value $1$ at $0$.
:::

:::

:::

:::
