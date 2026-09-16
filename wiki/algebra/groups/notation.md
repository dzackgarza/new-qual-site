---
order: 0
---

# Notation

Throughout, $G$ is a group, $H\le G$ is a subgroup, $g,h,x\in G$, and $X$ is a set.

## Subsets and subgroups

| Notation | Name | Definition |
| --- | --- | --- |
| $\mcp(X)$, $2^X$ | power set of $X$ | the set of subsets of $X$, in bijection with $\Hom_\Set(X,\ts{0,1})$ |
| $[g,h]$ | [[D-BQ4BQ\|commutator]] of $g$ and $h$ | $ghg\inv h\inv$ |
| $[G,H]$ | commutator subgroup of $G$ and $H$ | $\gens{[g,h] \st g\in G,\ h\in H}$ |
| $Z(G)$ | [[D-NK7G7\|center]] of $G$ | $\ts{x\in G \st gxg\inv = x \text{ for all } g\in G}$ |
| $C_G(x)$, $Z(x)$ | [[D-PX64W\|centralizer]] of $x$ | $\ts{g\in G \st [g,x]=1}$ |
| $C_G(H)$, $Z_G(H)$ | [[D-PX64W\|centralizer]] of $H$ | $\ts{g\in G \st [g,h]=1 \text{ for all } h\in H} = \Intersect_{h\in H} C_G(h)$ |
| $[x]$, $\Conj(x)$ | [[D-HLDEY\|conjugacy class]] of $x$ | $\ts{gxg\inv \st g\in G}\subseteq G$ |
| $N_G(H)$ | [[D-OZ2RR\|normalizer]] of $H$ | $\ts{g\in G \st gHg\inv = H}\le G$ |
| $\Inn(G)$ | inner automorphisms | $\ts{\varphi_g \st g\in G}\le\Aut(G)$, where $\varphi_g(x) = gxg\inv$ |
| $\Out(G)$ | outer automorphisms | $\Aut(G)/\Inn(G)$ |

## Group actions

For a [[D-3T6O2|group action]] of $G$ on $X$, given by a homomorphism $\phi\colon G\to\Aut_\Set(X)$, and for $x\in X$:

| Notation | Name | Definition |
| --- | --- | --- |
| $g\cdot x$ | action of $g$ on $x$ | $\phi(g)(x)$ |
| $\Orb(x)$, $Gx$ | [[D-WYC7C\|orbit]] of $x$ | $\ts{g\cdot x \st g\in G}\subseteq X$ |
| $\Stab(x)$, $\Stab_G(x)$, $G_x$ | [[D-WYC7C\|stabilizer]] of $x$ | $\ts{g\in G \st g\cdot x = x}\le G$ |
| $X/G$ | set of orbits | $\ts{\Orb(x) \st x\in X}\subseteq 2^X$ |
| $\Fix(X)$, $\Fix_G(X)$, $X^G$ | set of fixed points | $\ts{x\in X \st g\cdot x = x \text{ for all } g\in G}\subseteq X$ |
