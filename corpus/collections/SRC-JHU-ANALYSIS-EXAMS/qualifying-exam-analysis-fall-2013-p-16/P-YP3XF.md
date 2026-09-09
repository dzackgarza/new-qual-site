---
schema: qual/card@1
id: P-YP3XF
kind: problem
title: 'Multiplication operator on $L^2$ is self-adjoint but not compact'
classification:
  areas:
  - real-analysis
  topics:
  - Operator Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved JHU Fall 2013 Analysis qualifying exam packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

(a) Prove that the operator $T : L^2([0,1]) \to L^2([0,1])$ defined by setting $T[f](x) = xf(x)$ is continuous and symmetric (self-adjoint).

(b) Prove that $T$ is not compact.

::: {.solution}
<1>1. Prove boundedness and self-adjointness.
::: {.proof}
For $f\in L^2([0,1])$,
\[
\|Tf\|_2^2
=\int_0^1 x^2|f(x)|^2\,dx
\le \int_0^1|f(x)|^2\,dx
=\|f\|_2^2.
\]
Thus $T$ is bounded and $\|T\|\le1$. In fact $\|T\|=1$ by testing on functions supported near $1$.

For $f,g\in L^2([0,1])$,
\[
\langle Tf,g\rangle
=\int_0^1 xf(x)\overline{g(x)}\,dx
=\int_0^1 f(x)\overline{xg(x)}\,dx
=\langle f,Tg\rangle.
\]
Hence $T=T^*$.
:::

<1>2. Construct a bounded sequence whose image has no convergent subsequence.
::: {.proof}
For $n\in\mathbb Z$, set
\[
e_n(x):=\sqrt2\,e^{4\pi i n x}\mathbf1_{[1/2,1]}(x).
\]
Then $(e_n)$ is an orthonormal sequence in $L^2([0,1])$. Hence for $n\ne m$,
\[
\|e_n-e_m\|_2^2=2.
\]

Since $x\ge1/2$ on $[1/2,1]$,
\[
\begin{aligned}
\|Te_n-Te_m\|_2^2
&=\int_{1/2}^1x^2|e_n(x)-e_m(x)|^2\,dx\\
&\ge \frac14\|e_n-e_m\|_2^2\\
&=\frac12.
\end{aligned}
\]
Thus the sequence $(Te_n)$ is pairwise separated by at least $1/\sqrt2$, so it has no Cauchy subsequence and therefore no convergent subsequence.

The bounded sequence $(e_n)$ lies in the unit ball, but its image under $T$ is not relatively compact. Hence $T$ is not compact.
:::
:::
