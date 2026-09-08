---
schema: qual/card@1
id: P-RAF17D
kind: problem
title: "L^p integrability from weak-type boundedness"
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
  note: Checked against Problem 4 of the official UCSD Fall 2017 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Suppose that $(\Omega, \mathcal{B}, \mu)$ is a measure space, $\Omega_n \in \mathcal{B}$ with $\Omega_n \uparrow \Omega$ and $\mu(\Omega_n) < \infty$ for all $n \in \mathbb{N}$.
If $f : \Omega \to \mathbb{C}$ is a measurable function such that
$$
\int_\Omega |fg|\,d\mu < \infty \quad \text{for all } g \in L^{3/2}(\mu),
$$
show $f \in L^3(\mu)$, i.e. $\int_\Omega |f|^3\,d\mu < \infty$.

Hint: consider $f_n := \mathbf{1}_{\Omega_n} f \cdot \mathbf{1}_{|f| \leq n} \in L^3(\mu)$ for $n \in \mathbb{N}$ and recall $L^3(\mu) \cong L^{3/2}(\mu)^*$.
:::

::: solution
<1>1. Define the truncated functions and their functionals.
::: proof
Set
\[
f_n:=\mathbf1_{\Omega_n}f\,\mathbf1_{\{|f|\le n\}}.
\]
Since $|f_n|\le n$ and $\mu(\Omega_n)<\infty$, we have $f_n\in L^3(\mu)$.

Define
\[
T_n:L^{3/2}(\mu)\to\mathbb C,
\qquad
T_n(g)=\int_\Omega f_n g\,d\mu.
\]
By Hölder's inequality, $T_n$ is bounded. Under the standard duality
\[
(L^{3/2})^*\cong L^3,
\]
its norm is
\[
\|T_n\|=\|f_n\|_3.
\]
:::

<1>2. Show that the family $(T_n)$ is pointwise bounded.
::: proof
For every $g\in L^{3/2}(\mu)$,
\[
|T_n(g)|
\le\int_\Omega |f_n g|\,d\mu
\le\int_\Omega |fg|\,d\mu.
\]
The final quantity is finite by hypothesis and does not depend on $n$. Therefore
\[
\sup_n|T_n(g)|<\infty
\]
for every $g\in L^{3/2}(\mu)$.
:::

<1>3. Apply Uniform Boundedness and pass to the limit.
::: proof
Since $L^{3/2}(\mu)$ is Banach, the Principle of Uniform Boundedness gives
\[
\sup_n\|T_n\|<\infty.
\]
Thus there is $C<\infty$ such that
\[
\|f_n\|_3\le C
\qquad\text{for all }n.
\]

Because $\Omega_n\uparrow\Omega$ and the cutoffs $\mathbf1_{\{|f|\le n\}}$ also increase, we have
\[
|f_n|^3\uparrow |f|^3
\]
pointwise. Hence the Monotone Convergence Theorem gives
\[
\int_\Omega |f|^3\,d\mu
=\lim_{n\to\infty}\int_\Omega|f_n|^3\,d\mu
\le C^3<\infty.
\]
Therefore
\[
\boxed{f\in L^3(\mu).}
\]
:::
:::
