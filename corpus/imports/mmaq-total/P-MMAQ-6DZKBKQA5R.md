---
schema: qual/card@1
id: P-MMAQ-6DZKBKQA5R
kind: problem
title: Density of the span of interval indicators in $L^1(\mathbb{R})$
classification:
  areas:
  - real-analysis
  topics:
  - sequences-of-functions
  - convergence-of-functions
  - l1
  - density
relations: []
review: draft
solved: true
---

::: problem
Let
$$
S = \spanof_\CC\theset{\chi_{(a, b)} \suchthat a, b \in \RR},
$$
the complex linear span of characteristic functions of intervals of the form $(a, b)$.

Show that for every $f\in L^1(\RR)$, there exists a sequence of functions $\theset{f_n} \subset S$ such that
$$
\lim _{n \rightarrow \infty}\left\|f_{n}-f\right\|_{1}=0
$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $S = \operatorname{span}_\CC\{\chi_{(a, b)} : a < b, a, b \in \RR\}$ be the space of step functions on $\RR$. Prove that $S$ is dense in $L^1(\RR, \mathcal L, m)$ (i.e. for every $f \in L^1(\RR)$, there exists a sequence $\{f_n\} \subset S$ with $\|f_n - f\|_1 \to 0$).

<1>1. **Density of simple functions with finite measure support in $L^1(\RR)$.**
  <2>1. Let $\mathcal S_0 = \left\{\sum_{j=1}^m c_j \chi_{E_j} : m \in \NN, c_j \in \CC, E_j \in \mathcal L, m(E_j) < \infty\right\}$ be the space of integrable simple functions.
  <2>2. For every $f \in L^1(\RR)$ and every $\eps > 0$, there exists $\phi \in \mathcal S_0$ such that $\|f - \phi\|_1 < \frac{\eps}{2}$.
    Proof: By the standard construction of Lebesgue integrals: decomposing $f = (u^+ - u^-) + i(v^+ - v^-)$ into four non-negative $L^1$ functions, each can be approximated monotonically by simple functions whose integrals converge by the Monotone Convergence Theorem.

<1>2. **Approximation of characteristic functions of finite measure sets by step functions.**
  <2>1. Let $E \in \mathcal L$ be a Lebesgue measurable set with $m(E) < \infty$, and let $\eta > 0$ be given.
  <2>2. By regularity of Lebesgue measure, there exists an open set $U \subseteq \RR$ such that $E \subseteq U$ and $m(U \setminus E) < \frac{\eta}{2}$.
    Proof: By definition of Lebesgue outer measure / regularity, $m(E) = \inf\{m(U) : E \subseteq U, U \text{ open}\}$.
  <2>3. Every open set $U \subseteq \RR$ is a countable union of disjoint open intervals: $U = \bigcup_{k=1}^\infty (a_k, b_k)$.
    Proof: Connected components of open sets in $\RR$ are open intervals, and any collection of pairwise disjoint open intervals in $\RR$ is at most countable.
  <2>4. $m(U) = \sum_{k=1}^\infty (b_k - a_k) \leq m(E) + \frac{\eta}{2} < \infty$.
    Proof: By countable additivity of Lebesgue measure on disjoint intervals.
  <2>5. There exists $K \in \NN$ such that $\sum_{k=K+1}^\infty (b_k - a_k) < \frac{\eta}{2}$.
    Proof: The tail of the convergent series of interval lengths converges to $0$.
  <2>6. Define $V = \bigcup_{k=1}^K (a_k, b_k)$ and $\psi = \chi_V = \sum_{k=1}^K \chi_{(a_k, b_k)} \in S$.
  <2>7. $\|\chi_E - \psi\|_1 < \eta$.
    Proof: Since $V \subseteq U$ and $E \subseteq U$:
    $$
    \|\chi_E - \chi_V\|_1 = \int_\RR |\chi_E - \chi_V|\,dx = m(E \Delta V) \leq m(U \setminus E) + m(U \setminus V) < \frac{\eta}{2} + \frac{\eta}{2} = \eta.
    $$

<1>3. **Approximation of arbitrary simple functions in $\mathcal S_0$ by step functions in $S$.**
  <2>1. Let $\phi = \sum_{j=1}^m c_j \chi_{E_j} \in \mathcal S_0$ with $m(E_j) < \infty$.
  <2>2. For each $j \in \{1, \dots, m\}$, by <1>2 there exists $\psi_j \in S$ such that $\|\chi_{E_j} - \psi_j\|_1 < \frac{\eps}{2 m (|c_j| + 1)}$.
  <2>3. Define $g = \sum_{j=1}^m c_j \psi_j \in S$.
    Proof: $S$ is a complex linear subspace, so linear combinations of elements in $S$ remain in $S$.
  <2>4. $\|\phi - g\|_1 < \frac{\eps}{2}$.
    Proof: By the triangle inequality:
    $$
    \|\phi - g\|_1 = \left\| \sum_{j=1}^m c_j (\chi_{E_j} - \psi_j) \right\|_1 \leq \sum_{j=1}^m |c_j| \|\chi_{E_j} - \psi_j\|_1 < \sum_{j=1}^m |c_j| \frac{\eps}{2 m (|c_j| + 1)} < \frac{\eps}{2}.
    $$

<1>4. **Density and sequence construction.**
  <2>1. For every $f \in L^1(\RR)$ and $\eps > 0$, combining <1>1 and <1>3 gives $g \in S$ such that:
    $$
    \|f - g\|_1 \leq \|f - \phi\|_1 + \|\phi - g\|_1 < \frac{\eps}{2} + \frac{\eps}{2} = \eps.
    $$
  <2>2. For each $n \in \NN$, choosing $\eps = 1/n$ produces $f_n \in S$ such that $\|f_n - f\|_1 < 1/n$.
  <2>3. $\lim_{n\to\infty} \|f_n - f\|_1 = 0$.

<1>5. **Conclusion.**
  $S$ is dense in $L^1(\RR)$. Q.E.D.
:::
