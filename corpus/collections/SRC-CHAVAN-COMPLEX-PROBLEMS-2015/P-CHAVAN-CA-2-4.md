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
\[
p(z)=a_0+a_1z+\cdots+a_{n-1}z^{n-1}+z^n,
\qquad
R=\sqrt{|a_0|^2+\cdots+|a_{n-1}|^2+1}.
\]

1. If $R=1$, show that the zero set of $p$ is $\{0\}$.

2. If $R>1$ and $|z|=R$, show, using Cauchy-Schwarz, that
   \[
   |z^n-p(z)|<|z^n|.
   \]

Conclude that every zero of $p$ lies in the open disk $|z|<R$.
:::

::: {.solution}
<1>1. If $R=1$, then the zero set of $p$ is $\{0\}$.

::: {.proof}
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

<1>2. Assume $R>1$ and $|z|=R$. Then
$$
|z^n-p(z)|
\le
\sqrt{R^2-1}\,
\sqrt{1+R^2+\cdots+R^{2n-2}}.
$$

::: {.proof}
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

<1>3. Under the hypotheses of step <1>2,
$$
|z^n-p(z)|<|z^n|.
$$

::: {.proof}
The geometric-series identity gives
$$
(R^2-1)(1+R^2+\cdots+R^{2n-2})=R^{2n}-1.
$$
Since $R>1$,
$$
R^{2n}-1<R^{2n}.
$$
Taking square roots in the estimate from step <1>2 yields
$$
|z^n-p(z)|
\le\sqrt{R^{2n}-1}
<R^n
=|z^n|.
$$
:::

<1>4. Every zero of $p$ lies in the open disk $|z|<R$.

::: {.proof}
If $R=1$, this follows from step <1>1. Assume $R>1$. On the circle
$|z|=R$, step <1>3 gives
$$
|p(z)-z^n|<|z^n|.
$$
By Rouché's theorem, $p$ and $z^n$ have the same number of zeros in
$|z|<R$, counted with multiplicity. The polynomial $z^n$ has exactly
$n$ zeros there, counted with multiplicity, so $p$ also has $n$ zeros
in $|z|<R$. Since $p$ has degree $n$, these account for all of its
zeros. Therefore every zero of $p$ lies in the open disk.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 proves the case $R=1$, steps <1>2 and <1>3 establish the
requested boundary estimate for $R>1$, and step <1>4 gives the final
zero-location conclusion.
:::
:::
