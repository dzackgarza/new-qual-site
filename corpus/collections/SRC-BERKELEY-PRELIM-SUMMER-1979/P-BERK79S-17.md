---
schema: qual/card@1
id: P-BERK79S-17
kind: problem
title: A function vanishing exactly on the unit sphere can have negative Laplacian on the closed ball
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used the counterexample f(x,y,z)=1-x^2-y^2-z^2. Its zero set is exactly
    the unit sphere, but its Laplacian is the constant -6, so no point in
    the closed unit ball can satisfy the requested nonnegative-Laplacian
    inequality.
---

::: {.problem}
Let $f:\mathbb R^3\to\mathbb R$ have continuous partial derivatives through order $2$, and suppose
\[
f^{-1}(0)=\{v\in\mathbb R^3:\|v\|=1\}.
\]
Must there exist a point $p\in\mathbb R^3$ with $\|p\|\le1$ such that
\[
\frac{\partial^2f}{\partial x^2}(p)
+\frac{\partial^2f}{\partial y^2}(p)
+\frac{\partial^2f}{\partial z^2}(p)
\ge0?
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Define
$$
f(x,y,z)=1-x^2-y^2-z^2.
$$
Then $f$ has continuous partial derivatives through order $2$.

::: pf-proof

The function is a polynomial, hence is $C^\infty$ on $\RR^3$.

:::

:::

::: {.pf-step #s2}

Its zero set is exactly the Euclidean unit sphere:
$$
\boxed{
f^{-1}(0)=\{v\in\RR^3:\norm{v}=1\}.
}
$$

::: pf-proof

For $v=(x,y,z)$,
$$
f(v)=0
$$
if and only if
$$
x^2+y^2+z^2=1,
$$
which is equivalent to $\norm{v}=1$.

:::

:::

::: {.pf-step #s3}

The Laplacian of $f$ is
$$
\Delta f=-6
$$
at every point of $\RR^3$.

::: pf-proof

One has
$$
\frac{\partial^2f}{\partial x^2}
=
\frac{\partial^2f}{\partial y^2}
=
\frac{\partial^2f}{\partial z^2}
=
-2.
$$
Therefore
$$
\Delta f=-2-2-2=-6.
$$

:::

:::

::: {.pf-step #s4}

For this $f$, there is no point $p$ with $\norm{p}\leq1$ such that
$$
\Delta f(p)\geq0.
$$

::: pf-proof

By step [](#s3){.pf-ref},
$$
\Delta f(p)=-6<0
$$
for every $p\in\RR^3$.

:::

:::

::: {.pf-step #s5}

The answer is
$$
\boxed{\text{No.}}
$$

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} give a function satisfying all hypotheses for which the
requested point does not exist.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} answers the question.

:::

:::

:::
