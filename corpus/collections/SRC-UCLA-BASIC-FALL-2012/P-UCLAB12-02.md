---
schema: qual/card@1
id: P-UCLAB12-02
kind: problem
title: Riemann integrability of monotone functions
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $f(x)$ be a bounded real-valued function on the closed interval $[0, 1]$.

(a) Give a (correct) definition of the Riemann integral $\int_0^1 f(x)\,dx$ that includes a necessary and sufficient condition for the integral to exist.

(b) Use your answer to (a) to prove that $\int_0^1 f(x)\,dx$ exists if $f$ is non-decreasing (i.e. $f(x) \leq f(y)$ whenever $x \leq y$).
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For a partition
$$
P:\quad 0=x_0<x_1<\cdots<x_m=1,
$$
define
$$
M_i=\sup_{x\in[x_{i-1},x_i]}f(x),
\qquad
m_i=\inf_{x\in[x_{i-1},x_i]}f(x),
$$
and
$$
U(f,P)=\sum_{i=1}^mM_i(x_i-x_{i-1}),
\qquad
L(f,P)=\sum_{i=1}^m m_i(x_i-x_{i-1}).
$$


::: pf-proof

The function is bounded by hypothesis, so all $M_i$ and $m_i$ are finite.

:::

:::

::: {.pf-step #s1-2}

Define
$$
\overline{\int_0^1}f
=
\inf_P U(f,P)
$$
and
$$
\underline{\int_0^1}f
=
\sup_P L(f,P).
$$
Then $f$ is Riemann integrable exactly when
$$
\overline{\int_0^1}f
=
\underline{\int_0^1}f.
$$
Their common value is the Riemann integral.


::: pf-proof

This is the Darboux formulation of the definition of the Riemann integral.

:::

:::

::: {.pf-step #s1-3}

Equivalently, $f$ is Riemann integrable if and only if for every $\varepsilon>0$ there exists a partition $P$ such that
$$
U(f,P)-L(f,P)<\varepsilon.
$$


::: pf-proof

For every partition $P$,
$$
L(f,P)
\le
\underline{\int_0^1}f
\le
\overline{\int_0^1}f
\le
U(f,P).
$$
Thus arbitrarily small upper-minus-lower gaps force equality of the upper and lower integrals.

Conversely, if the upper and lower integrals are equal, choose one partition whose upper sum is within $\varepsilon/2$ of the common value and another whose lower sum is within $\varepsilon/2$. Passing to their common refinement can only decrease the upper sum and increase the lower sum, so the resulting gap is less than $\varepsilon$.

:::

:::

::: {.pf-step #s1-4}

Assume now that $f$ is non-decreasing. For every partition $P$,
$$
M_i=f(x_i)
\qquad\text{and}\qquad
m_i=f(x_{i-1}).
$$


::: pf-proof

If
$$
x_{i-1}\le x\le x_i,
$$
monotonicity gives
$$
f(x_{i-1})\le f(x)\le f(x_i).
$$
Hence the infimum and supremum on the subinterval are attained at its endpoints.

:::

:::

::: {.pf-step #s1-5}

For every partition $P$,
$$
U(f,P)-L(f,P)
=
\sum_{i=1}^m
\bigl(f(x_i)-f(x_{i-1})\bigr)(x_i-x_{i-1}).
$$


::: pf-proof

Substitute the endpoint formulas from step [](#s1-4){.pf-ref} into the definitions of the upper and lower sums.

:::

:::

::: {.pf-step #s1-6}

If the mesh of $P$ satisfies
$$
\max_i(x_i-x_{i-1})\le\delta,
$$
then
$$
U(f,P)-L(f,P)
\le
\delta\bigl(f(1)-f(0)\bigr).
$$


::: pf-proof

Every difference
$$
f(x_i)-f(x_{i-1})
$$
is nonnegative. Hence step [](#s1-5){.pf-ref} gives
$$
\begin{aligned}
U(f,P)-L(f,P)
&\le
\delta
\sum_{i=1}^m
\bigl(f(x_i)-f(x_{i-1})\bigr)\\
&=
\delta\bigl(f(1)-f(0)\bigr),
\end{aligned}
$$
because the sum telescopes.

:::

:::

::: {.pf-step #s1-7}

For every $\varepsilon>0$, there exists a partition $P$ such that
$$
U(f,P)-L(f,P)<\varepsilon.
$$


::: pf-proof

If
$$
f(1)=f(0),
$$
then monotonicity forces $f$ to be constant and the upper and lower sums are equal for every partition.

Otherwise choose
$$
0<\delta<
\frac{\varepsilon}{f(1)-f(0)}.
$$
Take any partition with mesh at most $\delta$. Step [](#s1-6){.pf-ref} gives
$$
U(f,P)-L(f,P)
<
\varepsilon.
$$

:::

:::

::: {.pf-step #s1-8}

Therefore every bounded non-decreasing function on $[0,1]$ is Riemann integrable.


::: pf-proof

Apply the criterion from step [](#s1-3){.pf-ref} using step [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} answer part (a), and steps [](#s1-4){.pf-ref} through [](#s1-8){.pf-ref} prove part (b).

:::

:::

:::
