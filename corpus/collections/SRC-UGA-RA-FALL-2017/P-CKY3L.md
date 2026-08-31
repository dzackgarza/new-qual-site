---
schema: qual/card@1
id: P-CKY3L
kind: problem
title: Density of the span of interval indicators in $L^1(\RR)$
classification:
  areas:
  - real-analysis
  topics:
  - Density
  - L¹
relations: []
review: draft
---

::: problem
Let $S = \operatorname{span}_{\mathbb{C}}\{\chi_{(a, b)} : a, b \in \mathbb{R}, \, a < b\}$ be the complex linear span of characteristic functions of bounded open intervals in $\mathbb{R}$.

Show that $S$ is dense in $L^1(\mathbb{R})$: for every $f \in L^1(\mathbb{R})$, there exists a sequence $(f_n)_{n=1}^\infty \subset S$ such that
$$
\lim_{n \to \infty} \|f_n - f\|_{L^1(\mathbb{R})} = 0.
$$
:::

::: solution
**Goal:** Prove that the span of interval indicator functions $S$ is dense in $L^1(\mathbb{R})$ using simple function density and Lebesgue regularity.

<1>1. Approximation of $f$ by integrable simple functions:
    *Proof:*
    <2>1. Let $f \in L^1(\mathbb{R})$ and let $\varepsilon > 0$ be given.
    <2>2. By the standard construction of Lebesgue integrals, the set of integrable simple functions is dense in $L^1(\mathbb{R})$.
    <2>3. Thus there exists a simple function
    $$\psi = \sum_{k=1}^m c_k \chi_{E_k},$$
    where $c_k \in \mathbb{C}$ and $E_k \subset \mathbb{R}$ are disjoint measurable sets with $m(E_k) < \infty$, such that
    $$\|f - \psi\|_{L^1} < \frac{\varepsilon}{2}.$$

<1>2. Approximation of measurable sets of finite measure by finite unions of open intervals:
    *Proof:*
    <2>1. Fix $k \in \{1, \dots, m\}$. Since $m(E_k) < \infty$, by the definition of Lebesgue outer measure, there exists an open set $U_k \supset E_k$ such that
    $$m(U_k \setminus E_k) < \frac{\varepsilon}{4 m (|c_k| + 1)}.$$
    <2>2. Every open set in $\mathbb{R}$ is a countable disjoint union of bounded open intervals: $U_k = \bigsqcup_{j=1}^\infty (a_{k, j}, b_{k, j})$.
    <2>3. Since $m(U_k) = \sum_{j=1}^\infty (b_{k, j} - a_{k, j}) < \infty$, there exists an integer $N_k \ge 1$ such that
    $$m\left( U_k \setminus \bigcup_{j=1}^{N_k} (a_{k, j}, b_{k, j}) \right) = \sum_{j=N_k+1}^\infty (b_{k, j} - a_{k, j}) < \frac{\varepsilon}{4 m (|c_k| + 1)}.$$
    <2>4. Define $V_k = \bigcup_{j=1}^{N_k} (a_{k, j}, b_{k, j})$, which is a finite union of bounded open intervals.
    <2>5. The symmetric difference satisfies $E_k \Delta V_k \subseteq (U_k \setminus E_k) \cup (U_k \setminus V_k)$, so
    $$m(E_k \Delta V_k) \le m(U_k \setminus E_k) + m(U_k \setminus V_k) < \frac{\varepsilon}{2 m (|c_k| + 1)}.$$
    <2>6. Therefore, the $L^1$ distance between indicators satisfies:
    $$\|\chi_{E_k} - \chi_{V_k}\|_{L^1} = \int_\mathbb{R} |\chi_{E_k} - \chi_{V_k}| \, dm = m(E_k \Delta V_k) < \frac{\varepsilon}{2 m (|c_k| + 1)}.$$

<1>3. Construction and approximation in $S$:
    *Proof:*
    <2>1. Since $V_k$ is a finite disjoint union of open intervals $(a_{k, j}, b_{k, j})$, the indicator function $\chi_{V_k} = \sum_{j=1}^{N_k} \chi_{(a_{k, j}, b_{k, j})} \in S$.
    <2>2. Define the function $g = \sum_{k=1}^m c_k \chi_{V_k}$. Since each $\chi_{V_k} \in S$, $g \in S$.
    <2>3. Bound the distance between $\psi$ and $g$:
    $$\|\psi - g\|_{L^1} = \left\| \sum_{k=1}^m c_k (\chi_{E_k} - \chi_{V_k}) \right\|_{L^1} \le \sum_{k=1}^m |c_k| \|\chi_{E_k} - \chi_{V_k}\|_{L^1} < \sum_{k=1}^m |c_k| \frac{\varepsilon}{2 m (|c_k| + 1)} < \frac{\varepsilon}{2}.$$

<1>4. Triangle inequality:
    *Proof:*
    <2>1. Combining the approximations:
    $$\|f - g\|_{L^1} \le \|f - \psi\|_{L^1} + \|\psi - g\|_{L^1} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.$$
    <2>2. Since $\varepsilon > 0$ was arbitrary, this establishes that $S$ is dense in $L^1(\mathbb{R})$.

<1>5. Conclusion:
    *Proof:*
    $S$ is dense in $L^1(\mathbb{R})$.
:::


