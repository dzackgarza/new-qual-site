---
title: Cyclotomic and radical extensions
order: 20
topics:
- Roots of Unity
- Cyclic Groups
- Solvable Groups
---

# Cyclotomic and radical extensions

## Cyclotomic extensions

[[D-JX3YC]]

[[FD-HM4P2]]

[[PR-JLDJ6]]

[[FF-MUJDE]] [[FF-UACKH]]

::: {.remark title="Galois group of $\QQ(\zeta_n)/\QQ$"}
For a primitive $n$th root of unity $\zeta_n$, $\QQ(\zeta_n)/\QQ$ is Galois of degree $\phi(n)$, and
$$
\Gal(\QQ(\zeta_n)/\QQ) \cong (\ZZ/n)^\times,
$$
where the automorphism $\sigma_a\colon \zeta_n \mapsto \zeta_n^a$ corresponds to $a$.
The group is abelian, so every intermediate field is Galois over $\QQ$, and the intermediate fields correspond to the subgroups of $(\ZZ/n)^\times$.

For a prime $p$, $(\ZZ/p)^\times$ is cyclic of order $p-1$, so $\QQ(\zeta_p)$ has exactly one subfield of each degree dividing $p-1$.
For positive integers $a\neq b$, $\QQ(\zeta_a) = \QQ(\zeta_b)$ if and only if one of $a,b$ is odd and the other is twice it.
:::

## Radical extensions

::: {.remark title="$x^n - a$"}
For $a\in\QQ^\times$, the splitting field of $x^n - a$ over $\QQ$ is $\QQ(\zeta_n, a^{1/n})$, and the tower
$$
\QQ \subseteq \QQ(\zeta_n) \subseteq \QQ(\zeta_n, a^{1/n})
$$
has first step abelian of degree $\phi(n)$ and second step cyclic of degree dividing $n$.
The Galois group embeds in $\ZZ/n \semidirect (\ZZ/n)^\times$, with $(\ZZ/n)^\times$ acting on $\ZZ/n$ by multiplication, and the embedding is an isomorphism if and only if $x^n - a$ is irreducible over $\QQ(\zeta_n)$.

For $x^3 - 2$, the tower $\QQ \subseteq \QQ(\zeta_3)\subseteq \QQ(\zeta_3, 2^{1/3})$ has degrees $2$ and $3$, so the Galois group has order $6$; it is nonabelian because $\QQ(2^{1/3})$ is not normal over $\QQ$, so it is $S_3\cong\ZZ/3\semidirect(\ZZ/3)^\times$.
:::

## Solvability

[[D-DFIDP]]

[[FD-T7IQV]]

[[T-QPMGT]]

[[T-EN5H4]]

::: {.remark title="Solvability by radicals"}
Over a field $K$ of characteristic $0$, a polynomial $f\in K[x]$ is solvable by radicals if and only if $\Gal(\SF(f)/K)$ is a [[D-DFIDP|solvable group]]. The symmetric group $S_n$ is solvable if and only if $n\leq 4$.
For example, $f = x^5-4x+2$ is irreducible by Eisenstein's criterion at $2$ and has exactly three real roots, so complex conjugation gives a transposition in its Galois group and irreducibility gives a $5$-cycle; hence its Galois group is $S_5$, and $f$ is not solvable by radicals.
:::
