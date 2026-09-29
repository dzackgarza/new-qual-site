---
schema: qual/card@1
id: P-BERK78S-05
kind: problem
title: The integral $\int_0^{2\pi}e^{e^{i\theta}-i\theta}\,d\theta$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Substituted z=e^{i theta}. The integral becomes
    (1/i) times the unit-circle integral of e^z/z^2. Its only enclosed pole
    is at zero, with residue one, so the residue theorem gives 2 pi.
---

::: {.problem}
Evaluate
\[
\int_0^{2\pi} e^{e^{i\theta}-i\theta}\,d\theta.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Under the substitution
$$
z=e^{i\theta},
$$
one has
$$
d\theta=\frac{dz}{iz}
$$
and
$$
e^{-i\theta}=\frac1z.
$$

::: pf-proof

Differentiating
$$
z=e^{i\theta}
$$
gives
$$
dz=iz\,d\theta,
$$
which yields the formula for $d\theta$. Since $\abs{z}=1$ on the contour,
$$
z=e^{i\theta}
$$
also gives
$$
e^{-i\theta}=z^{-1}.
$$

:::

:::

::: {.pf-step #s2}

The integral is
$$
\frac1i
\oint_{\abs{z}=1}
\frac{e^z}{z^2}\,dz.
$$

::: pf-proof

Using step [](#s1){.pf-ref},
$$
\begin{aligned}
e^{e^{i\theta}-i\theta}\,d\theta
&=
e^z e^{-i\theta}\frac{dz}{iz}\\
&=
e^z\frac1z\frac{dz}{iz}\\
&=
\frac1i\frac{e^z}{z^2}\,dz.
\end{aligned}
$$
As $\theta$ increases from $0$ to $2\pi$, the variable $z$ traverses the
unit circle once counterclockwise.

:::

:::

::: {.pf-step #s3}

The residue of
$$
\frac{e^z}{z^2}
$$
at $z=0$ is $1$.

::: pf-proof

The exponential series is
$$
e^z
=
1+z+\frac{z^2}{2!}+\cdots.
$$
Therefore
$$
\frac{e^z}{z^2}
=
\frac1{z^2}
+
\frac1z
+
\frac1{2!}
+
\cdots.
$$
The coefficient of $z^{-1}$ is $1$, which is the residue.

:::

:::

::: {.pf-step #s4}

The value of the integral is
$$
\boxed{2\pi}.
$$

::: pf-proof

The only pole inside the unit circle is $z=0$. By steps [](#s2){.pf-ref} and [](#s3){.pf-ref} and the
residue theorem,
$$
\begin{aligned}
\int_0^{2\pi} e^{e^{i\theta}-i\theta}\,d\theta
&=
\frac1i
\left(
2\pi i
\operatorname{Res}_{z=0}\frac{e^z}{z^2}
\right)\\
&=
\frac1i(2\pi i)\\
&=
2\pi.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives the requested value.

:::

:::

:::
