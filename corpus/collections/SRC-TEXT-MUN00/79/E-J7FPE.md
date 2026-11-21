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
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Corrected part (b)'s two covering-space steps and one slip of Yang's. First, the subgroup of the covering
    S^1 x R -> T, (z,t) |-> (z^m, e^{2 pi i t}), is now given as mZ x 0, the product of the subgroup mZ of the
    covering z |-> z^m with the subgroup 0 of R -> S^1, and derived from Theorem 60.1 (printed p. 371), instead
    of from a sentence about where a generator of pi_1(S^1) lifts, which named an endpoint (zeta_m, 1) without
    saying which path it was the endpoint of. Second, "f_A o p is again a covering map" is now proved in one
    line instead of cited: an open set U evenly covered by p has p^{-1}(U) the disjoint union of slices
    V_alpha, (f_A o p)^{-1}(f_A(U)) = p^{-1}(U) because f_A is a bijection, and f_A o p carries each V_alpha
    homeomorphically onto f_A(U). Neither citation this step carried before states it: Example 1 of §53 (printed
    p. 337) says only that the identity map is a covering map, and Exercise 4 of §53 (printed p. 341) is an
    exercise the book does not prove, so the card cites it nowhere. Theorem 53.3 (printed p. 339) is about a
    product of two covering maps and stays cited only for the products S^1 x R -> T and T -> T. Yang's footnote
    cites "Exercise 54.4" for the composition, a number whose exercise says nothing of the kind. Checked on the
    page images: Theorems 53.1, 53.3 and 60.1 at the pages cited, and Example 1 of §53 and Exercise 4 of §53
    read to establish that neither states what the step needs. Not covered:
    Theorem 60.1 gives the isomorphism of fundamental groups of a product and the card uses its naturality for
    the product map without proving it separately.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §79 Exercise 5(a),(b), printed pp. 483--484. Searched outside the checkout for issue #146; the
    record is tmp/sources/mse-searches-146.md and the saved sources are tmp/sources/mse-971171-E-J7FPE.md and
    tmp/sources/gh-dyang5-MATH104-Topology-E-J7FPE.md, both read whole. Part (a): Math StackExchange 971171
    (asked by ChesterX 2014-10-13) has one answer, 971387 by Sammy Black, which constructs the homeomorphism
    from a matrix in GL_2(Z) through the lift to R^2 and asserts (phi_A)_* = A; the card's proof is that
    construction with the computation of the induced map added, and now says which is which. Part (b): David
    Yang, MATH104 Fall 2023 Homework 11, HW/hw11.tex lines 35-77 at commit 12686a815d, proves it from the
    printed hint, part (a), the three product coverings and the equivalence theorem, with one slip (it writes
    that f, the homeomorphism of part (a), is "the composition of a covering map and a homeomorphism" where
    the composite q = f o p is meant; the card's text has the composite). The card's proof is that argument
    with the book's numbers in place of his references, and it is now recorded as his on the card with the
    commit and line range. Neither source omits a hypothesis of the exercise. Rejected in the search:
    mse 371075 (rank-2 subgroups only).
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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose in two headed parts with no `pf` structure. It is
    now a `pf` with eight steps covering (a) and (b), each carrying a `pf-proof`. The mathematics is
    transcribed from the two published answers the earlier event names: Sammy Black's answer 971387
    for part (a), whose identification $(f_A)_*=A$ is asserted there and computed here on the two
    factor circles, and David Yang's MATH104 Homework 11 for part (b), the normal form of the printed
    hint, the three product coverings and the equivalence theorem. Cited by numbered statement only:
    Munkres, Topology, §79 Exercise 5, Theorem 53.1, Theorem 53.3, Theorem 60.1, Theorem 79.4,
    Example 3 of §53 and Exercise 4 of §79. Checked: that $A(\ZZ^2)=\ZZ^2$ makes $f_A$ well defined
    with $p\circ L_A=f_A\circ p$, that $f_{A^{-1}}$ inverts $f_A$, that $(f_A)_*$ sends the two factor
    loops to the loops representing the columns of $A$, that $f_A\circ p$ is a covering with subgroup
    $A(H)$, and that each of the three model coverings has the subgroup claimed for it.

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

Both parts are transcribed from published answers. Part (a) is Sammy Black's, answer 971387 to Math Stack Exchange question 971171, "Automorphism of fundamental group of torus"; that answer asserts the identification $(f_A)_*=A$ without computing it, and the computation on the two factor circles below is this card's. Part (b) is David Yang's, *MATH104: Topology, Fall 2023*, Homework 11, the argument of its problem on covering spaces of the torus, with Munkres's numbered results cited where Yang cites his own. No retained set in `tmp/sources` answers this exercise; the search is recorded in the `COMPLAINTS.md` entry for Sections 74 to 85.

::: pf

::: {.pf-step #identification}
(a) The projections of $T=S^1\times S^1$ onto its two factors induce an isomorphism $\pi_1(T,x_0)\cong\ZZ^2$, and every isomorphism of $\pi_1(T,x_0)$ with itself corresponds under it to a matrix $A\in GL_2(\ZZ)$.

::: pf-proof
The fundamental group of a product is the product of the fundamental groups of the factors (Munkres, Theorem 60.1), so $\pi_1(T,x_0)\cong\ZZ\times\ZZ$, with the two factor circles $\{b_0\}\times S^1$ and $S^1\times\{b_0\}$ as generators. An automorphism of $\ZZ^2$ is given by an integer matrix with integer inverse, that is, by $A\in GL_2(\ZZ)$.
:::

:::

::: {.pf-step #action}
(a) For $A\in GL_2(\ZZ)$ the linear map $L_A:\RR^2\to\RR^2$ descends to a homeomorphism $f_A:T\to T$ with $p\circ L_A=f_A\circ p$ and $f_A(x_0)=x_0$.

::: pf-proof
Write $p:\RR^2\to T=\RR^2/\ZZ^2$ for the standard covering map (Munkres, Theorem 53.1). Since $A(\ZZ^2)=\ZZ^2$, equivalent vectors have equivalent images, so $f_A([v])=[Av]$ is well defined and $p\circ L_A=f_A\circ p$. $L_A(0)=0$ and $x_0=p(0)$, so $f_A$ fixes $x_0$. Since $A^{-1}\in GL_2(\ZZ)$, the map $f_{A^{-1}}$ is an inverse of $f_A$, so $f_A$ is a homeomorphism.
:::

:::

::: {.pf-step #induced-map}
(a) $(f_A)_*=A$ under the identification of step [#identification]{.pf-ref}.

::: pf-proof
Let $e_1,e_2$ be the standard basis of $\RR^2$ and let $\gamma_i(t)=[te_i]$ be the loop representing the $i$-th factor circle. Then $(f_A)_*[\gamma_i]$ is the class of $t\mapsto[A(te_i)]=t\mapsto tAe_i$, which is the loop representing $Ae_i$. The two classes $[\gamma_1],[\gamma_2]$ generate $\pi_1(T,x_0)$ by step [#identification]{.pf-ref}, so $(f_A)_*$ acts on the whole group as $A$.
:::

:::

::: {.pf-step #part-a}
(a) Every isomorphism of $\pi_1(T,x_0)$ with itself is induced by a homeomorphism of $T$ fixing $x_0$.

::: pf-proof
Given an isomorphism, step [#identification]{.pf-ref} gives the matrix $A\in GL_2(\ZZ)$ it corresponds to, and steps [#action]{.pf-ref} and [#induced-map]{.pf-ref} give a homeomorphism $f_A$ of $T$ fixing $x_0$ with $(f_A)_*=A$.
:::

:::

::: {.pf-step #subgroup}
(b) With $H=p_*\pi_1(E,e_0)\le\pi_1(T,x_0)\cong\ZZ^2$, the algebra result quoted in the exercise's hint puts $H$ into one of three normal forms after a change of basis.

::: pf-proof
The Convention of Munkres's Chapter 13 makes a covering map's total space and base path connected and locally path connected, so $\pi_1(E,e_0)$ is defined. If $H\ne0$, the printed algebra result applies to the free abelian group $\ZZ^2$ of rank $2$ and its nontrivial subgroup $H$: there is a basis $a_1,a_2$ with either $H=\langle ma_1\rangle$ or $H=\langle ma_1,na_2\rangle$, $m,n>0$. A change of basis is an element $A\in GL_2(\ZZ)$.
:::

:::

::: {.pf-step #replace-cover}
(b) Replacing $p$ by $f_A\circ p$ does not change the total space, so it is enough to treat the three normal forms.

::: pf-proof
$\mathrm{id}$ is a homeomorphism of $E$, so the total space is unchanged. The composite $f_A\circ p:E\to T$ is a covering map with subgroup $A(H)$: if $U$ is evenly covered by $p$ with slices $V_\alpha$, then $(f_A\circ p)^{-1}(f_A(U))=p^{-1}(U)$, since $f_A$ is a bijection, and $f_A\circ p$ carries each $V_\alpha$ homeomorphically onto $f_A(U)$. So the classification of $E$ depends only on $A(H)$.
:::

:::

::: {.pf-step #three-coverings}
(b) The coverings of $T$ with subgroups $0$, $\langle me_1\rangle$ and $\langle me_1,ne_2\rangle$ have total spaces $\RR^2$, $S^1\times\RR$ and $T$.

::: pf-proof
These are the three coverings of Munkres, Exercise 4 of §79. The universal covering $p:\RR^2\to T$ has subgroup $0$, as $\RR^2$ is convex and simply connected (Munkres, Theorem 53.1). The map $S^1\times\RR\to T$, $(z,t)\mapsto(z^m,e^{2\pi it})$, is the product of the covering $z\mapsto z^m$ of $S^1$ (Example 3 of §53) with $\RR\to S^1$ (Theorem 53.1), hence a covering map by Theorem 53.3; by Theorem 60.1 and the fact that a product map induces the product of the induced homomorphisms, its subgroup is $m\ZZ\times0=\langle me_1\rangle$. The map $T\to T$, $(z,w)\mapsto(z^m,w^n)$, is likewise a product of coverings and has subgroup $\langle me_1,ne_2\rangle$.
:::

:::

::: {.pf-step #part-b}
(b) $E$ is homeomorphic to $\RR^2$, to $S^1\times\RR$, or to $T$.

::: pf-proof
By the classification of coverings (Munkres, Theorem 79.4) two coverings of $T$ are equivalent exactly when their subgroups are conjugate, and $\pi_1(T,x_0)$ is abelian by step [#identification]{.pf-ref}, so conjugacy is equality. Hence $E$ is homeomorphic to the total space of the covering with subgroup $H$, which is one of the three of step [#three-coverings]{.pf-ref} by steps [#subgroup]{.pf-ref} and [#replace-cover]{.pf-ref}. So $\boxed{E\cong\RR^2,\ S^1\times\RR,\ \text{or}\ T}$.
:::

:::

:::

:::
