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

::: {.warnings title="The converse of Lagrange's theorem is false"}
A finite group $G$ need not have a subgroup of order $n$ for every $n \divides \size G$.

The group $A_5$ has order $60$ and no subgroup of order $30$: such a subgroup would have index $2$, hence be normal, and $A_5$ is simple.

The group $A_4$ has order $12$ and no subgroup of order $6$.
Suppose $H\le A_4$ has order $6$.
The $3$-cycles generate $A_4$, so some $3$-cycle $x$ satisfies $x\notin H$.
Since $[A_4 : H] = 2$, two of the cosets $H, xH, x^2H$ coincide.
But $H = xH$ gives $x\in H$; $x^2 H = H$ gives $\inverseof{x} = x^2 \in H$, hence $x\in H$; and $xH = x^2H$ gives $x = \inverseof{x} x^2 \in H$.
$\contradiction$
:::

[[T-XDMK2]]

::: {.proof}
Let $p$ be a prime dividing $\size G$, and let $X = \theset{(g_1,\ldots,g_p)\in G^p \st g_1g_2\cdots g_p = e}$.
Choosing $g_1,\ldots,g_{p-1}$ freely determines $g_p$, so $\size X = \size G^{p-1}$, which is divisible by $p$.
The group $\ZZ/p$ acts on $X$ by cyclic rotation of the coordinates, since $g_1g_2\cdots g_p = e$ implies $g_2\cdots g_pg_1 = \inverseof{g_1} e\, g_1 = e$.
Each orbit has size $1$ or $p$, and the orbits of size $1$ are the tuples $(g,\ldots,g)$ with $g^p = e$.
Hence the number of $g\in G$ with $g^p=e$ is congruent to $\size X\equiv 0 \pmod p$; it is at least $1$, because $g=e$ qualifies, so it is at least $p$, and some $g\neq e$ has order $p$.
:::

## Actions

[[D-WYC7C]]

[[D-3T6O2]]

::: {.remark}
A point $x$ is fixed if and only if $\Orb(x) = \theset x$, equivalently $\Stab_G(x) = G$.
The notation is listed on [[algebra/groups/notation|Notation]].
:::

[[D-KGGWK]]

## The orbit-stabilizer theorem

[[PR-GSDKO]]

::: {.proof title="of orbit-stabilizer"}
Define $\Phi\colon G/G_x\to\Orb(x)$ by $\Phi(gG_x) = g\cdot x$.

- $\Phi$ is well defined: if $gG_x = hG_x$, then $\inverseof{g} h \in G_x$, so $h\cdot x = g\cdot\big((\inverseof{g} h)\cdot x\big) = g\cdot x$.

- $\Phi$ is injective: if $g\cdot x=h\cdot x$, then $\inverseof{g} h \cdot x = x$, so $\inverseof{g} h \in G_x$ and $gG_x = hG_x$.

- $\Phi$ is surjective, since every element of $\Orb(x)$ has the form $g\cdot x$.
:::

[[PR-KGHJ2]]

[[T-QYDVH]]

## Fixed points and nontrivial orbits

::: {.proposition}
For an action $\phi$ of a finite group $G$ on a finite set $X$, let $x_1,\ldots,x_r$ be representatives of the orbits of size greater than $1$.
Then
$$
\size X = \size{\Fix(\phi)} + \sum_{i=1}^r [G:\Stab(x_i)],
$$
and each $[G:\Stab(x_i)]$ is a divisor of $\size G$ greater than $1$.
:::

::: {.proof}
The orbits partition $X$, the orbits of size $1$ are the fixed points, and $\size{\Orb(x_i)} = [G:\Stab(x_i)]$ by orbit-stabilizer.
:::

The class equation is this formula for the conjugation action of $G$ on itself; see [[algebra/group-actions/the-class-equation|The class equation]].

## Four actions

::: {.example title="Left translation on $G$"}
$G$ acts on itself by $\phi\colon g \mapsto (h\mapsto gh)$.

- $\Orb(x) = G$, so the action is transitive.

- $\Stab(x) = \theset e$, and $\Fix(\phi) = \emptyset$ unless $G$ is trivial.

- The kernel is trivial, so $G$ embeds in the symmetric group on the set $G$ (Cayley's theorem).

- Orbit-stabilizer gives the bijection $G/\theset e \to G$.
:::

::: {.example title="Conjugation on $G$: centers and centralizers"}
$G$ acts on itself by $g\cdot x = gx\inverseof{g}$.

- $\Orb(x) = [x]$ is the [[D-HLDEY|conjugacy class]] of $x$.
  The orbit of $e$ is $\theset e$, so the action is transitive only when $G$ is trivial; every orbit is a singleton if and only if $G$ is abelian.

- $\Fix(\phi) = Z(G)$, the [[D-NK7G7|center]].

- $\Stab(x) = C_G(x)$, the [[D-PX64W|centralizer]] of $x$.

- The kernel is $Z(G)$.

- Orbit-stabilizer gives a bijection $G/C_G(x)\to[x]$, so the size of a conjugacy class is the index of the centralizer.
:::

::: {.example title="Conjugation on subgroups: normalizers"}
$G$ acts on $\theset{H \st H\leq G}$ by conjugation.

- $\Orb(H) = \theset{gH\inverseof{g} \st g\in G}$ is the set of conjugates of $H$.

- $\Fix(\phi)$ is the set of normal subgroups of $G$.

- $\Stab(H) = N_G(H)$ is the [[D-OZ2RR|normalizer]] of $H$.

- The kernel is $\Intersect_{H\leq G} N_G(H)$.

- Orbit-stabilizer gives the number of conjugates of $H$:
  $$
  \size{\theset{ gH\inverseof{g} \st g \in G } } = [G: N_G(H)].
  $$
:::

::: {.example title="Left translation on cosets: the normal core"}
For a proper subgroup $H < G$, $G$ acts on $G/H$ by left translation.

- $\Orb(eH) = G/H$, so the action is transitive.

- $\Stab(xH) = xH\inverseof{x}$, since
  $$
  \begin{aligned}
  \Stab(xH) &= \theset{g\in G\st gxH = xH} \\
  &= \theset{g\in G \st \inverseof{x} g x\in H} \\
  &= xH\inverseof{x}.
  \end{aligned}
  $$

- $\Fix(\phi) = \emptyset$, because the action is transitive and $\size{G/H} > 1$.

- The kernel is $\Intersect_{g\in G} gH\inverseof{g}$, the [[D-QMVEB|normal core]] of $H$, which is the largest normal subgroup of $G$ contained in $H$.

This action gives the index bounds on [[algebra/group-actions/show-g-is-not-simple#A subgroup of small index|Show $G$ is not simple]].
:::

## Exercises

[[E-M6XGF]]
