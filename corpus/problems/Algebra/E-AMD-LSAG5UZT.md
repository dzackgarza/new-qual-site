---
schema: qual/card@1
id: E-AMD-LSAG5UZT
kind: problem
title: Groups of order $p^3$ have a normal subgroup of order $p^2$
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5
  date: 2026-08-30
---

::: {.exercise}
Let $p$ be a prime and $\abs{G} = p^3$. 
Prove that $G$ has a normal subgroup $N$ of order $p^2$.
- Suppose $N = \generators{h}$ is cyclic and classify all possibilities for $G$ if:
  - $\abs h = p^3$
  - $\abs h = p$.

  > Hint: Sylow and semidirect products.
:::

::: {.hint}
For a central $z$ of order $p$, the quotient $G/\generators{z}$ has order $p^2$ and is abelian; the preimage of a subgroup of order $p$ is normal of order $p^2$.
:::

::: {.solution}

::: pf

::: {.pf-step #p3-has-normal-p2-subgroup}
$G$ has a normal subgroup of order $p^2$.

::: pf-proof

::: pf-step
$G$ is a $p$-group, so the class equation
$$\abs G = \abs{Z(G)} + \sum_{i} [G : C_G(x_i)]$$
over representatives $x_i$ of the noncentral conjugacy classes has every index $[G:C_G(x_i)]$ divisible by $p$.
:::

::: {.pf-step #class-equation-nontrivial-center}
Hence $p \mid \abs{Z(G)}$, so $Z(G) \neq 1$.
:::

::: pf-step
By Cauchy's theorem applied to $Z(G)$, pick $z \in Z(G)$ with $\abs z = p$.
:::

::: pf-step
$\generators z \normal G$, because a central subgroup is normalized by every element of $G$.
:::

::: pf-step
$\abs{G/\generators z} = p^3/p = p^2$, and every group of order $p^2$ is abelian: if $Q$ has order $p^2$ then $Q/Z(Q)$ is cyclic by step [](#class-equation-nontrivial-center){.pf-ref} applied to $Q$, and a group with cyclic central quotient is abelian.
:::

::: pf-step
By Cauchy's theorem, $G/\generators z$ has a subgroup $\bar H$ with $\abs{\bar H} = p$, and $\bar H \normal G/\generators z$ because that quotient is abelian.
:::

::: pf-step
Let $N$ be the preimage of $\bar H$ under $\pi: G \to G/\generators z$. The correspondence theorem gives $N \normal G$, and
$$\abs N = \abs{\bar H}\cdot \abs{\generators z} = p \cdot p = p^2 .$$
:::

:::

:::

::: pf-step
The two classification cases are cases on the largest order of an element of $G$.

::: pf-proof

::: pf-step
$N$ has order $p^2$, so a generator of a cyclic $N$ has order $p^2$, never $p^3$ or $p$.
:::

::: pf-step
The orders $p^3$ and $p$ are therefore the orders of an element $h \in G$ of largest order, and they are the two extreme cases: $G$ is cyclic, or $G$ has exponent $p$.
:::

:::

:::

::: {.pf-step #cyclic-case-order-p3}
If $\abs h = p^3$ then $G \cong \ZZ/p^3$.

::: pf-proof

::: pf-step
$\generators h \leq G$ has $p^3 = \abs G$ elements, so $\generators h = G$.
:::

::: pf-step
A cyclic group is determined up to isomorphism by its order.
:::

:::

:::

::: {.pf-step #exponent-p-case}
If $\abs h = p$ for an element of largest order, then $G$ has exponent $p$, and $G$ is one of two groups.

::: pf-proof

::: pf-step
Every nonidentity element of $G$ has order $p$, since $p$ is the largest order occurring.
:::

::: {.pf-step #exponent-p-abelian-case}
Suppose first that $G$ is abelian. Then $G$ is a vector space over $\FF_p$ of dimension $3$, so $G \cong (\ZZ/p)^3$.
:::

::: pf-step
Suppose instead that $G$ is nonabelian. Then $\abs{Z(G)} \neq p^3$, and $\abs{Z(G)} \neq p^2$, since $G/Z(G)$ cyclic forces $G$ abelian. With step [](#p3-has-normal-p2-subgroup){.pf-ref}'s $Z(G) \neq 1$ this gives $\abs{Z(G)} = p$.
:::

::: pf-step
So $G/Z(G)$ has order $p^2$ and is not cyclic, hence $G/Z(G) \cong (\ZZ/p)^2$.
:::

::: pf-step
Choose $x, y \in G$ whose images generate $G/Z(G)$, and write $Z(G) = \generators z$. Then $G = \generators{x, y, z}$.
:::

::: pf-step
The commutator $[x,y]$ lies in $Z(G)$, because $G/Z(G)$ is abelian, and $[x,y] \neq 1$, because $x$ and $y$ do not commute. So $\generators{[x,y]} = Z(G)$, and after replacing $z$ by $[x,y]$ we may take
$$x^p = y^p = z^p = 1, \qquad [x,y] = z, \qquad z \text{ central}.$$
:::

::: pf-step
These relations write every element of $G$ once as $x^a y^b z^c$ with $0 \leq a,b,c < p$, so they present a single group of order $p^3$, namely the group of upper unitriangular $3\times 3$ matrices over $\FF_p$,
$$G \cong \theset{ \begin{pmatrix} 1 & a & c \\ 0 & 1 & b \\ 0 & 0 & 1\end{pmatrix} \st a,b,c \in \FF_p } \cong (\ZZ/p)^2 \semidirect \ZZ/p .$$
:::

::: pf-step
This case is empty for $p = 2$: exponent $2$ forces $g^2 = 1$ for all $g$, hence $(gh)^2 = 1$ and $gh = hg$, so $G$ is abelian and step [](#exponent-p-abelian-case){.pf-ref} applies.
:::

:::

:::

::: pf-qed
Step [](#p3-has-normal-p2-subgroup){.pf-ref} produces $N$, and steps [](#cyclic-case-order-p3){.pf-ref} and [](#exponent-p-case){.pf-ref} classify $G$ in the two stated cases.
:::

:::

:::
