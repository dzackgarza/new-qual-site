---
schema: qual/card@1
id: P-PRECALC2-13
kind: problem
title: Convergence of $\sum\frac{1}{\log(n!)}$ and $\sum\frac{1}{(\log n)^{\log n}}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Do the series $\displaystyle \sum_{n=2}^{\infty} \frac{1}{\log(n!)}$ and $\displaystyle \sum_{n=3}^{\infty} \frac{1}{\log(n)^{\log(n)}}$ converge or diverge?
:::

::: {.solution}

Consider first
$$
\sum_{n=2}^{\infty}\frac1{\log(n!)}.
$$

::: pf

::: {.pf-step #s1-1}

For every $n\ge2$,
$$
\boxed{n!\le n^n}.
$$


::: pf-proof

Each factor in
$$
n!=1\cdot2\cdots n
$$
is at most $n$, so the product is at most the product of $n$ copies of
$n$.

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\boxed{\log(n!)\le n\log n}.
$$


::: pf-proof

The logarithm is increasing on $(0,\infty)$. Apply $\log$ to step [](#s1-1){.pf-ref}:
$$
\log(n^n)=n\log n.
$$

:::

:::

::: {.pf-step #s1-3}

Hence
$$
\boxed{
\frac1{\log(n!)}
\ge
\frac1{n\log n}}.
$$


::: pf-proof

For $n\ge2$, both denominators are positive. Taking reciprocals reverses
the inequality in step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The comparison series
$$
\sum_{n=2}^{\infty}
\frac1{n\log n}
$$
diverges.


::: pf-proof

By the integral test,
$$
\int_2^\infty
\frac{dx}{x\log x}
=
\left[
\log\log x
\right]_2^\infty
=
\infty.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
\sum_{n=2}^{\infty}
\frac1{\log(n!)}
\text{ diverges}}.
$$


::: pf-proof

The terms are nonnegative, and step [](#s1-3){.pf-ref} bounds them below by the terms of
the divergent series in step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

One has
$$
\boxed{
(\log n)^{\log n}
=
n^{\log\log n}}.
$$


::: pf-proof

Using $a^b=e^{b\log a}$,
$$
(\log n)^{\log n}
=
e^{(\log n)(\log\log n)}.
$$
Also
$$
n^{\log\log n}
=
e^{(\log\log n)(\log n)}.
$$
The two expressions are equal.

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{
\frac1{(\log n)^{\log n}}
=
\frac1{n^{\log\log n}}}.
$$


::: pf-proof

Take reciprocals in step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

There exists $N$ such that for every $n\ge N$,
$$
\boxed{\log\log n\ge2}.
$$


::: pf-proof

Since
$$
\log\log n\longrightarrow\infty,
$$
it eventually exceeds $2$. For example, any
$$
N\ge e^{e^2}
$$
works.

:::

:::

::: {.pf-step #s1-9}

Therefore, for all $n\ge N$,
$$
\boxed{
\frac1{n^{\log\log n}}
\le
\frac1{n^2}}.
$$


::: pf-proof

By step [](#s1-8){.pf-ref},
$$
\log\log n\ge2.
$$
For $n>1$, increasing the positive exponent increases $n^\text{exponent}$,
so
$$
n^{\log\log n}\ge n^2.
$$
Take reciprocals.

:::

:::

::: {.pf-step #s1-10}

The series
$$
\sum_{n=N}^{\infty}
\frac1{n^2}
$$
converges.


::: pf-proof

This is a $p$-series with
$$
p=2>1.
$$

:::

:::

::: {.pf-step #s1-11}

Therefore
$$
\boxed{
\sum_{n=3}^{\infty}
\frac1{(\log n)^{\log n}}
\text{ converges}}.
$$


::: pf-proof

By steps [](#s1-7){.pf-ref} and [](#s1-9){.pf-ref}, its tail is bounded above by the convergent series in
step [](#s1-10){.pf-ref}. Finitely many initial terms do not affect convergence.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives divergence of the first series, and step [](#s1-11){.pf-ref} gives
convergence of the second.

:::

:::

:::
