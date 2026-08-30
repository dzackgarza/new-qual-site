---
title: The class equation
order: 20
problems:
  topics:
  - Conjugacy
  - Centralizers and Normalizers
  - Center of Groups
---

# The class equation

Conjugation applied to the counting trick.
Every element is either central, contributing a singleton conjugacy class, or it is not, and then its class has size the index of its centralizer.

[[C-O7CP3]]

[[FD-L2TEC]]

:::{.remark title="Where it comes from"}
$[G : Z(g)]$ is the size of the conjugacy class $[g]$, and $g\in Z(G)$ exactly when $[g] = \ts g$.
Applying the fixed-point count and substituting orbit-stabilizer,
\[
G &= \Fix(\phi) \Disjoint_{x}' \Orb(x) \\
&= Z(G) \Disjoint_{g}' [g]\\
&= Z(G) \Disjoint_{g}' {G\over Z(g) }
,\]
and taking cardinalities is the class equation.

:::

## What it is used for

Almost always for $p\dash$groups, where the two sides are compared mod $p$.

:::{.proposition title="A nontrivial $p$-group has nontrivial centre"}
Every term $[G : Z(g)]$ in the sum is a proper divisor of $\size G = p^k$, hence divisible by $p$, and $\size G$ is divisible by $p$.
So $\size{Z(G)}$ is divisible by $p$ and in particular is not $1$.

:::

That single fact carries most of the $p\dash$group results: groups of order $p^2$ are abelian, a $p$-group has a normal subgroup of every order dividing $\size G$, and a $p\dash$group is nilpotent.
It is also the reason a $p\dash$group is never simple unless it has prime order.

## Burnside

[[C-HE5SL]]

[[FD-XRRNZ]]

[[FF-OL75S]]

:::{.proof title="of Burnside's lemma"}
Count $A \da \ts{ (g,x) \in G\cross X \st g\actson x = x }$ two ways, writing $\Stab(x) = \ts{g\in G \st gx=x}$ and $\Fix(g) = \ts{x\in X\st gx = x}$.

Fibering over $G$:
\[
A = \Disjoint_{g_0\in G} \ts{ (g_0, x) \st g_0 x = x } \cong \Disjoint_{g_0\in G} \ts{g_0}\cross \Fix(g_0)
.\]
Fibering over $X$:
\[
A = \Disjoint_{x_0\in X} \ts{ (g, x_0) \st gx_0= x_0 } \cong \Disjoint_{x_0\in X} \Stab(x_0) \cross \ts{ x_0 }
.\]
Taking cardinalities,
\[
\sum_{g_0\in G} \size \Fix(g_0)
= \size A
= \sum_{x_0\in X} \size \Stab(x_0)
.\]
Orbit-stabilizer rearranges to $\size \Stab(x_0) = \size G/ \size \Orb(x_0)$, so
\[
{1\over \size G} \sum_{g_0\in G} \size \Fix(g_0)
= \sum_{x_0\in X} {1\over \size \Orb(x_0)}
,\]
and partitioning that sum by orbit collapses it:
\[
\sum_{x_0\in X}{1\over \size \Orb(x_0)}
&= \sum_{\Orb(x_0) \in X/G} \qty{1\over \size \Orb(x_0)}\sum_{y\in \Orb(x_0)} 1 \\
&= \sum_{\Orb(x_0) \in X/G} 1 \\
&= \size (X/G)
.\]

:::

:::{.remark title="What Burnside is for"}
Counting orbits, which on an exam means counting colourings up to symmetry: necklaces, faces of a cube, arrangements fixed by a rotation group.
The left side is an average over the group of how much each element fixes, so the computation is always a sum over conjugacy classes.

:::

[[E-6AOD7]]
