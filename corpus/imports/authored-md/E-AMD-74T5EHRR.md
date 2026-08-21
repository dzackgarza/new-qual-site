---
schema: qual/card@1
id: E-AMD-74T5EHRR
kind: exercise
title: The center of $S_n$ is trivial for $n\geq 3$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Permutations
relations: []
review: draft
solved: true
---

::: {.exercise}
Show that $Z(S_n) = 1$ for $n\geq 3$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $n \ge 3$ be an integer, and let $S_n$ be the symmetric group on $n$ elements.
Prove that the center $Z(S_n) = \{e\}$, where $e$ is the identity permutation.

<1>1. Definition of the center $Z(S_n)$: $Z(S_n) = \{\sigma \in S_n \mid \sigma \tau = \tau \sigma \text{ for all } \tau \in S_n\}$.
Proof: Standard definition of the center of a group.

<1>2. The identity permutation $e \in Z(S_n)$, so $\{e\} \subseteq Z(S_n)$.
Proof: $e \tau = \tau e = \tau$ for all $\tau \in S_n$.

<1>3. If $\sigma \in S_n$ and $\sigma \neq e$, then $\sigma \notin Z(S_n)$.
<2>1. Since $\sigma \neq e$, there exists an element $i \in \{1, 2, \dots, n\}$ such that $\sigma(i) = j$ with $j \neq i$.
Proof: A non-identity permutation must move at least one element.
<2>2. Since $n \ge 3$, there exists an element $k \in \{1, 2, \dots, n\}$ such that $k \notin \{i, j\}$.
Proof: The set $\{1, \dots, n\}$ has cardinality $n \ge 3$, and $\{i, j\}$ has cardinality $2$.
<2>3. Consider the transposition $\tau = (j\,k) \in S_n$.
Proof: Well-defined transposition since $j \neq k$.
<2>4. Evaluate the compositions $(\sigma \circ \tau)$ and $(\tau \circ \sigma)$ at the element $i$: <3>1. $(\tau \circ \sigma)(i) = \tau(\sigma(i)) = \tau(j) = k$.
Proof: By definition of $\sigma(i) = j$ and $\tau = (j\,k)$ sending $j \mapsto k$.
<3>2. $(\sigma \circ \tau)(i) = \sigma(\tau(i)) = \sigma(i) = j$.
Proof: Since $i \notin \{j, k\}$, $\tau(i) = i$.
Then $\sigma(i) = j$.
<3>3. $(\tau \circ \sigma)(i) \neq (\sigma \circ \tau)(i)$.
Proof: $k \neq j$ by choice of $k \notin \{i, j\}$.
<2>5. Therefore, $\tau \circ \sigma \neq \sigma \circ \tau$, so $\sigma$ does not commute with $\tau$.
Proof: Two permutations that disagree on an element $i$ are distinct functions.
<2>6. Consequently, $\sigma \notin Z(S_n)$.
Proof: $\sigma$ fails to commute with at least one element $\tau \in S_n$.
<2>7. Q.E.D. Proof: Follows from <2>1 through <2>6.

<1>4. Conclusion: $Z(S_n) = \{e\} = 1$.
Proof: By <1>2, $\{e\} \subseteq Z(S_n)$, and by <1>3, no non-identity element belongs to $Z(S_n)$.
Thus $Z(S_n) = 1$.
:::
