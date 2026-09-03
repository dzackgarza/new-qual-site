---
schema: qual/card@1
id: E-5DDIL
kind: problem
title: Fundamental groups of wedges with nice neighborhoods
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

Suppose $X$ is a space that is the union of the closed subspaces $X_1, \ldots, X_n$; assume there is a point $p$ of $X$ such that $X_i \cap X_j = \ts{p}$ for $i \neq j$.
Then we call $X$ the wedge of the spaces $X_1, \ldots, X_n$, and write $X = X_1 \vee \cdots \vee X_n$.
Show that if for each $i$, the point $p$ is a deformation retract of an open set $W_i$ of $X_i$, then $\pi_1(X, p)$ is the external free product of the groups $\pi_1(X_i, p)$ relative to the monomorphisms induced by inclusion.
:::

::: solution
**Goal:** Prove that the fundamental group of a wedge sum $X = X_1 \vee \dots \vee X_n$ of well-pointed spaces (where $p$ is a deformation retract of an open neighborhood $W_i \subseteq X_i$) is isomorphic to the free product $*_{i=1}^n \pi_1(X_i, p)$ via the Seifert-van Kampen Theorem.

<1>1. Base case ($n = 2$):
    Let $X = X_1 \cup X_2$ with closed subspaces $X_1, X_2$ intersecting at $X_1 \cap X_2 = \{p\}$.
    Then $\pi_1(X, p) \cong \pi_1(X_1, p) * \pi_1(X_2, p)$.
    *Proof:*
    <2>1. Define the subsets $U_1 = X_1 \cup W_2$ and $U_2 = X_2 \cup W_1$.
    <2>2. **Openness of $U_1$ and $U_2$ in $X$:**
        - The complement $X \setminus U_1 = X_2 \setminus W_2$.
        - Since $W_2$ is open in $X_2$, $X_2 \setminus W_2$ is closed in $X_2$.
        - Because $X_2$ is closed in $X$, $X_2 \setminus W_2$ is closed in $X$, so $U_1$ is open in $X$.
        - By identical reasoning, $U_2$ is open in $X$.
    <2>3. **Union and Intersection:**
        - $U_1 \cup U_2 = (X_1 \cup W_2) \cup (X_2 \cup W_1) = X_1 \cup X_2 = X$.
        - $U_1 \cap U_2 = (X_1 \cap X_2) \cup W_1 \cup W_2 = W_1 \cup W_2$.
    <2>4. **Homotopy types of $U_1, U_2,$ and $U_1 \cap U_2$:**
        - Since $W_2$ deformation retracts to $\{p\}$, extending the deformation retraction by the identity on $X_1$ exhibits $X_1$ as a deformation retract of $U_1$. Hence the inclusion $j_1: X_1 \hookrightarrow U_1$ induces an isomorphism $(j_1)_*: \pi_1(X_1, p) \xrightarrow{\cong} \pi_1(U_1, p)$.
        - Symmetrically, the inclusion $j_2: X_2 \hookrightarrow U_2$ induces $(j_2)_*: \pi_1(X_2, p) \xrightarrow{\cong} \pi_1(U_2, p)$.
        - The intersection $U_1 \cap U_2 = W_1 \cup W_2$ deformation retracts to $\{p\}$, so $U_1 \cap U_2$ is contractible and $\pi_1(U_1 \cap U_2, p) = \{1\}$.
    <2>5. **Application of Seifert-van Kampen:**
        - By the Seifert-van Kampen Theorem, the amalgamated product over the trivial group reduces to the free product:
          $$\pi_1(X, p) \cong \pi_1(U_1, p) *_{\pi_1(U_1 \cap U_2, p)} \pi_1(U_2, p) \cong \pi_1(X_1, p) * \pi_1(X_2, p).$$

<1>2. Induction step for $n \ge 3$:
    *Proof:*
    <2>1. Assume the statement holds for wedges of $k < n$ spaces.
    <2>2. Decompose $X = Y \vee X_n$, where $Y = X_1 \vee \dots \vee X_{n-1}$.
    <2>3. $Y$ is a closed subspace of $X$, and $W_Y = \bigcup_{i=1}^{n-1} W_i$ is an open neighborhood of $p$ in $Y$ that deformation retracts to $\{p\}$.
    <2>4. Applying the $n=2$ result from <1>1 gives:
        $$\pi_1(X, p) \cong \pi_1(Y, p) * \pi_1(X_n, p).$$
    <2>5. By the inductive hypothesis, $\pi_1(Y, p) \cong \pi_1(X_1, p) * \dots * \pi_1(X_{n-1}, p)$.
    <2>6. Thus $\pi_1(X, p) \cong \pi_1(X_1, p) * \dots * \pi_1(X_n, p)$.

<1>3. Conclusion:
    $\pi_1(X, p)$ is the free product $\bigAsterisk_{i=1}^n \pi_1(X_i, p)$ relative to the inclusion homomorphisms. Q.E.D.
:::
