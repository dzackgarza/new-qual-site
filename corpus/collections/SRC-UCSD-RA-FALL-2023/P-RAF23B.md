---
schema: qual/card@1
id: P-RAF23B
kind: problem
title: "Dilation converges in L^1"
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
  note: Checked against Problem 2 of the official UCSD Fall 2023 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
For $a > 0$, let $(S_a f)(x) = f(x/a)$ for Lebesgue measurable functions $f$ on $\mathbb{R}$.
Then for any $f \in L^1(\mathbb{R}, m)$, $S_a f \to f$ in $L^1$ as $a \to 1$.
:::

::: solution
<1>1. Compute the operator norm of the dilation.
::: proof
For $a>0$, the change of variables $y=x/a$ gives
\[
\|S_af\|_1
=\int_{\mathbb R}|f(x/a)|\,dx
=a\int_{\mathbb R}|f(y)|\,dy
=a\|f\|_1.
\]
Hence
\[
\|S_a\|_{L^1\to L^1}=a.
\]
In particular, the operators $S_a$ are uniformly bounded for $a$ in any fixed neighborhood of $1$.
:::

<1>2. Prove the claim for $C_c(\mathbb R)$.
::: proof
Let $g\in C_c(\mathbb R)$ and choose $M>0$ with
\[
\operatorname{supp}g\subset[-M,M].
\]
Restrict first to $a\in[1/2,2]$. Then
\[
\operatorname{supp}(S_ag)\subset[-2M,2M].
\]
Since $g$ is uniformly continuous on $\mathbb R$ and
\[
\sup_{|x|\le2M}|x/a-x|\longrightarrow0
\qquad(a\to1),
\]
we have
\[
\|S_ag-g\|_\infty\longrightarrow0.
\]
Both functions vanish outside a fixed compact interval, so
\[
\|S_ag-g\|_1\longrightarrow0.
\]
:::

<1>3. Pass to an arbitrary $L^1$ function by density.
::: proof
Fix $f\in L^1(\mathbb R)$ and $\varepsilon>0$. Choose $g\in C_c(\mathbb R)$ such that
\[
\|f-g\|_1<\varepsilon.
\]
For $a$ sufficiently close to $1$, say $a\in[1/2,2]$, Step 1 gives
\[
\|S_a(f-g)\|_1\le2\|f-g\|_1<2\varepsilon.
\]
Therefore
\[
\begin{aligned}
\|S_af-f\|_1
&\le \|S_a(f-g)\|_1+\|S_ag-g\|_1+\|g-f\|_1\\
&<3\varepsilon+\|S_ag-g\|_1.
\end{aligned}
\]
By Step 2, the final term tends to $0$ as $a\to1$. Hence
\[
\limsup_{a\to1}\|S_af-f\|_1\le3\varepsilon.
\]
Since $\varepsilon$ is arbitrary,
\[
\boxed{\|S_af-f\|_1\longrightarrow0\quad(a\to1).}
\]
:::
:::
