---
schema: qual/card@1
id: P-BKS08-8B
kind: problem
title: The recurrence $x_n=x_{n-1}-\frac12x_{n-2}$ with $x_0=x_1=1$
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
  note: Checked against the vendored UC Berkeley Spring 2008 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the characteristic roots and the constants determined
    by x_0=x_1=1 against the vendored solution.
---

::: {.problem}
Compute the sequence $\{x_n\}_{n=0}^\infty$ satisfying
$$
x_n=x_{n-1}-\frac12x_{n-2}\qquad(n\ge2),
$$
with
$$
x_0=1,\qquad x_1=1.
$$
:::

::: {.solution}
<1>1. The characteristic equation of the recurrence is
$$
r^2-r+\frac12=0,
$$
with roots
$$
r_\pm=\frac{1\pm i}{2}
=2^{-1/2}e^{\pm i\pi/4}.
$$

::: {.proof}
Substituting $x_n=r^n$ into
$x_n=x_{n-1}-\frac12x_{n-2}$ gives
$$
r^2=r-\frac12.
$$
The quadratic formula yields
$$
r=\frac{1\pm\sqrt{-1}}2=\frac{1\pm i}{2}.
$$
Their polar form follows from
$\abs{1\pm i}=\sqrt2$ and arguments $\pm\pi/4$.
:::

<1>2. Every real solution has the form
$$
x_n
=2^{-n/2}
\left(
A\cos\frac{n\pi}{4}
B\sin\frac{n\pi}{4}
\right)
$$
for real constants $A,B$.

::: {.proof}
The two distinct characteristic roots in step <1>1 give the complex
general solution
$$
x_n=C_+r_+^n+C_-r_-^n.
$$
Taking real linear combinations of the conjugate roots gives exactly
the displayed sine-cosine form.
:::

<1>3. The initial condition $x_0=1$ gives
$$
A=1.
$$

::: {.proof}
Setting $n=0$ in step <1>2 gives $x_0=A$.
:::

<1>4. The initial condition $x_1=1$ then gives
$$
B=1.
$$

::: {.proof}
Using $A=1$ from step <1>3,
$$
1=x_1
=2^{-1/2}
\left(
\cos\frac\pi4+B\sin\frac\pi4
\right)
=\frac{1+B}{2}.
$$
Hence $B=1$.
:::

<1>5. Therefore
$$
\boxed{
x_n
=2^{-n/2}
\left(
\cos\frac{n\pi}{4}
+\sin\frac{n\pi}{4}
\right)
=2^{(1-n)/2}
\cos\frac{(n-1)\pi}{4}.
}
$$

::: {.proof}
Substitute $A=B=1$ into step <1>2. The second expression follows from
$$
\cos\theta+\sin\theta
=\sqrt2\cos\left(\theta-\frac\pi4\right).
$$
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the unique sequence determined by the recurrence and
the two initial values.
:::
:::
