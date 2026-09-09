---
schema: qual/card@1
id: P-RASP22F
kind: problem
title: "Density one condition for Radon measure with continuous density"
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
  date: 2026-09-09
  note: Checked against Problem 6 of the official UCSD Spring 2022 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $X$ be an LCH space.
Let $\mu$ be a $\sigma$-finite measure on $X$ such that for any measurable set $E$, $\mu(E) = \inf\{\mu(U) : E \subset U, U \text{ open}\}$.
Let $f \geq 0$ be a bounded measurable function.
Prove that if $\mu(U) = \int_U f\,d\mu$ whenever $U$ is open, then $f = 1$ $\mu$-a.e.
:::


::: solution
Let
\[
M:=\|1-f\|_\infty<\infty.
\]
We first show that
\[
\int_E(1-f)\,d\mu=0
\]
for every measurable $E$ with $\mu(E)<\infty$.

Fix such an $E$ and let $\varepsilon>0$. By the assumed outer regularity, there exists an open set $U\supseteq E$ such that
\[
\mu(U)<\mu(E)+\varepsilon.
\]
In particular $\mu(U)<\infty$, so the hypothesis on open sets gives
\[
\int_U(1-f)\,d\mu
=\mu(U)-\int_Uf\,d\mu
=0.
\]
Therefore
\[
\begin{aligned}
\left|\int_E(1-f)\,d\mu\right|
&=\left|\int_{U\setminus E}(1-f)\,d\mu\right|\\
&\le M\mu(U\setminus E)\\
&\le M\varepsilon.
\end{aligned}
\]
Since $\varepsilon$ is arbitrary,
\[
\int_E(1-f)\,d\mu=0
\]
for every finite-measure measurable $E$.

Because $\mu$ is $\sigma$-finite, choose measurable sets $X_n$ with
\[
X=\bigcup_{n=1}^\infty X_n,
\qquad
\mu(X_n)<\infty.
\]
For $k,n\ge1$, put
\[
A_{k,n}:=X_n\cap\{f\ge1+1/k\}.
\]
Then $A_{k,n}$ has finite measure, and hence
\[
0=\int_{A_{k,n}}(1-f)\,d\mu
\le -\frac1k\mu(A_{k,n}).
\]
Thus $\mu(A_{k,n})=0$. Similarly, with
\[
B_{k,n}:=X_n\cap\{f\le1-1/k\},
\]
we have
\[
0=\int_{B_{k,n}}(1-f)\,d\mu
\ge \frac1k\mu(B_{k,n}),
\]
so $\mu(B_{k,n})=0$.

Finally,
\[
\{f\ne1\}
\subseteq
\bigcup_{n,k\ge1}(A_{k,n}\cup B_{k,n}),
\]
a countable union of null sets. Therefore
\[
\boxed{f=1\quad\mu\text{-a.e.}}
\]
as claimed.
:::
