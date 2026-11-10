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
Let $I=[0,1]$. The product $I^I=[0,1]^{[0,1]}$ is compact Hausdorff by Tychonoff's theorem (Theorem 37.3). By Exercise 30.16(a) the product $\RR^I$ has a countable dense subset; since $(0,1)$ is homeomorphic to $\RR$, the same holds for $(0,1)^I$, giving a countable set $D_0\subset(0,1)^I$ whose closure in $\RR^I$ contains the closure of $(0,1)^I$, namely $I^I$. So $D_0$ is a countable dense subset of $I^I$; as $I^I$ is infinite, $D_0$ is infinite, and enumerating it as $D=\{y_n\mid n\in\ZZ_+\}$ gives an injective map $f:\ZZ_+\to I^I$, $f(n)=y_n$. The domain $\ZZ_+$ is discrete, so $f$ is continuous, and it is an imbedding onto $D$; since $D$ is dense and $I^I$ is compact Hausdorff, $I^I$ is a compactification of $\ZZ_+$.

By Exercise 38.4 (card E-QZUV0), applied to the compactification $I^I$ of $\ZZ_+$, there is a continuous surjective map $g:\beta(\ZZ_+)\to I^I$. A surjection onto $I^I$ gives
$$
\cardinality{\beta(\ZZ_+)}\ge\cardinality{I^I}=(2^{\aleph_0})^{2^{\aleph_0}}=2^{2^{\aleph_0}}.
$$
:::
