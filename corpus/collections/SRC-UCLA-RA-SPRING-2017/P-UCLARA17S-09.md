---
schema: qual/card@1
id: P-UCLARA17S-09
kind: problem
title: Jensen's formula and the convergence exponent of zeros
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $f(z)$ be entire and assume $f(0)\ne0$. Let $\{a_n\}$ be the zeros of $f$, repeated according to multiplicity.

(a) Let $R>0$ be such that $|f(z)|>0$ on $|z|=R$. Prove
$$
\frac1{2\pi}\int_0^{2\pi}\log|f(Re^{i\theta})|\,d\theta
=\log|f(0)|+\sum_{|a_n|<R}\log\frac{R}{|a_n|}.
$$

(b) Prove that if there are constants $C$ and $\lambda$ such that $|f(z)|\le Ce^{|z|^\lambda}$ for all $z$, then
$$
\sum_n\left(\frac1{|a_n|}\right)^{\lambda+\varepsilon}<\infty
$$
for all $\varepsilon>0$. Hint: estimate $\#\{n:|a_n|<R\}$ using (a) on $|z|\sim2R$.
:::

::: {.solution}

::: pf

::: pf-step

For fixed $R>0$ with no zeros of $f$ on $|z|=R$, there are only finitely many zeros of $f$ in $|z|<R$, counted with multiplicity.


::: pf-proof

The zeros of a nonzero holomorphic function are discrete. Since the closed disk $\{|z|\le R\}$ is compact and contains no boundary zeros, it contains only finitely many zeros of $f$.

:::

:::

::: {.pf-step #s1-2}

If $b_1,\ldots,b_N$ are the zeros of $f$ in $|z|<R$, repeated according to multiplicity, then
$$
f(z)=g(z)\prod_{j=1}^N(z-b_j)
$$
on a neighborhood of the closed disk, where $g$ is holomorphic and nonvanishing there.


::: pf-proof

Divide $f$ successively by the corresponding linear factors, with repetitions matching the zero multiplicities. The quotient $g$ is holomorphic. By construction it has no zeros in the closed disk, and after shrinking the neighborhood slightly if necessary it remains nonvanishing there.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\frac1{2\pi}\int_0^{2\pi}\log|g(Re^{i\theta})|\,d\theta
=\log|g(0)|.
$$


::: pf-proof

Because $g$ is holomorphic and nonvanishing on a simply connected neighborhood of the closed disk, it has a holomorphic logarithm there. Hence $\log|g|$ is harmonic. The mean-value property for harmonic functions gives the identity.

:::

:::

::: {.pf-step #s1-4}

For every $b$ with $|b|<R$,
$$
\frac1{2\pi}\int_0^{2\pi}\log|Re^{i\theta}-b|\,d\theta
=\log R.
$$


::: pf-proof

Write
$$
Re^{i\theta}-b
=Re^{i\theta}\left(1-\frac bR e^{-i\theta}\right).
$$
The function
$$
z\longmapsto 1-\frac bR z
$$
is holomorphic and nonvanishing on the closed unit disk because $|b|/R<1$. Thus the mean-value property applied to its logarithmic modulus gives
$$
\frac1{2\pi}\int_0^{2\pi}
\log\left|1-\frac bR e^{-i\theta}\right|\,d\theta=0.
$$
Adding the constant $\log R$ proves the claim.

:::

:::

::: {.pf-step #s1-5}

Jensen's formula holds:
$$
\boxed{
\frac1{2\pi}\int_0^{2\pi}\log|f(Re^{i\theta})|\,d\theta
=\log|f(0)|+\sum_{|a_n|<R}\log\frac R{|a_n|}.}
$$


::: pf-proof

Using the factorization from step [](#s1-2){.pf-ref} and then steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref},
$$
\begin{aligned}
\frac1{2\pi}\int_0^{2\pi}\log|f(Re^{i\theta})|\,d\theta
&=\log|g(0)|+N\log R.
\end{aligned}
$$
Since $f(0)\ne0$, none of the $b_j$ is zero, and
$$
|f(0)|=|g(0)|\prod_{j=1}^N|b_j|.
$$
Therefore
$$
\log|g(0)|
=\log|f(0)|-\sum_{j=1}^N\log|b_j|,
$$
which gives the displayed formula.

:::

:::

::: {.pf-step #s1-6}

Let
$$
N(R)\coloneqq\#\{n:|a_n|<R\},
$$
counting multiplicities. If $\lambda>0$, then under the growth hypothesis in part (b) there is a constant $C_1$ such that
$$
N(R)\le C_1(1+R^\lambda)
$$
for every $R\ge1$.


::: pf-proof

Fix $R\ge1$. The set of moduli of zeros is discrete in every compact interval, so choose
$$
\rho\in[2R,3R]
$$
such that $f$ has no zero on $|z|=\rho$. Every zero with $|a_n|<R$ contributes at least $\log2$ to the Jensen sum at radius $\rho$. Hence step [](#s1-5){.pf-ref} and the growth hypothesis give
$$
\begin{aligned}
N(R)\log2
&\le\sum_{|a_n|<\rho}\log\frac\rho{|a_n|}\\
&=\frac1{2\pi}\int_0^{2\pi}\log|f(\rho e^{i\theta})|\,d\theta-\log|f(0)|\\
&\le \log C+\rho^\lambda-\log|f(0)|\\
&\le \log C+3^\lambda R^\lambda-\log|f(0)|.
\end{aligned}
$$
Absorbing the fixed constants into $C_1$ yields the claim.

:::

:::

::: {.pf-step #s1-7}

For every $\varepsilon>0$,
$$
\boxed{
\sum_n |a_n|^{-(\lambda+\varepsilon)}<\infty.}
$$


::: pf-proof

If $\lambda\le0$, then $|f(z)|\le Ce$ for every $|z|\ge1$; continuity bounds $f$ on the closed unit disk as well. Thus $f$ is bounded entire, hence constant by Liouville's theorem. Since $f(0)\ne0$, it has no zeros, and the sum is empty.

Assume now that $\lambda>0$.
There are only finitely many zeros with $|a_n|<1$, and none is zero because $f(0)\ne0$, so their contribution is finite. For $k\ge0$, let
$$
E_k=\{n:2^k\le|a_n|<2^{k+1}\}.
$$
By step [](#s1-6){.pf-ref},
$$
\#E_k\le N(2^{k+1})\le C_2\,2^{(k+1)\lambda}
$$
for a fixed constant $C_2$. Therefore
$$
\begin{aligned}
\sum_{n\in E_k}|a_n|^{-(\lambda+\varepsilon)}
&\le \#E_k\,2^{-k(\lambda+\varepsilon)}\\
&\le C_2\,2^\lambda\,2^{-k\varepsilon}.
\end{aligned}
$$
Summing over $k\ge0$ gives a convergent geometric series.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves part (a), and step [](#s1-7){.pf-ref} proves part (b).

:::

:::

:::
