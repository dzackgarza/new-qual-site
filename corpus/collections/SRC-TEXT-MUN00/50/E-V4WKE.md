---
schema: qual/card@1
id: E-V4WKE
kind: problem
title: The long line is normal but not metrizable
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Order Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution was located; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00.
    Checked against Munkres, Topology (2000), supplementary Exercise 5 of §50, printed p. 317, with the
    construction of the long line in the exercises of §24 and Theorem 32.4's method for the normality of an
    ordered space. Locally 1-euclidean: each point of the long line has a neighbourhood order-isomorphic to an
    open interval of R. Normal: the long line is a linear continuum, and a linear continuum in its order
    topology is normal. Not metrizable: a metrizable, connected, locally euclidean space has each component an
    m-manifold and so a countable basis, by the last supplementary exercise, while the long line has no
    countable basis. Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Math StackExchange 3460936, "Prove that the long line is
    normal" (asked 2019-12-03; the earlier version of this note said 2019-10-13, which is wrong), has the
    accepted answer 3460975 by Henno Brandsma, posted the same day, which records both halves of the
    non-metrizability: "The long line is not metrisable, because it is limit point compact but not compact (for
    metrisable spaces these notions are equivalent)." The answer's other content is that the long line is
    normal, which is the card's own argument from the linear continuum, and its non-metrizability half is
    the assertion quoted, not a proof. The card's non-metrizability argument therefore stays its own, and
    needs no page of that thread: metrizable, connected and locally
    1-euclidean forces a 1-manifold component with a countable basis by [[E-LI4O5]], and $L$ has none by
    [[E-PQHZN]]. Math StackExchange 2341869, "Locally metrizable but not metrizable space" (asked 2017-06-30,
    as a reader of the page reports; the date was not re-read from here, since the site answers this address
    with a human check and the question has no Wayback snapshot), is about the general phenomenon and gives
    the long line as an example without proving this exercise. Murayama and dbFin have no Chapter 8, and the
    AoPS post *Topology by Munkres Chapter 8 | Day 18*
    (https://artofproblemsolving.com/community/c3401823h3647630) answers §50 with its formulas lost.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Re-read on issue #144. The sentence "As a linearly ordered space in its order topology, $L$ is a linear
    continuum; every linear continuum is normal" had neither proof nor citation, and the card it pointed at,
    [[E-PQHZN]], proves neither statement. The two claims are now derived from the book: $S_\Omega\times[0,1)$
    is a linear continuum (Example 2 of §24, printed p. 155, Exercise 6 of §24, printed p. 158), a convex
    subset of a linear continuum with more than one point is one, $L$ is the ray above the deleted first
    element, and its order topology is the subspace topology (Theorem 16.4, printed p. 91); normality is
    Exercise 8 of §32, printed p. 206, whose conclusion is "every linear continuum is normal". The
    non-metrizability argument is unchanged. Read on their pages: §24 Examples 2 and Exercise 6, Theorem 16.4,
    §32 Exercise 8. Not read: §32 Exercise 8's own three steps, which are the book's proof and are quoted as
    the exercise's conclusion.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Three defects reported by a reader of this card. (a) The proof used the connectedness of L and never
    established it: the paragraph above derives that L is a linear continuum in its own order topology, and
    Theorem 24.1 (printed p. 153) is what makes such a space connected, so the citation is now there. (b)
    The 2026-11-15 note said that one sentence about limit point compactness was the whole of Brandsma's
    answer 3460975; the answer also carries the normality argument, which the card makes for itself from
    the linear continuum, and its non-metrizability half is only the assertion that the long line is limit
    point compact but not compact, so the note is corrected and the card keeps its own proof of
    non-metrizability. (c) The asking date of question 2341869 is 2017-06-30, as corrected in the note
    above. The non-metrizability argument and the local euclidean statement were re-read and kept.
---

::: {.exercise}

Show that the long line ([[E-PQHZN]]) is locally 1-euclidean and satisfies (iv) but not (iii) of Exercise 2.
:::

::: {.solution}
Let $L$ be the long line of [[E-PQHZN]], that is, the ordered set $S_\Omega\times[0,1)$ in the dictionary order with its smallest element $a_0\times 0$ deleted. By [[E-PQHZN]], every point of $L$ has a neighborhood homeomorphic to an open interval in $\RR$, so $L$ is locally $1$-euclidean.

$L$ is a linear continuum, as a linearly ordered set in its order topology. The set $S_\Omega\times[0,1)$ is one, because $S_\Omega$ is well-ordered (Example 2 of §24, printed p. 155, and Exercise 6 of §24, printed p. 158). The set $L$ is the ray $(a_0\times0,\to)$ of $S_\Omega\times[0,1)$, hence convex in it, and a convex subset of a linear continuum having more than one point is again a linear continuum: a nonempty subset of $L$ bounded above by $b\in L$ has the least upper bound it has in $S_\Omega\times[0,1)$, which lies between a point of the subset and $b$ and so in $L$; and between two points of $L$ there is a point of $S_\Omega\times[0,1)$ lying in the interval they span, hence one of $L$. By Theorem 16.4 (printed p. 91) the order topology of $L$ is the topology $L$ inherits as a subspace, so $L$ is a linear continuum in its own order topology, and by Theorem 24.1 (printed p. 153) it is connected. Exercise 8 of §32 (printed p. 206) proves that every linear continuum is normal; hence $L$ satisfies condition (iv) of [[E-OYPV7]].

It is not metrizable. If it were metrizable, then because it is connected and locally $1$-euclidean, [[E-LI4O5]] would make its unique component a $1$-manifold with a countable basis. But by [[E-PQHZN]] the long line has no countable basis. Therefore condition (iii) fails. Thus $L$ satisfies (iv) but not (iii).
:::
