---
schema: qual/card@1
id: P-BERK98S-13
kind: problem
title: Integral of $|dz|/|z-a|^2$ over the unit circle for $|a|<1$
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
  date: 2026-09-23
---

::: {.problem}
Let $a\in\mathbb C$ with $|a|<1$. Evaluate
\[
\int_{|z|=1}\frac{|dz|}{|z-a|^2}.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Parametrizing the unit circle by $z=e^{it}$ gives
$$
I
\coloneqq
\int_{\abs z=1}\frac{\abs{dz}}{\abs{z-a}^2}
=
\int_0^{2\pi}
\frac{dt}{\abs{e^{it}-a}^2}.
$$

::: pf-proof

For $z=e^{it}$,
$$
\abs{dz}
=
\abs{i e^{it}}\,dt
=dt.
$$
Substitution gives the displayed formula.

:::

:::

::: {.pf-step #s2}

The real integral in step [](#s1){.pf-ref} equals the contour integral
$$
I
=
\frac1i
\int_{\abs z=1}
\frac{dz}{(z-a)(1-\overline a z)},
$$
where the unit circle is positively oriented.

::: pf-proof

On $\abs z=1$ one has $\overline z=1/z$, so
$$
\abs{z-a}^2
=(z-a)(\overline z-\overline a)
=(z-a)\left(\frac1z-\overline a\right)
=
\frac{(z-a)(1-\overline a z)}{z}.
$$
Also, for $z=e^{it}$,
$$
dz=iz\,dt,
\qquad
dt=\frac{dz}{iz}.
$$
Substitution into step [](#s1){.pf-ref} gives the claimed contour integral.

:::

:::

::: {.pf-step #s3}

The integrand
$$
\frac1{i(z-a)(1-\overline a z)}
$$
has exactly one pole inside the unit circle, namely $z=a$, and its residue
there is
$$
\frac1{i(1-\abs a^2)}.
$$

::: pf-proof

The pole at $z=a$ lies inside because $\abs a<1$. If $a\neq0$, the only
other possible pole is
$$
z=\frac1{\overline a},
$$
whose modulus is $1/\abs a>1$, so it lies outside the unit circle. If
$a=0$, there is no second pole. Finally,
$$
\operatorname*{Res}_{z=a}
\frac1{i(z-a)(1-\overline a z)}
=
\frac1{i(1-\overline a a)}
=
\frac1{i(1-\abs a^2)}.
$$

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{
\int_{\abs z=1}\frac{\abs{dz}}{\abs{z-a}^2}
=
\frac{2\pi}{1-\abs a^2}
}.
$$

::: pf-proof

By steps [](#s2){.pf-ref} and [](#s3){.pf-ref}, the residue theorem gives
$$
I
=
2\pi i\,
\frac1{i(1-\abs a^2)}
=
\frac{2\pi}{1-\abs a^2}.
$$

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required evaluation.

:::

:::

:::
