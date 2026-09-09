---
schema: qual/card@1
id: P-KGSPZ
kind: problem
title: $\lim_n\int f^n$ is $\infty$ or $\mu(f^{-1}(1))$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the recorded UGA Spring 2014 real-analysis exam source. The prior solution contained contradictory dominated-convergence prose despite the finite-measure hypothesis.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $(X, \mathcal M, \mu)$ be a finite measure space and suppose $f$ is a non-negative measurable function on $X$.
Show that
$$
\lim _{n \rightarrow \infty} \int_{X} f^{n} ~d \mu =
\begin{cases}
\infty & \text{or} \\
\mu(f\inv(1)),
\end{cases}
$$
and characterize the collection of functions of each type.
:::

::: solution
<1>1. If $\mu\{f>1\}>0$, the integrals diverge to infinity.
::: proof
Let
\[
B:=\{x\in X:f(x)>1\}.
\]
Since
\[
B=\bigcup_{k=1}^\infty\{f\ge1+1/k\},
\]
positive measure of $B$ implies that for some $k$,
\[
C:=\{f\ge1+1/k\}
\]
has positive measure. Then
\[
\int_X f^n\,d\mu
\ge \int_C f^n\,d\mu
\ge (1+1/k)^n\mu(C)\longrightarrow\infty.
\]
:::

<1>2. If $f\le1$ almost everywhere, identify the finite limit.
::: proof
Assume
\[
\mu\{f>1\}=0.
\]
Then $0\le f\le1$ almost everywhere. Pointwise,
\[
f^n(x)\longrightarrow \mathbf1_{\{f=1\}}(x).
\]
Moreover,
\[
0\le f^n\le1,
\]
and the constant function $1$ is integrable because $\mu(X)<\infty$. By the Dominated Convergence Theorem,
\[
\lim_{n\to\infty}\int_X f^n\,d\mu
=\int_X\mathbf1_{\{f=1\}}\,d\mu
=\mu(f^{-1}(1)).
\]
:::

<1>3. State the exact dichotomy.
::: proof
Combining the two cases,
\[
\boxed{
\lim_{n\to\infty}\int_Xf^n\,d\mu
=\begin{cases}
\infty,&\mu\{f>1\}>0,\\[1ex]
\mu\{f=1\},&f\le1\text{ a.e.}
\end{cases}}
\]
Thus the first type consists exactly of the nonnegative measurable functions exceeding $1$ on a set of positive measure; the second type consists exactly of those satisfying $f\le1$ almost everywhere.
:::
:::
