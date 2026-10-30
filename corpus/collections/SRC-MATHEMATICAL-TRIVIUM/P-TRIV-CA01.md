---
schema: qual/card@1
id: P-TRIV-CA01
kind: problem
title: Polar forms of $3i$, $1-i$, $2+i$, $-4$, $2-i\sqrt3$ and $\frac{2-i}{1+4i}$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 1, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Write the following complex numbers in polar form:
$$
3i, \qquad 1 - i, \qquad 2 + i, \qquad -4, \qquad 2 - i\sqrt{3}, \qquad \frac{2 - i}{1 + 4i}, \qquad \abs{3 + i}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

One has
$$
3i
=
\boxed{3e^{i\pi/2}}.
$$


::: pf-proof

The modulus is $3$, and the point lies on the positive imaginary axis, whose
principal argument is $\pi/2$.

:::

:::

::: {.pf-step #s1-2}

One has
$$
1-i
=
\boxed{\sqrt2\,e^{-i\pi/4}}.
$$


::: pf-proof

Its modulus is
$$
\sqrt{1^2+(-1)^2}=\sqrt2,
$$
and its principal argument is $-\pi/4$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
2+i
=
\boxed{
\sqrt5\,
e^{,i\arctan(1/2)}
}.
$$


::: pf-proof

The modulus is
$$
\sqrt{2^2+1^2}=\sqrt5.
$$
The point lies in the first quadrant and satisfies
$$
\tan\theta=\frac12,
$$
so its principal argument is $\arctan(1/2)$.

:::

:::

::: {.pf-step #s1-4}

One has
$$
-4
=
\boxed{4e^{i\pi}}.
$$


::: pf-proof

The modulus is $4$, and the point lies on the negative real axis, whose
principal argument is $\pi$.

:::

:::

::: {.pf-step #s1-5}

One has
$$
2-i\sqrt3
=
\boxed{
\sqrt7\,
e^{-i\arctan(\sqrt3/2)}
}.
$$


::: pf-proof

The modulus is
$$
\sqrt{2^2+(\sqrt3)^2}
=
\sqrt7.
$$
The point lies in the fourth quadrant and
$$
\tan\abs{\theta}
=
\frac{\sqrt3}{2}.
$$
Hence the principal argument is
$$
-\arctan\left(\frac{\sqrt3}{2}\right).
$$

:::

:::

::: {.pf-step #s1-6}

The quotient simplifies to
$$
\frac{2-i}{1+4i}
=
\frac{-2-9i}{17}.
$$


::: pf-proof

Multiply numerator and denominator by the conjugate $1-4i$:
$$
\frac{2-i}{1+4i}
=
\frac{(2-i)(1-4i)}{1+16}
=
\frac{-2-9i}{17}.
$$

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\frac{2-i}{1+4i}
=
\boxed{
\sqrt{\frac5{17}},
e^{,i(-\pi+\arctan(9/2))}
}.
$$


::: pf-proof

By step [](#s1-6){.pf-ref}, the modulus is
$$
\frac{\sqrt{(-2)^2+(-9)^2}}{17}
=
\frac{\sqrt{85}}{17}
=
\sqrt{\frac5{17}}.
$$
The point lies in the third quadrant. Its reference angle satisfies
$$
\tan\phi=\frac92,
$$
so a principal argument is
$$
-\pi+\arctan\left(\frac92\right).
$$

:::

:::

::: {.pf-step #s1-8}

Finally,
$$
\abs{3+i}
=
\sqrt{10}
=
\boxed{\sqrt{10}\,e^{i0}}.
$$


::: pf-proof

One has
$$
\abs{3+i}
=
\sqrt{3^2+1^2}
=
\sqrt{10},
$$
which is a positive real number and therefore has argument $0$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-8){.pf-ref} give polar forms for all seven requested quantities.

:::

:::

:::
