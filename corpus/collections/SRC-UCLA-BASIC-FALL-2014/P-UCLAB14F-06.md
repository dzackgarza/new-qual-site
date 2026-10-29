---
schema: qual/card@1
id: P-UCLAB14F-06
kind: problem
title: Total variation of a $C^1$ function from uniform partitions
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
  note: Checked against Problem 6 of the retained UCLA Basic Examination, Fall 2014.
---

::: {.problem}
Problem 6. Let $f:[0,1]\to\RR$ be a $C^1$ function. Prove that
$$
\lim_{n\to\infty}\sum_{k=0}^{n-1}
\left|f\!\left(\frac{k+1}{n}\right)-f\!\left(\frac{k}{n}\right)\right|
=
\int_0^1 |f'(t)|\,dt.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For each $n$ and each
$$
k=0,\ldots,n-1,
$$
there exists
$$
\xi_{k,n}\in
\left(\frac{k}{n},\frac{k+1}{n}\right)
$$
such that
$$
f\!\left(\frac{k+1}{n}\right)
-
f\!\left(\frac{k}{n}\right)
=
\frac1n f'(\xi_{k,n}).
$$


::: pf-proof

Apply the mean value theorem to $f$ on the interval
$$
\left[\frac{k}{n},\frac{k+1}{n}\right].
$$
The hypotheses hold because $f$ is $C^1$, hence continuous on the closed interval and differentiable in its interior.

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\left|
f\!\left(\frac{k+1}{n}\right)
-
f\!\left(\frac{k}{n}\right)
\right|
=
\frac1n|f'(\xi_{k,n})|.
$$


::: pf-proof

Take absolute values in the identity from step [](#s1-1){.pf-ref} and use $1/n>0$.

:::

:::

::: {.pf-step #s1-3}

The sum in the problem equals the tagged Riemann sum
$$
\frac1n
\sum_{k=0}^{n-1}
|f'(\xi_{k,n})|
$$
for the function
$$
g(t)=|f'(t)|
$$
on the uniform partition of $[0,1]$.


::: pf-proof

Sum the identities from step [](#s1-2){.pf-ref} over
$$
k=0,\ldots,n-1.
$$
The point $\xi_{k,n}$ is a tag in the $k$th interval of the uniform partition, whose width is $1/n$.

:::

:::

::: {.pf-step #s1-4}

The function
$$
g(t)=|f'(t)|
$$
is continuous on $[0,1]$.


::: pf-proof

The derivative $f'$ is continuous because $f$ is $C^1$, and the absolute-value function is continuous.
Therefore their composition is continuous.

:::

:::

::: {.pf-step #s1-5}

The tagged Riemann sums in step [](#s1-3){.pf-ref} converge to
$$
\int_0^1|f'(t)|\,dt.
$$


::: pf-proof

For each $n$, the mesh of the uniform partition is
$$
\frac1n,
$$
which tends to $0$.
For a continuous function on a compact interval, every sequence of tagged Riemann sums whose mesh tends to $0$ converges to the Riemann integral.
Applying this theorem to the continuous function $g=|f'|$ from step [](#s1-4){.pf-ref} gives the claim.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\lim_{n\to\infty}
\sum_{k=0}^{n-1}
\left|
f\!\left(\frac{k+1}{n}\right)
-
f\!\left(\frac{k}{n}\right)
\right|
=
\int_0^1|f'(t)|\,dt
}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, the left side is exactly the sequence of tagged Riemann sums considered in step [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required identity.

:::

:::

:::
