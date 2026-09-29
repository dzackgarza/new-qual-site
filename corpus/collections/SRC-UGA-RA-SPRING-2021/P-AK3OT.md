---
schema: qual/card@1
id: P-AK3OT
kind: problem
title: $L^2([0,1])$ convergence of $\sum f_n$ when $\|f_n\|_2\le n^{-51/100}$ and
  $\operatorname{supp}\hat f_n\subseteq[2^n,2^{n+1}]$
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
  - L²
  - Hilbert Spaces
  - Series of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Problem 5 of the official UGA January 2021 Analysis qualifying examination DOCX. The legacy card mistranscribed discrete Fourier coefficients as a continuous Fourier transform; the source uses integer frequencies k.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Corrected the statement and proof to use Fourier series coefficients and Parseval on L2([0,1]); adjacent dyadic frequency blocks may share one endpoint coefficient, which is handled by Cauchy-Schwarz.
---

::: {.problem}
Let \( f_n \in L^2([0, 1]) \) for \( n\in \NN \), and assume that 

- \( \norm{f_n}_2 \leq n^{-51 \over 100} \)  for all \( n\in \NN \),

- the Fourier coefficients $\hat f_n(k)$ are supported in the integer frequencies in $[2^n,2^{n+1}]$, where
\[
\hat f_n(k)\da\int_0^1 f_n(x)e^{-2\pi ikx}\,dx=0
\qquad\text{for }k\in\ZZ\setminus[2^n,2^{n+1}].
\]

Prove that \( \sum_{n\in \NN} f_n \) converges in the Hilbert space \( L^2([0, 1]) \).

> Hint: Plancherel's identity may be helpful.

:::

::: {.warnings}
For Fourier series on $L^2([0,1])$, the identity in question is Parseval's identity:
\[
\sum_{k\in \ZZ} \abs{\hat{f}(k)}^2 = \int_0^1 \abs{f(x)}^2\dx
.\]

:::
::: {.solution}

::: pf

::: {.pf-step #parseval-identity}
Use Parseval for the Fourier series coefficients:
\[
\langle f,g\rangle_{L^2([0,1])}
=\sum_{k\in\ZZ}\hat f(k)\overline{\hat g(k)},
\qquad
\|f\|_2^2=\sum_{k\in\ZZ}|\hat f(k)|^2.
\]

::: pf-proof
Parseval's identity for the orthonormal Fourier basis of $L^2([0,1])$.
:::

:::

::: {.pf-step #disjoint-supports}
The coefficient supports of $f_n$ and $f_m$ are disjoint for $|n-m|\ge2$; for adjacent indices they can meet only at the single integer frequency $2^{n+1}$.

::: pf-proof
The dyadic intervals $[2^n,2^{n+1}]$ and $[2^m,2^{m+1}]$ have exactly this intersection pattern.
:::

:::

::: {.pf-step #inner-products-and-adjacent-bound}
Thus $\langle f_n,f_m\rangle=0$ for $|n-m|\ge2$, while
\[
|\langle f_n,f_{n+1}\rangle|\le\|f_n\|_2\|f_{n+1}\|_2.
\]

::: pf-proof
Apply Parseval from step [](#parseval-identity){.pf-ref} and the support information from step [](#disjoint-supports){.pf-ref}; the adjacent estimate is Cauchy--Schwarz.
:::

:::

::: {.pf-step #partial-sum-norm-bound}
For $N<M$,
\[
\left\|\sum_{n=N}^{M}f_n\right\|_2^2
\le\sum_{n=N}^{M}\|f_n\|_2^2
+2\sum_{n=N}^{M-1}\|f_n\|_2\|f_{n+1}\|_2.
\]

::: pf-proof
Expand the squared norm; cross terms between non-adjacent indices vanish by step [](#inner-products-and-adjacent-bound){.pf-ref}, and the adjacent terms are bounded by step [](#inner-products-and-adjacent-bound){.pf-ref}.
:::

:::

::: {.pf-step #tails-vanish}
The tails of both sums tend to $0$ as $N \to \infty$.

::: pf-proof

::: {.pf-step #square-tail-vanishes}
$\sum_{n=N}^{\infty}\|f_n\|_2^2 \le \sum_{n=N}^{\infty} n^{-51/50} \to 0$.

::: pf-proof
$\|f_n\|_2 \le n^{-51/100}$, and $\sum_n n^{-51/50} < \infty$ since $51/50 > 1$.
:::

:::

::: pf-step
$\sum_{n=N}^{\infty}\|f_n\|_2\|f_{n+1}\|_2 \le \sum_{n=N}^{\infty} n^{-51/100}(n+1)^{-51/100} \le \sum_{n=N}^{\infty} n^{-51/50} \to 0$.

::: pf-proof
$(n+1)^{-51/100} \le n^{-51/100}$, and step [](#square-tail-vanishes){.pf-ref}.
:::

:::

:::

:::

::: pf-qed
Steps [](#partial-sum-norm-bound){.pf-ref} and [](#tails-vanish){.pf-ref} show $\left\|\sum_{n=N}^{M}f_n\right\|_2^2 \to 0$ as $N \to \infty$ uniformly in $M > N$, i.e. the partial sums are Cauchy in the complete space $L^2([0,1])$; hence $\sum_n f_n$ converges in $L^2$.
:::

:::

:::
