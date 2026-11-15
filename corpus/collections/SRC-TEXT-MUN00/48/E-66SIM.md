---
schema: qual/card@1
id: E-66SIM
kind: problem
title: Locally compact Hausdorff spaces are Baire spaces
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §48 Exercise 3 (printed p. 299) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. (The Toronto MAT327 set proves the Baire category
    theorem for locally compact Hausdorff spaces as a course problem, in its assignment 6 solutions Question 1,
    but the statement there is the theorem itself, with the course's own definition of nowhere dense, and is not
    this exercise.) Checked line by line against the book: the criterion of Lemma 48.1 (a space is Baire iff a
    countable intersection of dense open sets is dense); Theorem 29.2 for the shrinking of a neighbourhood to
    one whose closure is compact and inside a given open set; and Theorem 26.9 for the finite intersection
    property, applied to the nested closed sets inside the compact set closure of V_1. What the card uses
    without saying so is that W cap U_1 is nonempty, which holds because U_1 is dense and W is a nonempty open
    set; the induction is sound and the intersection point lies in W and in every U_n. Nothing needed
    correction. The proof then on the card was written in the closed-set form and is replaced by the
    transcription recorded in the event below.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Transcribed, with one correction, from 杨荻 — the post's byline and the site's footer copyright name the
    author — on the site *Yougi — Nocturne* (hexo.yougi.top, whose footer brand is *Nocturne* 夜曲 and whose
    feed is *Yougi 的文字*),
    *Munkres Topology Solution: Chapter 8*, https://hexo.yougi.top/2025/07/10/Munkres-Topology-Solution-Chapter-8/,
    posted 2025-07-10, Ex. 48.3, text at tmp/sources/yougi-2025-munkres-chapter-8.md. The byline is the site's
    own: the post's page carries "© 2026 杨荻" in its footer and the site's feed names the author 杨荻, so
    neither "Yougi" nor "Nocturne" is the author's name — "Yougi" is the site's handle and "Nocturne" its
    brand. The post proves the exercise directly, as the book
    proves Theorem 48.2: given closed A_n with empty interior and an open U_0, choose x in U_0 outside A_1,
    a neighbourhood U_1 of x with compact closure inside U_0, and recurse so that the closures are nested
    inside U_{n-1} with compact closure; the closures are then nonempty closed subsets of the compact
    closure of U_1, so they have a point in common, and that point lies in U_0 and outside every A_n.
    The correction: the post records the recursion as "U_i not a subset of A_{i+1}", which gives no
    separation of the limit point from A_i, and its indexing of the two inclusions is loose; the card asks
    for closure U_n disjoint from A_n at stage n, which is what the choice of x outside A_n and the
    closedness of A_n give, and this is the relation the book's own proof of Theorem 48.2 carries. The
    post's alternative, "the one-point compactification of X is Baire while X is its open subspace", is
    not used: it needs Lemma 48.4, which the book asterisks.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Re-read on issue #144. The transcription above was credited to "Yougi"; the post's byline and the footer
    both name 杨荻, and neither "Yougi" nor "Nocturne" is the author's: the page's og:site_name and title read
    "Yougi — Nocturne", its feed is "Yougi 的文字", and its footer brand is "Nocturne 夜曲" over the theme
    directory /nocturne, so "Yougi" is the site's handle and "Nocturne" its brand. The credit now carries
    it. Nothing of the proof changed: the recursion, the correction of the post's "U_i not a subset of
    A_{i+1}", and the use of Theorem 26.9 for the nested closed sets inside the compact closure of U_1 stand as
    the earlier event records them.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    A reader of this card reported that two events disagree about the site: one called "Yougi" the author's
    account name and "Nocturne" the blog, the other called "Yougi" the name of the blog. Read again from the
    page's own bytes in tmp/sources/yougi-2025-munkres-chapter-8.html, the author is 杨荻 -- the post-meta
    byline is a span "杨荻" after the date, and the footer reads "© 2026 杨荻" -- while og:site_name and the
    title read "Yougi — Nocturne", the feed is "Yougi 的文字", and the footer's brand link is "Nocturne夜曲"
    over the theme directory /nocturne. So "Yougi" is the site's handle and "Nocturne" its brand, and neither
    is the author's name; both events now say that. The header of the text extraction carries the same
    correction. The mathematics was not re-read: the transcription, its correction of the post's "U_i not a
    subset of A_{i+1}" and the nested-closed-set argument stand as recorded.
---

::: {.exercise}

Show that every locally compact Hausdorff space is a Baire space.
:::

::: {.solution}
Let $A_1, A_2, \ldots$ be closed subsets of $X$, each with empty interior, and let $U_0$ be a nonempty open set. It suffices to produce a point of $U_0$ that lies in no $A_n$.

::: pf

::: {.pf-step #shrink}
For every $n \ge 1$ and every nonempty open set $V$ there is a nonempty open set $W$ with $\overline W \subseteq V$, $\overline W$ compact, and $\overline W \cap A_n = \varnothing$.

::: pf-proof
Since $A_n$ has empty interior, $V$ is not contained in $A_n$; choose $x \in V \setminus A_n$. The set $V \setminus A_n$ is a neighbourhood of $x$ because $A_n$ is closed, and $X$ is locally compact Hausdorff, so by Theorem 29.2 there is a neighbourhood $W$ of $x$ with $\overline W$ compact and $\overline W \subseteq V \setminus A_n$. Then $\overline W \cap A_n = \varnothing$.
:::

:::

::: {.pf-step #chain}
There are nonempty open sets $U_1, U_2, \ldots$ with $\overline U_n \subseteq U_{n-1}$, $\overline U_n$ compact, and $\overline U_n \cap A_n = \varnothing$ for every $n \ge 1$.

::: pf-proof
Recursion on $n$, applying step [](#shrink){.pf-ref} to $V = U_{n-1}$: the hypothesis of that step is only that $V$ is nonempty and open, which $U_0$ is by assumption and $U_{n-1}$ is by construction.
:::

:::

::: {.pf-step #point}
$\bigcap_{n \ge 1} \overline U_n \neq \varnothing$.

::: pf-proof
The sets $\overline U_1 \supseteq \overline U_2 \supseteq \cdots$ are closed and nonempty, and they lie in the compact space $\overline U_1$; so the family has the finite intersection property and Theorem 26.9 gives a point in the intersection.
:::

:::

::: pf-qed
Choose $x \in \bigcap_{n \ge 1} \overline U_n$. Since $\overline U_n \subseteq U_{n-1}$ for $n \ge 1$, the point $x$ lies in $U_0$, and since $x \in \overline U_m$ and $\overline U_m \cap A_m = \varnothing$ for every $m \ge 1$, it lies in no $A_m$. Every nonempty open $U_0$ therefore meets the complement of $\bigcup_n A_n$, so that union has empty interior and $X$ is a Baire space.
:::

:::

:::
