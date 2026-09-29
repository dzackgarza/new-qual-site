---
schema: qual/card@1
id: P-BKF88-8
kind: problem
title: Zeros of $e^z+z$ and $ze^z+1$ in the strip $\abs{\operatorname{Im}z}<\pi/2$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 in the deterministic MinerU Flash extraction assets/attachments/Fall88_extracted.md; Flash garbles $\operatorname{Im}z$ in the strip, restored from the complex-analytic context.
---

::: {.problem}
Do
\[
f(z)=e^z+z
\qquad\text{and}\qquad
g(z)=ze^z+1
\]
have the same number of zeros in the strip
\[
-\frac\pi2<\operatorname{Im}z<\frac\pi2?
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The function
$$
f(z)=e^z+z
$$
has exactly one zero in the strip
$$
-\frac{\pi}{2}<\operatorname{Im}z<\frac{\pi}{2}.
$$

::: pf-proof

Write a zero as $z=x+iy$. The equation $f(z)=0$ gives
$$
e^x\cos y=-x,
\qquad
e^x\sin y=-y.
$$
For $-\pi/2<y<\pi/2$, the numbers $\sin y$ and $y$ have the same sign. Thus the second equation is impossible when $y\neq0$, because its two sides then have opposite signs. Hence every zero of $f$ in the strip is real.

For real $x$, zeros are the solutions of
$$
h(x)=e^x+x=0.
$$
Since
$$
h'(x)=e^x+1>0,
$$
the function $h$ is strictly increasing. Moreover,
$$
\lim_{x\to-\infty}h(x)=-\infty,
\qquad
h(0)=1.
$$
The intermediate value theorem therefore gives exactly one real zero.

:::

:::

::: {.pf-step #s2}

The function
$$
g(z)=ze^z+1
$$
has no real zero.

::: pf-proof

For real $x$, the equation $g(x)=0$ would be
$$
xe^x=-1.
$$
The real function $q(x)=xe^x$ has derivative
$$
q'(x)=e^x(1+x),
$$
so its minimum occurs at $x=-1$ and equals $-e^{-1}>-1$. Hence the displayed equation has no real solution.

:::

:::

::: {.pf-step #s3}

Zeros of $g$ with
$$
0<\operatorname{Im}z<\frac{\pi}{2}
$$
are in one-to-one correspondence with zeros on $(0,\pi/2)$ of
$$
F(y)=\log\left(\frac{y}{\sin y}\right)-y\cot y.
$$

::: pf-proof

Write $z=x+iy$ with $0<y<\pi/2$. The equation $g(z)=0$ is equivalent to
$$
e^x(x\cos y-y\sin y)=-1,
\qquad
x\sin y+y\cos y=0.
$$
Since $\sin y>0$, the second equation gives
$$
x=-y\cot y.
$$
Substitution into the first gives
$$
e^{-y\cot y}\frac{y}{\sin y}=1.
$$
Both factors are positive, so taking logarithms yields
$$
\log\left(\frac{y}{\sin y}\right)-y\cot y=0.
$$
Every step is reversible, proving the correspondence.

:::

:::

::: {.pf-step #s4}

The function $F$ from step [](#s3){.pf-ref} has exactly one zero in $(0,\pi/2)$.

::: pf-proof

Its endpoint limits are
$$
\lim_{y\to0^+}F(y)=-1
$$
and
$$
\lim_{y\to(\pi/2)^-}F(y)
=
\log\left(\frac{\pi}{2}\right)
>0.
$$
Furthermore,
$$
F'(y)
=
\frac1y-2\cot y+y\csc^2y.
$$
Multiplying by the positive number $y\sin^2y$ gives
$$
\begin{aligned}
y\sin^2y\,F'(y)
&=
\sin^2y-2y\sin y\cos y+y^2\\
&=
(y-\sin y\cos y)^2+\sin^4y\\
&>0.
\end{aligned}
$$
Thus $F$ is strictly increasing. The intermediate value theorem and the endpoint signs show that it has exactly one zero.

:::

:::

::: {.pf-step #s5}

The function $g$ has exactly two zeros in the strip.

::: pf-proof

By steps [](#s3){.pf-ref} and [](#s4){.pf-ref}, $g$ has exactly one zero in the upper half of the strip. Since
$$
g(\overline z)=\overline{g(z)},
$$
complex conjugation gives exactly one zero in the lower half. Step [](#s2){.pf-ref} shows that there is no additional real zero. Hence the strip contains exactly two zeros of $g$.

:::

:::

::: {.pf-step #s6}

Every zero of either function in the strip is simple.

::: pf-proof

If $f(z)=f'(z)=0$, then $f'(z)=e^z+1=0$ gives $e^z=-1$, while $f(z)=0$ then gives $z=1$, a contradiction. Thus every zero of $f$ is simple.

Similarly,
$$
g'(z)=e^z(z+1).
$$
Since the exponential never vanishes, a multiple zero of $g$ would have to occur at $z=-1$, but
$$
g(-1)=1-e^{-1}\neq0.
$$
Thus every zero of $g$ is simple.

:::

:::

::: {.pf-step #s7}

The two functions do not have the same number of zeros in the strip:
$$
\boxed{f\text{ has one zero, whereas }g\text{ has two}.}
$$

::: pf-proof

This follows from steps [](#s1){.pf-ref} and [](#s5){.pf-ref}. Step [](#s6){.pf-ref} shows that the same counts hold when zeros are counted with multiplicity.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} answers the question.

:::

:::

:::
