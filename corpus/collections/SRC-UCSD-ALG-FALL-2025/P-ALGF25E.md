---
schema: qual/card@1
id: P-ALGF25E
kind: problem
title: Submodules isomorphic to $A/\mathfrak{P}$ and existence when $A$ is Noetherian
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $A$ be a unital commutative ring, $\operatorname{Spec}(A)$ denote the set of its prime ideals, and let $M$ be an $A$-module.

(a) Suppose $N_1$ and $N_2$ are two submodules of $M$ such that
\[
N_1 \simeq A/P_1 \qquad \text{and} \qquad N_2 \simeq A/P_2
\]
as $A$-modules for some $P_1, P_2 \in \operatorname{Spec}(A)$.
Prove that if $P_1 \neq P_2$, then $N_1 \cap N_2 = \{0\}$.
(Hint.
Consider $\operatorname{ann}(x)$ for $x \in N_i$.)

(b) Suppose $A$ is Noetherian.
Prove that there exist a submodule $N$ of $M$ and $P \in \operatorname{Spec}(A)$ such that $N \simeq A/P$.
(Hint.
Consider $\Sigma := \{\operatorname{ann}(x) \mid x \in M \setminus \{0\}\}$.)
:::

::: {.solution}
<1>1. Part (a): $N_1 \cap N_2 = \{0\}$ when $P_1 \neq P_2$:
<2>1. Let $x \in N_1 \setminus \{0\}$. Under the isomorphism $N_1 \cong A/P_1$, $x$ corresponds to a coset $a + P_1$ with $a \notin P_1$.
The annihilator of $x$ is:
\[
\operatorname{ann}(x) = \{r \in A \mid r a \in P_1\} = (P_1 : a).
\]
Proof: definition of annihilator for quotient modules.
<2>2. Because $P_1$ is a prime ideal and $a \notin P_1$, the condition $ra \in P_1$ implies $r \in P_1$.
Thus:
\[
\operatorname{ann}(x) = P_1 \quad \text{for every } x \in N_1 \setminus \{0\}.
\]
Proof: definition of prime ideal.
<2>3. By identical reasoning:
\[
\operatorname{ann}(y) = P_2 \quad \text{for every } y \in N_2 \setminus \{0\}.
\]
Proof: symmetry.
<2>4. Let $z \in N_1 \cap N_2$.
If $z \neq 0$, then simultaneously $\operatorname{ann}(z) = P_1$ and $\operatorname{ann}(z) = P_2$, which implies $P_1 = P_2$, contradicting $P_1 \neq P_2$.
Therefore $z = 0$, so $N_1 \cap N_2 = \{0\}$.
Proof: proof by contradiction.

<1>2. Part (b): Existence of $N \cong A/P$ over a Noetherian ring:
<2>1. Assuming $M \neq 0$, consider the family of ideals:
\[
\Sigma = \{ \operatorname{ann}(x) \mid x \in M \setminus \{0\} \}.
\]
Because $M \neq 0$, $\Sigma$ is non-empty.
Proof: existence of a non-zero element in $M$.
<2>2. Since $A$ is a Noetherian ring, the non-empty family $\Sigma$ has a maximal element with respect to inclusion.
Let $P = \operatorname{ann}(x_0) \in \Sigma$ be a maximal element for some $x_0 \in M \setminus \{0\}$.
Proof: Noetherian ascending chain condition on ideals.
<2>3. We show that $P$ is a prime ideal:
- Since $1 \cdot x_0 = x_0 \neq 0$, $1 \notin P$, so $P \subsetneq A$.
- Let $a, b \in A$ with $ab \in P$ and $b \notin P$.
- Since $b \notin P = \operatorname{ann}(x_0)$, the element $y = b x_0 \in M$ is non-zero.
- For every $r \in P$, $ry = r(bx_0) = b(rx_0) = b \cdot 0 = 0$, so $P \subseteq \operatorname{ann}(y)$.
- Furthermore, $a y = a(b x_0) = (ab)x_0 = 0$, so $a \in \operatorname{ann}(y)$.
- Since $y \neq 0$, $\operatorname{ann}(y) \in \Sigma$.
- By the maximality of $P$ in $\Sigma$ and $P \subseteq \operatorname{ann}(y)$, we must have $\operatorname{ann}(y) = P$.
- Since $a \in \operatorname{ann}(y) = P$, $a \in P$.
Thus $P \in \operatorname{Spec}(A)$.
Proof: primality verification via maximality in $\Sigma$.
<2>4. Consider the submodule $N = A x_0 \subseteq M$.
By the First Isomorphism Theorem for modules, the surjective homomorphism $A \to A x_0$ given by $r \mapsto r x_0$ has kernel $\operatorname{ann}(x_0) = P$, giving:
\[
N = A x_0 \cong A / P.
\]
Proof: First Isomorphism Theorem for modules.

<1>3. Conclusion:
Parts (a) and (b) are proven. Q.E.D.
Proof: <1>1 and <1>2.
:::
