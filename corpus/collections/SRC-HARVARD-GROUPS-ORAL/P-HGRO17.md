---
schema: qual/card@1
id: P-HGRO17
kind: problem
title: The inverse Galois problem over the rationals
classification:
  areas: [algebra]
  topics: [Galois Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction; current open-problem status independently checked against AMS references on the inverse Galois problem.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Is every finite group the Galois group over $\QQ$ of the splitting field of a polynomial in $\QQ[x]$?
:::

::: {.solution}
This is the inverse Galois problem over $\QQ$. It is not known in general
whether every finite group occurs in this way.

For a finite Galois extension $K/\QQ$, the primitive-element theorem gives
$K=\QQ(\alpha)$ for some algebraic $\alpha$, and because $K/\QQ$ is
normal, $K$ is the splitting field of the minimal polynomial of $\alpha$.
Thus the formulation in terms of splitting fields is equivalent to asking
whether every finite group is realizable as
$$
\operatorname{Gal}(K/\QQ)
$$
for some finite Galois extension $K/\QQ$.

Many classes of finite groups are known to occur, but no proof or counterexample
is known for the universal assertion.
:::
