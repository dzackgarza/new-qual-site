---
schema: qual/card@1
id: E-7NRBE
kind: problem
title: Cardinality of the Stone--Čech compactification of $\ZZ_+$
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Jesper Michael Møller, "Solutions to exercises in Munkres", file S38.pdf,
    Exercise 38.8, page 2 of the file (tmp/sources/munkres-solutions-poulsen-S38.pdf; the sheet is dated
    2 April 2005 and its section-38 items name no author; Internet Archive snapshot 20181222125939 of
    web.math.ku.dk/~moller/e02/3gt/opg/S38.pdf). Checked against Munkres, Topology (2000), Section 38
    Exercise 8, printed p. 242, and its printed hint, Exercise 30.16 (a countable dense subset of R^J),
    Tychonoff's theorem (Theorem 37.3) and Exercise 38.4 as proved on the card of E-QZUV0. The sheet's
    chain is: I^I is compact Hausdorff by Tychonoff, it has a countable dense subset by Exercise 30.16,
    and being infinite it is a compactification of Z_+ under an enumeration of that subset; by Exercise
    38.4 every compactification of Z_+ is a continuous image of beta(Z_+), so card beta(Z_+) >= card I^I
    and card I^I = (2^aleph_0)^(2^aleph_0) = 2^(2^aleph_0). What was corrected: the card had replaced the
    book's Exercise 30.16 by the Hewitt-Marczewski-Pondiczery theorem, whose statement it asserted without
    proof and without a reference, and it also carried an unneeded upper bound card beta(Z_+) <= 2^c; the
    card's proof is now the sheet's chain from the book's own hint, and the upper bound is dropped since
    the exercise asks only for the lower one.
---

::: {.exercise}

Show that $\beta(\ZZ_+)$ has cardinality at least as great as $I^I$, where $I = [0, 1]$.
[Hint: The space $I^I$ has a countable dense subset.]
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the countable dense subset of $I^{I}$ and the compactification step separated.

Let $I=[0,1]$.

::: pf

::: {.pf-step #dense}
$I^{I}$ has a countable dense subset.

:::: {.pf-proof}

::: {.pf-step #dense-open-interval}
$(0,1)^{I}$ has a countable dense subset.

::: pf-proof
$(0,1)$ is homeomorphic to $\RR$ (the map $t\mapsto\tan\big(\pi(t-1/2)\big)$), so the product $(0,1)^{I}$ is homeomorphic to $\RR^{I}$, which has a countable dense subset (Exercise 30.16(a), printed p. 195). A homeomorphism carries a countable dense subset to one.
:::

:::

::: {.pf-step #dense-closed-interval}
That countable set is dense in $I^{I}$.

::: pf-proof
$I^{I}$ is the product $\prod_{i\in I}[0,1]$, and the closure of the subset $(0,1)^{I}$ in it is $I^{I}$, because the closure of a product is the product of the closures in the product topology (each $(0,1)$ is dense in $[0,1]$). Density passes through a dense subspace: if $D$ is dense in $S$ and $S$ is dense in $T$, then $D$ is dense in $T$, since a nonempty open set of $T$ meets $S$ and hence meets $D$.
:::

:::

::::

:::

::: {.pf-step #compactification}
$I^{I}$ is a compactification of $\ZZ_{+}$.

::: pf-proof
$I^{I}$ is compact and Hausdorff (Theorem 37.3, Tychonoff's theorem, printed p. 233). Let $D$ be the countable dense subset of step [](#dense){.pf-ref}; $I^{I}$ is infinite, so $D$ is infinite, and enumerating $D=\theset{y_{n}\mid n\in\ZZ_{+}}$ gives a bijection $f:\ZZ_{+}\to D$. The subspace $\ZZ_{+}$ of $\RR$ is discrete, so every map out of it is continuous, and $f$ is injective: $f$ is an imbedding with dense image $D$. So $I^{I}$ is a compact Hausdorff space containing a dense homeomorphic copy of $\ZZ_{+}$, that is, a compactification of it.
:::

:::

::: {.pf-step #surjection}
There is a continuous surjection $\beta(\ZZ_{+})\to I^{I}$.

::: pf-proof
$I^{I}$ is a compactification of $\ZZ_{+}$ by step [](#compactification){.pf-ref}, and every compactification $Y$ of a space $X$ receives a continuous surjection from $\beta(X)$ (Exercise 38.4, printed p. 243; card [[E-QZUV0]]).
:::

:::

::: {.pf-qed}
A surjection onto $I^{I}$ gives $\cardinality{\beta(\ZZ_{+})}\ge\cardinality{I^{I}}=2^{2^{\aleph_{0}}}$, since $\cardinality{I^{I}}=(2^{\aleph_{0}})^{2^{\aleph_{0}}}=2^{2^{\aleph_{0}}}$.
:::

:::

:::
