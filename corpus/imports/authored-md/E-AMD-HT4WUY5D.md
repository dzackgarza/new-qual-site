---
schema: qual/card@1
id: E-AMD-HT4WUY5D
kind: exercise
title: Normality is not transitive
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Counterexamples
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Give an example showing that normality is not transitive: i.e. $H\trianglelefteq K \trianglelefteq G$ with $H$ *not* normal in $G$.
:::

::: solution
**Goal:** Construct an explicit example of a group $G$ and subgroups $H \le K \le G$ such that $H \trianglelefteq K$ and $K \trianglelefteq G$, but $H \not\trianglelefteq G$.

<1>1. Construction in the dihedral group $D_4$:
    *Proof:*
    <2>1. Let $G = D_4 = \langle r, s \mid r^4 = 1, \, s^2 = 1, \, s r s^{-1} = r^{-1} \rangle$ be the dihedral group of order $8$.
    <2>2. Define the subgroup $K = \{e, r^2, s, s r^2\} = \langle r^2, s \rangle \le G$.
    <2>3. Define the subgroup $H = \{e, s\} = \langle s \rangle \le K$.

<1>2. Proof that $K \trianglelefteq G$:
    *Proof:*
    <2>1. The index of $K$ in $G$ is $[G : K] = \frac{|G|}{|K|} = \frac{8}{4} = 2$.
    <2>2. Any subgroup of index $2$ is normal, so $K \trianglelefteq G$.

<1>3. Proof that $H \trianglelefteq K$:
    *Proof:*
    <2>1. The index of $H$ in $K$ is $[K : H] = \frac{|K|}{|H|} = \frac{4}{2} = 2$.
    <2>2. Any subgroup of index $2$ is normal (or since $K \cong \mathbb{Z}_2 \times \mathbb{Z}_2$ is abelian, every subgroup of $K$ is normal in $K$).
    <2>3. Thus $H \trianglelefteq K$.

<1>4. Proof that $H \not\trianglelefteq G$:
    *Proof:*
    <2>1. Consider the element $r \in G$ and $s \in H$.
    <2>2. Compute the conjugate of $s$ by $r$:
        $$r s r^{-1} = r (s r^3) = r (r s) = r^2 s = s r^{-2} = s r^2.$$
    <2>3. The conjugate $s r^2 \notin H = \{e, s\}$.
    <2>4. Therefore $r H r^{-1} \neq H$, so $H$ is not a normal subgroup of $G$.

<1>5. Alternative example in $A_4$:
    *Proof:*
    <2>1. In $G = A_4$, the Klein four-group $K = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$ is normal in $A_4$.
    <2>2. The subgroup $H = \{e, (1\,2)(3\,4)\}$ is of index $2$ in $K$, hence $H \trianglelefteq K$.
    <2>3. Conjugating $(1\,2)(3\,4)$ by $(1\,2\,3) \in A_4$ gives $(1\,3)(2\,4) \notin H$, so $H \not\trianglelefteq A_4$.

<1>6. Conclusion:
    Normality is not a transitive relation on subgroups. Q.E.D.
:::
