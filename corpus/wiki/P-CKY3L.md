---
schema: qual/card@1
id: P-CKY3L
kind: problem
title: Density of the span of interval indicators in $L^1(\RR)$
classification:
  areas:
  - real-analysis
  topics:
  - density
  - l1
relations: []
review: draft
solved: true
---
Let 
$$
S = \spanof_\CC\theset{\chi_{(a, b)} \suchthat a, b \in \RR},
$$
the complex linear span of characteristic functions of intervals of the form $(a, b)$.

Show that for every $f\in L^1(\RR)$, there exists a sequence of functions $\theset{f_n} \subset S$ such that 
\[
\lim _{n \rightarrow \infty}\left\|f_{n}-f\right\|_{1}=0
\]

:::{.concept}
\envlist
- From homework: $E$ is Lebesgue measurable iff there exists a finite union of closed cubes $A$ such that $m(E\Delta A) < \varepsilon$.
:::

:::{.solution}
\envlist

- Idea: first show this for characteristic functions, then simple functions, then for arbitrary $f$.

- For characteristic functions:
  - Consider $\chi_{A}$ for $A$ a measurable set.
  - By regularity of the Lebesgue measure, for every $\eps>0$ we can find an $I_\eps$ such that $m(A\Delta I_\eps)< \eps$ where $I_\eps$ is a finite disjoint union of intervals.
  - Then use
  \[
  \eps > m(A\Delta I\eps) = \int_X \abs{\chi_A - \chi_{I_\eps}}
  ,\]
  so the $\chi_{I_\eps}$ converge to $\chi_A$ in $L_1$.

  - Then just note that $\chi_{I_\eps} = \sum_{j\leq N} \chi_{I_j}$ where $I_\eps = \Disjoint_{j\leq N} I_j$, so $\chi_{I_\eps} \in S$.


- For simple functions:
  - Let $\psi = \sum_{k\leq N} c_k \chi_{E_k}$.
  - By the argument above, for each $k$ we can find $I_{\eps, k}$ such that $\chi_{I_{\eps, k}}$ converges to $\chi_{E_k}$ in $L^1$. 
  - So defining $\psi_\eps = \sum_{k\leq N} c_k \chi_{I_{\eps, k}}$, the claim is that this will converge to $\phi$ in $L_1$.
  - Note that 
  \[
  \psi_\eps = \sum_k c_k \chi_{I_{\eps, k}} 
  = \sum_k c_k \sum_j \chi_{I_{j, k} }
  = \sum_{k, j} c_k \chi_{ I_{j, k} } \in S
  \]
  since now the $I_{j, k}$ are indicators of intervals.
  - Moreover
  \[
  \norm{\psi_\eps - \psi} 
  = \norm{ \sum_k c_k \qty{ \chi_{E_k} - \chi_{I_{\eps, k} }}  }
  \leq \sum_k c_k \norm{ \chi_{E_k} - \chi_{I_{\eps, k}} }
  ,\]
  where the last norm can be bounded by the proof for characteristic functions.

- For arbitrary functions:

  - Now just use that every $f \in L^1$ can be approximated by simple functions $\phi_n$ so that $\norm{f-\phi_n}_1 < \eps$ for $n \gg 1$.
  - So find $\phi_n\to f$, and for each $n$, find $g_{n, k} \in S$ with $\norm{g_{n, k} - \phi_n}_1 \convergesto{k\to \infty} 0$, an approximation by functions in $S$.
  - Then
  \[
  \norm{f - g_{n, k}} \leq \norm{f - \phi_n} + \norm{\phi_n - g_{n, k}}
  ,\]
  which can be made arbitrarily small.

:::


