---
schema: qual/card@1
id: P-RAF22B
kind: problem
title: "In L^p on a finite measure space, pointwise convergence gives: norm convergence iff norms converge"
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Pointwise Convergence
  - Vitali Convergence Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the official UCSD Fall 2022 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $(X, \mathcal{M}, \mu)$ be a measure space with $\mu(X) < \infty$.
Let $1 \leq p < \infty$, let $f, f_n \in L^p(X, \mu)$ for $n \in \mathbb{N}$, and assume that $f_n \to f$ pointwise $\mu$-almost-everywhere.
Prove that $\|f_n - f\|_p \to 0$ if and only if $\|f_n\|_p \to \|f\|_p$.

(Note: You are not allowed to use the generalized Dominated Convergence Theorem unless you prove it.)
:::

::: solution
<1>1. Prove the easy implication.
::: proof
If
\[
\|f_n-f\|_p\to0,
\]
then the reverse triangle inequality gives
\[
\bigl|\|f_n\|_p-\|f\|_p\bigr|
\le\|f_n-f\|_p\to0.
\]
Hence
\[
\|f_n\|_p\to\|f\|_p.
\]
:::

<1>2. Show that the $p$th powers converge in $L^1$.
::: proof
Assume now that
\[
\|f_n\|_p\to\|f\|_p.
\]
Set
\[
g_n:=|f_n|^p,
\qquad
g:=|f|^p.
\]
Then $g_n\to g$ almost everywhere and
\[
\int_Xg_n\,d\mu=\|f_n\|_p^p
\longrightarrow
\|f\|_p^p=\int_Xg\,d\mu.
\]

Moreover,
\[
\min(g_n,g)\to g
\]
almost everywhere and $0\le\min(g_n,g)\le g\in L^1$. By the ordinary dominated convergence theorem,
\[
\int_X\min(g_n,g)\,d\mu\to\int_Xg\,d\mu.
\]
Since
\[
|g_n-g|=g_n+g-2\min(g_n,g),
\]
we obtain
\[
\boxed{\|g_n-g\|_1\to0.}
\]
:::

<1>3. Deduce uniform integrability of the difference powers.
::: proof
Convergence $g_n\to g$ in $L^1$ implies that the family $\{g_n:n\ge1\}$ is uniformly integrable. Indeed, given $\varepsilon>0$, first choose $N$ so that
\[
\|g_n-g\|_1<\varepsilon/4
\]
for $n\ge N$. By absolute continuity of the integrals of $g,g_1,\ldots,g_{N-1}$, there exists $\delta>0$ such that $\mu(E)<\delta$ implies
\[
\int_E g<\varepsilon/4
\]
and
\[
\int_E g_n<\varepsilon/2
\qquad(n<N).
\]
For $n\ge N$,
\[
\int_Eg_n
\le\|g_n-g\|_1+\int_Eg
<\varepsilon/2.
\]

Now put
\[
h_n:=|f_n-f|^p.
\]
The elementary inequality
\[
h_n\le2^{p-1}(g_n+g)
\]
shows that $(h_n)$ is uniformly integrable as well.
:::

<1>4. Combine Egorov with uniform integrability.
::: proof
We have $h_n\to0$ almost everywhere. Fix $\varepsilon>0$. By uniform integrability, choose $\delta>0$ such that
\[
\mu(E)<\delta
\quad\Longrightarrow\quad
\sup_n\int_Eh_n\,d\mu<\frac\varepsilon2.
\]
Because $\mu(X)<\infty$, Egorov's theorem gives a measurable $E\subset X$ with $\mu(E)<\delta$ such that $h_n\to0$ uniformly on $X\setminus E$. Hence, for all sufficiently large $n$,
\[
\int_{X\setminus E}h_n\,d\mu
\le \mu(X)\sup_{X\setminus E}h_n
<\frac\varepsilon2.
\]
Therefore
\[
\int_X|f_n-f|^p\,d\mu
=\int_Xh_n\,d\mu
<\varepsilon
\]
for all sufficiently large $n$. Thus
\[
\boxed{\|f_n-f\|_p\to0.}
\]
:::
:::
