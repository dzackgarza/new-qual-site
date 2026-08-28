---
schema: qual/card@1
id: E-6C2JI
kind: exercise
title: Fundamental groups under the Seifert-van Kampen hypotheses with trivial inclusions
classification:
  areas:
  - topology
  topics:
  - Seifert-van Kampen Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Assume the hypotheses of Theorem 59.1.

(a) What can you say about the fundamental group of $X$ if $j_*$ is the trivial homomorphism?
If both $i_*$ and $j_*$ are trivial?

(b) Give an example where $i_*$ and $j_*$ are trivial but neither $U$ nor $V$ have trivial fundamental groups.
:::

::: solution
**Goal:** Compute the fundamental group $\pi_1(X, x_0)$ under Seifert-van Kampen when one or both inclusion homomorphisms $i_*, j_*$ from $\pi_1(U \cap V)$ are trivial, and provide an explicit non-trivial example.

<1>1. General Seifert-van Kampen relation structure:
    Under the hypotheses of Theorem 59.1 ($X = U \cup V$ with $U, V, U \cap V$ open and path-connected), the fundamental group is the amalgamated free product:
    $$\pi_1(X, x_0) \cong (\pi_1(U, x_0) * \pi_1(V, x_0)) / N,$$
    where $N$ is the normal closure in $\pi_1(U) * \pi_1(V)$ of the subset:
    $$R = \{ i_*(g) j_*(g)^{-1} \mid g \in \pi_1(U \cap V, x_0) \}.$$

<1>2. Analysis of Part (a):
    *Proof:*
    <2>1. **Case 1 ($j_*$ is trivial):**
        - If $j_*(g) = 1$ for all $g \in \pi_1(U \cap V, x_0)$, then $i_*(g) j_*(g)^{-1} = i_*(g) \in \pi_1(U, x_0)$.
        - The relators lie entirely within the factor $\pi_1(U, x_0)$, so $N$ is the normal closure in $\pi_1(U, x_0)$ of $i_*(\pi_1(U \cap V, x_0))$.
        - Factoring out $N$ affects only the first factor, yielding:
          $$\pi_1(X, x_0) \cong (\pi_1(U, x_0) / \langle\langle i_*(\pi_1(U \cap V, x_0)) \rangle\rangle) * \pi_1(V, x_0).$$
    <2>2. **Case 2 (Both $i_*$ and $j_*$ are trivial):**
        - If $i_*(g) = 1$ and $j_*(g) = 1$ for all $g \in \pi_1(U \cap V, x_0)$, then $i_*(g) j_*(g)^{-1} = 1$.
        - Thus the set of relations is $R = \{1\}$, so the normal subgroup $N$ is trivial ($N = \{1\}$).
        - Therefore, the amalgamated product reduces directly to the free product:
          $$\pi_1(X, x_0) \cong \pi_1(U, x_0) * \pi_1(V, x_0).$$

<1>3. Construction for Part (b):
    *Proof:*
    <2>1. Let $X = S^1 \vee S^1 = A \vee B$ be the wedge sum of two circles with common basepoint $x_0$.
    <2>2. Choose points $p \in A \setminus \{x_0\}$ and $q \in B \setminus \{x_0\}$.
    <2>3. Define open subsets:
        $$U = X \setminus \{q\} = A \vee (B \setminus \{q\}) \quad \text{and} \quad V = X \setminus \{p\} = (A \setminus \{p\}) \vee B.$$
    <2>4. The open arc $B \setminus \{q\}$ deformation retracts to $x_0$, so $U \simeq A \cong S^1$ and $\pi_1(U, x_0) \cong \mathbb{Z} \neq \{1\}$.
    <2>5. Symmetrically, $V \simeq B \cong S^1$ and $\pi_1(V, x_0) \cong \mathbb{Z} \neq \{1\}$.
    <2>6. The intersection $U \cap V = (A \setminus \{p\}) \vee (B \setminus \{q\})$ is the wedge of two contractible open arcs, hence contractible:
        $$\pi_1(U \cap V, x_0) = \{1\}.$$
    <2>7. Since $\pi_1(U \cap V, x_0)$ is the trivial group, both homomorphisms $i_*$ and $j_*$ are trivial, while $\pi_1(U, x_0) \cong \mathbb{Z}$ and $\pi_1(V, x_0) \cong \mathbb{Z}$ are non-trivial. Q.E.D.
:::
