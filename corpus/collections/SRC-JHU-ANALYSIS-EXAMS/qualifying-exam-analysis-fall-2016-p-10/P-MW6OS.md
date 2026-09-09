---
schema: qual/card@1
id: P-MW6OS
kind: problem
title: "Norm-one sequences in an infinite-dimensional Hilbert space: subsequences"
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Weak Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 3 of the Fall 2016 JHU analysis qualifying exam in the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

3. Let H be an infinite dimensional Hilbert space.
   Determine if the following statements are true or false.
   If true, provide a proof.
   If false, provide a counter example.

(a) A sequence $\left\{ f _ { n } \right\}$ in H with $\left| \left| f _ { n } \right| \right| = 1$ for all n has a subsequence that converges in H.

(b) A sequence $\left\{ f _ { n } \right\}$ in H with $| | f _ { n } | | = 1$ for all n has a subsequence that converges weakly in H.

::: solution
<1>1. Part (a) is false.
::: proof
Because $H$ is infinite dimensional, it contains an infinite orthonormal sequence
\[
e_1,e_2,\dots.
\]
Each vector has norm $1$, but for $m\ne n$,
\[
\|e_n-e_m\|^2
=\|e_n\|^2+\|e_m\|^2-2\operatorname{Re}\langle e_n,e_m\rangle
=2.
\]
Thus every two distinct terms are distance $\sqrt2$ apart. No subsequence is Cauchy, hence no subsequence converges in norm.

Therefore part (a) is false.
:::

<1>2. Reduce part (b) to a separable Hilbert space.
::: proof
Let $(f_n)$ be any sequence with $\|f_n\|=1$ for all $n$, and set
\[
H_0:=\overline{\operatorname{span}}\{f_n:n\ge1\}.
\]
Then $H_0$ is a separable Hilbert space. Choose an orthonormal basis
\[
e_1,e_2,\dots
\]
for $H_0$.

For each fixed $j$, the scalar sequence
\[
\langle f_n,e_j\rangle
\]
is bounded by $1$. By repeated subsequence extraction and the diagonal argument, there is a subsequence $(f_{n_k})$ such that for every $j$ the limit
\[
a_j:=\lim_{k\to\infty}\langle f_{n_k},e_j\rangle
\]
exists.
:::

<1>3. Show that the limiting coordinates define a vector of $H_0$.
::: proof
For every $N$, Bessel's inequality gives
\[
\sum_{j=1}^N|\langle f_{n_k},e_j\rangle|^2
\le \|f_{n_k}\|^2=1.
\]
Letting $k\to\infty$ yields
\[
\sum_{j=1}^N|a_j|^2\le1.
\]
Since this holds for every $N$,
\[
\sum_{j=1}^\infty|a_j|^2\le1.
\]
Hence the series
\[
f:=\sum_{j=1}^\infty a_j e_j
\]
converges in $H_0$.
:::

<1>4. Prove weak convergence of the selected subsequence.
::: proof
First let
\[
g=\sum_{j=1}^N c_j e_j
\]
be a finite linear combination. Then
\[
\langle f_{n_k},g\rangle
\longrightarrow
\sum_{j=1}^N a_j\overline{c_j}
=\langle f,g\rangle.
\]

Now let $g\in H_0$ be arbitrary. Given $\varepsilon>0$, choose such a finite linear combination $g_N$ with
\[
\|g-g_N\|<\varepsilon.
\]
Since $\|f_{n_k}\|=1$ and $\|f\|\le1$,
\[
|\langle f_{n_k}-f,g-g_N\rangle|
\le2\varepsilon.
\]
Together with convergence against $g_N$, this gives
\[
\langle f_{n_k},g\rangle\to\langle f,g\rangle
\qquad(g\in H_0).
\]

Finally, if $g\in H_0^\perp$, then both $f_{n_k}$ and $f$ lie in $H_0$, so all these inner products are zero. Decomposing an arbitrary $g\in H$ into its $H_0$ and $H_0^\perp$ parts proves
\[
f_{n_k}\rightharpoonup f
\quad\text{in }H.
\]
Thus part (b) is true.
:::
:::
