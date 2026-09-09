---
schema: qual/card@1
id: P-RASP24B
kind: problem
title: "Scheffe's lemma and its failure for signed functions"
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
  note: Checked against Problem 2 of the official UCSD Spring 2024 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
(a) Let $(X, \mathcal{M}, \mu)$ be a measure space and let $f_n, f \in L^1(\mu)$ ($n \in \mathbb{N}$) be nonnegative functions.
If $f_n \to f$ almost everywhere and $\lim_{n \to \infty} \int_X f_n\,d\mu = \int_X f\,d\mu$, show that $f_n \to f$ in $L^1(\mu)$.

(b) Does the conclusion in (a) continue to hold when we drop the hypothesis that $f_n, f$ are non-negative?
Either prove this or find a counterexample.
:::

::: solution
<1>1. Prove Scheffe's lemma in the nonnegative case.
::: proof
Since $f_n\to f$ almost everywhere,
\[
\min(f_n,f)\to f
\]
almost everywhere. Moreover,
\[
0\le \min(f_n,f)\le f,
\]
and $f\in L^1(\mu)$. Hence the Dominated Convergence Theorem gives
\[
\int_X\min(f_n,f)\,d\mu\longrightarrow\int_X f\,d\mu.
\]
For nonnegative functions,
\[
|f_n-f|=f_n+f-2\min(f_n,f).
\]
Therefore
\[
\begin{aligned}
\|f_n-f\|_1
&=\int_Xf_n\,d\mu+\int_Xf\,d\mu
-2\int_X\min(f_n,f)\,d\mu\\
&\longrightarrow
\int_Xf\,d\mu+\int_Xf\,d\mu-2\int_Xf\,d\mu=0.
\end{aligned}
\]
Thus
\[
\boxed{f_n\to f\text{ in }L^1(\mu).}
\]
:::

<1>2. Show that nonnegativity is essential.
::: proof
Take $X=[0,1]$ with Lebesgue measure, let $f\equiv0$, and for $n\ge2$ define
\[
f_n(x)=n\mathbf1_{(0,1/n)}(x)-n\mathbf1_{(1/n,2/n)}(x).
\]
For every $x>0$, both intervals eventually lie to the left of $x$, so $f_n(x)=0$ for all sufficiently large $n$. Thus
\[
f_n\to0
\]
almost everywhere.

Also
\[
\int_0^1f_n(x)\,dx
=n\frac1n-n\frac1n=0
=\int_0^1f(x)\,dx
\]
for every $n$. However,
\[
\|f_n-f\|_1
=\int_0^1|f_n(x)|\,dx
=n\frac1n+n\frac1n=2.
\]
Hence $f_n$ does not converge to $f$ in $L^1$. Therefore the conclusion in part (a) is false without the nonnegativity hypothesis.
:::
:::
