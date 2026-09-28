---
schema: qual/card@1
id: P-BKS94-5
kind: problem
title: Minimal-order constant-coefficient ODE with solutions $\sin t$ and $\sin 2t$
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
  note: Checked against the vendored UC Berkeley Spring 1994 preliminary examination.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Used the characteristic polynomial to force roots at plus/minus i and
    plus/minus 2i; the same four roots are forced over complex coefficients,
    so the minimum order remains four.
---

::: {.problem}
1. Suppose the functions sin t and sin 2t are both solutions of the differential equation

$$
\sum _ { k = 0 } ^ { n } \ c _ { k } { \frac { d ^ { k } x } { d t ^ { k } } } = 0 \ ,
$$

where $c _ { 0 } , \ldots , c _ { n }$ are real constants. What is the smallest possible order of the equation? Write down an equation of minimum order having the given functions as solutions.

2. Will the answers to Part 1 be different if the constants $c _ { 0 } , \ldots , c _ { n }$ are allowed to be complex?
:::

::: {.solution}
Let
$$
P(z)\coloneqq\sum_{k=0}^n c_k z^k.
$$

<1>1. If $\sin t$ is a solution, then
$$
P(i)=P(-i)=0.
$$

::: {.proof}
Since
$$
\sin t=\frac{e^{it}-e^{-it}}{2i},
$$
one has
$$
P(D)\sin t
=
\frac{P(i)e^{it}-P(-i)e^{-it}}{2i}.
$$
If this function is identically zero, the linear independence of
$e^{it}$ and $e^{-it}$ over $\CC$ forces both coefficients to vanish.
:::

<1>2. If $\sin 2t$ is a solution, then
$$
P(2i)=P(-2i)=0.
$$

::: {.proof}
Likewise,
$$
\sin2t=\frac{e^{2it}-e^{-2it}}{2i},
$$
so
$$
P(D)\sin2t
=
\frac{P(2i)e^{2it}-P(-2i)e^{-2it}}{2i}.
$$
The two exponentials are linearly independent, giving the two asserted
roots.
:::

<1>3. Every nonzero constant-coefficient equation having both prescribed
solutions has order at least $4$.

::: {.proof}
Steps <1>1 and <1>2 show that its characteristic polynomial has the four
distinct roots
$$
i,-i,2i,-2i.
$$
Therefore its degree, which is the order of the equation, is at least $4$.
:::

<1>4. The fourth-order equation
$$
x^{(4)}+5x''+4x=0
$$
has both $\sin t$ and $\sin2t$ as solutions.

::: {.proof}
Its characteristic polynomial is
$$
z^4+5z^2+4
=(z^2+1)(z^2+4),
$$
whose roots are precisely
$$
\pm i,\qquad\pm2i.
$$
Thus $e^{\pm it}$ and $e^{\pm2it}$ are solutions, and hence so are their
linear combinations $\sin t$ and $\sin2t$.
:::

<1>5. For real coefficients, the smallest possible order is $4$, and one
minimum-order equation is
$$
\boxed{x^{(4)}+5x''+4x=0}.
$$

::: {.proof}
Step <1>3 gives the lower bound, while step <1>4 realizes it with real
coefficients.
:::

<1>6. Allowing the coefficients $c_k$ to be complex does not change either
answer.

::: {.proof}
The arguments in steps <1>1--<1>3 used only complex linear independence of
the exponential functions and therefore remain valid when the $c_k$ are
complex. Thus order at least $4$ is still necessary. The real-coefficient
equation in step <1>4 is also a complex-coefficient equation, so order $4$
is still attainable.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>5 and <1>6 answer the two parts.
:::
:::
