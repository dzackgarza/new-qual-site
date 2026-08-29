---
schema: qual/card@1
id: E-AMD-Y5JUYURM
kind: exercise
title: Maximal subgroups of a $p$-group are normal
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Normal Subgroups
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.exercise}
Show that every maximal subgroup $M$ of a finite $p$-group $G$ is **normal** in $G$ (and has index $[G : M] = p$).
:::

::: solution
**Goal:** Prove that if $G$ is a finite $p$-group and $M < G$ is a maximal proper subgroup, then $M \trianglelefteq G$ with $[G : M] = p$.

<1>1. Method 1: The Normalizer Condition in Finite $p$-Groups:
    *Proof:*
    <2>1. Let $G$ be a finite $p$-group of order $|G| = p^n$ ($n \ge 1$), and let $H < G$ be any proper subgroup.
    <2>2. We recall the standard lemma: **Every proper subgroup of a finite $p$-group is properly contained in its normalizer**:
        $$H \subsetneq N_G(H).$$
    <2>3. *Proof of Lemma:*
        - Let $H$ act on the set of left cosets $G/H = \{ gH \mid g \in G \}$ by left translation: $h \cdot (gH) = (hg)H$.
        - The number of cosets is $|G/H| = [G : H]$, which is a power of $p$ since $|G| = p^n$ and $H < G$.
        - By the Orbit-Stabilizer / Fixed Point formula for $p$-group actions on finite sets:
          $$|G/H| \equiv |(G/H)^H| \pmod{p} \implies |(G/H)^H| \equiv 0 \pmod{p}.$$
        - A coset $gH$ is fixed by $H$ if and only if $h(gH) = gH$ for all $h \in H$, which means $g^{-1}hg \in H$ for all $h \in H$, i.e. $g \in N_G(H)$.
        - Thus the fixed point set is $(G/H)^H = N_G(H)/H$.
        - The identity coset $eH = H$ is always fixed, so $|N_G(H)/H| \ge 1$.
        - Since $|N_G(H)/H| \equiv 0 \pmod{p}$ and is non-empty, we must have $|N_G(H)/H| \ge p > 1$.
        - Therefore, $H \subsetneq N_G(H)$.

<1>2. Application to Maximal Subgroup $M$:
    *Proof:*
    <2>1. Let $M < G$ be a maximal subgroup.
    <2>2. Since $M$ is a proper subgroup, by Step 1 we have $M \subsetneq N_G(H) \le G$.
    <2>3. Since $M$ is maximal (there are no subgroups strictly between $M$ and $G$), the subgroup $N_G(M)$ must be all of $G$:
        $$N_G(M) = G.$$
    <2>4. By definition of the normalizer, $N_G(M) = G \iff M \trianglelefteq G$.

<1>3. Index of the Maximal Subgroup:
    *Proof:*
    <2>1. Since $M \trianglelefteq G$, the quotient group $G/M$ is a non-trivial $p$-group.
    <2>2. By the Subgroup Correspondence Theorem (Lattice Isomorphism Theorem), subgroups of $G/M$ correspond bijectively to subgroups of $G$ containing $M$.
    <2>3. Since $M$ is maximal in $G$, $G/M$ contains **no non-trivial proper subgroups**.
    <2>4. The only non-trivial groups with no proper non-trivial subgroups are cyclic groups of prime order.
    <2>5. Since $|G/M|$ is a power of $p$, we must have:
        $$G/M \cong \mathbb{Z}/p\mathbb{Z}, \qquad [G : M] = p.$$

<1>4. Alternative Proof by Induction on $|G|$:
    *Proof:*
    <2>1. Base case $|G| = p$: The only proper subgroup is $\{e\}$, which is normal.
    <2>2. Inductive step: The center $Z(G)$ is non-trivial for any finite $p$-group.
    <2>3. If $Z(G) \not\subseteq M$, then $MZ(G)$ is a subgroup strictly containing $M$, so $MZ(G) = G$. Since $Z(G)$ is central, $M \trianglelefteq MZ(G) = G$.
    <2>4. If $Z(G) \subseteq M$, pass to $G/Z(G)$, where $M/Z(G)$ is maximal in $G/Z(G)$. By induction, $M/Z(G) \trianglelefteq G/Z(G) \implies M \trianglelefteq G$.

<1>5. Conclusion:
    Every maximal subgroup of a finite $p$-group is normal and has index $p$. Q.E.D.
:::
