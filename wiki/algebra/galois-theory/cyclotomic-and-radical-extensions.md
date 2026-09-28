---
title: Cyclotomic and radical extensions
order: 20
topics:
- Roots of Unity
- Cyclic Groups
- Solvable Groups
---

# Cyclotomic and radical extensions

## Cyclotomic

[[D-JX3YC]]

[[FD-HM4P2]]

[[PR-JLDJ6]]

[[FF-MUJDE]] [[FF-UACKH]]

:::{.remark title="What is known without computing"}
$\QQ(\zeta_n)/\QQ$ is Galois of degree $\varphi(n)$, with
\[
\Gal(\QQ(\zeta_n)/\QQ) \cong (\ZZ/n)^\times
,\]
the isomorphism sending $\sigma_a: \zeta_n \mapsto \zeta_n^a$ to $a$.
Since the group is abelian, every subextension is normal, and the subfields correspond to the subgroups of $(\ZZ/n)^\times$.

For prime $p$, $\QQ(\zeta_p)$ has a unique subfield of each degree dividing $p-1$, since $(\ZZ/p)^\times$ is cyclic. For positive $a,b$, $\QQ(\zeta_a) = \QQ(\zeta_b)$ exactly when $a=b$, or one is twice the other and the latter is odd.

:::

## Radical extensions

:::{.remark title="$x^n - a$"}
For $a\in\QQ^\times$ and $n\geq1$, the splitting field of $x^n - a$ over $\QQ$ is $\QQ(\zeta_n, a^{1/n})$, which sits in a tower
\[
\QQ \subseteq \QQ(\zeta_n) \subseteq \QQ(\zeta_n, a^{1/n})
\]
with the first step abelian of degree $\varphi(n)$ and the second cyclic of degree dividing $n$.
The Galois group is therefore a subgroup of the semidirect product $\ZZ/n \semidirect (\ZZ/n)^\times$. It is the full group exactly when $x^n-a$ is irreducible over $\QQ(\zeta_n)$, so the second step has degree $n$.

This is why $x^3 - 2$ has group $S_3$: the tower is $\QQ \subseteq \QQ(\zeta_3)\subseteq \QQ(\zeta_3, 2^{1/3})$ of degrees $2$ and $3$, and the intermediate $\QQ(2^{1/3})$ is not normal.

:::

## Solvability

[[D-DFIDP]]

[[FD-T7IQV]]

[[T-QPMGT]]

[[T-EN5H4]]

:::{.remark title="Solvability by radicals"}
$f$ is solvable by radicals exactly when $\Gal(\SF(f)/\QQ)$ is a solvable group.
Since $S_n$ is solvable exactly for $n\leq 4$, and a generic quintic has group $S_5$, the general quintic is not solvable by radicals.

An irreducible quintic with exactly three real roots has group $S_5$: complex conjugation gives a transposition and irreducibility gives a $5\dash$cycle.

:::
