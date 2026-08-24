---
schema: qual/card@1
id: P-LO76D
kind: problem
title: If $Q/N$ is a Sylow $p$-subgroup of $G/N$ then $Q$ contains a Sylow $p$-subgroup
  of $G$, and every Sylow $p$-subgroup of $G/N$ is such an image
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - Isomorphism Theorems
relations: []
review: draft
---

:::{.problem}
Let $G$ be a finite group and let $N \trianglelefteq G$,
and let $p$ be a prime number and $Q$ a subgroup of $G$ such that
$N \subset Q$ and $Q/N$ is a Sylow $p-$subgroup of $G/N$.

1.  Prove that $Q$ contains a Sylow $p-$subgroup of $G$.

2.  Prove that every Sylow $p-$subgroup of $G/N$ is the image of a Sylow
    $p-$subgroup of $G$.
:::

:::{.solution}
*Proof.*

1.  Since $Q/N$ is a Sylow $p-$subgroup of $G/N$, we can write
    $|G/N| = p^k l$ where $\gcd(p, l) = 1$, and $|Q/N| = p^k$.

    We can then write $|G| = p^n m$ with $\gcd(p, m) = 1$, where $n\geq k$ and $l\mid m$.

    By the third isomorphism theorem, we have
    $$\frac{G/N}{Q/N} \cong G/Q$$ and so
    $$\left| \frac{G/N}{Q/N} \right| = \frac{|G/N|}{|Q/N|} = \frac{p^k l}{p^k} = l$$

    and so $|G/Q| = l$ where $(p, l) = 1$, and thus
    $$|G/Q| = |G| / |Q| = l \implies |G| = |Q|~l.$$

    We then have $$p^n m = |Q|~l,$$

    and since $(p, l) = 1$, it must be the case that $p^n$ divides
    $|Q|$.

    So take $P \in \mathrm{Syl}(p, Q)$, a Sylow $p-$subgroup of $Q$. Then
    $|P| = p^n$, since $p^n$ is the full power of $p$ dividing $|Q|$, and
    $p^n$ is also the full power of $p$ dividing $|G|$. So $P$ is a Sylow
    $p-$subgroup of $G$ contained in $Q$, which is what was asked.

    Note that $Q$ itself need not be a Sylow $p-$subgroup: $p^n$ divides
    $|Q|$, but $|Q| = |G|/l$ carries the factor $m/l$ as well, so $Q$ is a
    $p-$group only in the case $m = l$.

2.  Let $P_N \in \mathrm{Syl}(p, G/N)$. By the subgroup correspondence
    theorem, $P_N = H/N$ for some $H\leq G$ such that $N \subseteq H$.

    So choose $P_H \in \mathrm{Syl}(p, H)$; the claim is that
    $P_H \in \mathrm{Syl}(p, G)$ and that $\frac{P_HN}{N} \cong P_N$,
    which exhibits $P_N$ as the image of a Sylow $p-$subgroup of $G$.

    We first have $P_H \in \mathrm{Syl}(p, G)$. Factor the index through
    $H$:
    $$[G : P_H] = [G : H]\,[H : P_H].$$
    Here $p$ does not divide $[H : P_H]$, since $P_H$ is Sylow in $H$.
    And by the correspondence theorem $[G : H] = [G/N : H/N] = [G/N :
    P_N]$, which $p$ does not divide either, since $P_N$ is Sylow in
    $G/N$. So $p$ does not divide $[G: P_H]$, which makes $P_H$ a maximal
    $p-$subgroup in $G$ and thus a Sylow $p-$subgroup.

    We then have $P_HN/N \leq P_N$, because
    $P_H \leq H$ and $N \leq H$ give $P_H N \leq H$, so
    $P_HN/N \leq H/N = P_N \leq G/N$.

    However, it is also the case that $P_HN/N \in \mathrm{Syl}(p, G/N)$.
    This follows because

    1.  $P_HN/N \cong P_H/(P_H \cap N)$ by the 2nd isomorphism theorem,
        a quotient of a $p-$group, so it is a $p-$group.

    2.  $P_H \subseteq P_HN \subseteq G \implies p$ doesn't divide
        $[G: P_HN]$, since $P_H$ is also a Sylow $p-$group of $G$ and
        thus has maximal prime power dividing $\left| G \right|$.

    3.  $N \subseteq P_H N \subseteq G \implies [G/N : P_H N/ N] = [G: P_H N]$

    Taken together, this says that $P_H N/ N$ is a $p$-group and $p$
    doesn't divide $[G/N : P_HN / N]$, so it is a maximal $p-$subgroup
    and $P_HN/N \in \mathrm{Syl}(p, G/N)$.

    But since $P_HN/N \leq P_N$ and
    $\left|P_HN/N\right| = \left|P_N\right|$, we must have
    $P_HN/N = P_N$ as desired.

 ◻
:::

