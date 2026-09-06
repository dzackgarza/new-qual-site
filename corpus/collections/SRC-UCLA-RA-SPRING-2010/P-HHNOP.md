---
schema: qual/card@1
id: P-HHNOP
kind: problem
title: 'Compactness of $A:X\to Y$ when $X$ is reflexive and $X^*$ is separable: every
  bounded sequence has a subsequence $x_{n_j}=\phi+r_{n_j}$ with $Ar_{n_j}\to 0$'
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against problem 13 of the UCLA Analysis Qualifying Exam, Spring 2010, from the collection provenance PDF; the UCLA solution compilation leaves this problem without a supplied solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Expanded the weak subsequence step: reflexivity identifies bounded balls with weak-star compact balls in X**, while separability of X* metrizes the weak topology on bounded sets, giving sequential compactness. Then used weak continuity of A to identify the norm limit of a compact image subsubsequence with A(phi).
---

::: {.problem}
Let $X$ and $Y$ be Banach spaces.
A bounded linear transformation $A:X\to Y$ is *compact* if for every bounded sequence $\{x_n\}\subseteq X$, the sequence $\{Ax_n\}$ has a convergent subsequence in $Y$.
Suppose $X$ is reflexive ($X^{**}=X$) and $X^*$ is separable.
Show that $A:X\to Y$ is compact if and only if for every bounded sequence $\{x_n\}\subseteq X$, there exists a subsequence $\{x_{n_j}\}$ and a vector $\phi\in X$ such that $x_{n_j} = \phi+r_{n_j}$ and $Ar_{n_j}\to 0$ in $Y$.
:::

::: {.solution}
We first record the sequential compactness consequence of the hypotheses on $X$.

<1>1. Every bounded sequence in $X$ has a weakly convergent subsequence.
::: {.proof}
Let $\{x_n\}$ be bounded, say
\[
\|x_n\|\le M
\qquad(n\ge1).
\]
If $M=0$, the sequence is identically zero, so assume $M>0$.

Let
\[
J:X\longrightarrow X^{**}
\]
be the canonical isometric embedding.
Since $X$ is reflexive, $J$ is onto.
Banach--Alaoglu says that the closed ball
\[
M B_{X^{**}}
\]
is compact for the weak-star topology $\sigma(X^{**},X^*)$.
Under the identification $J:X\cong X^{**}$, this weak-star topology restricted to $J(X)$ is exactly the weak topology $\sigma(X,X^*)$.
Hence
\[
M B_X
\]
is weakly compact.

Because $X^*$ is separable, choose a norm-dense sequence
\[
f_1,f_2,\ldots
\]
in the unit ball of $X^*$.
On $M B_X$, define
\[
d(x,y)=
\sum_{k=1}^{\infty}
2^{-k}\min\{1,|f_k(x-y)|\}.
\]
This metric induces the weak topology on $M B_X$.
Indeed, weak convergence implies convergence of every $f_k$, and the uniformly summable weights $2^{-k}$ then imply convergence in $d$.
Conversely, if $d(x_n,x)\to0$, then
\[
f_k(x_n-x)\to0
\]
for every $k$.
Given any $f\in X^*$ and $\varepsilon>0$, choose $f_k$ with
\[
\|f-f_k\|<\frac{\varepsilon}{4M}.
\]
Since $x_n,x\in M B_X$,
\[
\begin{aligned}
|f(x_n-x)|
&\le
|f_k(x_n-x)|+
\|f-f_k\|\,\|x_n-x\|\\
&\le
|f_k(x_n-x)|+2M\|f-f_k\|.
\end{aligned}
\]
The first term tends to zero and the second is less than $\varepsilon/2$.
Thus
\[
f(x_n-x)\to0
\]
for every $f\in X^*$, which is weak convergence.
The same density estimate shows directly that the metric and weak neighborhood topologies agree on the bounded ball.

Therefore $M B_X$ is a compact metrizable space in its weak topology, hence sequentially compact.
The bounded sequence $\{x_n\}\subseteq M B_X$ consequently has a weakly convergent subsequence.
:::

<1>2. If every bounded sequence has a subsequence of the stated form, then $A$ is compact.
::: {.proof}
Let $\{x_n\}$ be a bounded sequence in $X$.
By hypothesis there are a subsequence $\{x_{n_j}\}$, a vector $\phi\in X$, and vectors $r_{n_j}$ such that
\[
x_{n_j}=\phi+r_{n_j}
\]
and
\[
Ar_{n_j}\longrightarrow0
\qquad\text{in }Y.
\]
By linearity,
\[
Ax_{n_j}=A\phi+Ar_{n_j}\longrightarrow A\phi
\qquad\text{in }Y.
\]
Thus every bounded sequence in $X$ has a subsequence whose image converges in $Y$, which is exactly compactness of $A$.
:::

<1>3. Suppose $A$ is compact and $x_{n_j}\rightharpoonup\phi$ weakly in $X$.
Then every norm-convergent subsequence of $\{Ax_{n_j}\}$ converges to $A\phi$.
::: {.proof}
A bounded linear map is weak-to-weak continuous.
Indeed, for every $y^*\in Y^*$,
\[
y^*(Ax_{n_j})
=(A^*y^*)(x_{n_j})
\longrightarrow
(A^*y^*)(\phi)
=y^*(A\phi).
\]
Hence
\[
Ax_{n_j}\rightharpoonup A\phi
\qquad\text{weakly in }Y.
\]

Now suppose a subsequence satisfies
\[
Ax_{n_{j_k}}\longrightarrow y
\qquad\text{in norm}.
\]
Norm convergence implies weak convergence, so the same subsequence converges weakly to $y$.
The weak topology is Hausdorff, hence weak limits are unique.
Therefore
\[
y=A\phi.
\]
:::

<1>4. If $A$ is compact, then every bounded sequence has a subsequence of the required form.
::: {.proof}
Let $\{x_n\}$ be bounded.
By <1>1, pass to a subsequence, still denoted $\{x_{n_j}\}$, such that
\[
x_{n_j}\rightharpoonup\phi
\qquad\text{for some }\phi\in X.
\]
Since $A$ is compact, the image sequence $\{Ax_{n_j}\}$ has a norm-convergent subsequence.
Pass to that subsubsequence and relabel it again as $\{x_{n_j}\}$.
By <1>3, its image must converge to $A\phi$:
\[
Ax_{n_j}\longrightarrow A\phi.
\]
Define
\[
r_{n_j}=x_{n_j}-\phi.
\]
Then
\[
x_{n_j}=\phi+r_{n_j}
\]
and
\[
Ar_{n_j}
=Ax_{n_j}-A\phi
\longrightarrow0
\qquad\text{in }Y.
\]
This is the required decomposition.
:::

Combining <1>2 and <1>4 proves the equivalence.
:::
