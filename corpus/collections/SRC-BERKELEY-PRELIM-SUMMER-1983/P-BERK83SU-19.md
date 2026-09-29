---
schema: qual/card@1
id: P-BERK83SU-19
kind: problem
title: Area of the image of the unit disk under $f(z)=z+z^2/2$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    The factorization f(z)-f(w)=(z-w)(1+(z+w)/2) shows that f is injective
    on the unit disk. The holomorphic Jacobian is |f'|^2=|1+z|^2, whose
    integral over the disk is 3pi/2.
---

::: {.problem}
Compute the area of the image of the unit disk
\[
\{z\in\mathbb C:|z|<1\}
\]
under
\[
f(z)=z+\frac{z^2}{2}.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The map $f$ is injective on $\DD$.

::: pf-proof

For $z,w\in\DD$,
$$
f(z)-f(w)
=
(z-w)\left(1+\frac{z+w}{2}\right).
$$
If $f(z)=f(w)$ and $z\neq w$, then $z+w=-2$. But
$$
\abs{z+w}
\le
\abs{z}+\abs{w}
<
2,
$$
which is impossible when $z+w=-2$. Hence $z=w$.

:::

:::

::: {.pf-step #s2}

The real Jacobian determinant of $f$ at $z\in\DD$ is
$$
J_f(z)=\abs{1+z}^2.
$$

::: pf-proof

For a holomorphic map, the real Jacobian determinant is
$\abs{f'(z)}^2$. Here
$$
f'(z)=1+z,
$$
so
$$
J_f(z)=\abs{f'(z)}^2=\abs{1+z}^2.
$$
Since $-1\notin\DD$, this Jacobian is positive throughout $\DD$.

:::

:::

::: {.pf-step #s3}

The area of $f(\DD)$ is
$$
\int_{\DD}\abs{1+z}^2\,dA(z).
$$

::: pf-proof

By step [](#s1){.pf-ref}, $f$ is injective on $\DD$, and by step [](#s2){.pf-ref} its
Jacobian is positive there. The change-of-variables formula therefore
gives
$$
\operatorname{Area}(f(\DD))
=
\int_{\DD}J_f(z)\,dA(z)
=
\int_{\DD}\abs{1+z}^2\,dA(z).
$$

:::

:::

::: {.pf-step #s4}

The required area is
$$
\boxed{\frac{3\pi}{2}}.
$$

::: pf-proof

Writing $z=re^{i\theta}$,
$$
\abs{1+re^{i\theta}}^2
=
1+2r\cos\theta+r^2.
$$
Hence step [](#s3){.pf-ref} gives
$$
\begin{aligned}
\operatorname{Area}(f(\DD))
&=
\int_0^{2\pi}\int_0^1
\left(1+2r\cos\theta+r^2\right)r\,dr\,d\theta\\
&=
2\pi\int_0^1(r+r^3)\,dr\\
&=
2\pi\left(\frac12+\frac14\right)\\
&=
\frac{3\pi}{2}.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives the requested area.

:::

:::

:::
