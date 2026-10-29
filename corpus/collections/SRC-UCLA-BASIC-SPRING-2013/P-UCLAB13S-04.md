---
schema: qual/card@1
id: P-UCLAB13S-04
kind: problem
title: Existence of the Euler–Mascheroni limit
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 4 of the retained UCLA Basic Examination, Spring 2013.
---

::: {.problem}
Denote by $h_n$ the $n$th harmonic number,
$$
h_n=1+\frac12+\frac13+\cdots+\frac1n.
$$
Prove that the limit
$$
\gamma=\lim_{n\to\infty}(h_n-\ln n)
$$
exists.
:::

::: {.solution}

Define
$$
a_n=h_n-\ln n.
$$

::: pf

::: {.pf-step #s1-1}

For every $n\ge1$,
$$
\ln\left(1+\frac1n\right)
>
\frac1{n+1}.
$$


::: pf-proof

For $x>0$,
$$
\ln(1+x)
=
\int_0^x\frac{dt}{1+t}.
$$
On the interval $0\le t<x$,
$$
\frac1{1+t}
>
\frac1{1+x}.
$$
Hence
$$
\ln(1+x)
>
\int_0^x\frac{dt}{1+x}
=
\frac{x}{1+x}.
$$
Set
$$
x=\frac1n.
$$
Then
$$
\frac{x}{1+x}
=
\frac1{n+1}.
$$

:::

:::

::: {.pf-step #s1-2}

The sequence $(a_n)$ is strictly decreasing.


::: pf-proof

Compute
$$
\begin{aligned}
a_{n+1}-a_n
&=
\left(
h_n+\frac1{n+1}-\ln(n+1)
\right)
-
\left(
h_n-\ln n
\right)\\
&=
\frac1{n+1}
-
\ln\left(\frac{n+1}{n}\right)\\
&=
\frac1{n+1}
-
\ln\left(1+\frac1n\right).
\end{aligned}
$$
By step [](#s1-1){.pf-ref}, this quantity is negative.
Thus
$$
a_{n+1}<a_n.
$$

:::

:::

::: {.pf-step #s1-3}

For every $n\ge1$,
$$
h_n
\ge
\int_1^{n+1}\frac{dx}{x}.
$$


::: pf-proof

The function
$$
x\longmapsto\frac1x
$$
is decreasing on $(0,\infty)$.
Therefore on each interval
$$
[k,k+1],
$$
one has
$$
\frac1x
\le
\frac1k.
$$
Hence
$$
\int_k^{k+1}\frac{dx}{x}
\le
\frac1k.
$$
Summing from $k=1$ to $n$ gives
$$
\int_1^{n+1}\frac{dx}{x}
\le
\sum_{k=1}^n\frac1k
=
h_n.
$$

:::

:::

::: {.pf-step #s1-4}

The sequence $(a_n)$ is bounded below.


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
h_n
\ge
\ln(n+1).
$$
Thus
$$
\begin{aligned}
a_n
&=
h_n-\ln n\\
&\ge
\ln(n+1)-\ln n\\
&=
\ln\left(1+\frac1n\right)\\
&>
0.
\end{aligned}
$$
Therefore
$$
a_n>0
$$
for every $n$.

:::

:::

::: {.pf-step #s1-5}

The sequence $(a_n)$ converges.


::: pf-proof

By step [](#s1-2){.pf-ref}, $(a_n)$ is decreasing.
By step [](#s1-4){.pf-ref}, it is bounded below.
The monotone convergence theorem for real sequences therefore gives the existence of a finite limit.

:::

:::

::: {.pf-step #s1-6}

Consequently,
$$
\boxed{
\gamma
=
\lim_{n\to\infty}(h_n-\ln n)
}
$$
exists.


::: pf-proof

This is the limit of the convergent sequence $a_n$ from step [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
