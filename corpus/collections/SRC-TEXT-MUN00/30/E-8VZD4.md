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
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Part (a) transcribed from the located published solution: Ana Emilia de Orellana,
    "Solutions - Topology Munkres", Section 30 Exercise 1(a), printed p. 30
    (tmp/sources/munkres-solutions-anadeore.pdf), checked against Munkres, Topology (2000),
    Section 30, printed p. 194, and Theorem 30.3's definition of a countable basis at a point.
    Corrections on this card: the earlier solution presented the diagonal argument of part (b)
    as "shown in Section 30 Example 2", which is false -- Example 2 of Section 30 (printed
    p. 191) shows that R^omega in the UNIFORM topology is first-countable and not
    second-countable, and says nothing about the box topology; the citation is removed and
    the argument is now given in full. Part (b) has no complete published proof in any located
    set: Orellana, printed p. 30, asserts that the box topology on R^omega is not
    first-countable but her display only produces local bases of the coordinates and does not
    prove the negation; "Doug's World", "Munkres - Topology - Chapter 4 Solutions", printed
    p. 1, answers "I'm not sure what the answer here is" and offers only a guess. See the
    COMPLAINTS.md entry for this batch.
---

::: {.exercise}

(a) A $G_\delta$ set in a space $X$ is a set $A$ that equals a countable intersection of open sets of $X$.
Show that in a first-countable $T_1$ space, every one-point set is a $G_\delta$ set.

(b) There is a familiar space in which every one-point set is a $G_\delta$ set, which nevertheless does not satisfy the first countability axiom.
What is it?
:::

::: {.solution}
::: pf

::: pf-step
Part (a): Singletons are $G_\delta$ in first-countable $T_1$ spaces.

::: pf-proof

::: pf-step
Let $x \in X$. Since $X$ is first-countable, there exists a countable local neighborhood basis $\{B_n\}_{n=1}^\infty$ of open neighborhoods at $x$.
:::

::: pf-step
We claim that $\{x\} = \bigcap_{n=1}^\infty B_n$.
:::

::: pf-step
Since $x \in B_n$ for every $n \ge 1$, $\{x\} \subseteq \bigcap_{n=1}^\infty B_n$.
:::

::: pf-step
For any point $y \in X$ with $y \neq x$, the $T_1$ separation axiom implies that the complement $U = X \setminus \{y\}$ is an open neighborhood of $x$.
:::

::: pf-step
By definition of a local neighborhood basis, there exists some $n_0 \ge 1$ such that $B_{n_0} \subseteq U = X \setminus \{y\}$.
:::

::: pf-step
Thus $y \notin B_{n_0}$, which implies $y \notin \bigcap_{n=1}^\infty B_n$.
:::

::: pf-step
Therefore, $\bigcap_{n=1}^\infty B_n = \{x\}$.
:::

::: pf-step
Because each $B_n$ is open, $\{x\}$ is a countable intersection of open sets, hence a $G_\delta$ set.
:::

:::

:::

::: pf-step
Part (b): Space where singletons are $G_\delta$ but first-countability fails.
A familiar example is the product space $\RR^\omega = \prod_{n=1}^\infty \RR$ equipped with the **box topology**.

::: pf-proof

::: pf-step
**Singletons are $G_\delta$:**
Let $\mathbf{x} = (x_n)_{n=1}^\infty \in \RR^\omega$. For each integer $k \ge 1$, define the box-open set:
$$U_k = \prod_{n=1}^\infty \left(x_n - \frac{1}{k}, x_n + \frac{1}{k}\right).$$
Then:
$$\bigcap_{k=1}^\infty U_k = \prod_{n=1}^\infty \bigcap_{k=1}^\infty \left(x_n - \frac{1}{k}, x_n + \frac{1}{k}\right) = \prod_{n=1}^\infty \{x_n\} = \{\mathbf{x}\}.$$
Thus every one-point set in $\RR^\omega_{\text{box}}$ is a $G_\delta$ set.
:::

::: pf-step
**Failure of first countability:**
The origin $\mathbf{0} \in \RR^\omega$ has no countable local neighborhood basis in the box topology. Indeed, if $\{B_m\}_{m=1}^\infty$ were such a basis, choose for each $m$ a basic box $P_m=\prod_{n=1}^\infty(-\varepsilon_{m,n},\varepsilon_{m,n})\subseteq B_m$ about $\mathbf{0}$ with every $\varepsilon_{m,n}>0$; then $\{P_m\}$ would also be a local basis. But the box-open neighborhood $W=\prod_{n=1}^\infty(-\varepsilon_{n,n}/2,\varepsilon_{n,n}/2)$ of $\mathbf{0}$ contains no $P_m$: the $m$-th coordinate of $P_m$ is $(-\varepsilon_{m,m},\varepsilon_{m,m})$, which is not contained in $(-\varepsilon_{m,m}/2,\varepsilon_{m,m}/2)$. This contradicts the defining property of a local basis.
:::

::: pf-step
Hence $\RR^\omega$ in the box topology is not first-countable.
:::

:::

:::

::: pf-step
Singletons are $G_\delta$ in any first-countable $T_1$ space, and $\RR^\omega$ with the box topology is a non-first-countable space with $G_\delta$ singletons.
:::

:::

:::
