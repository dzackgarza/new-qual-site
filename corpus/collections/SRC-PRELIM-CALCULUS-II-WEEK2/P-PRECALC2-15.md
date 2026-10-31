---
schema: qual/card@1
id: P-PRECALC2-15
kind: problem
title: Telescoping sum $\sum_{n\ge1}\frac{m}{n(n+m)}$
classification:
  areas:
  - prelim
  topics:
  - Series
  - Telescoping Series
relations: []
review: draft
---

::: {.problem}
Fix an integer $m > 0$. Evaluate the infinite sum
$$
\sum_{n=1}^{\infty} \frac{m}{n(n + m)}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The summand has the partial-fraction decomposition
$$
\boxed{
\frac{m}{n(n+m)}
=
\frac1n-\frac1{n+m}}.
$$


::: pf-proof

$$
\frac1n-\frac1{n+m}
=
\frac{n+m-n}{n(n+m)}
=
\frac{m}{n(n+m)}.
$$

:::

:::

::: {.pf-step #s1-2}

Let
$$
S_N
=
\sum_{n=1}^{N}
\frac{m}{n(n+m)}.
$$
Then
$$
S_N
=
\sum_{n=1}^{N}\frac1n
-
\sum_{n=1}^{N}\frac1{n+m}.
$$


::: pf-proof

Sum the identity from step [](#s1-1){.pf-ref} for $1\le n\le N$.

:::

:::

::: {.pf-step #s1-3}

Reindex the second sum:
$$
\boxed{
\sum_{n=1}^{N}\frac1{n+m}
=
\sum_{k=m+1}^{N+m}\frac1k}.
$$


::: pf-proof

Set
$$
k=n+m.
$$
Then $n=1$ corresponds to $k=m+1$, and $n=N$ corresponds to
$k=N+m$.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
S_N
=
\sum_{k=1}^{N}\frac1k
-
\sum_{k=m+1}^{N+m}\frac1k.
$$


::: pf-proof

Combine steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

For $N\ge m$,
$$
\boxed{
S_N
=
\sum_{k=1}^{m}\frac1k
-
\sum_{k=N+1}^{N+m}\frac1k}.
$$


::: pf-proof

In step [](#s1-4){.pf-ref}, the terms
$$
\frac1{m+1},\dots,\frac1N
$$
cancel. The first sum leaves $1,\dots,m$, while the second sum leaves
$N+1,\dots,N+m$ with a minus sign.

:::

:::

::: {.pf-step #s1-6}

The tail term satisfies
$$
0
\le
\sum_{k=N+1}^{N+m}\frac1k
\le
\frac{m}{N+1}.
$$


::: pf-proof

There are $m$ terms, and each satisfies
$$
\frac1k
\le
\frac1{N+1}.
$$

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{
\sum_{k=N+1}^{N+m}\frac1k
\longrightarrow0}.
$$


::: pf-proof

By step [](#s1-6){.pf-ref},
$$
0
\le
\sum_{k=N+1}^{N+m}\frac1k
\le
\frac{m}{N+1}
\longrightarrow0.
$$
Apply the squeeze theorem.

:::

:::

::: pf-step

Therefore
$$
\boxed{
\sum_{n=1}^{\infty}
\frac{m}{n(n+m)}
=
\sum_{k=1}^{m}\frac1k}.
$$


::: pf-proof

Take $N\to\infty$ in step [](#s1-5){.pf-ref} and use step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Equivalently,
$$
\boxed{
\sum_{n=1}^{\infty}
\frac{m}{n(n+m)}
=
H_m},
$$
the $m$th harmonic number.


::: pf-proof

By definition,
$$
H_m
=
1+\frac12+\cdots+\frac1m.
$$

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the requested value.

:::

:::

:::
