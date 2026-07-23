---
schema: qual/card@1
id: P-LO76D
kind: problem
title: "Let $G$ be a finite group and let $N \\trianglelefteq G$,"
classification:
  areas:
  - algebra
  topics: []
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

    We can then write $|G| = p^n m$ where $n\geq l$ and $l\mid m$.

    By the third isomorphism theorem, we have
    $$\frac{G/N}{Q/N} \cong G/Q$$ and so
    $$\left| \frac{G/N}{Q/N} \right| = \frac{|G/N|}{|Q/N|} = \frac{p^k l}{p^k} = l$$

    and so $|G/Q| = l$ where $(p, l) = 1$, and thus
    $$|G/Q| = |G| / |Q| = l \implies |G| = |Q|~l.$$

    We then have $$p^n m = |Q|~l,$$

    and since $(p, l) = 1$, it must be the case that $p^n$ divides
    $|Q|$. But since $Q \leq G$, this means that $Q$ itself must be a
    Sylow $p-$ subgroup of $G$.

2.  Let $P_N \in \mathrm{Syl}(p, G/N)$. By the subgroup correspondence
    theorem, $P_n = H/N$ for some $H\leq G$ such that $N \subseteq H$.

    So choose $P_H \in \mathrm{Syl}(p, H)$; the claim is that
    $P_H \in \mathrm{Syl}(p, G)$ and that $\frac{P_HN}{N} \cong P_N$,
    which exhibits $P_N$ as the image of a Sylow $p-$subgroup of $G$.

    We first have $P_H \in \mathrm{Syl}(p, G)$, which follows because we
    have $[G/N, H/N] = [G: P_H]$ from the fourth isomorphism theorem,
    and thus $[G/N, P_N] = [G : P_H]$. In particular, since $P_N$ is a
    Sylow $p-$subgroup, $p$ does not divide $[G/N, P_N]$ and thus $p$
    doesn't divide $[G: P_H]$, which makes $P_H$ a maximal $p-$subgroup
    in $G$ and thus a Sylow $p-$subgroup.

    We then have $P_HN/N = P_N$, which follows because
    $P_H \leq H \implies P_HN/N \leq H/N = P_N \leq G/N$.

    However, it is also the case that $P_HN/N \in \mathrm{Syl}(p, G/N)$.
    This follows because

    1.  $P_HN/N = P_H/P_H \cap N$ by the 2nd isomorphism theorem, so it
        is a $p-$group.

    2.  $P_H \subseteq P_HN \subseteq G \implies p$ doesn't divide
        $[G: P_HN]$, since $P_H$ is also a Sylow $p-$group of $G$ and
        thus has maximal prime power dividing $\left| G \right|$.

    3.  $N \subseteq P_H N \subseteq G \implies [G/N : P_H N/ N] = [G: P_H N]$

    Taken together, this says that $P_H N/ N$ is a $p$-group and $p$
    doesn't divide $[G/N, P_HN / N]$, so it is a maximal $p-$subgroup
    and $P_HN/N \in \mathrm{Syl}(p, G/N)$.

    But since $P_HN/N \leq P_N$ and
    $\left|P_HN/N\right| = \left|P_N\right|$, we must have
    $P_HN/N = P_N$ as desired.

 ◻
:::

