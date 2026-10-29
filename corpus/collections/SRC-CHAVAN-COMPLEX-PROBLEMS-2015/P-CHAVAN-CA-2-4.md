---
schema: qual/card@1
id: P-CHAVAN-CA-2-4
kind: problem
title: A Cauchy-Schwarz bound on the zeros of a monic polynomial
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let
$$
p(z)=a_0+a_1z+\cdots+a_{n-1}z^{n-1}+z^n,
\qquad
R=\sqrt{|a_0|^2+\cdots+|a_{n-1}|^2+1}.
$$

1. If $R=1$, show that the zero set of $p$ is $\{0\}$.

2. If $R>1$ and $|z|=R$, show, using Cauchy-Schwarz, that
   $$
   |z^n-p(z)|<|z^n|.
   $$

Conclude that every zero of $p$ lies in the open disk $|z|<R$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $R=1$, then the zero set of $p$ is $\{0\}$.


::: pf-proof

The equality $R=1$ means
$$
|a_0|^2+\cdots+|a_{n-1}|^2+1=1.
$$
Hence
$$
a_0=a_1=\cdots=a_{n-1}=0,
$$
so $p(z)=z^n$. Thus the only zero of $p$ is $0$.

:::

:::

::: {.pf-step #s1-2}

Assume $R>1$ and $|z|=R$. Then
$$
|z^n-p(z)|
\le
\sqrt{R^2-1}\,
\sqrt{1+R^2+\cdots+R^{2n-2}}.
$$


::: pf-proof

Since
$$
z^n-p(z)=-\sum_{k=0}^{n-1}a_kz^k,
$$
the Cauchy--Schwarz inequality gives
$$
\begin{aligned}
|z^n-p(z)|
&\le
\left(\sum_{k=0}^{n-1}|a_k|^2\right)^{1/2}
\left(\sum_{k=0}^{n-1}|z|^{2k}\right)^{1/2}\\
&=
\sqrt{R^2-1}\,
\sqrt{1+R^2+\cdots+R^{2n-2}},
\end{aligned}
$$
because $\sum_{k=0}^{n-1}|a_k|^2=R^2-1$ and $|z|=R$.

:::

:::

::: {.pf-step #s1-3}

Under the hypotheses of step [](#s1-2){.pf-ref},
$$
|z^n-p(z)|<|z^n|.
$$


::: pf-proof

The geometric-series identity gives
$$
(R^2-1)(1+R^2+\cdots+R^{2n-2})=R^{2n}-1.
$$
Since $R>1$,
$$
R^{2n}-1<R^{2n}.
$$
Taking square roots in the estimate from step [](#s1-2){.pf-ref} yields
$$
|z^n-p(z)|
\le\sqrt{R^{2n}-1}
<R^n
=|z^n|.
$$

:::

:::

::: {.pf-step #s1-4}

Every zero of $p$ lies in the open disk $|z|<R$.


::: pf-proof

If $R=1$, this follows from step [](#s1-1){.pf-ref}. Assume $R>1$. On the circle
$|z|=R$, step [](#s1-3){.pf-ref} gives
$$
|p(z)-z^n|<|z^n|.
$$
By Rouché's theorem, $p$ and $z^n$ have the same number of zeros in
$|z|<R$, counted with multiplicity. The polynomial $z^n$ has exactly
$n$ zeros there, counted with multiplicity, so $p$ also has $n$ zeros
in $|z|<R$. Since $p$ has degree $n$, these account for all of its
zeros. Therefore every zero of $p$ lies in the open disk.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves the case $R=1$, steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} establish the
requested boundary estimate for $R>1$, and step [](#s1-4){.pf-ref} gives the final
zero-location conclusion.

:::

:::

:::
