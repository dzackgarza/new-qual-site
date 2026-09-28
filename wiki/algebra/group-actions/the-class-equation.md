---
title: The class equation
order: 20
topics:
- Conjugacy
- Centralizers and Normalizers
- Center of Groups
---

# The class equation

For a finite group $G$, each element $g$ either lies in the [[D-NK7G7|center]] $Z(G)$, and then its [[D-HLDEY|conjugacy class]] is $\ts g$, or its conjugacy class has size $[G:C_G(g)] > 1$.

[[C-O7CP3]]

[[FD-L2TEC]]

::: {.remark title="Derivation from orbit-stabilizer"}
For the conjugation action of $G$ on itself, the fixed points are the elements of $Z(G)$ and the orbit of $g$ is $[g]$, with $\size{[g]} = [G : C_G(g)]$.
If $g_1,\ldots,g_r$ represent the conjugacy classes of size greater than $1$, then
$$
\begin{aligned}
\size G &= \size{\Fix(\phi)} + \sum_{i=1}^r \size{\Orb(g_i)} \\
&= \size{Z(G)} + \sum_{i=1}^r \size{[g_i]} \\
&= \size{Z(G)} + \sum_{i=1}^r [G : C_G(g_i)],
\end{aligned}
$$
which is the class equation.
:::

## $p$-groups

::: {.proposition title="A nontrivial $p$-group has nontrivial center"}
If $\size G = p^k$ with $k\geq 1$, then $Z(G)\neq 1$.
:::

::: {.proof}
Each term $[G : C_G(g_i)]$ in the class equation is a divisor of $p^k$ greater than $1$, hence divisible by $p$, and $\size G$ is divisible by $p$.
So $\size{Z(G)}$ is divisible by $p$, and $Z(G) \neq 1$.
:::

Consequences for a group $G$ of order $p^k$:

- If $k=2$, then $G$ is abelian.

- $G$ has a normal subgroup of every order dividing $\size G$.

- $G$ is [[D-53JVH|nilpotent]].

- $G$ is simple if and only if $k=1$.

## Burnside's lemma

[[C-HE5SL]]

[[FD-XRRNZ]]

[[FF-OL75S]]

::: {.proof title="of Burnside's lemma"}
Let $A \da \ts{ (g,x) \in G\cross X \st g\actson x = x }$, and write $\Stab(x) = \ts{g\in G \st gx=x}$ and $\Fix(g) = \ts{x\in X\st gx = x}$.

Partitioning $A$ according to the first coordinate,
$$
A = \Disjoint_{g_0\in G} \ts{ (g_0, x) \st g_0 x = x } \cong \Disjoint_{g_0\in G} \ts{g_0}\cross \Fix(g_0).
$$
Partitioning $A$ according to the second coordinate,
$$
A = \Disjoint_{x_0\in X} \ts{ (g, x_0) \st gx_0= x_0 } \cong \Disjoint_{x_0\in X} \Stab(x_0) \cross \ts{ x_0 }.
$$
Taking cardinalities,
$$
\sum_{g_0\in G} \size \Fix(g_0)
= \size A
= \sum_{x_0\in X} \size \Stab(x_0).
$$
By orbit-stabilizer, $\size \Stab(x_0) = \size G/ \size \Orb(x_0)$, so
$$
{1\over \size G} \sum_{g_0\in G} \size \Fix(g_0)
= \sum_{x_0\in X} {1\over \size \Orb(x_0)}.
$$
Grouping the terms of the right-hand side by orbit,
$$
\begin{aligned}
\sum_{x_0\in X}{1\over \size \Orb(x_0)}
&= \sum_{\Orb(x_0) \in X/G} \qty{1\over \size \Orb(x_0)}\sum_{y\in \Orb(x_0)} 1 \\
&= \sum_{\Orb(x_0) \in X/G} 1 \\
&= \size (X/G).
\end{aligned}
$$
:::

::: {.remark title="Counting orbits"}
Burnside's lemma counts orbits, such as colorings of the beads of a necklace or of the faces of a cube up to the action of a rotation group.
For $g,h\in G$, $x\mapsto hx$ is a bijection $\Fix(g)\to\Fix(hgh\inv)$, so $\size{\Fix(g)}$ depends only on the conjugacy class of $g$, and the sum may be taken over conjugacy classes, each weighted by its size.
:::

[[E-6AOD7]]
