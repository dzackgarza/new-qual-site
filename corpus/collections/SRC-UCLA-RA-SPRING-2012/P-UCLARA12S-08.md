---
schema: qual/card@1
id: P-UCLARA12S-08
kind: problem
title: An unbounded harmonic function with zero boundary values
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Conformal Maps
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Spring 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let
$$
\Omega=\{x+iy:x>0,\ y>0,\ xy<1\}.
$$
Give an example of an unbounded harmonic function on $\Omega$ that extends continuously to $\partial\Omega$ and vanishes there.
:::

::: {.solution}

Define
$$
\boxed{u(z)\coloneqq\operatorname{Im}\!\left(e^{\pi z^2}\right)}.
$$

::: pf

::: {.pf-step #s1-1}

The function $u$ is harmonic on $\Omega$.


::: pf-proof

The function
$$
F(z)=e^{\pi z^2}
$$
is entire. The imaginary part of a holomorphic function is harmonic, so $u=\operatorname{Im}F$ is harmonic on $\CC$, hence on $\Omega$.

:::

:::

::: {.pf-step #s1-2}

For $z=x+iy$,
$$
u(x+iy)
=
e^{\pi(x^2-y^2)}\sin(2\pi xy).
$$


::: pf-proof

Since
$$
z^2=x^2-y^2+2ixy,
$$
one has
$$
e^{\pi z^2}
=
e^{\pi(x^2-y^2)}
e^{2\pi ixy}.
$$
Taking imaginary parts gives the formula.

:::

:::

::: {.pf-step #s1-3}

The function $u$ extends continuously to $\partial\Omega$ and vanishes there.


::: pf-proof

The formula in step [](#s1-2){.pf-ref} defines a continuous function on all of $\CC$, so it already supplies a continuous extension to the closure of $\Omega$.

The boundary of $\Omega$ consists of the nonnegative coordinate rays together with the hyperbola
$$
\{x+iy:x>0,\ y>0,\ xy=1\}.
$$
On either coordinate ray, $xy=0$, so
$$
\sin(2\pi xy)=0.
$$
On the hyperbola, $xy=1$, so
$$
\sin(2\pi xy)=\sin(2\pi)=0.
$$
Thus $u=0$ on all of $\partial\Omega$.

:::

:::

::: {.pf-step #s1-4}

The function $u$ is unbounded on $\Omega$.


::: pf-proof

For $x>0$, take
$$
z_x=x+\frac{i}{4x}.
$$
Then
$$
x\cdot\frac1{4x}=\frac14<1,
$$
so $z_x\in\Omega$. By step [](#s1-2){.pf-ref},
$$
u(z_x)
=
e^{\pi(x^2-1/(16x^2))}
\sin\!\left(\frac\pi2\right)
=
e^{\pi(x^2-1/(16x^2))}.
$$
This tends to $+\infty$ as $x\to\infty$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref}, and [](#s1-4){.pf-ref} verify respectively harmonicity, the zero continuous boundary extension, and unboundedness.

:::

:::

:::
