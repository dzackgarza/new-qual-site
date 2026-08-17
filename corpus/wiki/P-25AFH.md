---
schema: qual/card@1
id: P-25AFH
kind: problem
title: "Let $\\mu$ be a measure on a measurable space $(X, \\mathcal M)$ and $f$\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - radon-nikodym
  - measure-theory
  - integrals
relations: []
review: draft
solved: true
---
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

:::{.concept}
\envlist
- Absolute continuity of measures: $\lambda \ll \mu \iff E\in\mathcal{M}, \mu(E) = 0 \implies \lambda(E) = 0$.
- Radon-Nikodym: if $\lambda \ll \mu$, then there exists a measurable function $\dd{\lambda}{\mu} \definedas f$ where $\lambda(E) = \int_E f \,d\mu$.
- Chebyshev's inequality:
\[  
A_c \definedas \theset{ x\in X \suchthat \abs{f(x)} \geq c  } \implies \mu(A_c) \leq c^{-p} \int_{A_c} \abs{f}^p \,d\mu \quad \forall 0 < p < \infty
.\]
:::

:::{.solution}
\envlist

a.

- Strategy: use approximation by simple functions to show absolute continuity and apply Radon-Nikodym 

- Claim: $\lambda \ll \mu$, i.e. $\mu(E) = 0 \implies \lambda(E) = 0$.

  - Note that if this holds, by Radon-Nikodym, $f = \dd{\lambda}{\mu} \implies d\lambda = f d\mu$, which would yield 
  \[  
  \int g ~d\lambda = \int g f ~d\mu
  .\]

- So let $E$ be measurable and suppose $\mu(E) = 0$.

- Then
\[
\lambda(E) \definedas \int_E f ~d\mu 
&= \lim_{n\to\infty} \theset{\int_E s_n \,d\mu \suchthat s_n \definedas \sum_{j=1}^\infty c_j \mu(E_j),\, s_n \nearrow f}
\]
  where we take a sequence of simple functions increasing to $f$.

- But since each $E_j \subseteq E$, we must have $\mu(E_j) = 0$ for any such $E_j$, so every such $s_n$ must be zero and thus $\lambda(E) = 0$.

:::{.remark}
What is the final step in this approximation?
:::

b.

- Set $g(x) = x^2$, note that $g$ is positive and measurable.
- By part (a), there exists a positive $f$ such that for any $E\subseteq \RR$,
\[
\int_E g ~dm = \int_E gf ~d\mu 
\]

  - The LHS is zero by assumption and thus so is the RHS.

  - $m \ll \mu$ by construction.

  - Note that $gf$ is positive.

- Define $A_k = \theset{x\in X \suchthat gf \cdot \chi_E > {1 \over k} }$, for $k\in \ZZ^{\geq 0}$

- Then by Chebyshev with $p=1$, for every $k$ we have

\[
\mu(A_k) \leq k \int_E gf ~d\mu = 0
\]

- Then noting that $A_k \searrow A \definedas \theset{x\in X \suchthat gf\cdot \chi_E(x)  > 0}$, we have $\mu(A) = 0$.

- Since $gf$ is positive, we have 
\[
x\in E \iff gf\chi_E(x) > 0 \iff x\in A
\]
  so $E = A$ and $\mu(E) = \mu(A)$.

- But $m \ll \mu$ and $\mu(E) = 0$, so we can conclude that $m(E) = 0$.
:::

