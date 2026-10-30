---
schema: qual/card@1
id: P-PRECALC1-26
kind: problem
title: Integral of $\abs{x+1}$ over $[-3,3]$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Calculate $\displaystyle \int_{-3}^{3} \abs{x + 1}\, dx$.
:::

::: {.solution}

::: pf

::: pf-step

The expression $x+1$ changes sign at
$$
\boxed{x=-1}.
$$


::: pf-proof

Solve
$$
x+1=0.
$$

:::

:::

::: {.pf-step #s1-2}

For
$$
-3\le x\le-1,
$$
one has
$$
\boxed{\abs{x+1}=-(x+1)}.
$$


::: pf-proof

On this interval,
$$
x+1\le0.
$$

:::

:::

::: {.pf-step #s1-3}

For
$$
-1\le x\le3,
$$
one has
$$
\boxed{\abs{x+1}=x+1}.
$$


::: pf-proof

On this interval,
$$
x+1\ge0.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\int_{-3}^{3}\abs{x+1}\,dx
=
\int_{-3}^{-1}-(x+1)\,dx
+
\int_{-1}^{3}(x+1)\,dx.
$$


::: pf-proof

Split the integral at the sign-change point and use steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

The first integral equals
$$
\boxed{2}.
$$


::: pf-proof

$$
\begin{aligned}
\int_{-3}^{-1}-(x+1)\,dx
&=
\left[
-\frac{x^2}{2}-x
\right]_{-3}^{-1}\\
&=
\left(
-\frac12+1
\right)
-
\left(
-\frac92+3
\right)\\
&=
\frac12-\left(-\frac32\right)\\
&=
2.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-6}

The second integral equals
$$
\boxed{8}.
$$


::: pf-proof

$$
\begin{aligned}
\int_{-1}^{3}(x+1)\,dx
&=
\left[
\frac{x^2}{2}+x
\right]_{-1}^{3}\\
&=
\left(
\frac92+3
\right)
-
\left(
\frac12-1
\right)\\
&=
\frac{15}{2}+\frac12\\
&=
8.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{
\int_{-3}^{3}\abs{x+1}\,dx=10}.
$$


::: pf-proof

Combine steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref}:
$$
2+8=10.
$$

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the requested value.

:::

:::

:::
