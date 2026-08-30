---
schema: qual/card@1
id: E-AMD-LSAG5UZT
kind: exercise
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
- Suppose $N = \gens{h}$ is cyclic and classify all possibilities for $G$ if:
  - $\abs h = p^3$
  - $\abs h = p$.

  > Hint: Sylow and semidirect products.
:::

::: solution
**Goal:** produce a normal $N \normal G$ with $\abs N = p^2$ by pulling back a subgroup of the abelian quotient $G/\gens{z}$ for a central $z$ of order $p$, and then classify $G$ by the order of an element $h$ of largest order.

<1>1. $G$ has a normal subgroup of order $p^2$.
    *Proof:*
    <2>1. $G$ is a $p$-group, so the class equation
        $$\abs G = \abs{Z(G)} + \sum_{i} [G : C_G(x_i)]$$
        over representatives $x_i$ of the noncentral conjugacy classes has every index $[G:C_G(x_i)]$ divisible by $p$.
    <2>2. Hence $p \mid \abs{Z(G)}$, so $Z(G) \neq 1$.
    <2>3. By Cauchy's theorem applied to $Z(G)$, pick $z \in Z(G)$ with $\abs z = p$.
    <2>4. $\gens z \normal G$, because a central subgroup is normalized by every element of $G$.
    <2>5. $\abs{G/\gens z} = p^3/p = p^2$, and every group of order $p^2$ is abelian: if $Q$ has order $p^2$ then $Q/Z(Q)$ is cyclic by step <2>2 applied to $Q$, and a group with cyclic central quotient is abelian.
    <2>6. By Cauchy's theorem, $G/\gens z$ has a subgroup $\bar H$ with $\abs{\bar H} = p$, and $\bar H \normal G/\gens z$ because that quotient is abelian.
    <2>7. Let $N$ be the preimage of $\bar H$ under $\pi: G \to G/\gens z$. The correspondence theorem gives $N \normal G$, and
        $$\abs N = \abs{\bar H}\cdot \abs{\gens z} = p \cdot p = p^2 .$$

<1>2. The two classification cases are cases on the largest order of an element of $G$.
    *Proof:*
    <2>1. $N$ has order $p^2$, so a generator of a cyclic $N$ has order $p^2$, never $p^3$ or $p$.
    <2>2. The orders $p^3$ and $p$ are therefore the orders of an element $h \in G$ of largest order, and they are the two extreme cases: $G$ is cyclic, or $G$ has exponent $p$.

<1>3. If $\abs h = p^3$ then $G \cong \ZZ/p^3$.
    *Proof:*
    <2>1. $\gens h \leq G$ has $p^3 = \abs G$ elements, so $\gens h = G$.
    <2>2. A cyclic group is determined up to isomorphism by its order.

<1>4. If $\abs h = p$ for an element of largest order, then $G$ has exponent $p$, and $G$ is one of two groups.
    *Proof:*
    <2>1. Every nonidentity element of $G$ has order $p$, since $p$ is the largest order occurring.
    <2>2. Suppose first that $G$ is abelian. Then $G$ is a vector space over $\FF_p$ of dimension $3$, so $G \cong (\ZZ/p)^3$.
    <2>3. Suppose instead that $G$ is nonabelian. Then $\abs{Z(G)} \neq p^3$, and $\abs{Z(G)} \neq p^2$, since $G/Z(G)$ cyclic forces $G$ abelian. With step <1>1's $Z(G) \neq 1$ this gives $\abs{Z(G)} = p$.
    <2>4. So $G/Z(G)$ has order $p^2$ and is not cyclic, hence $G/Z(G) \cong (\ZZ/p)^2$.
    <2>5. Choose $x, y \in G$ whose images generate $G/Z(G)$, and write $Z(G) = \gens z$. Then $G = \gens{x, y, z}$.
    <2>6. The commutator $[x,y]$ lies in $Z(G)$, because $G/Z(G)$ is abelian, and $[x,y] \neq 1$, because $x$ and $y$ do not commute. So $\gens{[x,y]} = Z(G)$, and after replacing $z$ by $[x,y]$ we may take
        $$x^p = y^p = z^p = 1, \qquad [x,y] = z, \qquad z \text{ central}.$$
    <2>7. These relations write every element of $G$ once as $x^a y^b z^c$ with $0 \leq a,b,c < p$, so they present a single group of order $p^3$, namely the group of upper unitriangular $3\times 3$ matrices over $\FF_p$,
        $$G \cong \ts{ \begin{pmatrix} 1 & a & c \\ 0 & 1 & b \\ 0 & 0 & 1\end{pmatrix} \st a,b,c \in \FF_p } \cong (\ZZ/p)^2 \semidirect \ZZ/p .$$
    <2>8. This case is empty for $p = 2$: exponent $2$ forces $g^2 = 1$ for all $g$, hence $(gh)^2 = 1$ and $gh = hg$, so $G$ is abelian and step <2>2 applies.

<1>5. Q.E.D.
    *Proof:* Step <1>1 produces $N$, and steps <1>3 and <1>4 classify $G$ in the two stated cases.
:::
