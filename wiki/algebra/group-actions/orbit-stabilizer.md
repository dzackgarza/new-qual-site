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

[[T-GJNT5]]

::: {.proof title="of Lagrange's theorem"}
Let $N \da [G:H]$ and write $G/H = \ts{g_1 H, \ldots, g_N H}$.
Two left cosets are equal or disjoint, and $x\mapsto g_kx$ is a bijection $H\to g_kH$, so
$$
G = \disjoint_{k=1}^N g_k H \implies \size G = \sum_{k=1}^N \size{g_k H} = \sum_{k=1}^N \size H = N \size H.
$$
Hence $\size G = [G:H]\,\size H$, and both $\size H$ and $[G:H]$ divide $\size G$.
:::

[[C-HWX2P]]

::: {.corollary}
For a finite group $G$ and $g\in G$, the order of $g$ divides $\size G$, and $g^{\size G} = e$.
:::

::: {.warnings title="The converse of Lagrange's theorem is false"}
A finite group $G$ need not have a subgroup of order $n$ for every $n \divides \size G$.

The group $A_5$ has order $60$ and no subgroup of order $30$: such a subgroup would have index $2$, hence be normal, and $A_5$ is simple.

The group $A_4$ has order $12$ and no subgroup of order $6$.
Suppose $H\le A_4$ has order $6$.
The $3$-cycles generate $A_4$, so some $3$-cycle $x$ satisfies $x\notin H$.
Since $[A_4 : H] = 2$, two of the cosets $H, xH, x^2H$ coincide.
But $H = xH$ gives $x\in H$; $x^2 H = H$ gives $x\inv = x^2 \in H$, hence $x\in H$; and $xH = x^2H$ gives $x = x\inv x^2 \in H$.
$\contradiction$
:::

[[T-3KCD6]]

::: {.proof}
Let $p$ be a prime dividing $\size G$, and let $X = \ts{(g_1,\ldots,g_p)\in G^p \st g_1g_2\cdots g_p = e}$.
Choosing $g_1,\ldots,g_{p-1}$ freely determines $g_p$, so $\size X = \size G^{p-1}$, which is divisible by $p$.
The group $\ZZ/p$ acts on $X$ by cyclic rotation of the coordinates, since $g_1g_2\cdots g_p = e$ implies $g_2\cdots g_pg_1 = g_1\inv e\, g_1 = e$.
Each orbit has size $1$ or $p$, and the orbits of size $1$ are the tuples $(g,\ldots,g)$ with $g^p = e$.
Hence the number of $g\in G$ with $g^p=e$ is congruent to $\size X\equiv 0 \pmod p$; it is at least $1$, because $g=e$ qualifies, so it is at least $p$, and some $g\neq e$ has order $p$.
:::

## Actions

[[D-3T6O2]]

::: {.remark}
Lying in the same orbit is an equivalence relation, so the orbits partition $X$, and $G$ acts transitively on each orbit.
A point $x$ is fixed if and only if $\Orb(x) = \ts x$, equivalently $\Stab_G(x) = G$.
The notation is listed on [[algebra/groups/notation|Notation]].
:::

::: {.fact}
For an action $\psi\colon G\to\Aut_\Set(X)$, the kernel is the intersection of the stabilizers:
$$
\ker \psi = \Intersect_{x\in X} G_x.
$$
:::

[[D-KGGWK]]

[[FD-KSKDG]]

[[FD-IGEOR]]

## The orbit-stabilizer theorem

[[PR-GSDKO]]

::: {.proof title="of orbit-stabilizer"}
Define $\Phi\colon G/G_x\to\Orb(x)$ by $\Phi(gG_x) = g\actson x$.

- $\Phi$ is well defined: if $gG_x = hG_x$, then $g\inv h \in G_x$, so $h\actson x = g\actson\big((g\inv h)\actson x\big) = g\actson x$.

- $\Phi$ is injective: if $g\actson x=h\actson x$, then $g\inv h \actson x = x$, so $g\inv h \in G_x$ and $gG_x = hG_x$.

- $\Phi$ is surjective, since every element of $\Orb(x)$ has the form $g\actson x$.
:::

[[PR-KGHJ2]]

::: {.proof title="that stabilizers along an orbit are conjugate"}
Let $x\in X$ and $y\in \Orb(x)$, choose $g\in G$ with $g\actson x=y$, and write $H_x \da \Stab(x)$ and $H_y\da \Stab(y)$.
Then
$$
\begin{aligned}
h\in H_x &\iff hx = x \\
&\iff hg\inv y = g\inv y \\
&\iff ghg\inv y = y \\
&\iff ghg\inv \in H_y \\
&\iff h\in g\inv H_y g,
\end{aligned}
$$
so $H_x = g\inv H_y g$.
:::

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

- $\Stab(x) = \ts e$, and $\Fix(\phi) = \emptyset$ unless $G$ is trivial.

- The kernel is trivial, so $G$ embeds in the symmetric group on the set $G$ (Cayley's theorem).

- Orbit-stabilizer gives the bijection $G/\ts e \to G$.
:::

::: {.example title="Conjugation on $G$: centers and centralizers"}
$G$ acts on itself by $g\actson x = gxg\inv$.

- $\Orb(x) = [x]$ is the [[D-HLDEY|conjugacy class]] of $x$.
  The orbit of $e$ is $\ts e$, so the action is transitive only when $G$ is trivial; every orbit is a singleton if and only if $G$ is abelian.

- $\Fix(\phi) = Z(G)$, the [[D-NK7G7|center]].

- $\Stab(x) = C_G(x)$, the [[D-PX64W|centralizer]] of $x$.

- The kernel is $Z(G)$.

- Orbit-stabilizer gives a bijection $G/C_G(x)\to[x]$, so the size of a conjugacy class is the index of the centralizer.
:::

::: {.example title="Conjugation on subgroups: normalizers"}
$G$ acts on $\ts{H \st H\leq G}$ by conjugation.

- $\Orb(H) = \ts{gHg\inv \st g\in G}$ is the set of conjugates of $H$.

- $\Fix(\phi)$ is the set of normal subgroups of $G$.

- $\Stab(H) = N_G(H)$ is the [[D-OZ2RR|normalizer]] of $H$.

- The kernel is $\Intersect_{H\leq G} N_G(H)$.

- Orbit-stabilizer gives the number of conjugates of $H$:
$$
\size{\ts{ gHg ^{-1} \st g \in G } } = [G: N_G(H)].
$$
:::

::: {.example title="Left translation on cosets: the normal core"}
For a proper subgroup $H < G$, $G$ acts on $G/H$ by left translation.

- $\Orb(eH) = G/H$, so the action is transitive.

- $\Stab(xH) = xHx\inv$, since
$$
\begin{aligned}
\Stab(xH) &= \ts{g\in G\st gxH = xH} \\
&= \ts{g\in G \st x\inv g x\in H} \\
&= xHx\inv.
\end{aligned}
$$

- $\Fix(\phi) = \emptyset$, because the action is transitive and $\size{G/H} > 1$.

- The kernel is $\Intersect_{g\in G} gHg\inv$, the [[D-QMVEB|normal core]] of $H$, which is the largest normal subgroup of $G$ contained in $H$.

This action gives the index bounds on [[algebra/group-actions/show-g-is-not-simple#A subgroup of small index|Show $G$ is not simple]].
:::

## Exercises

[[E-M6XGF]]
