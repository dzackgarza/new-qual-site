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
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Rebuilt onto the located published solution: dbFin, "Section 30: Problem 1 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-30-the-countability-axioms/problem-1-solution/
    (read 2026-11-10; kept at tmp/sources/dbfin/section-30-the-countability-axioms/problem-1-solution.txt),
    checked against Munkres, Topology (2000), Section 30 Exercise 1, printed p. 194. Its (a) is the
    card's: the intersection of a countable local basis at x is {x} because a T1 space separates x
    from each other point. Its (b) is the card's space for the card's reason -- one-point sets are
    G_delta in any first-countable T1 space, hence in the metric R^omega, and remain G_delta in any
    finer topology, while the box topology is not first countable, "take a countable collection U_n
    of neighborhoods of a point and construct a neighborhood by taking the product of open proper
    subsets of U_nn". What was corrected: the source writes "it seems not to satisfy the
    first-countability axiom" and offers no verification, and its alternative "any countable T1
    space which is not first-countable" is not shown to be such; the card states the diagonal
    argument in full, with the m-th coordinate of P_m the interval that W halves. This supersedes
    the previous note, which recorded part (b) as having no complete published proof.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Twelve of the card's fourteen steps, among them every leaf of both parts and the closing
    step, asserted their claim with no proof body; each now carries a `pf-proof`. No claim was
    changed and the statements of (a) and (b) stand as printed. Checked: the argument of (a)
    against Munkres, Topology (2000), Section 30, printed p. 194, with Theorem 17.8 for the
    closedness of finite sets in a $T_1$ space, and the diagonal argument of (b) recomputed,
    including that the diagonal box W is a neighbourhood of the origin and that no basic box
    P_m is contained in it. Not checked: no published solution was re-read for this pass; the
    card's two earlier events record the searches that located the dbFin and Orellana texts.
---

::: {.exercise}

(a) A $G_\delta$ set in a space $X$ is a set $A$ that equals a countable intersection of open sets of $X$.
Show that in a first-countable $T_1$ space, every one-point set is a $G_\delta$ set.

(b) There is a familiar space in which every one-point set is a $G_\delta$ set, which nevertheless does not satisfy the first countability axiom.
What is it?
:::

::: {.solution}

Part (a) is the standard T1 argument; part (b) uses the box topology on $\RR^\omega$, where the singletons are still $G_\delta$ but the origin has no countable local basis.

::: pf

::: pf-step

Part (a): singletons are $G_\delta$ in first-countable $T_1$ spaces.

::: pf-proof

Steps 1.1--1.7 prove the equality $\{x\}=\bigcap_n B_n$ by the two inclusions, and step 1.8 reads off the definition of a $G_\delta$ set.

::: pf-step

Let $x \in X$. Since $X$ is first-countable, there exists a countable local neighborhood basis $\{B_n\}_{n=1}^\infty$ of open neighborhoods at $x$.

::: pf-proof

First countability at $x$ means that $x$ has a countable local basis: neighbourhoods $B_1,B_2,\dots$ of $x$ such that every neighbourhood of $x$ contains some $B_n$ (Munkres, §30). Each $B_n$ may be taken open, since a neighbourhood of $x$ contains an open neighbourhood of $x$, and replacing $B_n$ by such an open subset keeps the local-basis property: a set contained in $B_n$ is contained in every neighbourhood that contains $B_n$.

:::

:::

::: pf-step

We claim that $\{x\} = \bigcap_{n=1}^\infty B_n$.

::: pf-proof

The claim is an equality of sets and is proved by the two inclusions: $\{x\}\subseteq\bigcap_nB_n$ in step 1.3, and $\bigcap_nB_n\subseteq\{x\}$ in step 1.6.

:::

:::

::: pf-step

Since $x \in B_n$ for every $n \ge 1$, $\{x\} \subseteq \bigcap_{n=1}^\infty B_n$.

::: pf-proof

Each $B_n$ is a neighbourhood of $x$ and so contains $x$; hence $x$ belongs to every member of the family, that is to its intersection.

:::

:::

::: pf-step

For any point $y \in X$ with $y \neq x$, the $T_1$ separation axiom implies that the complement $U = X \setminus \{y\}$ is an open neighborhood of $x$.

::: pf-proof

In a $T_1$ space every finite subset is closed (Munkres, Theorem 17.8), so $\{y\}$ is closed and $U=X\setminus\{y\}$ is open. Since $y\ne x$, the point $x$ lies in $U$; so $U$ is an open neighbourhood of $x$.

:::

:::

::: pf-step

By definition of a local neighborhood basis, there exists some $n_0 \ge 1$ such that $B_{n_0} \subseteq U = X \setminus \{y\}$.

::: pf-proof

$U$ is a neighbourhood of $x$, and a local basis at $x$ has the defining property that every neighbourhood of $x$ contains one of its members; apply it to $U$.

:::

:::

::: pf-step

Thus $y \notin B_{n_0}$, which implies $y \notin \bigcap_{n=1}^\infty B_n$.

::: pf-proof

$B_{n_0}\subseteq X\setminus\{y\}$ says that no point of $B_{n_0}$ is $y$. A point missing from one member of the family is missing from the intersection.

:::

:::

::: pf-step

Therefore, $\bigcap_{n=1}^\infty B_n = \{x\}$.

::: pf-proof

Step 1.3 gives $\{x\}\subseteq\bigcap_nB_n$; step 1.6 shows that every $y\ne x$ lies outside the intersection, which is $\bigcap_nB_n\subseteq\{x\}$. The two inclusions give the equality.

:::

:::

::: pf-step

Because each $B_n$ is open, $\{x\}$ is a countable intersection of open sets, hence a $G_\delta$ set.

::: pf-proof

By step 1.7 $\{x\}$ is the intersection of the family $\{B_n\}_{n\ge1}$, which is countable and consists of open sets. That is precisely the definition of a $G_\delta$ set given in the statement.

:::

:::

:::

:::

::: pf-step

Part (b): a space where singletons are $G_\delta$ but first countability fails. A familiar example is the product space $\RR^\omega = \prod_{n=1}^\infty \RR$ equipped with the **box topology**.

::: pf-proof

Step 2.1 exhibits each singleton as a countable intersection of box-open sets, step 2.2 shows the origin has no countable local basis, and step 2.3 draws the conclusion for the box topology.

::: pf-step

**Singletons are $G_\delta$:**
Let $\mathbf{x} = (x_n)_{n=1}^\infty \in \RR^\omega$. For each integer $k \ge 1$, define the box-open set:
$$U_k = \prod_{n=1}^\infty \left(x_n - \frac{1}{k}, x_n + \frac{1}{k}\right).$$
Then:
$$\bigcap_{k=1}^\infty U_k = \prod_{n=1}^\infty \bigcap_{k=1}^\infty \left(x_n - \frac{1}{k}, x_n + \frac{1}{k}\right) = \prod_{n=1}^\infty \{x_n\} = \{\mathbf{x}\}.$$
Thus every one-point set in $\RR^\omega_{\text{box}}$ is a $G_\delta$ set.

::: pf-proof

Each $U_k$ is a product of open subsets of the factors, one in each factor, so it is open in the box topology. A point $\mathbf{y}$ lies in $\bigcap_kU_k$ exactly when for every $n$ and every $k$ its $n$-th coordinate satisfies $\abs{y_n-x_n}<1/k$; that holds exactly when $y_n=x_n$ for every $n$, that is exactly when $\mathbf{y}=\mathbf{x}$. So the intersection is $\{\mathbf{x}\}$, a countable intersection of box-open sets.

:::

:::

::: pf-step

**Failure of first countability:**
The origin $\mathbf{0} \in \RR^\omega$ has no countable local neighborhood basis in the box topology. Indeed, if $\{B_m\}_{m=1}^\infty$ were such a basis, choose for each $m$ a basic box $P_m=\prod_{n=1}^\infty(-\varepsilon_{m,n},\varepsilon_{m,n})\subseteq B_m$ about $\mathbf{0}$ with every $\varepsilon_{m,n}>0$; then $\{P_m\}$ would also be a local basis. But the box-open neighborhood $W=\prod_{n=1}^\infty(-\varepsilon_{n,n}/2,\varepsilon_{n,n}/2)$ of $\mathbf{0}$ contains no $P_m$: the $m$-th coordinate of $P_m$ is $(-\varepsilon_{m,m},\varepsilon_{m,m})$, which is not contained in $(-\varepsilon_{m,m}/2,\varepsilon_{m,m}/2)$. This contradicts the defining property of a local basis.

::: pf-proof

A basic box of the box topology about $\mathbf{0}$ is a product of open intervals about the coordinates of $\mathbf{0}$, so it has the displayed form with every $\varepsilon_{m,n}>0$; one lies inside the neighbourhood $B_m$, because the basic boxes form a basis and $B_m$ is open. Since $P_m\subseteq B_m$, every neighbourhood of $\mathbf{0}$ that contains $B_m$ also contains $P_m$, so $\{P_m\}_{m\ge1}$ is a local basis too. The set $W$ is box-open and contains $\mathbf{0}$, each factor being an interval about $0$. Its $m$-th factor is half the $m$-th factor of $P_m$, and $P_m$ has $m$-th coordinate interval $(-\varepsilon_{m,m},\varepsilon_{m,m})$: the point with $m$-th coordinate $3\varepsilon_{m,m}/4$ and all others $0$ lies in $P_m$ and not in $W$. So $P_m\nsubseteq W$ for every $m$, hence no $B_m$ is contained in $W$, and the neighbourhood $W$ of $\mathbf{0}$ contains no member of the supposed local basis.

:::

:::

::: pf-step

Hence $\RR^\omega$ in the box topology is not first-countable.

::: pf-proof

Step 2.2 exhibits a point of $\RR^\omega_{\text{box}}$ with no countable local basis. First countability requires a countable local basis at every point (Munkres, §30), so the box topology fails the axiom.

:::

:::

:::

:::

::: pf-step

Singletons are $G_\delta$ in any first-countable $T_1$ space, and $\RR^\omega$ with the box topology is a non-first-countable space with $G_\delta$ singletons.

::: pf-proof

The two clauses are parts (a) and (b): $\RR^\omega_{\text{box}}$ has $G_\delta$ singletons by step 2.1 and is not first countable by step 2.3, so it is the space the exercise asks for in (b), while (a) is steps 1.1--1.8.

:::

:::

:::
:::