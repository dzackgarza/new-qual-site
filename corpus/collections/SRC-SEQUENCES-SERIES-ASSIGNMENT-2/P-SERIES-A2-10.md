---
schema: qual/card@1
id: P-SERIES-A2-10
kind: problem
title: Divergence when $na_n\to\ell\ne0$ and convergence of $\sum a_n^p$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
(a) Show that if $a_n>0$ and
$$
\lim_{n\to\infty}n a_n=\ell\ne0,
$$
then $\sum a_n$ diverges.

(b) Given that $\sum a_n$ converges absolutely, show that $\sum a_n^p$ also converges whenever $p>1$. Give a counterexample when $\sum a_n$ only converges conditionally.
:::

::: {.solution}

## Part (a)

Assume
$$
a_n>0
$$
and
$$
na_n\to\ell\ne0.
$$

::: pf

::: pf-step

Since every $na_n>0$, the limit satisfies
$$
\boxed{\ell>0}.
$$


::: pf-proof

A limit of positive numbers is nonnegative. Since the limit is assumed
nonzero, it must be positive.

:::

:::

::: {.pf-step #s1-2}

Choose
$$
\varepsilon=\frac{\ell}{2}>0.
$$
Then there exists $N$ such that for all $n\ge N$,
$$
|na_n-\ell|<\frac{\ell}{2}.
$$


::: pf-proof

Apply the definition of convergence to the sequence $na_n\to\ell$.

:::

:::

::: {.pf-step #s1-3}

Hence, for $n\ge N$,
$$
na_n>\frac{\ell}{2}.
$$


::: pf-proof

From step [](#s1-2){.pf-ref},
$$
na_n
>
\ell-\frac{\ell}{2}
=
\frac{\ell}{2}.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
a_n>\frac{\ell}{2n}}
$$
for every $n\ge N$.


::: pf-proof

Divide step [](#s1-3){.pf-ref} by the positive integer $n$.

:::

:::

::: {.pf-step #s1-5}

The comparison series
$$
\sum_{n=N}^{\infty}
\frac{\ell}{2n}
$$
diverges.


::: pf-proof

It is the positive constant $\ell/2$ times the harmonic series.

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\boxed{
\sum_{n=1}^{\infty}a_n
\text{ diverges}}.
$$


::: pf-proof

By steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref}, the tail of $\sum a_n$ dominates a divergent
nonnegative series.

:::

:::

::: {.pf-step #s1-7}

Absolute convergence implies
$$
\boxed{|a_n|\to0}.
$$


::: pf-proof

The terms of any convergent series must tend to zero. Apply this to the
nonnegative series $\sum|a_n|$.

:::

:::

::: pf-step

Therefore there exists $N$ such that
$$
\boxed{|a_n|<1}
$$
for every $n\ge N$.


::: pf-proof

Apply step [](#s1-7){.pf-ref} with $\varepsilon=1$.

:::

:::

::: {.pf-step #s1-9}

If
$$
p>1
$$
and $n\ge N$, then
$$
\boxed{
|a_n|^p\le|a_n|}.
$$


::: pf-proof

For $0\le x\le1$ and $p>1$,
$$
x^p\le x.
$$
Apply this with $x=|a_n|$.

:::

:::

::: {.pf-step #s1-10}

Hence
$$
\boxed{
\sum_{n=1}^{\infty}|a_n|^p
\text{ converges}}
$$
for every real $p>1$.


::: pf-proof

The tail is bounded termwise by the convergent series
$$
\sum_{n=N}^{\infty}|a_n|
$$
using step [](#s1-9){.pf-ref}. Finitely many initial terms do not affect convergence.

:::

:::

::: {.pf-step #s1-11}

In particular, whenever $a_n^p$ is real-defined for every $n$,
$$
\boxed{
\sum a_n^p
\text{ converges absolutely}}.
$$


::: pf-proof

Whenever the real power is defined,
$$
|a_n^p|=|a_n|^p.
$$
Apply step [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

Define
$$
\boxed{
a_n=\frac{(-1)^n}{\sqrt n}}.
$$


::: pf-proof

This will give the requested conditional-convergence counterexample.

:::

:::

::: {.pf-step #s1-13}

The series
$$
\sum_{n=1}^{\infty}a_n
=
\sum_{n=1}^{\infty}
\frac{(-1)^n}{\sqrt n}
$$
converges.


::: pf-proof

The positive sequence
$$
n^{-1/2}
$$
decreases to zero, so the alternating-series test applies.

:::

:::

::: {.pf-step #s1-14}

It does not converge absolutely.


::: pf-proof

$$
\sum|a_n|
=
\sum\frac1{\sqrt n},
$$
which is a divergent $p$-series with exponent $1/2\le1$.

:::

:::

::: {.pf-step #s1-15}

Therefore
$$
\sum a_n
$$
converges conditionally.


::: pf-proof

Combine steps [](#s1-13){.pf-ref} through [](#s1-14){.pf-ref}.

:::

:::

::: {.pf-step #s1-16}

Take
$$
\boxed{p=2}.
$$
Then
$$
a_n^2=\frac1n.
$$


::: pf-proof

$$
\left(
\frac{(-1)^n}{\sqrt n}
\right)^2
=
\frac1n.
$$

:::

:::

::: {.pf-step #s1-17}

Hence
$$
\boxed{
\sum a_n^2
=
\sum\frac1n
\text{ diverges}}.
$$


::: pf-proof

This is the harmonic series.

:::

:::

::: {.pf-step #s1-18}

Thus absolute convergence in part (b) is essential.


::: pf-proof

Steps [](#s1-15){.pf-ref} through [](#s1-17){.pf-ref} give a conditionally convergent series whose square
series diverges.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves part (a); steps [](#s1-10){.pf-ref} through [](#s1-11){.pf-ref} prove the power-series
conclusion under absolute convergence; and steps [](#s1-12){.pf-ref} through [](#s1-18){.pf-ref} give the
counterexample.

:::

:::

:::
