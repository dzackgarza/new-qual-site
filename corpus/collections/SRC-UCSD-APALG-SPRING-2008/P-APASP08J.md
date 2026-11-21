---
schema: qual/card@1
id: P-APASP08J
kind: problem
title: "Pólya enumeration on the cube and Frobenius image"
classification:
  areas:
  - applied-algebra
  topics:
  - Combinatorics
  - Pólya Enumeration
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $\Gamma$ be the group of rotations of the cube.

1. Compute the Pólya enumerator of the action of $\Gamma$ on the edges of the cube.

2. Use the previous result to compute the number of ways to colour the edges of the cube using seven red and five yellow.

3. Show that the polynomial you computed in part 1 is the Frobenius image of the character of a representation of $S_{12}$.
:::

::: {.solution}

The argument is the card's own; no source text or solution set is retained for it.

Let $\Gamma$ be the rotation group of the cube, of order $24$, acting on the set $E$ of its $12$ edges.

::: pf

::: {.pf-step #classes}
The classes of $\Gamma$ and their edge cycle types are: identity $1^{12}$; $6$ quarter-turns about a face axis, type $4^{3}$; $3$ half-turns about a face axis, type $2^{6}$; $8$ third-turns about a body diagonal, type $3^{4}$; and $6$ half-turns about an edge axis, type $1^{2}2^{5}$. The counts total $1+6+3+8+6=24$.

::: pf-proof
Every rotation of the cube is about an axis through a pair of opposite faces, opposite vertices, or opposite edges, and these three families have $3$, $4$ and $6$ axes respectively, each contributing the nontrivial rotations about it: $3$ axes of face type give $3$ quarter-turns and $3$ half-turns, $4$ axes of diagonal type give $8$ third-turns, $6$ axes of edge type give $6$ half-turns, and with the identity the total is $1+6+3+8+6=24$, the known order of the rotation group. For the cycle types: a quarter-turn about a face axis carries each edge to one of the four edges of a "belt", giving three $4$-cycles; a half-turn about a face axis reverses each belt, giving six $2$-cycles; a third-turn about a diagonal cyclically permutes three edges at each of four positions, giving four $3$-cycles; and a half-turn about an edge axis fixes the two edges on the axis (as edge sets) and pairs the remaining ten, giving $1^{2}2^{5}$. Each type has $12$ edges accounted for.
:::

:::

::: {.pf-step #polya}
$Z_{\Gamma}(p_{1},p_{2},\dots)=\frac1{24}\left(p_{1}^{12}+6p_{4}^{3}+3p_{2}^{6}+8p_{3}^{4}+6p_{1}^{2}p_{2}^{5}\right)$.

::: pf-proof
The cycle index of a group action is $\frac{1}{\abs{\Gamma}}\sum_{g}p_{\lambda(g)}$, where $\lambda(g)$ is the cycle type of $g$ on the set acted on; summing over the classes of step [](#classes){.pf-ref}, with each class contributing its size times its monomial, gives the displayed polynomial.
:::

:::

::: {.pf-step #substitute}
The number of orbits of two-colourings with $7$ red and $5$ yellow edges is the coefficient of $r^{7}y^{5}$ in
$$
\frac1{24}\left[(r+y)^{12}+6(r^{4}+y^{4})^{3}+3(r^{2}+y^{2})^{6}+8(r^{3}+y^{3})^{4}+6(r+y)^{2}(r^{2}+y^{2})^{5}\right].
$$

::: pf-proof
By Burnside's lemma the number of orbits of colourings is the average number of fixed colourings, and a colouring with prescribed red/yellow counts is a weight-$r^{7}y^{5}$ monomial when the substitution $p_{k}\mapsto r^{k}+y^{k}$ is made: a $k$-cycle coloured monochromatically contributes $r^{k}$ if red and $y^{k}$ if yellow. Substituting in step [](#polya){.pf-ref} gives the displayed polynomial, whose coefficient of $r^{7}y^{5}$ counts the orbits with seven red and five yellow edges.
:::

:::

::: {.pf-step #coefficient}
That coefficient is $\frac{792+6\cdot20}{24}=38$.

::: pf-proof
The second, third and fourth terms involve only cycle lengths $4$, $2$ and $3$, so every monomial they produce has red exponent divisible by $4$, even, or divisible by $3$; none can have red exponent $7$. The first term contributes $\binom{12}{7}=792$. For the last term $6(r+y)^{2}(r^{2}+y^{2})^{5}$: a choice of $k$ red factors from $(r+y)^{2}$ and $j$ red $2$-cycles from $(r^{2}+y^{2})^{5}$ contributes $r^{k+2j}y^{(2-k)+2(5-j)}$, and $k+2j=7$ with $0\leq k\leq2$ forces $k=1$, $j=3$; the number of such choices is $\binom21\binom53=20$. So the coefficient is $792+6\cdot20=912$, and dividing by $\abs{\Gamma}=24$ gives $38$.
:::

:::

::: {.pf-step #frobenius}
The enumerator of step [](#polya){.pf-ref} is the Frobenius characteristic of the character of $\operatorname{Ind}_{\Gamma}^{S_{12}}\mathbf{1}$, where $\Gamma\le S_{12}$ acts on the twelve edges.

::: pf-proof
For a representation with character $\chi$ of $S_{12}$ the Frobenius characteristic is $\operatorname{ch}(\chi)=\sum_{\lambda\vdash12}\frac{\chi(C_{\lambda})}{z_{\lambda}}p_{\lambda}$, and for an induced trivial character the induced-character formula gives $\chi(C_{\lambda})=\frac{1}{\abs{\Gamma}}\#\{g\in\Gamma:\lambda(g)=\lambda\}\cdot z_{\lambda}$; substituting cancels $z_{\lambda}$ and leaves
$$
\operatorname{ch}\left(\operatorname{Ind}_{\Gamma}^{S_{12}}\mathbf{1}\right)=\frac{1}{\abs{\Gamma}}\sum_{g\in\Gamma}p_{\lambda(g)}=\frac1{24}\left(p_{1}^{12}+6p_{4}^{3}+3p_{2}^{6}+8p_{3}^{4}+6p_{1}^{2}p_{2}^{5}\right),
$$
which is step [](#polya){.pf-ref}. So the Pólya enumerator is the Frobenius image of an honest representation of $S_{12}$, namely the permutation representation on the cosets of $\Gamma$.
:::

:::

::: {.pf-step}
The enumerator is $\frac1{24}(p_1^{12}+6p_4^3+3p_2^6+8p_3^4+6p_1^2p_2^5)$, the count is $38$, and the enumerator is a Frobenius image from $S_{12}$.

::: pf-proof
Steps [](#polya){.pf-ref}, [](#coefficient){.pf-ref} and [](#frobenius){.pf-ref} are parts 1, 2 and 3.
:::

:::

:::

:::
