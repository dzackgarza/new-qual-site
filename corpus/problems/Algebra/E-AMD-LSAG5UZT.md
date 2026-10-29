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
- event: source-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source part (b) read "Suppose N = <h> is cyclic and classify all possibilities for G if |h| = p^3, |h| = p", which is inconsistent since |N| = p^2; the statement takes h to be an element of G of largest order. The source hint "Sylow and semidirect products" moved to a hint block.'
---

::: {.exercise}
Let $p$ be a prime and let $G$ be a group with $\abs{G} = p^3$.

(a) Prove that $G$ has a normal subgroup $N$ of order $p^2$.

(b) Let $h \in G$ be an element of largest order. Classify all possibilities for $G$ if (i) $\abs h = p^3$; (ii) $\abs h = p$.
:::

::: {.hint}
Sylow and semidirect products.
:::

::: {.hint}
For a central $z$ of order $p$, the quotient $G/\generators{z}$ has order $p^2$ and is abelian; the preimage of a subgroup of order $p$ is normal of order $p^2$.
:::

::: {.solution}

::: pf

::: {.pf-step #p3-has-normal-p2-subgroup}
(a) $G$ has a normal subgroup of order $p^2$.

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
(b) If $h$ has largest order in $G$, then (i) $\abs h = p^3$ gives $G \cong \ZZ/p^3$, and (ii) $\abs h = p$ gives $G \cong (\ZZ/p)^3$ or, for odd $p$, the Heisenberg group of order $p^3$.

::: pf-proof

::: {.pf-step #cyclic-case-order-p3}
(i) If $\abs h = p^3$ then $G \cong \ZZ/p^3$.

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
(ii) If $\abs h = p$ for an element of largest order, then $G$ has exponent $p$, and $G$ is one of two groups.

::: pf-proof

::: pf-step
Every nonidentity element of $G$ has order $p$, since $p$ is the largest order occurring.
:::

::: {.pf-step #exponent-p-abelian-case}
Suppose first that $G$ is abelian. Then $G$ is a vector space over $\FF_p$ of dimension $3$, so $G \cong (\ZZ/p)^3$.
:::

::: pf-step
Suppose instead that $G$ is nonabelian. Then $\abs{Z(G)} \neq p^3$, and $\abs{Z(G)} \neq p^2$, since $G/Z(G)$ cyclic forces $G$ abelian. With $Z(G) \neq 1$ from step [](#class-equation-nontrivial-center){.pf-ref} this gives $\abs{Z(G)} = p$.
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

:::

:::

:::

:::
