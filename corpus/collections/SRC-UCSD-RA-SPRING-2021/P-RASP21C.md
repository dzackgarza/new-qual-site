---
schema: qual/card@1
id: P-RASP21C
kind: problem
title: "Function with prescribed moments"
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
  note: Checked against Problem 3 of the official UCSD Spring 2021 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
If $f \in L^1([0,1])$ and $\int_0^1 x^{2n} f(x)\,dx = \frac{1}{2n+2}$ for all $n = 0, 1, 2, \ldots$, is $f(x) = x$ a.e.?
:::


::: solution
Yes. Set
\[
h(x):=f(x)-x.
\]
Since $f\in L^1([0,1])$, we have $h\in L^1([0,1])$. The hypotheses give
\[
\int_0^1 x^{2n}h(x)\,dx=0
\qquad(n=0,1,2,\ldots),
\]
because
\[
\int_0^1x^{2n+1}\,dx=\frac1{2n+2}.
\]
Hence
\[
\int_0^1 p(x^2)h(x)\,dx=0
\]
for every polynomial $p$.

The algebra
\[
\mathcal A:=\{p(x^2):p\text{ a polynomial}\}
\]
contains the constants and separates points of $[0,1]$, since $x\mapsto x^2$ is injective on that interval. By the Stone--Weierstrass theorem, $\mathcal A$ is uniformly dense in $C([0,1])$.

Fix $\varphi\in C([0,1])$ and choose $p_k$ so that
\[
\|p_k(x^2)-\varphi(x)\|_\infty\to0.
\]
Then
\[
\left|\int_0^1h(x)\varphi(x)\,dx\right|
\le
\left|\int_0^1h(x)p_k(x^2)\,dx\right|
+\|h\|_1\,\|\varphi-p_k(x^2)\|_\infty.
\]
The first term is zero and the second tends to zero, so
\[
\int_0^1h\varphi=0
\]
for every continuous $\varphi$.

Thus the finite signed measure $h(x)\,dx$ annihilates $C([0,1])$, hence is the zero measure. Therefore $h=0$ almost everywhere, i.e.
\[
\boxed{f(x)=x\quad\text{for a.e. }x\in[0,1].}
\]
:::
