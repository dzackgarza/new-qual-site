---
schema: qual/card@1
id: P-XWL4U
kind: problem
title: If $f_k\to f$ a.e. with $\|f_k\|_2\leq M$ on $[0,1]$, then $f\in L^2$, $\|f\|_2\leq
  M$, and $\int f_k\to\int f$
classification:
  areas:
  - real-analysis
  topics:
  - L²
  - Fatou
  - Egorov
  - Convergence of Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the UGA Spring 2019 real-analysis qualifying exam recorded by SRC-UGA-RA-SPRING-2019.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---


::: problem
Let $(f_k)$ be a sequence in $L^2([0,1])$ satisfying
\[
\|f_k\|_2\le M
\qquad\text{for every }k.
\]
Assume $f_k\to f$ almost everywhere. Prove that $f\in L^2([0,1])$, that $\|f\|_2\le M$, and that
\[
\int_0^1 f_k(x)\,dx\longrightarrow\int_0^1 f(x)\,dx.
\]
:::

::: solution
<1>1. The limit belongs to $L^2$ with the same bound.
::: proof
Since $|f_k|^2\to |f|^2$ almost everywhere, Fatou's lemma gives
\[
\int_0^1|f|^2
\le \liminf_{k\to\infty}\int_0^1|f_k|^2
\le M^2.
\]
Hence
\[
f\in L^2([0,1])
\qquad\text{and}\qquad
\|f\|_2\le M.
\]
:::

<1>2. Prove $f_k\to f$ in $L^1$.
::: proof
Fix $\varepsilon>0$. Choose $\delta>0$ such that
\[
2M\sqrt\delta<\frac\varepsilon2.
\]
By Egorov's theorem, there is a measurable set $F\subset[0,1]$ such that
\[
m([0,1]\setminus F)<\delta
\]
and $f_k\to f$ uniformly on $F$.

Thus for all sufficiently large $k$,
\[
\int_F|f_k-f|
\le m(F)\sup_F|f_k-f|
<\frac\varepsilon2.
\]
On the exceptional set $E=[0,1]\setminus F$, Cauchy--Schwarz gives
\[
\begin{aligned}
\int_E|f_k-f|
&\le m(E)^{1/2}\|f_k-f\|_2\\
&\le \sqrt\delta\,(\|f_k\|_2+\|f\|_2)\\
&\le 2M\sqrt\delta
<\frac\varepsilon2.
\end{aligned}
\]
Therefore
\[
\|f_k-f\|_1<\varepsilon
\]
for all sufficiently large $k$. Hence
\[
f_k\to f\quad\text{in }L^1([0,1]).
\]
:::

<1>3. Conclude convergence of the integrals.
::: proof
Since
\[
\left|\int_0^1 f_k-\int_0^1 f\right|
\le \int_0^1|f_k-f|
=\|f_k-f\|_1,
\]
Step 2 yields
\[
\boxed{
\int_0^1 f_k(x)\,dx\to\int_0^1 f(x)\,dx.}
\]
:::
:::
