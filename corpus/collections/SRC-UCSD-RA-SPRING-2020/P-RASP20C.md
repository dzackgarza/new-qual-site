---
schema: qual/card@1
id: P-RASP20C
kind: problem
title: "Unit ball of L^2 is closed and has empty interior in L^1"
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
  note: Checked against Problem 3 of the official UCSD Spring 2020 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Consider the Lebesgue measure $m$ on $[0,1]$ and denote by $\|\cdot\|_p$ the $L^p([0,1])$-norm for any $p \in [1, \infty]$.
Define $B = \{f \in L^2([0,1]) : \|f\|_2 \leq 1\}$.
Prove that, with respect to the $L^1([0,1])$-norm, $B$ is closed and has an empty interior.
:::


::: solution
<1>1. Prove that \(B\) is closed in the \(L^1\)-norm.
::: proof
Let \((f_n)\subset B\) and suppose
\[
f_n\to f
\qquad\text{in }L^1([0,1]).
\]
Passing to a subsequence, still denoted \((f_n)\), we may assume
\[
f_n(x)\to f(x)
\]
for almost every \(x\in[0,1]\). Since \(\|f_n\|_2\le1\), Fatou's lemma gives
\[
\int_0^1|f|^2\,dx
\le \liminf_{n\to\infty}\int_0^1|f_n|^2\,dx
\le1.
\]
Hence \(f\in L^2([0,1])\) and \(\|f\|_2\le1\), so \(f\in B\). Therefore \(B\) is \(L^1\)-closed.
:::

<1>2. Prove that \(B\) has empty \(L^1\)-interior.
::: proof
Fix \(f\in B\) and \(\varepsilon>0\). Let
\[
h(x)=c\,x^{-1/2}\mathbf1_{(0,1)}(x),
\]
where \(c>0\) is chosen so that \(2c<\varepsilon\). Then
\[
\|h\|_1=2c<\varepsilon,
\]
but
\[
\int_0^1|h(x)|^2\,dx
=c^2\int_0^1\frac{dx}{x}=\infty,
\]
so \(h\notin L^2\).

Now
\[
\|(f+h)-f\|_1=\|h\|_1<\varepsilon.
\]
If \(f+h\in L^2\), then
\[
h=(f+h)-f\in L^2,
\]
contradicting the choice of \(h\). Hence \(f+h\notin B\).

Thus every \(L^1\)-ball around every point of \(B\) contains a point outside \(B\), so
\[
\boxed{\operatorname{int}_{L^1}(B)=\varnothing.}
\]
:::
:::
