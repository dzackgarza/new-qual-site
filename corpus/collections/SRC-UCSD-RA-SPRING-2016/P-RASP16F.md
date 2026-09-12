---
schema: qual/card@1
id: P-RASP16F
kind: problem
title: "L^p boundedness plus L^1 convergence implies L^q convergence for q < p"
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Interpolation
  - Uniform Integrability
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 6 of the official UCSD Spring 2016 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $(X, \mathcal{M}, \mu)$ be a measure space with $\mu(X) < \infty$.
Let $1 < p < \infty$.
Suppose $f_k \in L^p(\mu)$ ($k = 1, 2, \ldots$) are such that $\sup_{k \geq 1} \|f_k\|_p < \infty$ and $f_k \to f$ in $L^1(\mu)$ for some $f \in L^1(\mu)$.
Prove that $f \in L^p(\mu)$ and $f_k \to f$ in $L^q(\mu)$ for any $q \in (1, p)$.
:::


::: solution
<1>1. Show that the limit belongs to \(L^p\).
::: proof
Let
\[
M:=\sup_k\|f_k\|_p<\infty.
\]
Since \(f_k\to f\) in \(L^1\), there is a subsequence \((f_{k_j})\) such that
\[
f_{k_j}(x)\to f(x)
\]
for almost every \(x\in X\). By Fatou's lemma,
\[
\int_X |f|^p\,d\mu
\le \liminf_{j\to\infty}\int_X |f_{k_j}|^p\,d\mu
\le M^p.
\]
Hence
\[
\boxed{f\in L^p(\mu),\qquad \|f\|_p\le M.}
\]
:::

<1>2. Obtain a uniform \(L^p\) bound for the differences.
::: proof
Set
\[
h_k:=f_k-f.
\]
Then
\[
\|h_k\|_1\longrightarrow0
\]
and, by the triangle inequality,
\[
\|h_k\|_p
\le \|f_k\|_p+\|f\|_p
\le 2M.
\]
:::

<1>3. Interpolate between \(L^1\) and \(L^p\).
::: proof
Fix \(q\in(1,p)\). Choose \(\theta\in(0,1)\) so that
\[
\frac1q=\frac\theta1+\frac{1-\theta}{p}.
\]
The standard interpolation inequality gives
\[
\|h_k\|_q
\le \|h_k\|_1^\theta\|h_k\|_p^{1-\theta}.
\]
For completeness, this follows from Hölder after writing
\[
|h_k|^q=|h_k|^{\theta q}|h_k|^{(1-\theta)q}
\]
with conjugate exponents
\[
\frac1{\theta q}
\qquad\text{and}\qquad
\frac p{(1-\theta)q},
\]
whose reciprocals sum to \(1\) precisely because of the defining relation for \(\theta\).

Using Step 2,
\[
\|f_k-f\|_q
=\|h_k\|_q
\le (2M)^{1-\theta}\|h_k\|_1^\theta
\longrightarrow0.
\]
Therefore
\[
\boxed{f_k\to f\text{ in }L^q(\mu)\text{ for every }1<q<p.}
\]
:::
:::
