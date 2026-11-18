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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps along the book's hint; checked the symmetric
    neighbourhood with compact closure (Theorem 29.2 and continuity of inversion), that the
    union of the K^n is an open subgroup containing U, that it is also closed and hence all
    of G by connectedness, that G is then sigma-compact, and that a regular sigma-compact
    space is paracompact (E-KVFCT(a)). The argument is the card's own; no retained set is
    cited. Munkres §41 Exercise 7, printed p. 257. The printed statement needed no repair.
---

::: {.exercise}

Let $G$ be a locally compact, connected topological group.
Show that $G$ is paracompact.
[Hint: Let $U_1$ be a neighborhood of $e$ having compact closure. In general, define $U_{n+1} = \overline{U}_n \cdot U_1$. Show the union of the sets $\overline{U}_n$ is both open and closed in $G$.]

This result holds without assuming $G$ is connected, but the proof requires more effort.
:::

::: {.solution}
The argument is the card's own, following the book's hint; no retained solution set is cited on the card. It is checked against Munkres §41 Exercise 7, printed p. 257, with [[E-KVFCT]](a) (a regular $\sigma$-compact space is paracompact).

::: pf

::: {.pf-step #compact-neighbourhood}
There is a symmetric open neighbourhood $U$ of $e$ whose closure $K=\overline{U}$ is compact and satisfies $K=K^{-1}$.

::: pf-proof
$G$ is locally compact Hausdorff, so by Theorem 29.2 applied to the point $e$ and the neighbourhood $G$ there is an open set $U'$ with $e\in U'$ and $\overline{U'}$ compact. Replacing $U'$ by $U'\cap U'^{-1}$, which is open by continuity of inversion, contains $e$ and is symmetric, keeps the closure inside $\overline{U'}$ and so compact; set $U=U'\cap U'^{-1}$ and $K=\overline{U}$. Since inversion is a homeomorphism fixing $U$, it fixes $K$, so $K=K^{-1}$.
:::

:::

::: {.pf-step #subgroup}
$H=\bigcup_{n\in\ZZ_{+}}K^{n}$, where $K^{n}$ is the set of products of $n$ elements of $K$, is an open subgroup of $G$ containing $U$.

::: pf-proof
$K^{n}$ is compact, being the image of the compact space $K^{n}$ under the continuous multiplication map $G^{n}\to G$. Since $e\in K$ one has $K^{m}K^{n}\subset K^{m+n}$, so $H$ is closed under multiplication, and $K=K^{-1}$ gives $H^{-1}=\bigcup_{n}(K^{n})^{-1}=\bigcup_{n}K^{n}=H$; also $e\in K\subset H$. So $H$ is a subgroup. It contains the open set $U$, hence it is open, being the union of the open sets $hU$ for $h\in H$.
:::

:::

::: {.pf-step #all-of-G}
$H=G$.

::: pf-proof
An open subgroup $H$ is also closed, because its complement is the union of the other cosets $gH$, each of which is open as a translate of $H$. So $H$ is a nonempty set both open and closed in the connected space $G$, hence $H=G$.
:::

:::

::: {.pf-step #sigma-compact}
$G$ is $\sigma$-compact.

::: pf-proof
$G=H=\bigcup_{n}K^{n}$ by step [](#all-of-G){.pf-ref}, and each $K^{n}$ is compact by step [](#subgroup){.pf-ref}; so $G$ is a countable union of compact sets.
:::

:::

::: {.pf-step #paracompact}
$G$ is paracompact.

::: pf-proof
A topological group is regular: it is Hausdorff by Supplementary Exercise TG.7(b) of §22, and every neighbourhood of a point contains a closed neighbourhood by TG.7(a) and the continuity of multiplication. A regular $\sigma$-compact space is paracompact by [[E-KVFCT]](a). So $G$ is paracompact.
:::

:::

:::
:::
