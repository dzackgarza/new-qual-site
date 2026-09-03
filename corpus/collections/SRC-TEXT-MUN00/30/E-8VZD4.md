---
schema: qual/card@1
id: E-8VZD4
kind: problem
title: One-point sets are G-delta in first-countable T1 spaces
classification:
  areas:
  - topology
  topics:
  - Countability
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

(a) A $G_\delta$ set in a space $X$ is a set $A$ that equals a countable intersection of open sets of $X$.
Show that in a first-countable $T_1$ space, every one-point set is a $G_\delta$ set.

(b) There is a familiar space in which every one-point set is a $G_\delta$ set, which nevertheless does not satisfy the first countability axiom.
What is it?
:::

::: solution
**Goal:** Prove that one-point sets in first-countable $T_1$ spaces are $G_\delta$ sets, and identify a familiar non-first-countable space with $G_\delta$ singletons.

<1>1. Part (a): Singletons are $G_\delta$ in first-countable $T_1$ spaces.
    *Proof:*
    <2>1. Let $x \in X$. Since $X$ is first-countable, there exists a countable local neighborhood basis $\{B_n\}_{n=1}^\infty$ of open neighborhoods at $x$.
    <2>2. We claim that $\{x\} = \bigcap_{n=1}^\infty B_n$.
    <2>3. Since $x \in B_n$ for every $n \ge 1$, $\{x\} \subseteq \bigcap_{n=1}^\infty B_n$.
    <2>4. For any point $y \in X$ with $y \neq x$, the $T_1$ separation axiom implies that the complement $U = X \setminus \{y\}$ is an open neighborhood of $x$.
    <2>5. By definition of a local neighborhood basis, there exists some $n_0 \ge 1$ such that $B_{n_0} \subseteq U = X \setminus \{y\}$.
    <2>6. Thus $y \notin B_{n_0}$, which implies $y \notin \bigcap_{n=1}^\infty B_n$.
    <2>7. Therefore, $\bigcap_{n=1}^\infty B_n = \{x\}$.
    <2>8. Because each $B_n$ is open, $\{x\}$ is a countable intersection of open sets, hence a $G_\delta$ set.

<1>2. Part (b): Space where singletons are $G_\delta$ but first-countability fails.
    A familiar example is the product space $\mathbb{R}^\omega = \prod_{n=1}^\infty \mathbb{R}$ equipped with the **box topology**.
    *Proof:*
    <2>1. **Singletons are $G_\delta$:**
        Let $\mathbf{x} = (x_n)_{n=1}^\infty \in \mathbb{R}^\omega$. For each integer $k \ge 1$, define the box-open set:
        $$U_k = \prod_{n=1}^\infty \left(x_n - \frac{1}{k}, x_n + \frac{1}{k}\right).$$
        Then:
        $$\bigcap_{k=1}^\infty U_k = \prod_{n=1}^\infty \bigcap_{k=1}^\infty \left(x_n - \frac{1}{k}, x_n + \frac{1}{k}\right) = \prod_{n=1}^\infty \{x_n\} = \{\mathbf{x}\}.$$
        Thus every one-point set in $\mathbb{R}^\omega_{\text{box}}$ is a $G_\delta$ set.
    <2>2. **Failure of first countability:**
        As shown in §30 Example 2, the origin $\mathbf{0} \in \mathbb{R}^\omega$ has no countable local neighborhood basis in the box topology (given any countable family $\{B_m\}_{m=1}^\infty$ of box-open neighborhoods of $\mathbf{0}$ with $B_m = \prod_{n=1}^\infty (-\varepsilon_{m, n}, \varepsilon_{m, n})$, the diagonal open neighborhood $W = \prod_{n=1}^\infty (-\frac{1}{2}\varepsilon_{n, n}, \frac{1}{2}\varepsilon_{n, n})$ contains no $B_m$).
    <2>3. Hence $\mathbb{R}^\omega$ in the box topology is not first-countable.

<1>3. Conclusion:
    Singletons are $G_\delta$ in any first-countable $T_1$ space, and $\mathbb{R}^\omega$ with the box topology is a non-first-countable space with $G_\delta$ singletons. Q.E.D.
:::
