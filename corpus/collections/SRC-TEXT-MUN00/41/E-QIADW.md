---
schema: qual/card@1
id: E-QIADW
kind: problem
title: Locally compact connected topological groups are paracompact
classification:
  areas:
  - topology
  topics:
  - Paracompactness
  - Topological Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    No complete published solution was located for this exercise, so the proof is checked line by line
    against the book and the search is recorded in the COMPLAINTS.md entry for §39--§42 of SRC-TEXT-MUN00.
    Searched: the sets listed in that entry --- Aleksey Zinger's MAT 530 sheets, the *Praying For Stockholm*
    posts, Moller's S38, the Riverside Math 205A solutions, Orellana, Doug's World, Whitman,
    "positron0802", "shenapse", "9beach", "kyp44", the seven further GitHub manuals, dbfin and Gardner's
    ETSU notes --- none of which solves this exercise.
    Checked against Munkres, Topology (2000), Section 41 Exercise 9, printed p. 261, with the supplementary exercises of §22 on topological groups, Exercise 41.6(a) as proved on the card of E-KVFCT, and the fact that an open subgroup is closed. No correction was needed; the card takes a symmetric open neighbourhood $U$ of $e$ with $K=\overline U$ compact and shows $G=\bigcup_nK^n$.
- event: source-corrected
  by: claude
  date: 2026-11-10
  note: >-
    The card asserted that Hausdorff topological groups are regular; the book proves it, as Exercise 7(c) of
    the supplementary exercises on topological groups in §22, together with 7(a) (a symmetric neighbourhood)
    and 7(b) (Hausdorff), so the card now cites it there rather than asserting it. Everything else in the
    proof is unchanged: $K=\overline U$ compact, $K^n$ compact by Theorem 26.5 and Theorem 26.7, $H=\bigcup
    K^n$ an open subgroup and therefore closed, connectedness forcing $H=G$, and Exercise 41.6(a) giving
    paracompactness from $\sigma$-compactness.
---

::: {.exercise}

Let $G$ be a locally compact, connected topological group.
Show that $G$ is paracompact.
[Hint: Let $U_1$ be a neighborhood of $e$ having compact closure. In general, define $U_{n+1} = \overline{U}_n \cdot U_1$. Show the union of the sets $\overline{U}_n$ is both open and closed in $G$.]

This result holds without assuming $G$ is connected, but the proof requires more effort.
:::

::: {.solution}
Because $G$ is locally compact Hausdorff, choose a symmetric open neighborhood $U$ of the identity $e$ whose closure
$$
K=\overline U
$$
is compact. Replacing $U$ by $U\cap U^{-1}$ if necessary preserves compact closure and makes $K=K^{-1}$.

Set
$$
H=\bigcup_{n\ge1}K^n.
$$
Each $K^n$ is compact, since multiplication $G^n\to G$ is continuous. Also $H$ is a subgroup: $e\in K$, products send $K^mK^n$ into $K^{m+n}$, and symmetry of $K$ gives closure under inverses. Since $U\subset K\subset H$, the subgroup $H$ contains an open neighborhood of the identity, hence $H$ is open. Every open subgroup of a topological group is also closed, since its other cosets are open. Connectedness of $G$ therefore forces $H=G$.

Thus
$$
G=\bigcup_{n\ge1}K^n
$$
is $\sigma$-compact. A topological group satisfies the regularity axiom (Exercise 7(c) of the supplementary exercises on topological groups in §22; Exercises 7(a) and 7(b) there give the symmetric neighbourhood and the Hausdorff property), and every regular $\sigma$-compact space is paracompact by [[E-KVFCT]](a). Hence $G$ is paracompact.
:::
