---
schema: qual/card@1
id: P-TNOTE
kind: problem
title: Spring 2021, 1
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Measure Theory
  - Borel-Cantelli
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Problem 1 of the official UGA January 2021 Analysis qualifying examination DOCX.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Replaced the legacy pointwise-convergence argument, which incorrectly fixed one N uniformly over all epsilon, by the exact eventual-membership characterization for indicator functions.
---

::: {.problem}
Let \( (X, \mathcal{M},\mu)  \) be a measure space and let $E_n \in \mathcal{M}$ be a measurable set for $n\geq 1$.
Let $f_n \da \chi_{E_n}$ be the indicator function of the set $E_n$ and show that 

a. $f_n \converges{n\to\infty}\to 1$ uniformly \( \iff \) there exists $N\in \NN$ such that $E_n = X$ for all $n\geq N$.

b. $f_n(x) \converges{n\to\infty}\to 1$ for almost every $x$ \( \iff \) 
\[
\mu \qty{ \Intersect_{n \geq 0} \Union_{k \geq n} (X \sm E_k) } = 0
.\]
:::

::: {.solution}
<1>1. Uniform convergence is equivalent to eventual equality $E_n=X$.
::: {.proof}
If $\chi_{E_n}\to1$ uniformly, take $\varepsilon=1/2$. For all sufficiently large $n$ and every $x\in X$,
\[
|\chi_{E_n}(x)-1|<\frac12.
\]
Since $\chi_{E_n}(x)$ is either $0$ or $1$, this forces $\chi_{E_n}(x)=1$ for every $x$, hence $E_n=X$.

Conversely, if $E_n=X$ for every $n\ge N$, then $\chi_{E_n}\equiv1$ for $n\ge N$, so the convergence is uniform.
:::

<1>2. Identify the exceptional set for pointwise convergence.
::: {.proof}
For a fixed $x\in X$, because the values are only $0$ and $1$,
\[
\chi_{E_n}(x)\to1
\iff
x\in E_n\text{ for all sufficiently large }n.
\]
Thus convergence fails exactly when $x\notin E_n$ for infinitely many $n$. The set of such points is
\[
\limsup_{n\to\infty}(X\setminus E_n)
=\bigcap_{N=1}^\infty\bigcup_{k\ge N}(X\setminus E_k).
\]
Therefore $\chi_{E_n}(x)\to1$ for almost every $x$ if and only if
\[
\mu\left(\bigcap_{N=1}^\infty\bigcup_{k\ge N}(X\setminus E_k)\right)=0.
\]
:::
:::
