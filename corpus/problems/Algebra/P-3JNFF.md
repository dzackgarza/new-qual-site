---
schema: qual/card@1
id: P-3JNFF
kind: problem
title: Normal subgroups of $A_4$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Find all normal subgroups of $A_4$.
:::

::: solution
**Goal:** Determine every normal subgroup of $A_4$.

<1>1. The elements of $A_4$:
    *Proof:*
    <2>1. $|A_4| = 12$. The elements are: $e$, eight 3-cycles $(i\,j\,k)$, and three products of disjoint transpositions $(1\,2)(3\,4)$, $(1\,3)(2\,4)$, $(1\,4)(2\,3)$.
    <2>2. The conjugacy classes in $A_4$ are:
        - $\{e\}$ (size 1),
        - $\{(1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$ (size 3),
        - $\{(1\,2\,3), (1\,3\,4), (2\,4\,3), (1\,2\,4)\}$ (size 4),
        - $\{(1\,3\,2), (1\,4\,3), (2\,3\,4), (1\,4\,2)\}$ (size 4).

<1>2. Normal subgroups must be unions of conjugacy classes:
    *Proof:*
    <2>1. A subgroup $N \trianglelefteq A_4$ is a union of conjugacy classes (since $gNg^{-1} = N$), and must contain $\{e\}$.
    <2>2. By Lagrange's Theorem, $|N|$ divides $12$, so $|N| \in \{1, 2, 3, 4, 6, 12\}$.
    <2>3. We must find subsets of $\{1, 3, 4, 4\}$ (the conjugacy class sizes) that sum to a divisor of 12 and include the class $\{e\}$ of size 1.

<1>3. Enumeration:
    *Proof:*
    <2>1. $|N| = 1$: $N = \{e\}$. ✓
    <2>2. $|N| = 4$: $1 + 3 = 4$. Take $N = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$. This is the Klein four-group $V_4$, closed under multiplication, and a union of conjugacy classes. ✓
    <2>3. $|N| = 12$: $N = A_4$. ✓
    <2>4. $|N| = 2$: Need a conjugacy class of size 1 besides $\{e\}$. No such class exists.
    <2>5. $|N| = 3$: $1 + ?$. No conjugacy class has size 2. Not possible.
    <2>6. $|N| = 6$: $1 + 3 + ? = 6$ requires a class of size 2 (none exists), or $1 + 4 + ? = 6$ requires size 1 (only $\{e\}$ used). Not achievable.

<1>4. Conclusion:
    The normal subgroups of $A_4$ are exactly:
    $$\{e\}, \quad V_4 = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}, \quad A_4.$$
    Q.E.D.
:::
