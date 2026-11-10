---
schema: qual/card@1
id: E-LESK3
kind: problem
title: Strong hypotheses short of metrizability
classification:
  areas:
  - topology
  topics:
  - Metrizability
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Jesper Michael Moller, "Solutions to exercises
    in Munkres", file S34.pdf, Exercise 34.2, page 1 of the file
    (tmp/sources/munkres-solutions-poulsen-S34.pdf, Internet Archive snapshot 20180827202044),
    checked against Munkres, Topology (2000), Section 34 Exercise 2, printed p. 218, Example 3 of
    Section 30 (printed p. 192) and Exercise 30.6. Its example is the Sorgenfrey line, and its
    list of properties is the card's: completely normal, first countable, Lindelof, separable, and
    not metrizable. What was corrected: Moller gives "completely normal [Ex 32.4]", and Exercise
    32.4 is the normality of regular Lindelof spaces; the complete normality of R_l is Exercise
    32.7(g), and the card now cites it, having previously justified it by a hereditary-Lindelof
    argument that is no longer on E-RIGIX.
---

::: {.exercise}

Give an example showing that a space can be completely normal, and satisfy the first countability axiom, the Lindelöf condition, and have a countable dense subset, and still not be metrizable.
:::

::: {.solution}
The Sorgenfrey line $\RR_\ell$ is such an example.

- It is completely normal, by Exercise 32.7(g): every pair of separated subsets has disjoint neighbourhoods, built from the basis of half-open intervals.
- It is first countable: the intervals
$$
[x,x+1/n),\qquad n\ge1,
$$
form a countable local basis at $x$.
- It is Lindelöf, indeed hereditarily Lindelöf.
- It is separable: $\QQ$ is dense, since every nonempty basic interval $[a,b)$ contains a rational.
- It is not metrizable. If it were, separability would imply second countability, but $\RR_\ell$ is not second countable: any basis must contain distinct elements $B_x$ with
$$
x\in B_x\subset[x,x+1),
$$
for all real $x$, giving an uncountable basis.

Thus all the listed hypotheses can hold without metrizability.
:::
