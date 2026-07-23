---
schema: qual/card@1
id: P-CFMLS
kind: problem
title: "Define"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Define
$$
E:=\left\{x \in \mathbb{R}:\left|x-\frac{p}{q}\right|<q^{-3} \text { for infinitely many } p, q \in \mathbb{N}\right\}.
$$

Prove that $m(E) = 0$.

:::{.concept}
\envlist
- Borel-Cantelli: If $\theset{E_k}_{k\in\ZZ}\subset 2^\RR$ is a countable collection of Lebesgue measurable sets with $\sum_{k\in \ZZ} m(E_k) < \infty$, then almost every $x\in \RR$ is in *at most finitely* many $E_k$.
  - Equivalently (?), $m(\limsup_{k\to\infty} E_k) = 0$, where $\limsup_{k\to\infty} E_k = \Intersect_{k=1}^\infty \Union_{j\geq k} E_j$, the elements which are in $E_k$ for infinitely many $k$.
:::

:::{.solution}
\envlist

- Strategy: Borel-Cantelli.

- We'll show that $m(E) \Intersect [n, n+1] = 0$ for all $n\in \ZZ$; then the result follows from 
\[
m(E) = m \qty{\Union_{n\in \ZZ} E \Intersect [n, n+1]} \leq \sum_{n=1}^\infty m(E \Intersect [n, n+1]) = 0
.\]

- By translation invariance of measure, it suffices to show $m(E \Intersect [0, 1]) = 0$.
  - So WLOG, replace $E$ with $E\Intersect [0, 1]$.

- Define
\[
E_j \definedas \theset{x\in [0, 1] \suchthat \
\exists p\in \ZZ^{\geq 0} \text{ s.t. } \abs{x - \frac{p}{j} } < \frac 1 {j^3}} 
.\]

  - Note that $E_j \subseteq \disjoint_{p\in \ZZ^{\geq 0}} B_{j^{-3}}\qty{p\over j}$, i.e. a union over integers $p$ of intervals of radius $1/j^3$ around the points $p/j$.
    Since $1/j^3 < 1/j$, this union is in fact disjoint.

- Importantly, note that 
  \[
\limsup_{j\to\infty} E_j \definedas \Intersect_{n=1}^\infty \Union_{j=n}^\infty E_j = E
  \]
  
  since 
  
  \[
  x \in \limsup_j E_j 
  &\iff x \in E_j \text{ for infinitely many } j  \\
  &\iff \text{ there are infinitely many $j$ for which there exist a $p$ such that } \abs{x - {p\over j}} < j^{-3}  \\
  &\iff \text{ there are infinitely many such pairs $p, j$}  \\
  &\iff x\in E
  .\]

- Intersecting with $[0, 1]$, we can write $E_j$ as a union of intervals:
\[
E_j =& \qty{0, {j^{-3}}} 
\quad \disjoint \quad 
B_{j^{-3}}\qty{1\over j} \disjoint
B_{j^{-3}}\qty{2\over j} \disjoint
\cdots \disjoint
B_{j^{-3}}\qty{j-1\over j} 
\quad \disjoint \quad 
(1 - {j^{-3}}, 1)
,\]
  where we've separated out the "boundary" terms to emphasize that they are balls about $0$ and $1$ intersected with $[0, 1]$.


- Since $E_j$ is a union of open sets, it is Borel and thus Lebesgue measurable.

- Computing the measure of $E_j$:

  - For a fixed $j$, there are exactly $j+1$ possible choices for a numerator ($0, 1, \cdots, j$), thus there are exactly $j+1$ sets appearing in the above decomposition.

  - The first and last intervals are length $1 \over j^3$ 
  - The remaining $(j+1)-2 = j-1$ intervals are twice this length, $2 \over j^3$
  - Thus
  $$
  m(E_j) = 2 \qty{1 \over j^3} + (j-1) \qty{2 \over j^3} = {2 \over j^2}
  $$

- Note that 
\[
\sum_{j\in \NN} m(E_j) =  2\sum_{j\in \NN} \frac 1 {j^2} < \infty
,\]
  which converges by the $p\dash$test for sums.
  
- But then
\[
m(E) 
&= m(\limsup_j E_j) \\
&= m(\Intersect_{n\in \NN} \Union_{j\geq n} E_j) \\
&\leq m(\Union_{j\geq N} E_j) \quad\text{for every } N \\
&\leq \sum_{j\geq N} m(E_j) \\
&\converges{N\to\infty}\to 0 \quad\text{}
.\]

- Thus $E$ is measurable as a subset of a null set and $m(E) = 0$.
:::

