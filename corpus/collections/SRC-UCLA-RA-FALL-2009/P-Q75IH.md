---
schema: qual/card@1
id: P-Q75IH
kind: problem
title: The symmetric derivative of a singular measure vanishes Lebesgue-a.e.
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against problem 4 of the UCLA Analysis Qualifying Exam, Fall 2009, from the collection provenance PDF.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Replaced the previous invocation of a differentiation theorem for the
    auxiliary measure mu+m by a direct proof. A centered weak maximal inequality
    controls a small-mass remainder after compact approximation of the singular
    support, forcing the upper symmetric density to vanish Lebesgue-a.e.
---

::: {.problem}
Prove the following variant of the Lebesgue differentiation theorem: Let $\mu$ be a finite Borel measure on $\mathbb{R}$, singular with respect to Lebesgue measure.
Then for Lebesgue almost every $x\in\mathbb{R}$, $$\lim_{\epsilon\to 0} \frac{\mu([x-\epsilon,x+\epsilon])}{2\epsilon} = 0.$$
:::

::: {.solution}
Let $m$ denote Lebesgue measure.
For a finite positive Borel measure $\nu$ on $\mathbb R$, define its centered maximal function by
\[
M\nu(x)
=\sup_{r>0}\frac{\nu([x-r,x+r])}{2r}.
\]

<1>1. For every finite positive Borel measure $\nu$ and every $t>0$,
\[
m\{x:M\nu(x)>t\}
\le\frac{3\nu(\mathbb R)}{t}.
\]
::: {.proof}
Let
\[
E_t=\{x:M\nu(x)>t\}.
\]
This set is open.
Indeed, if $x\in E_t$, choose $r>0$ with
\[
\nu([x-r,x+r])>2tr.
\]
For all $y$ sufficiently close to $x$, the interval
\[
[x-r,x+r]
\]
is contained in
\[
[y-(r+|x-y|),y+(r+|x-y|)],
\]
and the strict inequality persists after the arbitrarily small increase of the denominator.
Hence $M\nu(y)>t$ for all $y$ near $x$.

It suffices, by inner regularity of Lebesgue measure, to prove the same bound for every compact set $F\subseteq E_t$.

For each $x\in F$, choose $r_x>0$ such that
\[
\nu([x-r_x,x+r_x])>2tr_x.
\]
Enlarging $r_x$ slightly if necessary, choose an open interval $I_x$ centered at $x$ such that
\[
\nu(I_x)>t|I_x|.
\]
The intervals $(I_x)_{x\in F}$ form an open cover of $F$, so compactness gives a finite subcover.

From this finite family choose a disjoint subfamily $I_1,\ldots,I_N$ by repeatedly taking an interval of maximal length and discarding all intervals that meet it.
Every discarded interval $J$ meets some selected $I_j$ with
\[
|J|\le|I_j|.
\]
Hence $J$ is contained in the concentric interval $3I_j$ of three times the length.
Therefore
\[
F\subseteq\bigcup_{j=1}^N3I_j.
\]
It follows that
\[
\begin{aligned}
m(F)
&\le3\sum_{j=1}^N|I_j|\\
&<\frac3t\sum_{j=1}^N\nu(I_j)\\
&\le\frac{3\nu(\mathbb R)}t,
\end{aligned}
\]
because the selected intervals are disjoint.
Taking the supremum over compact $F\subseteq E_t$ proves the claim.
:::

<1>2. Since $\mu\perp m$, there is a Borel set $N\subseteq\mathbb R$ such that
\[
m(N)=0
\qquad\text{and}\qquad
\mu(\mathbb R\setminus N)=0.
\]
For every $\delta>0$, there is a compact set $K\subseteq N$ such that
\[
\mu(\mathbb R\setminus K)<\delta.
\]
::: {.proof}
The first assertion is the definition of singularity of $\mu$ with respect to Lebesgue measure.

A finite Borel measure on $\mathbb R$ is regular, so it is inner regular on the Borel set $N$.
Thus, for every $\delta>0$, there is compact $K\subseteq N$ with
\[
\mu(N\setminus K)<\delta.
\]
Since $\mu(\mathbb R\setminus N)=0$,
\[
\mu(\mathbb R\setminus K)
=\mu(N\setminus K)
<\delta.
\]
:::

<1>3. Define the upper symmetric density
\[
D^*\mu(x)
=\limsup_{r\downarrow0}
\frac{\mu([x-r,x+r])}{2r}.
\]
For every $t>0$ and every $\delta>0$,
\[
m\{x:D^*\mu(x)>t\}
\le\frac{3\delta}{t}.
\]
::: {.proof}
Choose $K$ as in <1>2 and decompose
\[
\mu=\mu_K+\nu,
\]
where
\[
\mu_K(A)=\mu(A\cap K)
\qquad\text{and}\qquad
\nu(A)=\mu(A\setminus K).
\]
Then
\[
\nu(\mathbb R)=\mu(\mathbb R\setminus K)<\delta.
\]

If $x\notin K$, compactness of $K$ gives
\[
d(x,K)>0.
\]
Thus for all sufficiently small $r$,
\[
[x-r,x+r]\cap K=\varnothing,
\]
and hence
\[
\mu([x-r,x+r])
=\nu([x-r,x+r]).
\]
Consequently, if $x\notin K$ and $D^*\mu(x)>t$, then
\[
M\nu(x)>t.
\]
Therefore
\[
\{D^*\mu>t\}
\subseteq
K\cup\{M\nu>t\}.
\]
Since $K\subseteq N$ and $m(N)=0$, we have $m(K)=0$.
Applying <1>1 to $\nu$ gives
\[
m\{D^*\mu>t\}
\le
\frac{3\nu(\mathbb R)}t
<\frac{3\delta}t.
\]
:::

<1>4. For every $t>0$,
\[
m\{x:D^*\mu(x)>t\}=0.
\]
::: {.proof}
The estimate in <1>3 holds for every $\delta>0$.
Letting $\delta\downarrow0$ forces the measure of the set to be zero.
:::

<1>5. One has
\[
D^*\mu(x)=0
\]
for Lebesgue almost every $x$.
::: {.proof}
Since $D^*\mu\ge0$,
\[
\{D^*\mu>0\}
=\bigcup_{j=1}^\infty\{D^*\mu>1/j\}.
\]
Each set on the right has Lebesgue measure zero by <1>4, so their countable union has measure zero.
:::

<1>6. Therefore, for Lebesgue almost every $x\in\mathbb R$,
\[
\boxed{
\lim_{\epsilon\to0}
\frac{\mu([x-\epsilon,x+\epsilon])}{2\epsilon}
=0.}
\]
::: {.proof}
For almost every $x$, <1>5 gives
\[
\limsup_{\epsilon\downarrow0}
\frac{\mu([x-\epsilon,x+\epsilon])}{2\epsilon}=0.
\]
The quotient is nonnegative, so its liminf is at least $0$.
Hence the limsup and liminf are both $0$, and the limit exists and equals $0$.
:::
:::
