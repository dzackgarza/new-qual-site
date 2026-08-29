---
schema: qual/card@1
id: P-HGRO28
kind: problem
title: A Sylow normalizer is self-normalizing
classification:
  areas: [algebra]
  topics: [Sylow Theory]
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $P = S_p$ be a Sylow $p$-subgroup of a finite group $G$.
Prove that the normalizer of $N_G(P)$ is self-normalizing:
$$N_G\bigl(N_G(P)\bigr) = N_G(P).$$
:::

::: solution
**Goal:** Prove that $N_G(N_G(P)) = N_G(P)$ for any Sylow $p$-subgroup $P$ of a finite group $G$ using the Frattini Argument / Sylow's Theorem.

<1>1. Setting and Containments:
    *Proof:*
    <2>1. Let $P$ be a Sylow $p$-subgroup of $G$, and let $N \coloneqq N_G(P)$ be its normalizer in $G$.
    <2>2. By definition of the normalizer of a subgroup, $N \subseteq N_G(N)$.
    <2>3. It remains to show the reverse containment: $N_G(N) \subseteq N$.

<1>2. Proof via Sylow Conjugacy in $N_G(N)$:
    *Proof:*
    <2>1. Let $g \in N_G(N)$.
    <2>2. By definition of $N_G(N)$, conjugation by $g$ stabilizes $N$:
        $$g N g^{-1} = N.$$
    <2>3. Since $P \le N$, conjugating $P$ by $g$ gives a subgroup:
        $$g P g^{-1} \le g N g^{-1} = N.$$
    <2>4. Since $|g P g^{-1}| = |P|$, $g P g^{-1}$ is a $p$-subgroup of $N$ of maximum possible size $|P|$ (since $|P|$ is the full $p$-part of $|G|$, hence also the full $p$-part of $|N|$).
    <2>5. Thus $P$ and $g P g^{-1}$ are both **Sylow $p$-subgroups of the subgroup $N$**.
    <2>6. By **Sylow's Second Theorem** applied inside the group $N$, any two Sylow $p$-subgroups of $N$ are conjugate by an element of $N$.
    <2>7. Therefore, there exists some $n \in N$ such that:
        $$g P g^{-1} = n P n^{-1}.$$
    <2>8. Multiplying both sides by $n^{-1}$:
        $$(n^{-1} g) P (n^{-1} g)^{-1} = P.$$
    <2>9. This equation states that $n^{-1} g$ normalizes $P$, which means:
        $$n^{-1} g \in N_G(P) = N.$$
    <2>10. Since $n \in N$ and $n^{-1} g \in N$, their product is in $N$:
        $$g = n (n^{-1} g) \in N.$$
    <2>11. Since $g \in N_G(N)$ was arbitrary, we have proven $N_G(N) \subseteq N$.

<1>3. Conclusion:
    Combining $N \subseteq N_G(N)$ and $N_G(N) \subseteq N$ establishes:
    $$N_G(N_G(P)) = N_G(P).$$
    Q.E.D.
:::
