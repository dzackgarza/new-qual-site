---
schema: qual/card@1
id: P-TRIV-CA18
kind: problem
title: $\int_0^{2\pi}\frac{d\theta}{1+a\cos\theta}$ for $\abs{a}<1$
classification:
  areas: [complex-analysis]
  topics:
  - Residue Theorem
  - Trigonometric Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 18, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned the formula of Complex Analysis Problem 18 against page 15 of the source PDF and added a remark on the stray dx printed in the source.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source prints a stray trailing dx after d theta; the statement reads the integral with respect to theta only.
---

::: {.problem}
Compute $\displaystyle\int_0^{2\pi} \frac{d\theta}{1 + a\cos\theta}$ with $\abs{a} < 1$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $a=0$, then
$$
\int_0^{2\pi}\frac{d\theta}{1+a\cos\theta}
=
2\pi.
$$


::: pf-proof

For $a=0$ the integrand is identically $1$.

:::

:::

::: {.pf-step #s1-2}

Assume
$$
0<\abs{a}<1
$$
and set
$$
z=e^{i\theta}.
$$
Then
$$
d\theta=\frac{dz}{iz}
$$
and
$$
\cos\theta
=
\frac12\left(z+\frac1z\right).
$$


::: pf-proof

Differentiate $z=e^{i\theta}$ to get
$$
dz=iz\,d\theta.
$$
Euler's formula gives the standard expression for cosine.

:::

:::

::: pf-step

The integral becomes
$$
\int_0^{2\pi}\frac{d\theta}{1+a\cos\theta}
=
\oint_{\abs{z}=1}
\frac{2}{i(az^2+2z+a)}\,dz.
$$


::: pf-proof

Substituting step [](#s1-2){.pf-ref},
$$
1+a\cos\theta
=
1+\frac a2\left(z+\frac1z\right)
=
\frac{az^2+2z+a}{2z}.
$$
Multiplying its reciprocal by $dz/(iz)$ gives the displayed contour
integrand.

:::

:::

::: {.pf-step #s1-4}

The roots of
$$
az^2+2z+a
$$
are
$$
z_\pm
=
\frac{-1\pm\sqrt{1-a^2}}{a}.
$$


::: pf-proof

Apply the quadratic formula.

:::

:::

::: pf-step

Exactly one of the roots in step [](#s1-4){.pf-ref} lies inside the unit circle,
namely
$$
z_+
=
\frac{-1+\sqrt{1-a^2}}{a}
=
-\frac{a}{1+\sqrt{1-a^2}}.
$$


::: pf-proof

Rationalizing the first expression gives the second. Hence
$$
\abs{z_+}
=
\frac{\abs{a}}
{1+\sqrt{1-a^2}}
<1.
$$
The product of the two roots is
$$
z_+z_-=1,
$$
so
$$
\abs{z_-}>1.
$$

:::

:::

::: {.pf-step #s1-6}

The residue of
$$
\frac{2}{i(az^2+2z+a)}
$$
at $z=z_+$ is
$$
\frac1{i\sqrt{1-a^2}}.
$$


::: pf-proof

The derivative of the quadratic denominator is
$$
2az+2.
$$
At $z=z_+$,
$$
az_++1
=
\sqrt{1-a^2}.
$$
Thus the residue is
$$
\frac2{i(2az_++2)}
=
\frac1{i\sqrt{1-a^2}}.
$$

:::

:::

::: {.pf-step #s1-7}

Therefore, for $0<\abs{a}<1$,
$$
\int_0^{2\pi}\frac{d\theta}{1+a\cos\theta}
=
\frac{2\pi}{\sqrt{1-a^2}}.
$$


::: pf-proof

The unit circle encloses only the pole $z_+$. By the residue theorem and
step [](#s1-6){.pf-ref},
$$
\oint_{\abs{z}=1}
\frac{2}{i(az^2+2z+a)}\,dz
=
2\pi i
\frac1{i\sqrt{1-a^2}}
=
\frac{2\pi}{\sqrt{1-a^2}}.
$$

:::

:::

::: {.pf-step #s1-8}

For every real $a$ with $\abs{a}<1$,
$$
\boxed{
\int_0^{2\pi}\frac{d\theta}{1+a\cos\theta}
=
\frac{2\pi}{\sqrt{1-a^2}}.
}
$$


::: pf-proof

Step [](#s1-1){.pf-ref} handles $a=0$, and step [](#s1-7){.pf-ref} handles $0<\abs{a}<1$. The same formula
gives $2\pi$ at $a=0$.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the requested value.

:::

:::

:::
