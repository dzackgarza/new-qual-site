---
schema: qual/card@1
id: P-BKS16-5A
kind: problem
title: Evaluation of $\int_0^{2\pi}d\theta/(3+e^{-i\theta})^2$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Checked the statement and contour-substitution solution against Problem 5A in the vendored Berkeley Spring 2016 solution packet.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the z=e^{i theta} substitution, the second-order pole at -1/3, and its residue.
---

::: {.problem}
Compute
$$
\int_0^{2\pi}\frac{d\theta}{(3+e^{-i\theta})^2}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Under the substitution
$$
z=e^{i\theta},
$$
the integral becomes
$$
\oint_{\abs z=1}
\frac{z}{i(3z+1)^2}\,dz,
$$
where the unit circle is oriented counterclockwise.

::: pf-proof

One has
$$
e^{-i\theta}=z^{-1}
$$
and
$$
d\theta=\frac{dz}{iz}.
$$
Therefore
$$
\begin{aligned}
\frac{d\theta}{(3+e^{-i\theta})^2}
&=
\frac1{(3+z^{-1})^2}\frac{dz}{iz}\\
&=
\frac{z^2}{(3z+1)^2}\frac{dz}{iz}\\
&=
\frac{z}{i(3z+1)^2}\,dz.
\end{aligned}
$$
As $\theta$ runs from $0$ to $2\pi$, $z$ traverses the unit circle once counterclockwise.

:::

:::

::: {.pf-step #s2}

The integrand
$$
F(z)=\frac{z}{i(3z+1)^2}
$$
has a unique pole inside the unit circle, at $z=-1/3$, and
$$
\operatorname{Res}_{z=-1/3}F(z)=\frac1{9i}.
$$

::: pf-proof

Since
$$
(3z+1)^2=9\left(z+\frac13\right)^2,
$$
the only pole is the second-order pole $z=-1/3$, which lies inside $\abs z=1$. Its residue is
$$
\begin{aligned}
\operatorname{Res}_{z=-1/3}F(z)
&=
\left.
\frac{d}{dz}
\left(
\left(z+\frac13\right)^2F(z)
\right)
\right|_{z=-1/3}\\
&=
\left.
\frac{d}{dz}\left(\frac{z}{9i}\right)
\right|_{z=-1/3}\\
&=
\frac1{9i}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s3}

Hence
$$
\boxed{
\int_0^{2\pi}\frac{d\theta}{(3+e^{-i\theta})^2}
=
\frac{2\pi}{9}
}.
$$

::: pf-proof

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref} and the residue theorem,
$$
\oint_{\abs z=1}F(z)\,dz
=
2\pi i\cdot\frac1{9i}
=
\frac{2\pi}{9}.
$$

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the requested value.

:::

:::

:::
