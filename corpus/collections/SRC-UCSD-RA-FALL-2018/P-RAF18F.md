---
schema: qual/card@1
id: P-RAF18F
kind: problem
title: "A bounded linear functional on L^infinity not arising from L^1"
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
  note: Checked against Problem 6 of the official UCSD Fall 2018 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Consider the Banach space $L^\infty([0,1], m)$ and its vector subspace
$$
V = \{f \in L^\infty([0,1], m) : \text{the limit } \lim_{n \to \infty} n \int_{[0,1/n]} f\,dm \text{ exists}\}.
$$

1. Prove that there exists $\varphi \in L^\infty([0,1], m)^*$ such that $\varphi(f) = \lim_{n \to \infty} n \int_{[0,1/n]} f\,dm$ for every $f \in V$.

2. Let $\varphi \in L^\infty([0,1], m)^*$ such that $\varphi(f) = \lim_{n \to \infty} n \int_{[0,1/n]} f\,dm$ for every $f \in V$.
   Prove that there does not exist $g \in L^1([0,1], m)$ such that $\varphi(f) = \int fg\,dm$ for every $f \in L^\infty([0,1], m)$.
:::

::: solution
<1>1. Define the functional on $V$ and extend it.
::: proof
For $f\in V$, set
\[
L(f):=\lim_{n\to\infty}n\int_0^{1/n}f(x)\,dx.
\]
The space $V$ is a vector subspace and $L$ is linear, because limits respect finite linear combinations.

For every $n$,
\[
\left|n\int_0^{1/n}f(x)\,dx\right|
\le n\frac1n\|f\|_\infty
=\|f\|_\infty.
\]
Passing to the limit gives
\[
|L(f)|\le\|f\|_\infty.
\]
Thus $L$ is a bounded linear functional on $V$ with norm at most $1$. By the Hahn--Banach theorem, $L$ extends to a bounded linear functional
\[
\varphi\in L^\infty([0,1])^*
\]
with the same norm. Hence
\[
\varphi(f)=L(f)
\]
for every $f\in V$.
:::

<1>2. Test the extension on shrinking interval indicators.
::: proof
For $k\ge1$, let
\[
f_k=\mathbf1_{[0,1/k]}.
\]
If $n\ge k$, then $[0,1/n]\subseteq[0,1/k]$, so
\[
n\int_0^{1/n}f_k(x)\,dx
=n\frac1n=1.
\]
Therefore $f_k\in V$ and
\[
\varphi(f_k)=1
\qquad\text{for every }k.
\]
:::

<1>3. Rule out representation by an $L^1$ density.
::: proof
Suppose there were $g\in L^1([0,1])$ such that
\[
\varphi(f)=\int_0^1 f(x)g(x)\,dx
\]
for every $f\in L^\infty([0,1])$. Applying this to $f_k$ gives
\[
1=\varphi(f_k)=\int_0^{1/k}g(x)\,dx.
\]
But absolute continuity of the Lebesgue integral for $g\in L^1$ implies
\[
\int_0^{1/k}g(x)\,dx\longrightarrow0
\]
as $k\to\infty$, a contradiction. Hence no such $g$ exists.
:::
:::
