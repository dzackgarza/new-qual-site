---
schema: qual/card@1
id: P-UGCNF
kind: problem
title: $-\frac12\bigl(z+\frac1z\bigr)$ maps the upper half-disk conformally onto the
  upper half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
---

::: {.problem}
Prove that $\displaystyle f(z)=-\frac{1}{2}\left(z+\frac{1}{z}\right)$ is a conformal equivalence from the open half disc $D^+=\{z=x+iy:\ \abs{z}<1,\ y>0\}$ to the upper half plane $\halfplane=\{z=x+iy:\ y>0\}$.
:::

::: {.solution}

::: pf

::: {.pf-step #into}
$f$ is holomorphic on $D^+$ and $f(D^+)\subseteq\halfplane$.

::: pf-proof
The only pole of $f$ is $0\notin D^+$. For $z=re^{i\theta}$ with $0<r<1$ and $0<\theta<\pi$,
$$
\operatorname{Im}f(z)=-\frac12\Bigl(r-\frac1r\Bigr)\sin\theta=\frac12\Bigl(\frac1r-r\Bigr)\sin\theta>0.
$$
:::

:::

::: {.pf-step #bij}
For each $w\in\halfplane$ there is exactly one $z\in D^+$ with $f(z)=w$.

::: pf-proof
The equation $f(z)=w$ is equivalent to $z^2+2wz+1=0$, whose two roots $z_1,z_2$ satisfy $z_1z_2=1$. Neither root has modulus $1$: for $z=e^{i\theta}$, $f(z)=-\cos\theta\in\RR$, but $w\notin\RR$. So exactly one root, say $z_1$, has $\abs{z_1}<1$. Write $z_1=re^{i\theta}$ with $0<r<1$. As in step [](#into){.pf-ref}, $\operatorname{Im}w=\frac12(\frac1r-r)\sin\theta$, and $\operatorname{Im}w>0$ forces $\sin\theta>0$. Hence $z_1\in D^+$, and $z_2\notin D^+$ because $\abs{z_2}>1$.
:::

:::

::: pf-qed
By steps [](#into){.pf-ref} and [](#bij){.pf-ref}, $f$ is a holomorphic bijection $D^+\to\halfplane$. A holomorphic bijection between open sets has a holomorphic inverse, so $f$ is a conformal equivalence.
:::

:::

:::
