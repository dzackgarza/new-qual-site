---
schema: qual/card@1
id: P-BKS13-4A
kind: problem
title: Contour integral of $\cosh(\pi z)/(z(z^2+1))$ over $|z|=2$
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
  note: Compared the authored statement with page 2 of the retained Spring 2013 solution PDF and independently reviewed the residue computation.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the pole set, all three residues, and the positive-orientation residue theorem.
---

::: {.problem}
Find

$$
\int _ { C } { \frac { \cosh ( \pi z ) } { z ( z ^ { 2 } + 1 ) } } d z
$$

when $C$ is the circle $\abs{z} = 2$, described in the positive sense.
:::

::: {.solution}
Set
$$
F(z)
\coloneqq
\frac{\cosh(\pi z)}{z(z^2+1)}.
$$

::: pf

::: pf-step

The poles of $F$ inside
$$
C=\{z:\abs{z}=2\}
$$
are
$$
0,\ i,\ -i,
$$
and they are all simple.

::: pf-proof

The denominator factors as
$$
z(z^2+1)
=
z(z-i)(z+i).
$$
Its three zeros are distinct and all have modulus less than $2$. The
numerator is entire.

:::

:::

::: {.pf-step #s2}

The residue at $0$ is
$$
\operatorname{Res}_{z=0}F(z)=1.
$$

::: pf-proof

Since the pole is simple,
$$
\operatorname{Res}_{z=0}F(z)
=
\lim_{z\to0}
\frac{\cosh(\pi z)}{z^2+1}
=
1.
$$

:::

:::

::: {.pf-step #s3}

The residue at $i$ is
$$
\operatorname{Res}_{z=i}F(z)
=
\frac12.
$$

::: pf-proof

Using
$$
\cosh(\pi i)=\cos\pi=-1,
$$
one gets
$$
\begin{aligned}
\operatorname{Res}_{z=i}F(z)
&=
\frac{\cosh(\pi i)}
{i(i+i)}\\
&=
\frac{-1}{i(2i)}
=
\frac12.
\end{aligned}
$$

:::

:::

::: {.pf-step #s4}

The residue at $-i$ is
$$
\operatorname{Res}_{z=-i}F(z)
=
\frac12.
$$

::: pf-proof

Similarly,
$$
\cosh(-\pi i)=\cos\pi=-1,
$$
and therefore
$$
\begin{aligned}
\operatorname{Res}_{z=-i}F(z)
&=
\frac{\cosh(-\pi i)}
{(-i)(-i-i)}\\
&=
\frac{-1}{(-i)(-2i)}
=
\frac12.
\end{aligned}
$$

:::

:::

::: {.pf-step #s5}

The contour integral is
$$
\boxed{
\int_C
\frac{\cosh(\pi z)}{z(z^2+1)}\,dz
=
4\pi i
}.
$$

::: pf-proof

The contour is positively oriented. By the residue theorem and steps
[](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref},
$$
\begin{aligned}
\int_CF(z)\,dz
&=
2\pi i
\left(
1+\frac12+\frac12
\right)\\
&=
4\pi i.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required value.

:::

:::

:::
