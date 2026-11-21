---
schema: qual/card@1
id: E-CTM3H
kind: problem
title: Where the countable intersection property breaks the Tychonoff argument
classification:
  areas:
  - topology
  topics:
  - Countability
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    No complete published solution was located for this exercise, so the proof has been checked line by
    line against the book and the search is recorded in the COMPLAINTS.md entry for §37--§42 of
    SRC-TEXT-MUN00. Searched: Aleksey Zinger, "MAT 530" Problem Sets 2-9 (Chapter 5 and 6 items: p235 #1,
    p236 #5, p260 #2, p260 #7 only); "Solutions to exercises in Munkres", file S38.pdf (Exercise 38.4
    onwards); "Solutions to exercises for Mathematics 205A" (UC Riverside, Fall 2014), section VI.4;
    Orellana (§37 selection), Doug's World (Chapter 4), Whitman (to §22), "positron0802" (Chapters 2 and
    3), "shenapse" (§1--§11), "9beach" (§1--§4), "kyp44" (§1--§22); and the dbFin pages, which have no
    chapter-5 or chapter-6 section. Checked against Munkres, Topology (2000), Section 37 Exercise 3,
    printed p. 235, with Lemma 37.2 for the finite case, Exercise 37.2 for the passage from the countable
    intersection property of the projections to a point of their closures' intersection, and Exercise 30.9
    (a closed subspace of a Lindelof space is Lindelof) for the failure of (iii) at the Sorgenfrey plane,
    whose antidiagonal is an uncountable closed discrete subspace. What was corrected: part (c) said that
    the products' failure is "for the Sorgenfrey plane" without saying why the plane is not Lindelof; the
    card now names the antidiagonal. No other correction was needed; the Zorn step's failure is the
    sheet-free argument on the card, namely that a countable intersection in the union of a chain may use
    one element from each member of the chain.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Read for #169 and rewritten: what stood here was a skeleton whose proof fields said "setup.",
    "assume for contradiction.", "(i)." and "(ii).", so the card carried no argument for any of
    the three parts. Searched for a published solution first: Ana Emilia de Orellana's Section 37
    Exercise 3 is a corrupted fragment that breaks off inside part (a), answers part (b) with the
    sentence about the maximum element that does not address statement (ii), and leaves (c)
    unwritten; Poulsen's §38 sheet runs 38.4 to 38.9; dbFin's index stops at §67; no other
    retained set reaches §37. So the proof is the card's own, and each step was checked against
    Lemma 37.1, Lemma 37.2 and Exercise 37.2. Part (a): the complements of a cover with no
    countable subcover have the countable intersection property, (i) extends them to a maximal
    family, (ii) makes that family closed under finite intersections and makes a set meeting every
    member a member, each projection's closures have the countable intersection property because
    the projection is onto and the family is closed under countable intersections, Exercise 37.2
    in the Lindelöf factor picks a point in all of them, and the point of the product so built lies
    in the closure of every member, which contradicts the cover for the member indexed by the open
    set containing it. Part (b): adjoining a countable intersection, or a set meeting every member,
    preserves the property, so maximality puts both in the family. Part (c): the Sorgenfrey line
    and its square, Examples 3 and 4 of §30, kill (iii) and hence (i); and the step of Lemma 37.1
    that fails is the union of a chain, which for the countable property can lose it -- on the
    positive integers the chain of collections of cofinite tails, each with the property, has a
    union whose countable intersection is empty. Not checked: nothing in this card is transcribed,
    there being no usable published proof.
---

::: {.exercise}

Consider the three statements:

(i) If $X$ is a set and $\mathcal{A}$ is a collection of subsets of $X$ having the countable intersection property, then there is a collection $\mathcal{D}$ of subsets of $X$ such that $\mathcal{D} \supset \mathcal{A}$ and $\mathcal{D}$ is maximal with respect to the countable intersection property.

(ii) Suppose $\mathcal{D}$ is maximal with respect to the countable intersection property.
Then countable intersections of elements of $\mathcal{D}$ are in $\mathcal{D}$.
Furthermore, if $A$ is a subset of $X$ that intersects every element of $\mathcal{D}$, then $A$ is an element of $\mathcal{D}$.

(iii) Products of Lindelöf spaces are Lindelöf.

(a) Show that (i) and (ii) together imply (iii).

(b) Show that (ii) holds.

(c) Products of Lindelöf spaces need not be Lindelöf (see §30). Therefore (i) does not hold.
If one attempts to generalize the proof of Lemma 37.1 to the countable intersection property, at what point does the proof break down?
:::

::: {.solution}
No usable published solution of this exercise was located in the retained sets. The one that reaches it, Ana Emilia de Orellana's *Munkres solutions* (`tmp/sources/munkres-solutions-anadeore.md`), Section 37 Exercise 3, is a corrupted fragment: part (a) breaks off inside its first display, part (b) is the single sentence "The existance of the maximum element in the sequence is what fails in the countable space", which does not bear on statement (ii) at all, and part (c) is not written. Poulsen's §38 sheet covers Exercises 38.4 to 38.9, dbFin's index stops at §67 with a gap before it, and no other retained set covers §37. The argument is therefore the card's own; every step is checked against Lemma 37.1 and Lemma 37.2 of §37 and against Exercise 37.2.

A collection has the *countable intersection property*, CIP, when the intersection of any countable subcollection is nonempty. A single set is a countable subcollection of itself, so every member of such a collection is nonempty.

::: pf

::: {.pf-step #a1}
(a) Assume (i) and (ii). Let $\{X_\alpha\}_{\alpha\in J}$ be Lindelöf and let $\mathcal U$ be an open cover of $X=\prod_\alpha X_\alpha$ with no countable subcover. Then $\mathcal A=\{X\setminus U\mid U\in\mathcal U\}$ has the countable intersection property.

::: pf-proof
Were $\bigcap_n(X\setminus U_n)=\varnothing$ for countably many members, then $X=\bigcup_nU_n$ would be a countable subcover, contrary to the choice of $\mathcal U$.
:::

:::

::: {.pf-step #a2}
There is a collection $\mathcal D\supseteq\mathcal A$, maximal with respect to the countable intersection property, and it has the two properties of (ii).

::: pf-proof
The first is (i) applied to $\mathcal A$, which has the property by step [](#a1){.pf-ref}; the second is (ii).
:::

:::

::: {.pf-step #a3}
Finite intersections of members of $\mathcal D$ are members of $\mathcal D$, the set $X$ is a member, and any $B\subseteq X$ meeting every member of $\mathcal D$ is a member.

::: pf-proof
A finite intersection is a countable one, so the first clause of (ii) gives the first assertion, and $X$ is the intersection of one member with itself. For the last, $X$ meets every member of $\mathcal D$ because members are nonempty, so $X\in\mathcal D$; and $B$ meets every member, so the second clause of (ii) gives $B\in\mathcal D$.
:::

:::

::: {.pf-step #a4}
For each $\alpha$ there is a point $x_\alpha$ of $X_\alpha$ lying in $\overline{\pi_\alpha(D)}$ for every $D\in\mathcal D$.

::: pf-proof
The family $\{\overline{\pi_\alpha(D)}\mid D\in\mathcal D\}$ has the countable intersection property: for countably many members, $\bigcap_n\overline{\pi_\alpha(D_n)}\supseteq\bigcap_n\pi_\alpha(D_n)\supseteq\pi_\alpha\bigl(\bigcap_nD_n\bigr)$, which is nonempty because $\mathcal D$ has the property and $\pi_\alpha$ is onto. The space $X_\alpha$ is Lindelöf, so Exercise 37.2 puts a point in the total intersection of the closures.
:::

:::

::: {.pf-step #a5}
The point $x=(x_\alpha)$ lies in $\overline D$ for every $D\in\mathcal D$.

::: pf-proof
Let $B=\bigcap_{\alpha\in F}\pi_\alpha^{-1}(U_\alpha)$ be a basis element containing $x$, with $F$ finite and $U_\alpha$ a neighbourhood of $x_\alpha$. For $\alpha\in F$ one has $x_\alpha\in\overline{\pi_\alpha(D)}$, so $U_\alpha$ meets $\pi_\alpha(D)$, that is, $\pi_\alpha^{-1}(U_\alpha)$ meets $D$; by step [](#a3){.pf-ref} then $\pi_\alpha^{-1}(U_\alpha)\in\mathcal D$, and by the same step $B\in\mathcal D$, being a finite intersection. Since $D\in\mathcal D$ as well and $\mathcal D$ has the property, $B\cap D\ne\varnothing$. Every basis element about $x$ therefore meets $D$.
:::

:::

::: {.pf-step #a6}
$X$ is Lindelöf, and so (a) holds.

::: pf-proof
Since $\mathcal U$ covers $X$, choose $U\in\mathcal U$ with $x\in U$. Its complement $X\setminus U$ belongs to $\mathcal A\subseteq\mathcal D$, and it is closed, so by step [](#a5){.pf-ref} $x\in\overline{X\setminus U}=X\setminus U$, which contradicts $x\in U$. Hence no open cover of $X$ lacks a countable subcover.
:::

:::

::: {.pf-step #b1}
(b) Let $\mathcal D$ be maximal with respect to the countable intersection property. Then a countable intersection of members of $\mathcal D$ is a member of $\mathcal D$.

::: pf-proof
Let $E=\bigcap_nD_n$ with each $D_n\in\mathcal D$. The collection $\mathcal D\cup\{E\}$ has the property: a countable subcollection either omits $E$ and is a countable subcollection of $\mathcal D$, or contains $E$, and then its intersection is $E\cap\bigcap_mD'_m=\bigcap_nD_n\cap\bigcap_mD'_m$, an intersection of countably many members of $\mathcal D$, hence nonempty. So $\mathcal D\cup\{E\}$ contains $\mathcal D$ and has the property, and maximality forces $E\in\mathcal D$.
:::

:::

::: {.pf-step #b2}
If $A\subseteq X$ meets every member of $\mathcal D$, then $A\in\mathcal D$, and this completes (b).

::: pf-proof
The collection $\mathcal D\cup\{A\}$ has the property: a countable subcollection omitting $A$ is one of $\mathcal D$, and one containing $A$ has intersection $A\cap D_1\cap\cdots\cap D_m$, where $D_1\cap\cdots\cap D_m\in\mathcal D$ by step [](#b1){.pf-ref} and a finite intersection is countable, so that intersection is nonempty because $A$ meets every member of $\mathcal D$. Maximality gives $A\in\mathcal D$. With step [](#b1){.pf-ref} this is statement (ii).
:::

:::

::: {.pf-step #c1}
(c) Products of Lindelöf spaces need not be Lindelöf, so statement (i) fails.

::: pf-proof
The Sorgenfrey line is Lindelöf and its square is not: both are Example 3 and Example 4 of §30. If (i) held, (a) and (b) would make every product of Lindelöf spaces Lindelöf, since (b) is a theorem; so (i) fails.
:::

:::

::: {.pf-step #c2}
The step of Lemma 37.1 that breaks down for the countable intersection property is the passage from a chain to its union.

::: pf-proof
Lemma 37.1 orders the collections with the finite intersection property by inclusion and applies Zorn's lemma; the union of a chain of such collections has the finite intersection property because a finite subfamily of the union lies in one member of the chain, a chain being directed for finite subfamilies. For the countable intersection property this fails. On $X=\ZZ_+$ let $\mathcal D_n=\{\ZZ_+\setminus\{1\},\ldots,\ZZ_+\setminus\{n\}\}$; each $\mathcal D_n$ has the property, its members being finitely many and their intersections nonempty, and $\mathcal D_1\subseteq\mathcal D_2\subseteq\cdots$, while the union contains every $\ZZ_+\setminus\{k\}$ and their countable intersection is empty. So the union of the chain lacks the property, Zorn's lemma does not apply, and (i) is not available — as it must not be, by step [](#c1){.pf-ref}.
:::

:::

::: {.pf-step}
Parts (a), (b) and (c) answer the exercise.

::: pf-proof
Step [](#a6){.pf-ref} proves (a) from (i) and (ii), steps [](#b1){.pf-ref} and [](#b2){.pf-ref} prove (ii) outright, and steps [](#c1){.pf-ref} and [](#c2){.pf-ref} give the failure of (i) and name the broken step.
:::

:::

:::
:::
