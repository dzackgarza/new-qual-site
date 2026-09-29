---
schema: qual/card@1
id: P-BKF20-5B
kind: problem
title: A Blaschke factor and an extremal value at the origin
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2020 Blaschke-factor argument.
    The factor g(z)=(z-1/2)/(1-z/2) has unit boundary modulus, and
    f/(g e^z) extends holomorphically across z=1/2 before maximum modulus is
    applied.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked holomorphy and zeros of the Blaschke factor, its boundary modulus,
    removability of the quotient at 1/2, the maximum-modulus estimate, and
    attainment of the bound by g(z)e^z.
---

::: {.problem}
(a) Find a function holomorphic on the closed unit disk, of absolute value $1$ on the unit circle, whose only zero in the disk is $1/2$.

(b) Let $f$ be holomorphic on the closed disk with $f(1/2)=0$ and $|f(z)|\le|e^z|$ for $|z|=1$. How large can $|f(0)|$ be?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Define
$$
g(z)
\coloneqq
\frac{z-\frac12}{1-\frac z2}.
$$
Then $g$ is holomorphic on a neighborhood of the closed unit disk and
its only zero there is
$$
z=\frac12.
$$

::: pf-proof

The denominator vanishes only at $z=2$, which lies outside the closed
unit disk. Thus $g$ is holomorphic on a neighborhood of that disk.
Its numerator has the unique zero $z=1/2$, and the denominator is
nonzero there.

:::

:::

::: {.pf-step #s2}

For every $|z|=1$,
$$
|g(z)|=1.
$$

::: pf-proof

If $|z|=1$, then $\overline z=z^{-1}$ and
$$
\begin{aligned}
\left|z-\frac12\right|^2
&=
\left(z-\frac12\right)
\left(\overline z-\frac12\right)\\
&=
\frac54-\frac12(z+\overline z),
\end{aligned}
$$
while
$$
\begin{aligned}
\left|1-\frac z2\right|^2
&=
\left(1-\frac z2\right)
\left(1-\frac{\overline z}{2}\right)\\
&=
\frac54-\frac12(z+\overline z).
\end{aligned}
$$
The numerator and denominator of $|g(z)|^2$ are therefore equal.
Together with step [](#s1){.pf-ref}, this proves part (a).

:::

:::

::: {.pf-step #s3}

For a function $f$ as in part (b), the quotient
$$
h(z)
\coloneqq
\frac{f(z)}{g(z)e^z}
$$
has a removable singularity at $z=1/2$ and extends holomorphically to
the unit disk.

::: pf-proof

The exponential has no zeros. The function $g$ has a simple zero at
$1/2$, while $f(1/2)=0$. Hence one may write locally
$$
f(z)
=
\left(z-\frac12\right)u(z)
$$
with $u$ holomorphic, and
$$
g(z)
=
\left(z-\frac12\right)
\frac1{1-z/2}.
$$
Thus near $1/2$,
$$
h(z)
=
\frac{u(z)(1-z/2)}{e^z},
$$
which is holomorphic. This gives the desired extension.

:::

:::

::: {.pf-step #s4}

On the unit circle,
$$
|h(z)|\le1.
$$

::: pf-proof

For $|z|=1$, step [](#s2){.pf-ref} and the hypothesis on $f$ give
$$
|h(z)|
=
\frac{|f(z)|}{|g(z)|\,|e^z|}
\le
\frac{|e^z|}{1\cdot|e^z|}
=
1.
$$

:::

:::

::: {.pf-step #s5}

One has
$$
|f(0)|\le\frac12.
$$

::: pf-proof

By step [](#s3){.pf-ref}, $h$ is holomorphic on the unit disk and continuous on its
boundary. Step [](#s4){.pf-ref} and the maximum modulus principle imply
$$
|h(0)|\le1.
$$
Since
$$
g(0)=-\frac12
\qquad\text{and}\qquad
e^0=1,
$$
we have
$$
|h(0)|
=
\frac{|f(0)|}{|g(0)|}
=
2|f(0)|.
$$
Therefore
$$
|f(0)|\le\frac12.
$$

:::

:::

::: {.pf-step #s6}

The bound in step [](#s5){.pf-ref} is attained.

::: pf-proof

Take
$$
f(z)=g(z)e^z.
$$
Then $f$ is holomorphic on the closed unit disk and
$$
f\left(\frac12\right)=0.
$$
For $|z|=1$, step [](#s2){.pf-ref} gives
$$
|f(z)|
=
|g(z)|\,|e^z|
=
|e^z|.
$$
Finally,
$$
|f(0)|
=
|g(0)|
=
\frac12.
$$

:::

:::

::: {.pf-step #s7}

Hence the largest possible value is
$$
\boxed{\frac12}.
$$

::: pf-proof

Step [](#s5){.pf-ref} gives the upper bound and step [](#s6){.pf-ref} realizes it.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove part (a), and steps [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} prove part (b).

:::

:::

:::
