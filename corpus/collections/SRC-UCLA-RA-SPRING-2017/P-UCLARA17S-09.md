---
schema: qual/card@1
id: P-UCLARA17S-09
kind: problem
title: Jensen's formula and the convergence exponent of zeros
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Zeros
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

(a) Let $R>0$ be such that $\abs{f(z)}>0$ on $\abs{z}=R$. Prove
$$
\frac1{2\pi}\int_0^{2\pi}\log\abs{f(Re^{i\theta})}\,d\theta
=\log\abs{f(0)}+\sum_{\abs{a_n}<R}\log\frac{R}{\abs{a_n}}.
$$

(b) Prove that if there are constants $C$ and $\lambda$ such that $\abs{f(z)}\le Ce^{\abs{z}^\lambda}$ for all $z$, then
$$
\sum_n\left(\frac1{\abs{a_n}}\right)^{\lambda+\varepsilon}<\infty
$$
for all $\varepsilon>0$. Hint: estimate $\#\{n:\abs{a_n}<R\}$ using (a) on $\abs{z}\sim2R$.
:::

::: {.solution}

::: pf

::: pf-step

For fixed $R>0$ with no zeros of $f$ on $\abs{z}=R$, there are only finitely many zeros of $f$ in $\abs{z}<R$, counted with multiplicity.


::: pf-proof

The zeros of a nonzero holomorphic function are discrete. Since the closed disk $\{\abs{z}\le R\}$ is compact and contains no boundary zeros, it contains only finitely many zeros of $f$.

:::

:::

::: {.pf-step #s1-2}

If $b_1,\ldots,b_N$ are the zeros of $f$ in $\abs{z}<R$, repeated according to multiplicity, then
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
\frac1{2\pi}\int_0^{2\pi}\log\abs{g(Re^{i\theta})}\,d\theta
=\log\abs{g(0)}.
$$


::: pf-proof

Because $g$ is holomorphic and nonvanishing on a simply connected neighborhood of the closed disk, it has a holomorphic logarithm there. Hence $\log\abs{g}$ is harmonic. The mean-value property for harmonic functions gives the identity.

:::

:::

::: {.pf-step #s1-4}

For every $b$ with $\abs{b}<R$,
$$
\frac1{2\pi}\int_0^{2\pi}\log\abs{Re^{i\theta}-b}\,d\theta
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
is holomorphic and nonvanishing on the closed unit disk because $\abs{b}/R<1$. Thus the mean-value property applied to its logarithmic modulus gives
$$
\frac1{2\pi}\int_0^{2\pi}
\log\abs{1-\frac bR e^{-i\theta}}\,d\theta=0.
$$
Adding the constant $\log R$ proves the claim.

:::

:::

::: {.pf-step #s1-5}

Jensen's formula holds:
$$
\boxed{
\frac1{2\pi}\int_0^{2\pi}\log\abs{f(Re^{i\theta})}\,d\theta
=\log\abs{f(0)}+\sum_{\abs{a_n}<R}\log\frac R{\abs{a_n}}.}
$$


::: pf-proof

Using the factorization from step [](#s1-2){.pf-ref} and then steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref},
$$
\begin{aligned}
\frac1{2\pi}\int_0^{2\pi}\log\abs{f(Re^{i\theta})}\,d\theta
&=\log\abs{g(0)}+N\log R.
\end{aligned}
$$
Since $f(0)\ne0$, none of the $b_j$ is zero, and
$$
\abs{f(0)}=\abs{g(0)}\prod_{j=1}^N\abs{b_j}.
$$
Therefore
$$
\log\abs{g(0)}
=\log\abs{f(0)}-\sum_{j=1}^N\log\abs{b_j},
$$
which gives the displayed formula.

:::

:::

::: {.pf-step #s1-6}

Let
$$
N(R)\coloneqq\#\{n:\abs{a_n}<R\},
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
such that $f$ has no zero on $\abs{z}=\rho$. Every zero with $\abs{a_n}<R$ contributes at least $\log2$ to the Jensen sum at radius $\rho$. Hence step [](#s1-5){.pf-ref} and the growth hypothesis give
$$
\begin{aligned}
N(R)\log2
&\le\sum_{\abs{a_n}<\rho}\log\frac\rho{\abs{a_n}}\\
&=\frac1{2\pi}\int_0^{2\pi}\log\abs{f(\rho e^{i\theta})}\,d\theta-\log\abs{f(0)}\\
&\le \log C+\rho^\lambda-\log\abs{f(0)}\\
&\le \log C+3^\lambda R^\lambda-\log\abs{f(0)}.
\end{aligned}
$$
Absorbing the fixed constants into $C_1$ yields the claim.

:::

:::

::: {.pf-step #s1-7}

For every $\varepsilon>0$,
$$
\boxed{
\sum_n \abs{a_n}^{-(\lambda+\varepsilon)}<\infty.}
$$


::: pf-proof

If $\lambda\le0$, then $\abs{f(z)}\le Ce$ for every $\abs{z}\ge1$; continuity bounds $f$ on the closed unit disk as well. Thus $f$ is bounded entire, hence constant by Liouville's theorem. Since $f(0)\ne0$, it has no zeros, and the sum is empty.

Assume now that $\lambda>0$.
There are only finitely many zeros with $\abs{a_n}<1$, and none is zero because $f(0)\ne0$, so their contribution is finite. For $k\ge0$, let
$$
E_k=\{n:2^k\le\abs{a_n}<2^{k+1}\}.
$$
By step [](#s1-6){.pf-ref},
$$
\#E_k\le N(2^{k+1})\le C_2\,2^{(k+1)\lambda}
$$
for a fixed constant $C_2$. Therefore
$$
\begin{aligned}
\sum_{n\in E_k}\abs{a_n}^{-(\lambda+\varepsilon)}
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
