---
schema: qual/card@1
id: E-YQUO1
kind: problem
title: Peano spaces and the Hahn-Mazurkiewicz theorem
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Connectedness
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
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §44 Exercise 4 (printed p. 275) was located; the sets searched are listed in
    the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against the book, part
    (a) following the exercise's hint. Compactness and connectedness of X = f(I) are Theorem 26.5 and
    Theorem 23.5. The hint is discharged: a closed subset of the compact space I has compact image, closed
    in the Hausdorff space X, so f is a closed map, and its fibers are closed subsets of I hence compact
    (Theorem 26.2 and Theorem 17.5), which is the definition of a perfect map in Exercise 31.7.
    Weak local connectedness is proved on the card in the form of §25: for x in U take the compact fiber F
    inside the open set f^{-1}(U), cover F by finitely many connected basis intervals inside f^{-1}(U),
    and use closedness of f to obtain a neighbourhood of x whose image lies in the union of the images of
    those intervals, a connected set inside U. Metrizability follows because second countability is
    transferred by the perfect map (the already sourced Exercise 31.7(d), card E-Y4MFU) and a second
    countable compact Hausdorff space is metrizable by the Urysohn metrization theorem (Theorem 34.1,
    with Theorem 32.3 giving normality and Theorem 30.2 hereditary second countability). Part (b) is the
    exercise's own instruction to assume the Hahn-Mazurkiewicz theorem and verify its hypotheses for
    I^omega: compactness by the Tychonoff theorem (Theorem 37.3), metrizability by Theorem 20.5,
    connectedness because a product of connected spaces is connected (Theorem 23.6 for the finite pieces,
    Theorem 23.3 for their union over a common point and Theorem 23.4 for the closure, an argument the
    card now writes out in place of the bare appeal it made before), and weak local connectedness from the
    basis of products of connected intervals, connected for the same reason.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). For part (a), Math StackExchange 2594189, "Peano
    space is a continuous image of the unit interval I" (2018-01-06), has Henno Brandsma's answer
    2594343 proving compactness, connectedness, local connectedness and metrizability of such an
    image by citing Willard's Theorems 17.7, 26.3, 27.12 and Corollary 23.2, not by proving them
    from a text at hand, so it is a pointer rather than a proof and is not transcribed. For part
    (b), answer 74824 by GEdgar to Math StackExchange 74766 (2011-10-22) constructs a continuous
    surjection I -> I^\omega from a continuous surjection onto I^2 by composing components, which
    is what part (b) asks for once the Hahn--Mazurkiewicz theorem is assumed, and the card's own
    part (b) neither cites nor is that construction. No published treatment of either part against
    Munkres' numbering was located: dbFin has no chapter-7 or chapter-8 page here (404, checked
    2026-11-15), and no GitHub Munkres repository named in the COMPLAINTS.md entry for §30--§36
    reaches Chapter 7. The card keeps its own proof, which this pass did not re-read; the search is
    recorded in the COMPLAINTS.md entry for §43--§50 with every query.

- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). The AoPS blog post by cinnamon_e, "Topology by
    Munkres Chapter 7 | Day 16" (2025-09-09, listed on the blog's topology tag page
    https://artofproblemsolving.com/community/c3401823t440f3401823_topology, text at
    tmp/sources/aops-shooting-star-munkres-ch7-day16.md), answers this exercise, at its item 4 of
    §44. The text is held, but the formulas are not: the extraction drops every inline formula, so
    the answer reads as the words between blanks and cannot be transcribed or checked. It is
    recorded here and in the COMPLAINTS.md entry for §43--§50 as located with its formulas
    unreadable, the site answering an automated request with a Cloudflare human check, which is not
    worked around. The card keeps its own proof.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2 with (a) and (b) as the top-level parts and (b) as
    the QED step. Re-checked every claim: $I$ compact and connected gives the same for the image;
    a closed subset of $I$ is compact so its image is closed, and fibres are closed and compact,
    which is the perfect map; the fibre over $x$ is covered by finitely many intervals inside
    $f^{-1}(U)$, their images are connected with common point $x$, and $X-f(I-W)$ is an open
    neighbourhood of $x$ inside $C$ because $f$ is closed and onto; second countability transfers by
    E-Y4MFU(d); and compact Hausdorff gives regularity, so Urysohn's theorem metrizes. For (b):
    Tychonoff, Theorem 20.5, the union of the $X_F$ for connectedness, and connected basic
    neighbourhoods for weak local connectedness. Added: the explicit verification that
    $f^{-1}(x)\cap V_i\ne\varnothing$ and that the closure of a connected set is connected, both
    used implicitly before, and the observation that weak local connectedness implies the local
    connectedness that Hahn--Mazurkiewicz needs (§25 Exercise 6). Not claimed: a published solution;
    the located §44 set is unreadable for formulas, as the audit records.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Rendered wording only. The opening sentence called the AoPS post "the one located, on §44",
    although the `source-checked` event of 2026-11-15 names it by author, date and file and records
    why it cannot be transcribed: the extraction drops every inline formula, and the site answers an
    automated request with a human check. The sentence now says that, so a reader of the solution
    alone learns which retained document covers the exercise and why the card keeps its own proof.
    No step of the proof changed, and no claim about the post beyond the recorded one is added.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Issue #169 read, with one duplicated sentence removed and the #184 repair. (a): $I$ compact and
    connected give the same for $X$; a closed subset of $I$ is compact, its image is compact hence
    closed in the Hausdorff $X$, and a fibre is closed, so $f$ is perfect; weak local connectedness
    is witnessed by $C=\bigcup_if(V_i)$, connected through the common point $x$ and containing the
    open neighbourhood $X-f(I-W)$ of $x$; and $X$ is second countable as the image of a perfect map,
    E-Y4MFU (d), with Theorem 34.1 metrizing it. (b): the Hilbert cube is compact (Theorem 37.3),
    metrizable (Theorem 20.5) and connected, the union of the connected sets $X_F$ being connected
    and dense; each basic neighbourhood is connected by the same argument, so the cube is weakly
    locally connected and hence locally connected by §25 Exercise 6, whose statement is as quoted;
    Hahn--Mazurkiewicz then applies. The solution's own citation of [H-Y] by page is replaced by
    the exercise's reference to it. Citation by number: §44 Exercise 4, Theorems 20.5, 23.3, 23.5,
    23.6, 24.1, 26.2, 26.3, 26.5, 27.1, 34.1 and 37.3, and §25 Exercise 6.

- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Issue #169 second read, on the verification member's report of this card. Five one-line
    repairs, none affecting a conclusion. The base of $I$ is not the family of open intervals but
    the sets $I\cap(c,d)$, the rays included: for the quotient $I\to S^1$ the fibre $\{0,1\}$ over
    the image of the endpoints lies in no open interval of $I$ contained in the preimage of a
    neighbourhood of that point. The second countability sentence inverted the exercise: what is
    used is that the image of a second countable space under a perfect map is second countable.
    Perfect maps are defined in §31 Exercise 7, not in §46. Theorem 20.5 metrizes
    $\RR^\omega$ in the uniform metric, not $\RR^\omega$ as a product, so $I^\omega$ is metrizable
    as a subspace of it. And $X_F$ is homeomorphic to, not equal to, a finite product of intervals.

---

::: {.exercise}

(a) Let $X$ be a Hausdorff space.
Show that if there is a continuous surjective map $f: I \to X$, then $X$ is compact, connected, weakly locally connected, and metrizable.
[Hint: Show $f$ is a perfect map.]

(b) The converse of the result in (a) is a famous theorem of point-set topology called the Hahn-Mazurkiewicz theorem (see [H-Y], p. 129). Assuming this theorem, show there is a continuous surjective map $f: I \to I^\omega$.

A Hausdorff space that is the continuous image of the closed unit interval is often called a Peano space.
:::

::: {.solution}
The retained solution that answers this exercise is the AoPS blog post by cinnamon_e, *Topology by Munkres Chapter 7 | Day 16* (2025-09-09), at its item 4 of §44, held as `tmp/sources/aops-shooting-star-munkres-ch7-day16.md`; the extraction drops every inline formula, so its answer reads as the words between blanks and cannot be transcribed, and the blog's site answers an automated request with a human check that is not worked around. The argument below is therefore the card's own, checked against the book's numbered theorems; the audit events record the search that located that post.

::: pf

::: {.pf-step #compact-connected}
(a) If $f\colon I\to X$ is continuous and onto and $X$ is Hausdorff, then $X$ is compact and connected.

::: pf-proof
$I$ is compact (Theorem 27.1), and a continuous image of a compact space is compact (Theorem 26.5), so $X=f(I)$ is compact. $I$ is connected (Theorem 24.1), and a continuous image of a connected space is connected (Theorem 23.5), so $X$ is connected.
:::

:::

::: {.pf-step #perfect}
(a) $f$ is a closed map and each of its fibres is compact.

::: pf-proof
A closed subset $F$ of $I$ is compact, being a closed subset of a compact space (Theorem 26.2); its image $f(F)$ is compact (Theorem 26.5) and therefore closed in the Hausdorff space $X$ (Theorem 26.3). A fibre $f^{-1}(x)$ is closed in $I$ because $\{x\}$ is closed in $X$ and $f$ is continuous, hence compact. So $f$ is a perfect map in the sense of §31 Exercise 7.
:::

:::

::: {.pf-step #weakly-locally-connected}
(a) $X$ is weakly locally connected.

:::: pf-proof

::: {.pf-step #finitely-many-intervals}
For $x\in X$ and an open neighbourhood $U$ of $x$ there are finitely many connected open intervals $V_1,\ldots,V_m$ with $f^{-1}(x)\subseteq V_1\cup\cdots\cup V_m\subseteq f^{-1}(U)$.

::: pf-proof
$f^{-1}(x)$ is compact by step [](#perfect){.pf-ref} and lies in the open set $f^{-1}(U)$, since $f(f^{-1}(x))=\{x\}\subseteq U$. The sets $I\cap(c,d)$, the rays $[0,b)$ and $(a,1]$ among them, form a base for $I$, so each point of $f^{-1}(x)$ lies in one of them contained in $f^{-1}(U)$, and compactness extracts a finite subcover; each is connected.
:::

:::

::: {.pf-step #connected-neighbourhood}
The set $C=\bigcup_{i=1}^{m}f(V_i)$ is connected, lies in $U$, and contains an open neighbourhood of $x$.

::: pf-proof
Each $f(V_i)$ is connected, being a continuous image of a connected set, and contains $x=f(p)$ for any $p\in V_i\cap f^{-1}(x)$, which is nonempty because the $V_i$ cover $f^{-1}(x)$. A union of connected sets with a common point is connected, so $C$ is connected; and $f(V_i)\subseteq U$ because $V_i\subseteq f^{-1}(U)$. For the neighbourhood: $W=V_1\cup\cdots\cup V_m$ is open with $f^{-1}(x)\subseteq W$, so $x\notin f(I-W)$, and $X-f(I-W)$ is open because $f$ is closed by step [](#perfect){.pf-ref}. Moreover $X-f(I-W)\subseteq C$: if $y\notin f(I-W)$ then $f^{-1}(y)\subseteq W$, and $f^{-1}(y)\ne\varnothing$ because $f$ is onto, so $f^{-1}(y)$ meets some $V_i$ and $y\in f(V_i)\subseteq C$. Hence $x\in X-f(I-W)\subseteq C$, and $C\subseteq U$.
:::

:::

:::

:::

::: {.pf-step #metrizable}
(a) If there is a continuous surjection $f\colon I\to X$ and $X$ is Hausdorff, then $X$ is metrizable.

::: pf-proof
$I$ is second countable, and the image of a second countable space under a perfect map is second countable, which is [[E-Y4MFU]](d): $f$ is closed with compact fibres by step [](#perfect){.pf-ref}. A compact Hausdorff space is normal, hence regular, so the Urysohn metrization theorem (Theorem 34.1) applies to the second countable regular space $X$ and gives a metric inducing its topology. With steps [](#compact-connected){.pf-ref} and [](#weakly-locally-connected){.pf-ref}, this proves (a).
:::

:::

::: {.pf-step}
(b) There is a continuous surjection $f\colon I\to I^\omega$.

:::: pf-proof

::: {.pf-step #cube-facts}
The Hilbert cube $I^\omega=\prod_{n\ge1}I$ is compact, connected, metrizable and weakly locally connected.

::: pf-proof
Compactness is Tychonoff's theorem (Theorem 37.3). Metrizability: $I^\omega$ is a subspace of $\RR^\omega$, which is metrizable by Theorem 20.5, and a subspace of a metrizable space is metrizable. For connectedness: fix $a\in I^\omega$; for each finite $F\subseteq\ZZ_+$ the set $X_F=\{x:x_i=a_i\text{ for }i\notin F\}$ is homeomorphic to a finite product of intervals, hence connected (Theorem 23.6), and all the $X_F$ contain $a$, so their union $Y$ is connected (Theorem 23.3); $Y$ is dense in $I^\omega$ because a basic open set constrains only finitely many coordinates, and the closure of a connected set is connected, so $I^\omega$ is connected. For weak local connectedness: a basic neighbourhood of a point is $\prod_{i\le N}J_i\times\prod_{i>N}I$ with $J_i$ open intervals containing the coordinates, and this is a product of connected spaces, hence connected by the same union-of-$X_F$ argument; basic sets form a neighbourhood base, so every neighbourhood of a point contains a connected one.
:::

:::

::: {.pf-step}
(b) The Hahn--Mazurkiewicz theorem, assumed as the exercise directs, applies.

::: pf-proof
That theorem states that a Hausdorff space which is compact, connected, locally connected and metrizable is a continuous image of $I$ (the exercise cites [H-Y] for it). Step [](#cube-facts){.pf-ref} supplies compactness, connectedness and metrizability, and supplies weak local connectedness at each point, which by §25 Exercise 6 implies local connectedness; so the hypotheses hold and there is a continuous surjection $I\to I^\omega$.
:::

:::

:::

:::

:::
:::
