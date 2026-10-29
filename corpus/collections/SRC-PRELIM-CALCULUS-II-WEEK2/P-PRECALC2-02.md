---
schema: qual/card@1
id: P-PRECALC2-02
kind: problem
title: Integral of $\frac{1}{x\log x}$ over $[e^{-3},e^{-2}]$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Compute $\int _ { e ^ { - 3 } } ^ { e ^ { - 2 } } \frac { d x } { x \log ( x ) } .$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Set
$$
\boxed{u=\log x}.
$$


::: pf-proof

This substitution is natural because the integrand contains the factor
$$
\frac{dx}{x}.
$$

:::

:::

::: {.pf-step #s1-2}

Then
$$
\boxed{du=\frac{dx}{x}}.
$$


::: pf-proof

Differentiate
$$
u=\log x.
$$

:::

:::

::: {.pf-step #s1-3}

The lower bound transforms as
$$
x=e^{-3}
\quad\Longrightarrow\quad
\boxed{u=-3}.
$$


::: pf-proof

$$
\log(e^{-3})=-3.
$$

:::

:::

::: {.pf-step #s1-4}

The upper bound transforms as
$$
x=e^{-2}
\quad\Longrightarrow\quad
\boxed{u=-2}.
$$


::: pf-proof

$$
\log(e^{-2})=-2.
$$

:::

:::

::: pf-step

Therefore
$$
\int_{e^{-3}}^{e^{-2}}
\frac{dx}{x\log x}
=
\int_{-3}^{-2}
\frac{du}{u}.
$$


::: pf-proof

Substitute steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} into the original integral.

:::

:::

::: {.pf-step #s1-6}

An antiderivative of $1/u$ on the interval $[-3,-2]$ is
$$
\boxed{\log|u|}.
$$


::: pf-proof

Since the interval does not contain $0$,
$$
\frac{d}{du}\log|u|
=
\frac1u.
$$

:::

:::

::: pf-step

Hence
$$
\begin{aligned}
\int_{-3}^{-2}\frac{du}{u}
&=
\log|-2|-\log|-3|\\
&=
\log2-\log3.
\end{aligned}
$$


::: pf-proof

Apply the fundamental theorem of calculus using step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
\int_{e^{-3}}^{e^{-2}}
\frac{dx}{x\log x}
=
\log\frac23}.
$$


::: pf-proof

Use the logarithm identity
$$
\log2-\log3
=
\log\left(\frac23\right).
$$

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the requested value.

:::

:::

:::
