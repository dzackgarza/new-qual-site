---
schema: qual/card@1
id: P-25AFH
kind: problem
title: Integration against $f\,d\mu$, and $\int_E x^2\,dm=0$ implies $m(E)=0$
classification:
  areas:
  - real-analysis
  topics:
  - Radon-Nikodym
  - Measure Theory
  - Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Problem 2 of the UGA Spring 2017 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Replaced the incomplete Radon-Nikodym detour by the direct simple-function approximation and level-set proofs.
---

::: {.problem}
a. 
Let $\mu$ be a measure on a measurable space $(X, \mathcal M)$ and $f$ a positive measurable function.
  
  Define a measure $\lambda$ by
\[
\lambda(E):=\int_{E} f ~d \mu, \quad E \in \mathcal{M}
\]

Show that for $g$ any positive measurable function, 
\[
\int_{X} g ~d \lambda=\int_{X} f g ~d \mu
\]

b. 
Let $E \subset \RR$ be a measurable set such that 
\[
\int_{E} x^{2} ~d m=0.
\]
Show that $m(E) = 0$.
:::

::: {.concept}
\envlist
- Absolute continuity of measures: $\lambda \ll \mu \iff E\in\mathcal{M}, \mu(E) = 0 \implies \lambda(E) = 0$.
- Radon-Nikodym: if $\lambda \ll \mu$, then there exists a measurable function $\dd{\lambda}{\mu} \definedas f$ where $\lambda(E) = \int_E f \,d\mu$.
- Chebyshev's inequality:
\[  
A_c \definedas \theset{ x\in X \suchthat \abs{f(x)} \geq c  } \implies \mu(A_c) \leq c^{-p} \int_{A_c} \abs{f}^p \,d\mu \quad \forall 0 < p < \infty
.\]
:::

::: {.solution}
<1>1. Prove the integration formula for indicator functions and simple functions.
::: {.proof}
For every measurable $E\subseteq X$, the definition of $\lambda$ gives
\[
\int_X \mathbf1_E\,d\lambda
=\lambda(E)
=\int_E f\,d\mu
=\int_X f\mathbf1_E\,d\mu.
\]
Therefore, if
\[
s=\sum_{j=1}^N a_j\mathbf1_{E_j}
\qquad(a_j\ge0),
\]
then linearity of the integral yields
\[
\int_X s\,d\lambda
=\sum_{j=1}^N a_j\lambda(E_j)
=\int_X fs\,d\mu.
\]
:::

<1>2. Pass to an arbitrary positive measurable $g$.
::: {.proof}
Choose nonnegative simple functions $s_n$ with
\[
s_n\uparrow g.
\]
Then
\[
fs_n\uparrow fg.
\]
Applying the Monotone Convergence Theorem first with respect to $\lambda$ and then with respect to $\mu$ gives
\[
\begin{aligned}
\int_X g\,d\lambda
&=\lim_{n\to\infty}\int_X s_n\,d\lambda\\
&=\lim_{n\to\infty}\int_X fs_n\,d\mu\\
&=\int_X fg\,d\mu.
\end{aligned}
\]
Thus
\[
\boxed{\int_X g\,d\lambda=\int_X fg\,d\mu.}
\]
:::

<1>3. Prove part (b) by level sets away from the unique zero of $x^2$.
::: {.proof}
For $n\ge1$, set
\[
E_n:=E\cap\{|x|\ge1/n\}.
\]
On $E_n$ one has $x^2\ge n^{-2}$, hence
\[
0=\int_E x^2\,dm
\ge \int_{E_n}x^2\,dm
\ge \frac1{n^2}m(E_n).
\]
Therefore $m(E_n)=0$ for every $n$.

Every nonzero point of $E$ belongs to some $E_n$, so
\[
E\subseteq \{0\}\cup\bigcup_{n=1}^\infty E_n.
\]
The singleton $\{0\}$ has Lebesgue measure zero, as does each $E_n$. Hence
\[
\boxed{m(E)=0.}
\]
:::
:::
