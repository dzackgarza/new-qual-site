---
schema: qual/card@1
id: P-JHUMAY09ANH
kind: problem
title: "Successive moment ratios converge to the essential supremum"
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: 'Checked against Problem 8 of the JHU Analysis Qualifying Exam, May 2009, in the preserved exam collection. The source omits the necessary nonzero hypothesis: if f=0 almost everywhere, every a_n is zero and a_{n+1}/a_n is undefined.'
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f\in L^\infty([0,1])$ and assume $f$ is not zero almost everywhere.
Define
\[
a_n=\int_0^1|f(x)|^n\,dx.
\]
Prove that
\[
\lim_{n\to\infty}\frac{a_{n+1}}{a_n}=\|f\|_\infty.
\]
:::

::: {.solution}
Set
\[
M=\|f\|_\infty>0.
\]

<1>1. The ratios are nondecreasing and bounded above by $M$.
::: {.proof}
By Cauchy--Schwarz,
\[
a_{n+1}^2
=\left(\int |f|^{n/2}|f|^{(n+2)/2}\right)^2
\le a_n a_{n+2}.
\]
Since $a_n>0$,
\[
\frac{a_{n+1}}{a_n}\le\frac{a_{n+2}}{a_{n+1}}.
\]
Thus the ratios are nondecreasing.
Also $|f|\le M$ almost everywhere, so
\[
a_{n+1}\le M a_n,
\]
and hence
\[
\frac{a_{n+1}}{a_n}\le M.
\]
Therefore the ratios converge to some $L\le M$.
:::

<1>2. The limit cannot be smaller than $M$.
::: {.proof}
Fix $0<\varepsilon<M$.
By the definition of essential supremum, the set
\[
E_\varepsilon=\{x:|f(x)|>M-\varepsilon\}
\]
has positive measure.
Hence
\[
a_n\ge m(E_\varepsilon)(M-\varepsilon)^n.
\]
On the other hand, since the ratios increase to $L$, each ratio is at most $L$, so for $n\ge1$,
\[
a_n=a_1\prod_{k=1}^{n-1}\frac{a_{k+1}}{a_k}\le a_1L^{n-1}.
\]
Combining the two estimates and taking $n$th roots gives
\[
M-\varepsilon
\le m(E_\varepsilon)^{-1/n}a_1^{1/n}L^{(n-1)/n}.
\]
Letting $n\to\infty$ yields
\[
M-\varepsilon\le L.
\]
Since $\varepsilon>0$ is arbitrary, $M\le L$.
Together with $L\le M$, this gives
\[
L=M=\|f\|_\infty.
\]
Thus
\[
\boxed{\displaystyle \lim_{n\to\infty}\frac{a_{n+1}}{a_n}=\|f\|_\infty}.
\]
:::
:::
