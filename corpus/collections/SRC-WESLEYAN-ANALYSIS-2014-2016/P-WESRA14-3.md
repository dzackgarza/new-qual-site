---
schema: qual/card@1
id: P-WESRA14-3
kind: problem
title: '$\sigma$-finiteness characterized by a strictly positive $L^1$ function'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Prove that a measure $\mu$ is $\sigma$-finite if and only if there exists $f\in L^1(\mu)$ such that
$$
f(x)>0\qquad(x\in X).
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Assume first that
$$
\mu
$$
is
$$
\sigma\text{-finite}.
$$
Then there exist measurable sets
$$
E_1,E_2,\dots
$$
such that
$$
X
=
\bigcup_{n=1}^{\infty}E_n
$$
and
$$
\mu(E_n)<\infty
\qquad
(n\ge1).
$$


::: pf-proof

This is the definition of
$$
\sigma\text{-finiteness}.
$$

:::

:::

::: {.pf-step #s1-2}

Define disjoint measurable sets
$$
A_1=E_1,
$$
and for
$$
n\ge2,
$$
$$
A_n
\coloneqq
E_n
\setminus
\bigcup_{k=1}^{n-1}E_k.
$$
Then
$$
X
=
\bigsqcup_{n=1}^{\infty}A_n,
$$
and
$$
\mu(A_n)<\infty.
$$


::: pf-proof

Each $A_n$ is measurable and satisfies
$$
A_n\subseteq E_n,
$$
so
$$
\mu(A_n)
\le
\mu(E_n)
<
\infty.
$$

By construction the $A_n$ are pairwise disjoint.
Every point $x\in X$ lies in at least one $E_n$; taking the least such $n$
places $x$ in $A_n$.
Thus the $A_n$ partition $X$.

:::

:::

::: {.pf-step #s1-3}

For each
$$
n\ge1,
$$
set
$$
c_n
\coloneqq
\frac{2^{-n}}
{1+\mu(A_n)}.
$$
Then
$$
c_n>0.
$$


::: pf-proof

The denominator is a finite positive number by step [](#s1-2){.pf-ref}, so each $c_n$ is
strictly positive.

:::

:::

::: {.pf-step #s1-4}

Define
$$
f
\coloneqq
\sum_{n=1}^{\infty}
c_n\mathbf 1_{A_n}.
$$
Then $f$ is measurable and
$$
f(x)>0
$$
for every
$$
x\in X.
$$


::: pf-proof

The indicator functions are measurable, and the countable sum of
nonnegative measurable functions is measurable.

Because the sets $A_n$ partition $X$, every point belongs to exactly one
$A_n$.
Thus if
$$
x\in A_n,
$$
then
$$
f(x)=c_n>0.
$$

:::

:::

::: {.pf-step #s1-5}

The function $f$ belongs to
$$
L^1(\mu).
$$


::: pf-proof

Using the disjoint partition,
$$
\begin{aligned}
\int_X f\,d\mu
&=
\sum_{n=1}^{\infty}
c_n\mu(A_n)\\
&=
\sum_{n=1}^{\infty}
2^{-n}
\frac{\mu(A_n)}
{1+\mu(A_n)}\\
&\le
\sum_{n=1}^{\infty}
2^{-n}\\
&=
1.
\end{aligned}
$$
Hence
$$
\int_X |f|,d\mu
<
\infty.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\mu
\text{ is }\sigma\text{-finite}
\quad\Longrightarrow\quad
\exists f\in L^1(\mu)
\text{ with }f>0\text{ everywhere}.
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref} construct such an $f$.

:::

:::

::: pf-step

Conversely, suppose
$$
f\in L^1(\mu)
$$
and
$$
f(x)>0
\qquad
(x\in X).
$$
For
$$
n\ge1,
$$
define
$$
F_n
\coloneqq
\left\{
x\in X:
f(x)\ge\frac1n
\right\}.
$$


::: pf-proof

Because $f$ is measurable, every superlevel set $F_n$ is measurable.

:::

:::

::: {.pf-step #s1-8}

The sets
$$
F_n
$$
cover $X$:
$$
X
=
\bigcup_{n=1}^{\infty}F_n.
$$


::: pf-proof

Fix
$$
x\in X.
$$
Since
$$
f(x)>0,
$$
there exists
$$
n
$$
large enough that
$$
\frac1n
\le
f(x).
$$
Hence
$$
x\in F_n.
$$

:::

:::

::: {.pf-step #s1-9}

Each $F_n$ has finite measure.


::: pf-proof

On
$$
F_n,
$$
one has
$$
f
\ge
\frac1n.
$$
Therefore
$$
\begin{aligned}
\int_X |f|\,d\mu
&\ge
\int_{F_n}f\,d\mu\\
&\ge
\frac1n\mu(F_n).
\end{aligned}
$$
Thus
$$
\mu(F_n)
\le
n
\int_X |f|\,d\mu
<
\infty.
$$

:::

:::

::: {.pf-step #s1-10}

Hence
$$
\mu
$$
is
$$
\sigma\text{-finite}.
$$


::: pf-proof

By step [](#s1-8){.pf-ref}, the measurable sets $F_n$ cover $X$.
By step [](#s1-9){.pf-ref}, each has finite measure.
That is exactly the definition of
$$
\sigma\text{-finiteness}.
$$

:::

:::

::: {.pf-step #s1-11}

Therefore
$$
\boxed{
\mu\text{ is }\sigma\text{-finite}
\iff
\exists f\in L^1(\mu)
\text{ with }f(x)>0\text{ for every }x\in X.
}
$$


::: pf-proof

Step [](#s1-6){.pf-ref} proves the forward implication and step [](#s1-10){.pf-ref} proves the reverse
implication.

:::

:::

::: pf-qed

Step [](#s1-11){.pf-ref} is the desired equivalence.

:::

:::

:::
