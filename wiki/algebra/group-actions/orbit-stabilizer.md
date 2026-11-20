---
title: Orbit-stabilizer
order: 10
topics:
- Group Actions
- Orbit-Stabilizer
- Cosets and Lagrange
---

# Orbit-stabilizer

## Lagrange and Cauchy

[[E-NNTQB]]

The converse of Lagrange's theorem fails, and the two standard counterexamples are on [[algebra/counterexamples|Counterexamples]]: $A_4$ has order $12$ and no subgroup of order $6$, and $A_5$ has order $60$ and no subgroup of order $30$.
Cauchy's theorem is the converse for prime divisors.

[[T-XDMK2]]

## Actions

[[D-WYC7C]]

[[D-3T6O2]]

[[D-KGGWK]]

## The orbit-stabilizer theorem

[[PR-GSDKO]]

[[PR-KGHJ2]]

[[T-QYDVH]]

## Fixed points and nontrivial orbits

::: {.fact title="A finite set is a fixed-point set plus orbits"}
The orbits partition the set, the orbits of size one are the fixed points, and every other orbit has size $[G:G_x]$, so the size of a finite set is the number of fixed points plus a sum of indices of stabilizers, each of them a divisor of $\size G$ greater than $1$.
:::

[[L-DJKXL]]

For the conjugation action of $G$ on itself that count is the class equation, on [[algebra/group-actions/the-class-equation|The class equation]].

## Four actions

::: {.example title="Left translation on $G$"}
$G$ acts on itself by $g\cdot x = gx$.

- The orbit $Gx$ is all of $G$, so the action is transitive.

- The stabilizer $G_x$ is trivial, and the fixed-point set is empty unless $G$ is trivial.

- The kernel is trivial, so $G$ embeds in the symmetric group on the set $G$, which is Cayley's theorem.

- Orbit-stabilizer gives the bijection $G/\theset e\to G$.
:::

::: {.example title="Conjugation on $G$: centers and centralizers"}
$G$ acts on itself by $g\cdot x = gx\inverseof{g}$.

- The orbit $Gx$ is the [[D-HLDEY|conjugacy class]] $\Cl_G(x)$. The orbit of $e$ is $\theset e$, so the action is transitive only when $G$ is trivial, and every orbit is a singleton exactly when $G$ is abelian.

- The fixed-point set $G^G$ of the action is the [[D-NK7G7|center]] $Z(G)$.

- The stabilizer $G_x$ is the [[D-PX64W|centralizer]] $C_G(x)$, and the kernel of the action is $Z(G)$.

- Orbit-stabilizer gives a bijection $G/C_G(x)\to\Cl_G(x)$, so the size of a conjugacy class is the index of its centralizer.
:::

::: {.example title="Conjugation on subgroups: normalizers"}
$G$ acts on the set of its subgroups by $g\cdot H = gH\inverseof{g}$.

- The orbit $GH$ is the set of subgroups [[D-ES7MP|conjugate]] to $H$.

- The fixed-point set is the set of normal subgroups of $G$.

- The stabilizer $G_H$ is the [[D-OZ2RR|normalizer]] $N_G(H)$, and the kernel of the action is $\Intersect_{H\leq G} N_G(H)$.

- Orbit-stabilizer gives the number of conjugates of $H$:
  $$
  \size{\theset{ gH\inverseof{g} \st g \in G } } = [G: N_G(H)].
  $$
:::

::: {.example title="Left translation on cosets: the normal core"}
For a proper subgroup $H < G$, $G$ acts on $G/H$ by left translation.

- The orbit of $eH$ is $G/H$, so the action is transitive.

- The stabilizer of $xH$ is $xH\inverseof{x}$, since
  $$
  \begin{aligned}
  G_{xH} &= \theset{g\in G\st gxH = xH} \\
  &= \theset{g\in G \st \inverseof{x} g x\in H} \\
  &= xH\inverseof{x}.
  \end{aligned}
  $$

- The fixed-point set is empty, because the action is transitive and $\size{G/H} > 1$.

- The kernel is $\Intersect_{g\in G} gH\inverseof{g}$, the [[D-QMVEB|normal core]] of $H$, which is the largest normal subgroup of $G$ contained in $H$.

This action gives the index bounds on [[algebra/group-actions/show-g-is-not-simple#A subgroup of small index|Show $G$ is not simple]].
:::

## Exercises

[[E-M6XGF]]
