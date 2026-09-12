---
schema: qual/card@1
id: P-HGRO27
kind: problem
title: A finite group whose elements have prime-power order
classification:
  areas: [algebra]
  topics: [Group Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Suppose every element of a finite group $G$ has order equal to a power of one fixed prime $p$.
Must $|G|$ be a power of $p$?
Justify your answer.
:::

::: solution
Yes.

Suppose, for contradiction, that some prime $q\ne p$ divides $|G|$. By
Cauchy's theorem, $G$ then contains an element of order $q$. But by hypothesis
every element of $G$ has order a power of $p$, and no positive power of $p$
equals the distinct prime $q$. This is a contradiction.

Therefore no prime other than $p$ divides $|G|$, so
\[
|G|=p^n
\]
for some $n\ge0$.
:::
