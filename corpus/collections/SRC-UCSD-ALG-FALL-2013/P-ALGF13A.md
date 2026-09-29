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

::: {.problem}
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

::: pf

::: pf-step
Show that $C_G(P) \cap \Omega \subseteq P$:

::: pf-proof

::: pf-step
Let $g \in C_G(P) \cap \Omega$.

::: pf-proof
setup.
:::

:::

::: pf-step
$g$ commutes with every element of $P$ and $g^p = 1$, so $\langle g \rangle$ is a cyclic group of order 1 or $p$ centralizing $P$.

::: pf-proof
$g \in C_G(P)$ and $g \in \Omega$.
:::

:::

::: pf-step
Consider the subgroup $H = P\langle g\rangle \le G$.

::: pf-proof
since $g \in C_G(P)$, $\langle g \rangle$ normalizes $P$ (in fact centralizes $P$), so $P\langle g\rangle$ is a subgroup of $G$.
:::

:::

::: {.pf-step #s1-4}
The order of $H$ is $|H| = \frac{|P| |\langle g\rangle|}{|P \cap \langle g\rangle|}$.

::: pf-proof
product formula for subgroups.
:::

:::

::: pf-step
Since $|P| = p^a$ and $|\langle g\rangle| \in \{1, p\}$, $|H|$ is a power of $p$, so $H$ is a $p$-subgroup of $G$.

::: pf-proof
step [](#s1-4){.pf-ref}.
:::

:::

::: pf-step
$P \le H$ and $P$ is a Sylow $p$-subgroup of $G$ (a maximal $p$-subgroup), which implies $H = P$.

::: pf-proof
definition of Sylow $p$-subgroup.
:::

:::

::: pf-step
Thus $g \in P$, so $C_G(P) \cap \Omega \subseteq P$.

::: pf-proof
$g \in H = P$.
:::

:::

:::

:::

::: {.pf-step #s2}
Show that $C_G(P) \cap \Omega = Z(P) \cap \Omega$ is a non-trivial $p$-subgroup of $P$:

::: pf-proof

::: pf-step
Since $C_G(P) \cap \Omega \subseteq P$, $C_G(P) \cap \Omega = (C_G(P) \cap P) \cap \Omega = Z(P) \cap \Omega$.

::: pf-proof
$C_G(P) \cap P = Z(P)$.
:::

:::

::: {.pf-step #s2-2}
$Z(P) \cap \Omega = \{z \in Z(P) : z^p = 1\}$ is the $p$-torsion subgroup of the abelian group $Z(P)$, hence an elementary abelian $p$-subgroup.

::: pf-proof
$Z(P)$ is an abelian group, so the map $z \mapsto z^p$ is a homomorphism whose kernel is $Z(P) \cap \Omega$.
:::

:::

::: pf-step
Since $p \mid |G|$, $P$ is non-trivial ($|P| = p^a \ge p$), so the center $Z(P)$ is non-trivial ($|Z(P)| \ge p$).

::: pf-proof
non-trivial $p$-groups have non-trivial centers.
:::

:::

::: {.pf-step #s2-4}
By Cauchy's Theorem for abelian groups, $Z(P)$ contains an element of order $p$.

::: pf-proof
$p$ divides $|Z(P)|$.
:::

:::

::: pf-step
Thus $Z(P) \cap \Omega$ contains elements other than the identity, so $C_G(P) \cap \Omega$ is a non-trivial $p$-subgroup of $P$.

::: pf-proof
step [](#s2-2){.pf-ref} and step [](#s2-4){.pf-ref}.
:::

:::

:::

:::

:::

**Part (b).**

::: pf

::: pf-step
Consider the conjugation action of $P$ on $\Omega$: $(x, g) \mapsto xgx^{-1}$ for $x \in P, g \in \Omega$.

::: pf-proof

::: pf-step
For any $g \in \Omega$ and $x \in P$, $(xgx^{-1})^p = xg^p x^{-1} = x(1)x^{-1} = 1$, so $xgx^{-1} \in \Omega$.

::: pf-proof
conjugation preserves powers.
:::

:::

::: pf-step
This defines a valid group action of $P$ on the set $\Omega$.

::: pf-proof
$1g1^{-1} = g$ and $(xy)g(xy)^{-1} = x(ygy^{-1})x^{-1}$.
:::

:::

:::

:::

::: pf-step
Apply the fixed point congruence for $p$-group actions:

::: pf-proof

::: pf-step
The fixed point set of the action is:
\[
\Omega^P = \{g \in \Omega : xgx^{-1} = g \text{ for all } x \in P\} = \{g \in \Omega : g \in C_G(P)\} = C_G(P) \cap \Omega.
\]

::: pf-proof
definition of centralizer.
:::

:::

::: pf-step
Since $P$ is a $p$-group, the size of every non-trivial orbit is a multiple of $p$.

::: pf-proof
Orbit–Stabilizer Theorem: $|\operatorname{Orb}(g)| = [P : \operatorname{Stab}_P(g)]$, which divides $|P| = p^a$.
:::

:::

::: {.pf-step #s4-3}
Thus $|\Omega| \equiv |\Omega^P| \pmod p$.

::: pf-proof
partition of $\Omega$ into orbits.
:::

:::

:::

:::

::: {.pf-step #s5}
Determine $|\Omega^P| \pmod p$:

::: pf-proof

::: pf-step
By Part (a), $\Omega^P = Z(P) \cap \Omega$ is a non-trivial elementary abelian $p$-group.

::: pf-proof
step [](#s2){.pf-ref}.
:::

:::

::: pf-step
Thus $|\Omega^P| = p^k$ for some integer $k \ge 1$.

::: pf-proof
order of an elementary abelian $p$-group is $p^k$.
:::

:::

::: pf-step
In particular, $|\Omega^P| \equiv 0 \pmod p$.

::: pf-proof
$k \ge 1 \implies p \mid p^k$.
:::

:::

:::

:::

::: pf-step
Conclusion: $|\Omega| \equiv |\Omega^P| \equiv 0 \pmod p$, so $p$ divides $|\Omega|$.

::: pf-proof
step [](#s4-3){.pf-ref} and step [](#s5){.pf-ref}.
:::

:::

:::
:::
