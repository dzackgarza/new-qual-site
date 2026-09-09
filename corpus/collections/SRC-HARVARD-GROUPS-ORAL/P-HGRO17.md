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

::: problem
Is every finite group the Galois group over $\mathbb Q$ of the splitting field of a polynomial in $\mathbb Q[x]$?
:::

::: solution
This is the inverse Galois problem over $\mathbb Q$. It is not known in general
whether every finite group occurs in this way.

For a finite Galois extension $K/\mathbb Q$, the primitive-element theorem gives
$K=\mathbb Q(\alpha)$ for some algebraic $\alpha$, and because $K/\mathbb Q$ is
normal, $K$ is the splitting field of the minimal polynomial of $\alpha$.
Thus the formulation in terms of splitting fields is equivalent to asking
whether every finite group is realizable as
\[
\operatorname{Gal}(K/\mathbb Q)
\]
for some finite Galois extension $K/\mathbb Q$.

Many classes of finite groups are known to occur, but no proof or counterexample
is known for the universal assertion.
:::
