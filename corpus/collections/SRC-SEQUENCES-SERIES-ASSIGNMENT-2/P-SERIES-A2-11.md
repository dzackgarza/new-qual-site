---
schema: qual/card@1
id: P-SERIES-A2-11
kind: problem
title: 'Convergent series: $\sum a_nb_n$, $\sum n^2a_n$ and $na_n\to0$'
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
For each proposition, give a short proof if it is true and a counterexample if it is false.

(a) If $\sum a_n$ converges and the sequence $\{b_n\}$ also converges, then $\sum a_n b_n$ converges.

(b) If $\sum a_n$ converges conditionally, then $\sum n^2a_n$ diverges.

(c) If $\{a_n\}$ is decreasing and $\sum a_n$ converges, then
$$
\lim_{n\to\infty} n a_n=0.
$$
:::

::: {.solution}

## Part (a)

The proposition is false.

::: pf

::: pf-step

Define
$$
\boxed{
a_n=\frac{(-1)^n}{\sqrt n},
\qquad
b_n=\frac{(-1)^n}{\sqrt n}}.
$$


::: pf-proof

These sequences will give a counterexample.

:::

:::

::: {.pf-step #s1-2}

The series
$$
\sum_{n=1}^{\infty}a_n
$$
converges.


::: pf-proof

The positive sequence
$$
n^{-1/2}
$$
decreases to $0$, so the alternating-series test applies.

:::

:::

::: {.pf-step #s1-3}

The sequence $(b_n)$ converges to $0$.


::: pf-proof

$$
\abs{b_n}=\frac1{\sqrt n}\to0.
$$

:::

:::

::: {.pf-step #s1-4}

But
$$
\boxed{
a_nb_n=\frac1n}.
$$


::: pf-proof

$$
\frac{(-1)^n}{\sqrt n}
\frac{(-1)^n}{\sqrt n}
=
\frac{(-1)^{2n}}{n}
=
\frac1n.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\sum_{n=1}^{\infty}a_nb_n
$$
diverges.


::: pf-proof

By step [](#s1-4){.pf-ref}, this is the harmonic series.

:::

:::

::: {.pf-step #s1-6}

Hence proposition (a) is
$$
\boxed{\text{false}}.
$$


::: pf-proof

Steps [](#s1-2){.pf-ref} through [](#s1-5){.pf-ref} satisfy the hypotheses but not the conclusion.

:::

:::

::: {.pf-step #s1-7}

Suppose, toward a contradiction, that
$$
\sum n^2a_n
$$
converges.


::: pf-proof

We will show this forces absolute convergence of $\sum a_n$.

:::

:::

::: {.pf-step #s1-8}

Then
$$
\boxed{
n^2a_n\to0}.
$$


::: pf-proof

The terms of every convergent series tend to zero.

:::

:::

::: {.pf-step #s1-9}

Hence there exists $N$ such that for every $n\ge N$,
$$
\boxed{
\abs{n^2a_n}<1}.
$$


::: pf-proof

Apply step [](#s1-8){.pf-ref} with $\varepsilon=1$.

:::

:::

::: {.pf-step #s1-10}

Therefore, for $n\ge N$,
$$
\boxed{
\abs{a_n}<\frac1{n^2}}.
$$


::: pf-proof

Divide step [](#s1-9){.pf-ref} by the positive number $n^2$.

:::

:::

::: {.pf-step #s1-11}

Hence
$$
\sum_{n=N}^{\infty}\abs{a_n}
$$
converges.


::: pf-proof

By step [](#s1-10){.pf-ref}, compare with the convergent $p$-series
$$
\sum_{n=N}^{\infty}\frac1{n^2}.
$$

:::

:::

::: pf-step

Thus
$$
\sum a_n
$$
would converge absolutely.


::: pf-proof

Adding finitely many initial absolute values does not affect convergence.
Apply step [](#s1-11){.pf-ref}.

:::

:::

::: pf-step

This contradicts conditional convergence.


::: pf-proof

Conditional convergence means convergence without absolute convergence.

:::

:::

::: {.pf-step #s1-14}

Therefore
$$
\boxed{
\sum n^2a_n
\text{ diverges}}.
$$


::: pf-proof

The assumption in step [](#s1-7){.pf-ref} led to a contradiction.

:::

:::

::: pf-step

One has
$$
\boxed{a_n\to0}.
$$


::: pf-proof

The terms of a convergent series tend to zero.

:::

:::

::: {.pf-step #s1-16}

Since $(a_n)$ is decreasing and tends to $0$,
$$
\boxed{a_n\ge0}
$$
for every $n$.


::: pf-proof

If some $a_N<0$, then decreasingness would give
$$
a_n\le a_N<0
$$
for all $n\ge N$, contradicting $a_n\to0$.

:::

:::

::: {.pf-step #s1-17}

Let
$$
\varepsilon>0.
$$
By the Cauchy criterion for the convergent series $\sum a_n$, there exists
$N$ such that whenever $q>p\ge N$,
$$
\boxed{
\sum_{k=p}^{q}a_k<\frac{\varepsilon}{2}}.
$$


::: pf-proof

All terms are nonnegative by step [](#s1-16){.pf-ref}, so the absolute value in the Cauchy
criterion may be omitted.

:::

:::

::: {.pf-step #s1-18}

Let $n>2N$ and set
$$
m=\left\lfloor\frac n2\right\rfloor.
$$
Then
$$
m\ge N.
$$


::: pf-proof

Since $n>2N$,
$$
\frac n2>N.
$$
Taking the floor gives $m\ge N$.

:::

:::

::: {.pf-step #s1-19}

Since the sequence is decreasing,
$$
a_k\ge a_n
$$
for every
$$
m\le k\le n.
$$


::: pf-proof

For $k\le n$, decreasingness gives $a_k\ge a_n$.

:::

:::

::: {.pf-step #s1-20}

Hence
$$
\sum_{k=m}^{n}a_k
\ge
(n-m+1)a_n.
$$


::: pf-proof

There are $n-m+1$ terms, each at least $a_n$ by step [](#s1-19){.pf-ref}.

:::

:::

::: {.pf-step #s1-21}

One has
$$
n-m+1\ge\frac n2.
$$


::: pf-proof

Since
$$
m=\left\lfloor\frac n2\right\rfloor\le\frac n2,
$$
$$
n-m+1
\ge
n-\frac n2
=
\frac n2.
$$

:::

:::

::: {.pf-step #s1-22}

Therefore
$$
\boxed{
\sum_{k=m}^{n}a_k
\ge
\frac n2\,a_n}.
$$


::: pf-proof

Combine steps [](#s1-20){.pf-ref} through [](#s1-21){.pf-ref} and use $a_n\ge0$.

:::

:::

::: {.pf-step #s1-23}

By step [](#s1-17){.pf-ref},
$$
\sum_{k=m}^{n}a_k<\frac{\varepsilon}{2}.
$$


::: pf-proof

Step [](#s1-18){.pf-ref} gives $m\ge N$, so the Cauchy tail estimate applies.

:::

:::

::: {.pf-step #s1-24}

Combining steps [](#s1-22){.pf-ref} through [](#s1-23){.pf-ref},
$$
\frac n2\,a_n<\frac{\varepsilon}{2}.
$$


::: pf-proof

The same tail sum is bounded below and above by those two quantities.

:::

:::

::: {.pf-step #s1-25}

Hence
$$
\boxed{
na_n<\varepsilon}
$$
for every $n>2N$.


::: pf-proof

Multiply step [](#s1-24){.pf-ref} by $2$.

:::

:::

::: {.pf-step #s1-26}

Therefore
$$
\boxed{
na_n\to0}.
$$


::: pf-proof

Step [](#s1-25){.pf-ref} is the $\varepsilon$-definition of convergence to $0$.

:::

:::

::: {.pf-step #s1-27}

Thus the answers are:
$$
\boxed{
\text{(a) false,\qquad (b) true,\qquad (c) true}.}
$$


::: pf-proof

Use steps [](#s1-6){.pf-ref} and [](#s1-14){.pf-ref}, and [](#s1-26){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-27){.pf-ref} gives the required dispositions.

:::

:::

:::
