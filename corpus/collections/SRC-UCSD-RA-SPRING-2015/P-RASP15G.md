---
schema: qual/card@1
id: P-RASP15G
kind: problem
title: "Weak but not strong convergence of sin(kx) in L^p"
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
  note: Checked against Problem 7 of the official UCSD Spring 2015 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $X = [-\pi, \pi]$ and consider the Lebesgue measure.
Let $p$ be a real number with $1 \leq p < \infty$.
Define for each integer $k \geq 1$ that $f_k(x) = \sin(kx)$ ($x \in X$).

(a) Prove that the sequence $\{f_k\}$ converges weakly to $0$ in $L^p(X)$.

(b) Prove that the sequence $\{f_k\}$ does not converge to $0$ strongly in $L^p(X)$.
:::

::: solution
<1>1. Prove weak convergence to $0$.
::: proof
Let $p'$ be the conjugate exponent, with $p'=\infty$ when $p=1$. Since $X=[-\pi,\pi]$ has finite measure,
\[
L^{p'}(X)\subseteq L^1(X)
\]
for every $1\le p'\le\infty$.

Fix $g\in L^{p'}(X)$. By the Riemann--Lebesgue lemma,
\[
\int_{-\pi}^{\pi}g(x)e^{ikx}\,dx\longrightarrow0.
\]
Taking imaginary parts gives
\[
\int_{-\pi}^{\pi}g(x)\sin(kx)\,dx\longrightarrow0.
\]
Thus every continuous linear functional on $L^p(X)$ tends to $0$ on $f_k$, and therefore
\[
\boxed{f_k\rightharpoonup0\text{ in }L^p(X).}
\]
:::

<1>2. Show that the norms do not tend to zero.
::: proof
For every integer $k\ge1$,
\[
\begin{aligned}
\|f_k\|_p^p
&=\int_{-\pi}^{\pi}|\sin(kx)|^p\,dx\\
&=\frac1k\int_{-k\pi}^{k\pi}|\sin u|^p\,du.
\end{aligned}
\]
Since $|\sin u|^p$ has period $\pi$, the interval $[-k\pi,k\pi]$ consists of $2k$ periods. Hence
\[
\|f_k\|_p^p
=2\int_0^\pi\sin^p u\,du,
\]
which is a positive constant independent of $k$. Consequently
\[
\|f_k\|_p\not\to0,
\]
so $f_k$ does not converge strongly to $0$ in $L^p(X)$.
:::
:::
