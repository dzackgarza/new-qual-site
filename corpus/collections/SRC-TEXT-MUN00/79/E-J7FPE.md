---
schema: qual/card@1
id: E-J7FPE
kind: problem
title: Coverings of the torus are classified by rank
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 79 Exercise 5, printed pp. 483--484. Part (a): every element of GL_2(Z) is induced by the torus homeomorphism of the linear map. Part (b): the three possible subgroups of Z^2 up to basis change, and the three standard coverings, so E is R^2, S^1 x R or T. Checked against Theorem 79.4 and the algebraic fact quoted in the printed hint. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. The proof now cites Munkres by number and page at each step: Exercise 4 of §79 (printed p. 483) for the identification pi_1(T) = Z^2, Theorem 53.1 (printed p. 337) for the covering R^2 -> T, Theorem 53.3 (printed p. 339) for products of coverings, Theorem 54.6 (printed p. 346) for p_* injective, Chapter 13 Convention (printed p. 477) for path and local path connectedness, and Theorem 79.4 (printed p. 482) for equivalence of coverings with conjugate subgroups. Corrected: part (b) said "assume the covering p: E -> T is connected", which the Chapter 13 Convention (printed p. 477) already gives for every covering map of the chapter, so the sentence now cites the Convention instead of assuming a hypothesis; and it now states that replacing p by f_A o p keeps E and changes H by A, which is what lets the three normal forms of the hint be applied. What the certificate does not cover: the algebra result in the hint (free abelian groups of rank 2) is used as the printed hint allows, not proved on the card.
---

::: {.exercise}

Let $T = S^1 \times S^1$ be the torus; let $x_0 = b_0 \times b_0$.

(a) Prove the following.

Theorem.
Every isomorphism of $\pi_1(T, x_0)$ with itself is induced by a homeomorphism of $T$ with itself that maps $x_0$ to $x_0$.

[Hint: Let $p: \RR^2 \to T$ be the usual covering map. If $A$ is a $2 \times 2$ matrix with integer entries, the linear map $T_A: \RR^2 \to \RR^2$ with matrix $A$ induces a continuous map $f: T \to T$. Furthermore, $f$ is a homeomorphism if $A$ is invertible over the integers.]

(b) Prove the following.

Theorem.
If $E$ is a covering space of $T$, then $E$ is homeomorphic either to $\RR^2$, or to $S^1 \times \RR$, or to $T$.

[Hint: You may use the following result from algebra: if $F$ is a free abelian group of rank 2 and $N$ is a nontrivial subgroup, then there is a basis $a_1, a_2$ for $F$ such that either (1) $ma_1$ is a basis for $N$, for some positive integer $m$, or (2) $ma_1, na_2$ is a basis for $N$, where $m$ and $n$ are positive integers.]
:::

::: {.solution}
Write $p: \RR^2 \to T = \RR^2/\ZZ^2$ for the standard covering map of Theorem 53.1 (printed p. 337); it is the universal covering, since $\RR^2$ is convex and a loop $f$ in $\RR^2$ is path homotopic to the constant loop at $f(0)$ by $H(s,t) = (1-t)f(s)$.

(a) The torus is $S^1 \times S^1$, so by Exercise 4 of §79 (printed p. 483) the projections of $T$ onto its two factors induce an isomorphism
$$
\pi_1(T,x_0)\cong\ZZ^2 .
$$
Every automorphism of $\ZZ^2$ is given by a matrix $A \in GL_2(\ZZ)$, so every isomorphism of $\pi_1(T,x_0)$ with itself corresponds to such an $A$ under that isomorphism.

Let $L_A:\RR^2\to\RR^2$ be the linear map with matrix $A$. Since $A(\ZZ^2)=\ZZ^2$, the map $L_A$ carries the equivalence classes of $p$ to equivalence classes, so it induces
$$
f_A:T\to T,\qquad [v]\mapsto[Av].
$$
As $L_A(0)=0$ and $x_0 = p(0)$, the map $f_A$ fixes $x_0$, and $p \circ L_A = f_A \circ p$. Since $A^{-1}\in GL_2(\ZZ)$, the map $f_{A^{-1}}$ is an inverse for $f_A$, so $f_A$ is a homeomorphism.

On fundamental groups, $(f_A)_*$ carries the class of the loop $t \mapsto [te_i]$ to the class of $t \mapsto [A(te_i)]$, which is the image under $A$ of the class of $t\mapsto[te_i]$, for $i=1,2$; those two classes correspond to the two factor circles, hence generate $\pi_1(T,x_0)$ by the same Exercise 4 of §79. Therefore $(f_A)_* = A$, and every isomorphism of $\pi_1(T,x_0)$ with itself is induced by a homeomorphism of $T$ fixing $x_0$.

(b) By the Convention of Chapter 13 (printed p. 477), a covering map of this chapter has path connected and locally path connected total space and base, so there is nothing to assume. Put
$$
H=p_*\pi_1(E,e_0)\le\pi_1(T,x_0)\cong\ZZ^2 .
$$
The subgroup $H$ is nonzero or zero. If $H \ne 0$, the algebra result quoted in the printed hint of the exercise (printed p. 484), applied to the free abelian group $F=\ZZ^2$ of rank $2$ and to the subgroup $H$, gives a basis $a_1,a_2$ of $\ZZ^2$ in which either $H=\langle m a_1\rangle$ or $H=\langle m a_1, n a_2\rangle$, with $m,n>0$. A basis change is an element $A \in GL_2(\ZZ)$, and by part (a) it is realised by the homeomorphism $f_A$ of $T$ fixing $x_0$. The map $f_A \circ p: E \to T$ is again a covering map with the same total space, and its subgroup is $A(H)$, so it is enough to treat the three normal forms $H=0$, $H=\langle m e_1\rangle$, $H=\langle m e_1, n e_2\rangle$.

The coverings of $T$ whose subgroups are these are the three displayed in [[E-XFMJA]] (Exercise 4 of §79, printed p. 483): the universal covering $p:\RR^2\to T$ with subgroup $0$; the covering
$$
S^1\times\RR\longrightarrow T,\qquad (z,t)\longmapsto (z^m,e^{2\pi i t}),
$$
which is the product of the covering $z\mapsto z^m$ of $S^1$ (Example 3 of §53, printed p. 338) with the covering $\RR\to S^1$ of Theorem 53.1 (printed p. 337), hence a covering map by Theorem 53.3 (printed p. 339), and which corresponds to the subgroup $\langle m e_1\rangle$ because a generator of $\pi_1(S^1)$ lifts to a path in $S^1\times\RR$ from $(1,0)$ to $(\zeta_m,1)$ exactly when its degree is divisible by $m$; and the covering
$$
T\longrightarrow T,\qquad (z,w)\longmapsto(z^m,w^n),
$$
again a product of coverings by Theorem 53.3, whose subgroup is $\langle m e_1, n e_2\rangle$.

By Theorem 79.4 (printed p. 482) two coverings of $T$ are equivalent if and only if their subgroups are conjugate, and $\pi_1(T,x_0)$ is abelian, so conjugacy is equality. Hence $E$ is homeomorphic to the total space of the covering of $T$ with subgroup $H$, and therefore
$$
\boxed{E\cong\RR^2,\quad S^1\times\RR,\quad\text{or}\quad T.}
$$
:::
