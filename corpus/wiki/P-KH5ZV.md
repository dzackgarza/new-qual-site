---
schema: qual/card@1
id: P-KH5ZV
kind: problem
title: Absolute continuity of $\int_E|f|$ for $f\in L^1(\RR)$
classification:
  areas:
  - real-analysis
  topics:
  - Continuity of Measure
  - L¹
  - Measure Theory
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
Let $f\in L^1(\RR)$. Show that
\[
\forall\varepsilon > 0 \exists \delta > 0 \text{ such that } \qquad 
m(E) < \delta 
\implies 
\int _{E} |f(x)| \, dx < \varepsilon
\]

:::

:::{.solution title="by contradiction" }

- Note that if $m(E) = 0$ then $\int_E f = 0$ for any $f$.
- Toward a contradiction, suppose there exists an $\eps>0$ such that for all $\delta>0$ there exists a set $E_\delta \subseteq \RR$ with $m(E) < \delta$ but $\int_{E_\delta} \abs f > \eps$.
- Let $\delta_n \decreasesto 0$ be any sequence converging to zero and choose $E_n$ with $\int_{E_n} \abs f > \eps$ for every $n$.
- Define $E \da \limsup_n E_n \da \Intersect_{N\geq 1} \Union_{n\geq N} E_n$, then $m(E) = 0$ by Borel-Cantelli.
- Now estimate using Fatou:
\[
\int_{E} \abs{f} 
&= \int_X \chi_E \abs{f} \\
&= \int_X \limsup_n \chi_{E_n} \abs{f} \\
&\geq \limsup_n \int_X \chi_{E_n }\abs{f}  \\
&\geq \limsup_n \int_{E_n} \abs{f} \\
&\geq \limsup_n \eps \\
&= \eps
,\]
however $\displaystyle\int_E \abs{f}\dm = 0$ since $m(E) = 0$, a contradiction. $\contradiction$.
:::

:::{.solution title="direct" }
Note that this is clear for simple functions: let $\phi = \sum_{k\leq n} c_k m(A_k) < \infty$ be simple function. then $\phi$ is necessarily bounded on $\RR$, so let $M\da \sup_\RR \phi$ and estimate
\[
\int_E \phi 
&\da \sum_k c_k m(A_k \intersect E) \\
&\leq \sum_k M\cdot m(E)\\ 
&= C M m(E) 
,\]
for some constant $C$, so choosing $\delta < { \eps \over C M}$ (and its corresponding $E$ with $m(E) < \delta$) bounds this above by $\eps$.

For arbitrary $f \in L^1$, there is a sequence of simple functions $\phi_n$ with $\int \phi_n \increasesto \int f$ and $\norm{\phi_n - f}_{L_1} \convergesto{n\to\infty} 0$.
Choose $\delta$ and $E$ as above,
and use the triangle inequality to estimate
\[
\int_E \abs{f} 
&= \int_E \abs{f - \phi_n + \phi_n} \\
&\leq \int_E \abs{f - \phi_n} + \int_E \abs{\phi_n}
,\]
choose $n\gg 1$ to bound the first term by $\eps$, noting that the second term is bounded by $\eps$ by the case for simple functions.


:::

