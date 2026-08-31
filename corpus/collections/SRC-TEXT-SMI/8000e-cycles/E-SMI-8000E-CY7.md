---
schema: qual/card@1
id: E-SMI-8000E-CY7
kind: exercise
title: The 2-cycle relation on a subgroup of the symmetric group
classification:
  areas:
  - algebra
  topics:
  - Symmetric Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.exercise}
Let $H$ be a subgroup of the symmetric group $S_n$.
Define a binary relation $\sim$ on the set $\{1, 2, \dots, n\}$ by setting:
$$j \sim k \iff (j = k) \text{ or } ((j\,k) \in H).$$
Prove that $\sim$ is an **equivalence relation** on $\{1, 2, \dots, n\}$.
*(Note: If $j \sim k$ is defined solely by $(j\,k) \in H$, adding $j=k$ makes reflexivity explicit).*
:::

::: solution
**Goal:** Prove that the transposition membership relation on indices defines an equivalence relation (reflexive, symmetric, transitive).

<1>1. Reflexivity ($j \sim j$):
    *Proof:*
    <2>1. For every $j \in \{1, 2, \dots, n\}$, the first clause of the definition applies: $j = j$, so $j \sim j$.

<1>2. Symmetry ($j \sim k \implies k \sim j$):
    *Proof:*
    <2>1. Let $j, k \in \{1, 2, \dots, n\}$ with $j \sim k$.
    <2>2. If $j = k$, then $k = j$, so $k \sim j$.
    <2>3. If $j \ne k$, then by definition the 2-cycle (transposition) $(j\,k) \in H$.
    <2>4. Since every 2-cycle is symmetric as a permutation:
        $$(k\,j) = (j\,k).$$
    <2>5. Since $(j\,k) \in H$, we have $(k\,j) \in H$.
    <2>6. Therefore, $k \sim j$.

<1>3. Transitivity ($j \sim k \text{ and } k \sim \ell \implies j \sim \ell$):
    *Proof:*
    <2>1. Let $j, k, \ell \in \{1, 2, \dots, n\}$ with $j \sim k$ and $k \sim \ell$.
    <2>2. If any two of $j, k, \ell$ are equal:
        - If $j = k$, then $j \sim \ell$ follows directly from $k \sim \ell$.
        - If $k = \ell$, then $j \sim \ell$ follows directly from $j \sim k$.
        - If $j = \ell$, then $j \sim \ell$ holds by reflexivity.
    <2>3. Now assume $j, k, \ell$ are **three distinct indices**.
    <2>4. Since $j \sim k$ and $k \sim \ell$ with distinct indices, both transpositions belong to $H$:
        $$(j\,k) \in H \quad \text{and} \quad (k\,\ell) \in H.$$
    <2>5. Since $H$ is a subgroup, $H$ is closed under group multiplication.
    <2>6. Consider the product $(j\,k)(k\,\ell)(j\,k) \in H$:
        - Under $(j\,k)$: $j \mapsto k$, $k \mapsto j$, $\ell \mapsto \ell$.
        - Then under $(k\,\ell)$: $k \mapsto \ell$, $j \mapsto j$, $\ell \mapsto k$.
        - Then under $(j\,k)$: $\ell \mapsto \ell$, $j \mapsto k$, $k \mapsto j$.
        - Tracking each element through the composition $\sigma = (j\,k)(k\,\ell)(j\,k)$:
          - $\sigma(j) = (j\,k)(k\,\ell)(k) = (j\,k)(\ell) = \ell$.
          - $\sigma(\ell) = (j\,k)(k\,\ell)(\ell) = (j\,k)(k) = j$.
          - $\sigma(k) = (j\,k)(k\,\ell)(j) = (j\,k)(j) = k$.
          - For any other index $m \notin \{j, k, \ell\}$, $\sigma(m) = m$.
    <2>7. Thus the conjugation product is precisely the transposition $(j\,\ell)$:
        $$(j\,\ell) = (j\,k)(k\,\ell)(j\,k) \in H.$$
    <2>8. Since $(j\,\ell) \in H$, we have $j \sim \ell$.

<1>4. Conclusion:
    $\sim$ is reflexive, symmetric, and transitive, hence an equivalence relation on $\{1, 2, \dots, n\}$. Q.E.D.
:::
