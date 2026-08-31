---
title: Orbit-stabilizer
order: 10
problems:
  topics:
  - Group Actions
  - Orbit-Stabilizer
  - Cosets and Lagrange
---

# Orbit-stabilizer

## Counting first: Lagrange and Cauchy

[[T-GJNT5]]

:::{.proof title="of Lagrange's theorem"}
Write $G/H = \ts{g_0 H, g_1 H, \cdots, g_N H}$ for $N \da [G:H]$.
Cosets are equal or disjoint and all have the same cardinality, so
\[
G = \disjoint_{k \leq N} g_k H \implies \size G = \sum_{k\leq N} \size \qty{g_k H} = \sum_{k\leq N} \size H = N \size H
,\]
giving $\size G = N\size H$: both $\size H$ and $[G:H]$ divide $\size G$.

:::

[[C-HWX2P]]

:::{.corollary}
The order of every element divides the order of $G$:
$$
g\in G \implies o(g) \divides o(G) \implies g^{\abs G} = e
.$$

:::

:::{.warnings title="The converse of Lagrange is false"}
There need not be an $H\leq G$ of order $n$ for every $n \divides \size G$.

$A_5$ has order $60$ and no subgroup of order $30$: such a subgroup would have index $2$, hence be normal, contradicting simplicity of $A_{n\geq 5}$.

More directly, $\size{A_4} = 12$ and $A_4$ has no subgroup of order $6$.
Such an $H$ could not contain every $3\dash$cycle, since those generate $A_4$.
Take a $3\dash$cycle $x\notin H$; then $[A_4 : H] = 2$, so among $H, xH, x^2H$ two coincide.
$x\notin H$ rules out $H = xH$; $x^2 H = H$ gives $x\inv = x^2 \in H$ hence $x\in H$; and $xH = x^2H$ gives $x\inv x^2 = x \in H$.
$\contradiction$

:::

[[T-3KCD6]]

:::{.proof}
See [Keith Conrad's notes on proofs of Cauchy's theorem](https://kconrad.math.uconn.edu/blurbs/grouptheory/cauchypf.pdf).

:::

## Actions

[[D-3T6O2]]

:::{.remark}
Being in the same orbit is an equivalence relation, so orbits partition $X$, and $G$ acts transitively on each one.
A point is fixed exactly when $\Orb(x) = \ts x$, equivalently when $\Stab_G(x) = G$.
Notation is on [[algebra/groups/notation|the algebra notation page]].

:::

:::{.fact}
For any action, the kernel is the intersection of the stabilizers:
\[
\ker \psi = \Intersect_{x\in X} G_x
.\]
This one identity is behind most of the examples below: each choice of $X$ turns it into a statement about centres, centralizers or normalizers.

:::

[[D-KGGWK]]

[[FD-KSKDG]]

[[FD-IGEOR]] [[FD-W3MQW]]

## The theorem

[[PR-GSDKO]]

:::{.proof title="of orbit-stabilizer"}
\envlist

- Well defined: $gG_x = hG_x \iff gh\inv \in G_x \iff g\inv h\actson x = x$, and then
  \[
  \Phi(hG_x) \da h\actson x = (gg\inv) h\actson x = g(g\inv h)\actson x = g\actson x = \Phi(gG_x)
  .\]

- Injective: $\Phi(gG_x) = \Phi(hG_x) \iff g\actson x=h\actson x \iff gh\inv \actson x = x \iff gh\inv \in G_x \iff gG_x = hG_x$.

- Surjective: this is transitivity onto the orbit.

:::

[[PR-KGHJ2]]

:::{.proof title="that stabilizers along an orbit are conjugate"}
\envlist

- Fix $x\in X$ and $y\in \Orb(x)$, so $g\actson x=y$ for some $g$, and write $H_x \da \Stab(x)$, $H_y\da \Stab(y)$.
- Then
\[
h\in H_x &\iff hx = x \\
&\iff hg\inv y = g\inv y \\
&\iff ghg\inv y = y \\
&\iff ghg\inv \in H_y \\
&\iff h\in g\inv H_y g
,\]
so $H_x = g\inv H_y g$.

:::

[[T-QYDVH]]

## The counting trick

:::{.remark title="Fixed points plus nontrivial orbits"}
Since orbits partition $X$, for any action $\phi: G\actson X$,
\[
X = \Fix(\phi) + \Disjoint_{x}' \Orb(x)
,\]
where $\Fix(\phi)$ collects the orbits of size one and the remaining union takes one representative from each nontrivial orbit.
Substituting orbit-stabilizer into the second term is how every counting formula in this chapter is produced, the class equation included.

:::

## The four standard actions

:::{.example title="Left translation on $G$"}
$G$ acts on itself by $\phi: g \mapsto (h\mapsto gh)$.

- $\Orb(x) = G$, so the action is transitive.
- $\Fix(\phi) = \ts e$ and $\Stab(x) = \ts e$.
- The kernel is trivial.
- Orbit-stabilizer says only $G \cong G/\ts e$.

:::

:::{.example title="Conjugation on $G$: centres and centralizers"}
$G$ acts on itself by $g\actson x = gxg\inv$.

- $\Orb(g) = [g]$ is the conjugacy class.
  The action is transitive only when $\size G \leq 2$; every orbit is a singleton exactly when $G$ is abelian.
- $\Fix(\phi) = Z(G)$, the centre.
- $\Stab(g) = Z(g)$, the centralizer.
- The kernel is again $Z(G)$.
- Orbit-stabilizer says $[g] \cong G/Z(g)$: **the size of a conjugacy class is the index of the centralizer**.

:::

:::{.example title="Conjugation on subgroups: normalizers"}
$G$ acts on $\ts{H \st H\leq G}$ by conjugation.

- $\Orb(H) = \ts{gHg\inv \st g\in G}$ is the set of conjugates of $H$.
- $\Fix(\phi)$ is the set of normal subgroups.
- $\Stab(H) = N_G(H)$ is the normalizer.
- The kernel is $\Intersect_{H\leq G} N_G(H)$.
- Orbit-stabilizer gives the count that Sylow 3 uses:
\[
\size{\ts{ gHg ^{-1} \st g \in G } } = [G: N_G(H)]
.\]

:::

:::{.example title="Left translation on cosets: the normal core"}
For $H < G$ proper, $G$ acts on $G/H$ by left translation.

- $\Orb(xH) = G/H$: transitive, since the orbit of $eH$ is everything.
- $\Stab(xH) = xHx\inv$, since
  \[
  \Stab(xH) &= \ts{g\in G\st gxH = xH} \\
  &= \ts{g\in G \st x\inv g x\in H} \\
  &= \ts{g\in G\st g\in xHx\inv} \\
  &= xHx\inv
  .\]
- $\Fix(\phi) = \emptyset$, by transitivity.
- The kernel is $\Intersect_{g\in G} gHg\inv$, the **normal core** of $H$: the largest normal subgroup of $G$ contained in $H$.

This is the action behind arguments 3, 4 and 7 on [[algebra/group-actions/show-g-is-not-simple|Show $G$ is not simple]].

:::

## Exercises

[[E-M6XGF]]
