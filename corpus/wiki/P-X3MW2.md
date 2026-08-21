---
schema: qual/card@1
id: P-X3MW2
kind: problem
title: Bessel's inequality and Riesz–Fischer for orthonormal sequences
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - L²
relations: []
review: draft
solved: true
---

Let $\{u_n\}_{n=1}^∞$ be an orthonormal sequence in a Hilbert space $\mathcal{H}$.

a.
Prove that for every $x ∈ \mathcal H$ one has 
\[
\displaystyle\sum_{n=1}^{\infty}\left|\left\langle x, u_{n}\right\rangle\right|^{2} \leq\|x\|^{2}
\]

b.
Prove that for any sequence $\{a_n\}_{n=1}^\infty \in \ell^2(\NN)$ there exists an element $x\in\mathcal H$ such that 
\[
a_n = \inner{x}{u_n} \text{ for all } n\in \NN
\]
and
\[
\norm{x}^2 = \sum_{n=1}^{\infty}\left|\left\langle x, u_{n}\right\rangle\right|^{2}
\]

:::{.concept}
\envlist

- Bessel's Inequality
- Pythagoras
- Surjectivity of the Riesz map
- Parseval's Identity
- Trick -- remember to write out finite sum $S_N$, and consider $\norm{x - S_N}$.
:::

:::{.solution}
\envlist

:::{.proof title="of a"}
\envlist

- Equivalently, we can show
\[
\norm{x}^2 - \sum_{n=1}^\infty \abs{ \inner{x}{u_n} }^2 \geq 0
.\]

- Claim: the LHS is the norm of an element in $H$, and thus non-negative.
  More precisely, set $S_N\da \sum_{n=1}^N \inner{x}{u_n}u_n$, then the above is equal to
  \[
  \norm{x - \lim_{N\to\infty} S_N}^2
  .\]
  Note that if this is true, we're done.

- To see this, expand the norm in terms of inner products:
\[
  \norm{x - S_N}^2
  &= \inner{x-S_N}{x-S_N} \\
  &= \inner{x}{x} - \inner{x}{S_N} - \inner{S_N}{x} + \inner{S_N}{S_N} \\
  &= \norm{x}^2 + \norm{S_N}^2 - \qty{\inner{x}{S_N} + \conjugate{\inner{x}{S_N}} } \\
  &= \norm{x}^2 + \norm{S_N}^2 - 2\Re\qty{\inner x {S_N} } \\
  &= \norm{x}^2 + \norm{S_N}^2 - 2\Re\qty{ \inner{x} {\sum_{n=1}^N \inner{x}{u_n} u_n } } \\
  &= \norm{x}^2 + \norm{S_N}^2 - 2\Re\qty{ \sum_{n=1}^N \inner{x} {\inner{x}{u_n} u_n } } \\
  &= \norm{x}^2 + \norm{S_N}^2 - 2\Re\qty{ \sum_{n=1}^N \conjugate{\inner{x}{u_n} } \inner{x} {u_n } } \\
  &= \norm{x}^2 + \norm{S_N}^2 - 2\Re \sum_{n=1}^N \abs{\inner{x}{u_n} }^2 \\
  &= \norm{x}^2 + \norm{S_N}^2 - 2\sum_{n=1}^N \abs{\inner{x}{u_n} }^2 \\
  &= \norm{x}^2 + \norm{\sum_{n=1}^N \inner{x}{u_n} u_n}^2 - 2\sum_{n=1}^N \abs{\inner{x}{u_n} }^2 \\
  &= \norm{x}^2 + 
  \inner
  {\sum_{n=1}^N \inner{x}{u_n} u_n} 
  {\sum_{m=1}^N \inner{x}{u_m} u_m} 
  - 2\sum_{n=1}^N \abs{\inner{x}{u_n} }^2 \\
  &= \norm{x}^2 + 
  \sum_{n, m \leq N}\inner{x}{u_n} \conjugate{\inner{x}{u_m} }\inner{u_n}{u_m}
  - 2\sum_{n=1}^N \abs{\inner{x}{u_n} }^2 \\
  &= \norm{x}^2 + \sum_{n, m\leq N} \inner{x}{u_n} \conjugate{\inner{x}{u_m}} \delta_{mn}
  - 2\sum_{n=1}^N \abs{\inner{x}{u_n} }^2 \\
  &= \norm{x}^2 + \sum_{n\leq N} \abs{\inner{x}{u_n}}^2
  - 2\sum_{n=1}^N \abs{\inner{x}{u_n} }^2 \\
  &= \norm{x}^2 
  - \sum_{n=1}^N \abs{\inner{x}{u_n} }^2 
.\]

- Now take $\lim_{N\to\infty}$ and use that $\norm{\wait}$ is continuous.
:::


:::{.proof title="of b"}
\envlist

- Set 
\[
x\da \sum_{n\in \NN} a_n u_n
.\]

- Checking the first desired property:
\[
\inner{x}{u_m} &= \inner{ \sum_{n\geq 1} a_n u_n }{u_m} \\
&=\sum_{n\geq 1} a_n  \inner{ u_n }{u_m} \\
&=\sum_{n\geq 1} a_n  \delta_{mn} \\
&= a_m
.\]


- That $x\in H$: this would follow from 
\[
\norm{x}^2 = \sum_n \abs{\inner x {u_n }}^2 = \sum_n \abs{a_n}^2 <\infty
.\]
  The inequality holds by assumption since $\ts{a_n}\in\ell^2$, so it suffices to show the first equality:

\[
\norm{x}^2 &\da \inner{x}{x} \\
&= \inner
{\sum_n a_n u_n}
{\sum_m a_m u_m} \\
&= \sum_{n, m} a_n \conjugate{a_m} \inner{u_n}{u_m} \\
&= \sum_{n, m} a_n \conjugate{a_m} \delta_{mn} \\
&= \sum_{n} a_n \conjugate{a_n} \\
&= \sum_{n} \abs{a_n}^2 \\
&= \sum_n \abs{\inner x {u_n}}^2
.\]
:::


:::
