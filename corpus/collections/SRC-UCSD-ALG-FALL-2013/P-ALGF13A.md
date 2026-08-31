---
schema: qual/card@1
id: P-ALGF13A
kind: problem
title: Centralizer meet $\Omega$ and $p$ dividing $|\Omega|$ for $g^p=1$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $G$ be a finite group.
Let $p$ be a prime factor of the order $|G|$ of $G$.
Let $\Omega = \{g \in G \mid g^p = 1\}$ and let $P$ be a Sylow $p$-subgroup of $G$.

(a) Prove that $C_G(P) \cap \Omega$ is a nontrivial $p$-subgroup of $P$.
(Hint: Consider $P\langle g\rangle$ for $g \in C_G(P) \cap \Omega$.)

(b) Prove that $p$ divides $|\Omega|$.
(Hint: Use the fact that $P$ acts on $\Omega$ by conjugation.)
:::

::: {.solution}
**Part (a).**

<1>1. Show that $C_G(P) \cap \Omega \subseteq P$: <2>1. Let $g \in C_G(P) \cap \Omega$.
::: {.proof}
setup.
:::
<2>2. $g$ commutes with every element of $P$ and $g^p = 1$, so $\langle g \rangle$ is a cyclic group of order 1 or $p$ centralizing $P$.
::: {.proof}
$g \in C_G(P)$ and $g \in \Omega$.
:::
<2>3. Consider the subgroup $H = P\langle g\rangle \le G$.
::: {.proof}
since $g \in C_G(P)$, $\langle g \rangle$ normalizes $P$ (in fact centralizes $P$), so $P\langle g\rangle$ is a subgroup of $G$.
:::
<2>4. The order of $H$ is $|H| = \frac{|P| |\langle g\rangle|}{|P \cap \langle g\rangle|}$.
::: {.proof}
product formula for subgroups.
:::
<2>5. Since $|P| = p^a$ and $|\langle g\rangle| \in \{1, p\}$, $|H|$ is a power of $p$, so $H$ is a $p$-subgroup of $G$.
::: {.proof}
<2>4. <2>6. $P \le H$ and $P$ is a Sylow $p$-subgroup of $G$ (a maximal $p$-subgroup), which implies $H = P$.
:::
::: {.proof}
definition of Sylow $p$-subgroup.
:::
<2>7. Thus $g \in P$, so $C_G(P) \cap \Omega \subseteq P$.
::: {.proof}
$g \in H = P$.
:::

<1>2. Show that $C_G(P) \cap \Omega = Z(P) \cap \Omega$ is a non-trivial $p$-subgroup of $P$: <2>1. Since $C_G(P) \cap \Omega \subseteq P$, $C_G(P) \cap \Omega = (C_G(P) \cap P) \cap \Omega = Z(P) \cap \Omega$.
::: {.proof}
$C_G(P) \cap P = Z(P)$.
:::
<2>2. $Z(P) \cap \Omega = \{z \in Z(P) : z^p = 1\}$ is the $p$-torsion subgroup of the abelian group $Z(P)$, hence an elementary abelian $p$-subgroup.
::: {.proof}
$Z(P)$ is an abelian group, so the map $z \mapsto z^p$ is a homomorphism whose kernel is $Z(P) \cap \Omega$.
:::
<2>3. Since $p \mid |G|$, $P$ is non-trivial ($|P| = p^a \ge p$), so the center $Z(P)$ is non-trivial ($|Z(P)| \ge p$).
::: {.proof}
non-trivial $p$-groups have non-trivial centers.
:::
<2>4. By Cauchy's Theorem for abelian groups, $Z(P)$ contains an element of order $p$.
::: {.proof}
$p$ divides $|Z(P)|$.
:::
<2>5. Thus $Z(P) \cap \Omega$ contains elements other than the identity, so $C_G(P) \cap \Omega$ is a non-trivial $p$-subgroup of $P$.
::: {.proof}
<2>2 and <2>4.
:::

**Part (b).**

<1>3. Consider the conjugation action of $P$ on $\Omega$: $(x, g) \mapsto xgx^{-1}$ for $x \in P, g \in \Omega$.
<2>1. For any $g \in \Omega$ and $x \in P$, $(xgx^{-1})^p = xg^p x^{-1} = x(1)x^{-1} = 1$, so $xgx^{-1} \in \Omega$.
::: {.proof}
conjugation preserves powers.
:::
<2>2. This defines a valid group action of $P$ on the set $\Omega$.
::: {.proof}
$1g1^{-1} = g$ and $(xy)g(xy)^{-1} = x(ygy^{-1})x^{-1}$.
:::

<1>4. Apply the fixed point congruence for $p$-group actions: <2>1. The fixed point set of the action is:
\[
\Omega^P = \{g \in \Omega : xgx^{-1} = g \text{ for all } x \in P\} = \{g \in \Omega : g \in C_G(P)\} = C_G(P) \cap \Omega.
\]
::: {.proof}
definition of centralizer.
:::
<2>2. Since $P$ is a $p$-group, the size of every non-trivial orbit is a multiple of $p$.
::: {.proof}
Orbit–Stabilizer Theorem: $|\operatorname{Orb}(g)| = [P : \operatorname{Stab}_P(g)]$, which divides $|P| = p^a$.
:::
<2>3. Thus $|\Omega| \equiv |\Omega^P| \pmod p$.
::: {.proof}
partition of $\Omega$ into orbits.
:::

<1>5. Determine $|\Omega^P| \pmod p$: <2>1. By Part (a), $\Omega^P = Z(P) \cap \Omega$ is a non-trivial elementary abelian $p$-group.
::: {.proof}
<1>2. <2>2. Thus $|\Omega^P| = p^k$ for some integer $k \ge 1$.
:::
::: {.proof}
order of an elementary abelian $p$-group is $p^k$.
:::
<2>3. In particular, $|\Omega^P| \equiv 0 \pmod p$.
::: {.proof}
$k \ge 1 \implies p \mid p^k$.
:::

<1>6. Conclusion: $|\Omega| \equiv |\Omega^P| \equiv 0 \pmod p$, so $p$ divides $|\Omega|$.
::: {.proof}
<2>3 and <1>5.
:::
Q.E.D.
:::
