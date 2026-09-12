---
schema: qual/card@1
id: P-RASP16D
kind: problem
title: "Convergence of Riemann-Stieltjes sums and the norm of Riemann-Stieltjes functionals"
classification:
  areas:
  - real-analysis
  topics:
  - Riemann-Stieltjes Integration
  - Uniform Boundedness Principle
  - Riesz Representation
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 4 of the official UCSD Spring 2016 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $0 = x_0^{(k)} < x_1^{(k)} < \cdots < x_k^{(k)} = 1$ ($k = 1, 2, \ldots$) and $0 \neq A_j^{(k)} \in \mathbb{R}$ ($j = 0, \ldots, k$, $k = 1, 2, \ldots$). Define for any $f \in C([0, 1])$
$$
I[f] = \int_0^1 f(x) \, dx \quad \text{and} \quad I_k[f] = \sum_{j=0}^{k} A_j^{(k)} f(x_j^{(k)}) \quad (k = 1, 2, \ldots).
$$

(1) Assume $\sup_{k \geq 1} \sum_{j=0}^{k} |A_j^{(k)}| < \infty$ and $\lim_{k \to \infty} I_k[p] = I[p]$ for any polynomial $p$.
Prove $\lim_{k \to \infty} I_k[f] = I[f]$ for $f \in C([0, 1])$.

(2) (a) For any $k > 1$, $I_k$ is a linear functional on the Banach space $C([0, 1])$ with the uniform norm.
Prove that $\|I_k\| = \sum_{j=0}^{k} |A_j^{(k)}|$.

(b) Assume $\lim_{k \to \infty} I_k[f] = I[f]$ for any $f \in C([0, 1])$.
Prove $\sup_{k \geq 1} \sum_{j=0}^{k} |A_j^{(k)}| < \infty$.
:::


::: solution
<1>1. Extend convergence from polynomials to all continuous functions.
::: proof
Put
\[
M:=\sup_{k\ge1}\sum_{j=0}^k |A_j^{(k)}|<\infty.
\]
For every \(f\in C([0,1])\),
\[
|I_k[f]|
\le \sum_{j=0}^k |A_j^{(k)}|\,\|f\|_\infty
\le M\|f\|_\infty.
\]
Also
\[
|I[f]|\le \|f\|_\infty.
\]
Fix \(f\in C([0,1])\) and \(\varepsilon>0\). By the Weierstrass approximation theorem, choose a polynomial \(p\) with
\[
\|f-p\|_\infty<\frac{\varepsilon}{2(M+1)}.
\]
Then
\[
\begin{aligned}
|I_k[f]-I[f]|
&\le |I_k[f-p]|+|I_k[p]-I[p]|+|I[p-f]|\\
&\le (M+1)\|f-p\|_\infty+|I_k[p]-I[p]|.
\end{aligned}
\]
The first term is below \(\varepsilon/2\), and the second tends to \(0\) by hypothesis. Hence
\[
I_k[f]\longrightarrow I[f].
\]
:::

<1>2. Compute the norm of \(I_k\).
::: proof
For \(\|f\|_\infty\le1\),
\[
|I_k[f]|
\le \sum_{j=0}^k |A_j^{(k)}|,
\]
so
\[
\|I_k\|\le \sum_{j=0}^k |A_j^{(k)}|.
\]
Conversely, because the nodes
\[
0=x_0^{(k)}<x_1^{(k)}<\cdots<x_k^{(k)}=1
\]
are distinct, there is a continuous piecewise-linear function \(f_k\) with
\[
f_k(x_j^{(k)})=\operatorname{sgn}(A_j^{(k)})
\]
for every \(j\), and \(\|f_k\|_\infty=1\). Therefore
\[
I_k[f_k]
=\sum_{j=0}^k A_j^{(k)}\operatorname{sgn}(A_j^{(k)})
=\sum_{j=0}^k |A_j^{(k)}|.
\]
Hence
\[
\boxed{\|I_k\|=\sum_{j=0}^k |A_j^{(k)}|.}
\]
:::

<1>3. Deduce uniform boundedness of the coefficient sums from pointwise convergence.
::: proof
Assume \(I_k[f]\to I[f]\) for every \(f\in C([0,1])\). For each fixed \(f\), the scalar sequence \((I_k[f])_k\) converges and is therefore bounded:
\[
\sup_k |I_k[f]|<\infty.
\]
Since \(C([0,1])\) is Banach, the Uniform Boundedness Principle gives
\[
\sup_k\|I_k\|<\infty.
\]
Using Step 2,
\[
\boxed{
\sup_{k\ge1}\sum_{j=0}^k |A_j^{(k)}|<\infty.}
\]
:::
:::
