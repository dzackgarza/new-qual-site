---
schema: qual/card@1
id: P-AXFG7
kind: problem
title: "Let $m_*$ denote the Lebesgue outer measure on \\( \\RR \\)."
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
relations: []
review: draft
---
Let $m_*$ denote the Lebesgue outer measure on \( \RR \).

a.. 
Prove that for every $E\subseteq \RR$ there exists a Borel set $B$ containing $E$ such that
\[
m_*(B) = m_*(E)
.\]

b.. 
Prove that if $E\subseteq \RR$ has the property that
\[
m_*(A) = m_*(A\Intersect E) + m_*(A\Intersect E^c)
\]
for every set $A\subseteq \RR$, then there exists a Borel set $B\subseteq \RR$ such that $E = B\setminus N$ with $m_*(N) = 0$.

Be sure to address the case when $m_*(E) = \infty$.

:::{.concept}
\envlist
- Definition of outer measure: 
  \[ 
  m_*(E) = \inf_{\theset{Q_j} \covers E} \sum \abs {Q_j}
  \] 
  where $\theset{Q_j}$ is a countable collection of closed cubes.
- Break $\RR$ into $\disjoint_{n\in \ZZ} [n, n+1)$, each with finite measure.
- Theorem: $m_*(Q) = \abs{Q}$ for $Q$ a closed cube (i.e. the outer measure equals the volume).
:::

:::{.solution}
\envlist

:::{.proof}
\envlist
- $m_*(Q) \leq \abs{Q}$:
- Since $Q\subseteq Q$, $Q\covers Q$ and $m_*(Q) \leq \abs{Q}$ since $m_*$ is an infimum over such coverings.
- $\abs{Q} \leq m_*(Q)$:
- Fix $\eps > 0$.
- Let $\theset{Q_i}_{i=1}^\infty \covers Q$ be arbitrary, it suffices to show that 
    $$\abs{Q} \leq \qty{\sum_{i=1}^\infty \abs{Q_i}} + \eps.$$
-  Pick open cubes $S_i$ such that $Q_i\subseteq S_i$ and $\abs{Q_i} \leq \abs{S_i} \leq (1+\eps)\abs{Q_i}$.
- Then $\theset{S_i} \covers Q$, so by compactness of $Q$ pick a finite subcover with $N$ elements.

- Note 
\[
Q \subseteq \Union_{i=1}^N S_i \implies \abs{Q} \leq \sum_{i=1}^N \abs{S_i} \leq \sum_{i=1}^N (1+\eps) \abs{Q_j} \leq (1+\eps)\sum_{i=1}^\infty \abs{Q_i } 
.\]
- Taking an infimum over coverings on the RHS preserves the inequality, so 
  $$\abs{Q} \leq (1+\eps) m_*(Q)$$
- Take $\eps\to 0$ to obtain final inequality.
:::

a.

- If $m_*(E) = \infty$, then take $B = \RR^n$ since $m(\RR^n) = \infty$.
- Suppose $N \definedas m_*(E) < \infty$.

- Since $m_*(E)$ is an infimum, by definition, for every $\eps> 0$ there exists a covering by closed cubes $\theset{Q_i(\eps)}_{i=1}^\infty \covers E$ depending on $\eps$ such that 
$$
\sum_{i=1}^\infty \abs{Q_i(\eps)} < N + \eps
.$$

- For each fixed $n$, set $\eps_n = {1\over n}$ to produce such a covering $\theset{Q_i(\eps_n)}_{i=1}^\infty$ and set $B_n \definedas \Union_{i=1}^\infty Q_i(\eps_n)$.

- The outer measure of cubes is *equal* to the sum of their volumes, so 
\[
m_*(B_n) = \sum_{i=1}^\infty \abs{Q_i(\eps_n)} < N + \eps_n = N + {1\over n}
.\]

- Now set $B \definedas \Intersect_{n=1}^\infty B_n$.

  - Since $E\subseteq B_n$ for every $n$, $E\subseteq B$
  - Since $B$ is a countable intersection of countable unions of closed sets, $B$ is Borel.
  - Since $B_n \subseteq B$ for every $n$, we can apply subadditivity to obtain the inequality
  \[
  E \subseteq B \subseteq B_n \implies
  N \leq m_*(B) \leq m_*(B_n) < N + {1\over n} \qtext{for all} n\in \ZZ^{\geq 1}
  .\]

- This forces $m_*(E) = m_*(B)$.


b.

Suppose $m_*(E) < \infty$.

- By (a), find a Borel set $B\supseteq E$ such that $m_*(B) = m_*(E)$
- Note that $E\subseteq B \implies B\Intersect E = E$ and $B\Intersect E^c = B\setminus E$.
- By assumption, 
\[
m_*(B) &= m_*(B\Intersect E) + m_*(B\Intersect E^c) \\
m_*(E) &= m_*(E) + m_*(B\setminus E) \\ 
m_*(E) - m_*(E) &= m_*(B\setminus E) \qquad\qquad\text{since } m_*(E) < \infty \\ 
\implies m_*(B\setminus E) &= 0
.\]
- So take $N = B\setminus E$; this shows $m_*(N) = 0$ and $E = B\setminus (B\setminus E) = B\setminus N$.


If $m_*(E) = \infty$:

- Apply result to $E_R\definedas E \Intersect [R, R+1)^n \subset \RR^n$ for $R\in \ZZ$, so $E = \disjoint_R E_R$
- Obtain $B_R, N_R$ such that $E_R = B_R \setminus N_R$, $m_*(E_R) = m_*(B_R)$, and $m_*(N_R) = 0$.
- Note that
  -   $B\definedas \Union_R B_R$ is a union of Borel sets and thus still Borel
  -  $E = \Union_R E_R$
  - $N\definedas B\setminus E$
  - $N' \definedas \Union_R N_R$ is a union of null sets and thus still null
- Since $E_R \subset B_R$ for every $R$, we have $E\subset B$
- We can compute
\[
N = B\setminus E = \qty{ \Union_R B_R } \setminus \qty{\Union_R E_R } \subseteq \Union_R \qty{B_R\setminus E_R} = \Union_R N_R \definedas N'
\]
where $m_*(N') = 0$ since $N'$ is null, and thus subadditivity forces $m_*(N) = 0$.
:::
