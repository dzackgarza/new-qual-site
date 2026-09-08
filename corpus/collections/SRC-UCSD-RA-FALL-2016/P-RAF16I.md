---
schema: qual/card@1
id: P-RAF16I
kind: problem
title: "Ratio of L^k norms converges to L^infinity norm"
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
  note: Checked against Problem 9 of the official UCSD Fall 2016 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $(X, \mathcal{M}, \mu)$ be a measure space with $\mu(X) < \infty$.
Let $f \in L^\infty(\mu)$ with $\|f\|_\infty > 0$.
Define
$$
\alpha_k = \int_X |f|^k\,d\mu \qquad \text{for } k = 1, 2, \ldots.
$$
Prove that
$$
\lim_{k \to \infty} \frac{\alpha_{k+1}}{\alpha_k} = \|f\|_\infty.
$$
:::

::: solution
<1>1. Show that the moment ratios are increasing and bounded above.
::: proof
Put
\[
M:=\|f\|_\infty>0,
\qquad
r_k:=\frac{\alpha_{k+1}}{\alpha_k}.
\]
Since $M>0$, the set on which $|f|>0$ has positive measure, so $\alpha_k>0$ for every $k$.

By Cauchy--Schwarz,
\[
\alpha_{k+1}^2
=\left(\int |f|^{k/2}|f|^{(k+2)/2}\,d\mu\right)^2
\le \alpha_k\alpha_{k+2}.
\]
Hence
\[
r_k\le r_{k+1}.
\]
Also $|f|\le M$ almost everywhere, so
\[
\alpha_{k+1}\le M\alpha_k,
\]
and therefore
\[
r_k\le M.
\]
Thus $(r_k)$ is increasing and bounded, so
\[
r_k\longrightarrow L
\]
for some $L\le M$.
:::

<1>2. Recall the finite-measure $L^k$-norm limit.
::: proof
We claim
\[
\alpha_k^{1/k}=\|f\|_k\longrightarrow M.
\]
The upper bound is
\[
\alpha_k^{1/k}
\le M\,\mu(X)^{1/k},
\]
so
\[
\limsup_{k\to\infty}\alpha_k^{1/k}\le M.
\]

Conversely, fix $a<M$. By the definition of essential supremum,
\[
E_a:=\{|f|>a\}
\]
has positive measure. Hence
\[
\alpha_k\ge a^k\mu(E_a),
\]
so
\[
\liminf_{k\to\infty}\alpha_k^{1/k}\ge a.
\]
Letting $a\uparrow M$ proves
\[
\boxed{\alpha_k^{1/k}\to M.}
\]
:::

<1>3. Identify the ratio limit.
::: proof
Since
\[
\alpha_k=\alpha_1\prod_{j=1}^{k-1}r_j,
\]
we have
\[
\alpha_k^{1/k}
=\alpha_1^{1/k}
\left(\prod_{j=1}^{k-1}r_j\right)^{1/k}.
\]
Because $r_j\to L$, the geometric means of $(r_j)$ also converge to $L$, while $\alpha_1^{1/k}\to1$. Therefore
\[
\alpha_k^{1/k}\longrightarrow L.
\]
Step 2 shows that the same sequence converges to $M$. Hence
\[
L=M,
\]
and consequently
\[
\boxed{\lim_{k\to\infty}\frac{\alpha_{k+1}}{\alpha_k}=\|f\|_\infty.}
\]
:::
:::
