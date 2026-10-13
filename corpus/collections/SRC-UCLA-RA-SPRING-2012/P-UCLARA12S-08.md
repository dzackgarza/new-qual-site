---
schema: qual/card@1
id: P-UCLARA12S-08
kind: problem
title: An unbounded harmonic function with zero boundary values
classification:
  areas:
  - real-analysis
  topics: []
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
\[
\Omega=\{x+iy:x>0,\ y>0,\ xy<1\}.
\]
Give an example of an unbounded harmonic function on $\Omega$ that extends continuously to $\partial\Omega$ and vanishes there.
:::

::: {.solution}
Define
$$
\boxed{u(z)\coloneqq\operatorname{Im}\!\left(e^{\pi z^2}\right)}.
$$

<1>1. The function $u$ is harmonic on $\Omega$.

::: {.proof}
The function
$$
F(z)=e^{\pi z^2}
$$
is entire. The imaginary part of a holomorphic function is harmonic, so $u=\operatorname{Im}F$ is harmonic on $\CC$, hence on $\Omega$.
:::

<1>2. For $z=x+iy$,
$$
u(x+iy)
=
e^{\pi(x^2-y^2)}\sin(2\pi xy).
$$

::: {.proof}
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

<1>3. The function $u$ extends continuously to $\partial\Omega$ and vanishes there.

::: {.proof}
The formula in step <1>2 defines a continuous function on all of $\CC$, so it already supplies a continuous extension to the closure of $\Omega$.

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

<1>4. The function $u$ is unbounded on $\Omega$.

::: {.proof}
For $x>0$, take
$$
z_x=x+\frac{i}{4x}.
$$
Then
$$
x\cdot\frac1{4x}=\frac14<1,
$$
so $z_x\in\Omega$. By step <1>2,
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

<1>5. Q.E.D.

::: {.proof}
Steps <1>1, <1>3, and <1>4 verify respectively harmonicity, the zero continuous boundary extension, and unboundedness.
:::
:::
