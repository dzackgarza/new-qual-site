---
schema: qual/card@1
id: P-RASP06A
kind: problem
title: "True/false on functions of bounded variation, measures, and Banach space duals"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the official UCSD Spring 2006 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $m = dx$ denote Lebesgue measure, and let $(X, \mathcal{M}, \mu)$ be a measure space.

Determine if the statements below are True or False.
If True, give a brief proof.
If False, give a counterexample.

(a) If $f \in C([0,1])$, $f'$ exists a.e. ($m$) and $f' = 0$ a.e. ($m$), then $f$ is constant.

(b) If $X \supset E_1 \supset E_2 \supset \cdots$ are $\mathcal{M}$-measurable sets such that $\mu\bigl(\bigcap_j E_j\bigr) = 0$, then $\lim_{j \to \infty} \mu(E_j) = 0$.

(c) Suppose $\{f_j\}$ is a sequence in $L^1(X, \mu)$ with $f_1 \geq f_2 \geq \cdots \geq 0$ a.e. ($\mu$), and let $f(x) = \lim_{j \to \infty} f_j(x)$ a.e. ($\mu$). Then $\int_X f\,d\mu = \lim_{j \to \infty} \int_X f_j\,d\mu$.

(d) Let $\nu$ be a finite signed measure on $X$, and $\totalvariation{\nu}$ its total variation.
Then there is $f \in \mathcal{L}^1(X, \totalvariation{\nu})$ such that for every $g \in L^1(X, \nu)$, $\int_X g\,d\nu = \int_X gf\,d\totalvariation{\nu}$.

(e) Let $X$ be a Banach space and $X^*$ its dual.
Let $\{x_j^*\}$ be a sequence in $X^*$ such that $\lim_{j \to \infty} x_j^*(x)$ exists (as a complex number) for every $x \in X$.
Then there is $x^* \in X^*$ such that $x^*(x) = \lim_{j \to \infty} x_j^*(x)$ for every $x \in X$.
:::

::: {.solution}

::: pf

::: pf-step

Part (a) is false.

::: pf-proof

The Cantor--Lebesgue function $F:[0,1]\to[0,1]$ is continuous and nonconstant, while
$$
F'(x)=0
$$
for almost every $x\in[0,1]$. Hence continuity together with existence of the derivative a.e. and $f'=0$ a.e. does not force constancy.

:::

:::

::: pf-step

Part (b) is false.

::: pf-proof

Take $X=\RR$ with $\mu=m$ and $E_j=[j,\infty)$. The sets decrease and $\bigcap_jE_j=\varnothing$, so $\mu\bigl(\bigcap_jE_j\bigr)=0$. But $\mu(E_j)=\infty$ for every $j$, so $\mu(E_j)\not\to0$. (Continuity from above needs $\mu(E_j)<\infty$ for some $j$.)

:::

:::

::: pf-step

Part (c) is true.

::: pf-proof

Because
$$
0\le f_j\le f_1
$$
almost everywhere and $f_1\in L^1(X,\mu)$, while $f_j\to f$ almost everywhere, the Dominated Convergence Theorem gives
$$
\boxed{\int_X f\,d\mu=\lim_{j\to\infty}\int_X f_j\,d\mu.}
$$

:::

:::

::: pf-step

Part (d) is true.

::: pf-proof

The total variation measure $\totalvariation{\nu}$ dominates $\nu$, so
$$
\nu\ll\totalvariation{\nu}.
$$
By the Radon--Nikodym theorem there is a measurable function
$$
f=\frac{d\nu}{d\totalvariation{\nu}}
$$
such that
$$
\nu(E)=\int_E f\,d\totalvariation{\nu}
$$
for every measurable $E$. For a finite signed measure one has
$$
\abs{f}=1
$$
$\totalvariation{\nu}$-almost everywhere, so $f\in L^1(X,\totalvariation{\nu})$ because $\totalvariation{\nu}(X)<\infty$.

By the defining integration identity for the Radon--Nikodym derivative, every $g$ integrable with respect to $\nu$ satisfies
$$
\boxed{\int_X g\,d\nu=\int_X gf\,d\totalvariation{\nu}.}
$$

:::

:::

::: pf-step

Part (e) is true.

::: pf-proof

For each fixed $x\in X$, the scalar sequence $(x_j^*(x))$ converges and is therefore bounded. Thus
$$
\sup_j\abs{x_j^*(x)}<\infty
\qquad\text{for every }x\in X.
$$
Since $X$ is Banach, the Uniform Boundedness Principle gives
$$
M:=\sup_j\norm{x_j^*}<\infty.
$$
Define
$$
x^*(x):=\lim_{j\to\infty}x_j^*(x).
$$
Pointwise limits preserve linearity, so $x^*$ is linear. Moreover,
$$
\abs{x^*(x)}
=\lim_j\abs{x_j^*(x)}
\le M\norm{x}.
$$
Hence $x^*\in X^*$ and
$$
\boxed{x^*(x)=\lim_{j\to\infty}x_j^*(x)\quad\text{for every }x\in X.}
$$

:::

:::

:::

:::
