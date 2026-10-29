---
schema: qual/card@1
id: P-PRECALC2-03
kind: problem
title: The integral $\int_0^\infty x^ne^{-x}\,dx$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
For $n \in \NN ,$ evaluate $\int _ { 0 } ^ { \infty } x ^ { n } e ^ { - x } d x .$
:::

::: {.solution}

For $n\ge0$, define
$$
I_n
=
\int_0^\infty x^n e^{-x}\,dx.
$$

::: pf

::: {.pf-step #s1-1}

The base case is
$$
\boxed{I_0=1}.
$$


::: pf-proof

$$
I_0
=
\int_0^\infty e^{-x}\,dx
=
\left[-e^{-x}\right]_0^\infty
=
0-(-1)
=
1.
$$

:::

:::

::: {.pf-step #s1-2}

For every integer $n\ge1$,
$$
\lim_{x\to\infty}x^ne^{-x}=0.
$$


::: pf-proof

Using the exponential series,
$$
e^x
=
\sum_{k=0}^{\infty}\frac{x^k}{k!}
\ge
\frac{x^{n+1}}{(n+1)!}
\qquad(x>0).
$$
Hence
$$
0
\le
x^ne^{-x}
\le
\frac{(n+1)!}{x}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-3}

For $n\ge1$, integration by parts gives
$$
I_n
=
\left[-x^ne^{-x}\right]_0^\infty
+
n\int_0^\infty x^{n-1}e^{-x}\,dx.
$$


::: pf-proof

Take
$$
u=x^n,
\qquad
dv=e^{-x}\,dx.
$$
Then
$$
du=nx^{n-1}\,dx,
\qquad
v=-e^{-x}.
$$
Apply integration by parts to the improper integral, understood as the limit
over $[0,R]$.

:::

:::

::: {.pf-step #s1-4}

The boundary term in step [](#s1-3){.pf-ref} is zero:
$$
\boxed{
\left[-x^ne^{-x}\right]_0^\infty=0}.
$$


::: pf-proof

At $x=\infty$, step [](#s1-2){.pf-ref} gives
$$
x^ne^{-x}\to0.
$$
At $x=0$, since $n\ge1$,
$$
x^ne^{-x}=0.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{I_n=nI_{n-1}}
\qquad(n\ge1).
$$


::: pf-proof

Combine steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Iterating the recurrence gives
$$
I_n
=
n(n-1)\cdots2\cdot1\,I_0.
$$


::: pf-proof

Repeatedly apply step [](#s1-5){.pf-ref}:
$$
I_n=nI_{n-1}
=n(n-1)I_{n-2}
=\cdots
=n!I_0.
$$

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{
\int_0^\infty x^ne^{-x}\,dx
=
n!}.
$$


::: pf-proof

By step [](#s1-6){.pf-ref} and the base value $I_0=1$ from step [](#s1-1){.pf-ref},
$$
I_n=n!.
$$

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the requested value.

:::

:::

:::
