---
schema: qual/card@1
id: P-JHUMAY06ANB
kind: problem
title: "Zeros of a septic in the disks of radius one and two"
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared the septic polynomial and the two open disks with May 2006 problem 2 on PDF page 40."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the strict Rouche comparisons on both circles, including the constant one half, and excluded boundary zeros."
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "PDF page 40 prints a normal question mark after the unit disk; restored that punctuation and independently retained the two complete Rouche comparisons."
---

::: {.problem}
2. How many zeros does the polynomial

$$
z ^ { 7 } - 4 z ^ { 3 } + z - { \textstyle { \frac { 1 } { 2 } } }
$$

have in the unit disk $\{|z|<1\}$? How many zeros does it
have in the disk $\{|z|<2\}$ of radius two? Justify your answers.
:::

::: solution
Write $p(z)=z^7-4z^3+z-1/2$. The requested zero counts,
with multiplicities, are $\boxed{3}$ in $|z|<1$ and
$\boxed{7}$ in $|z|<2$.

<1>1. The cubic term determines the unit-disk count.
::: proof
For $|z|=1$,
$$
|p(z)-(-4z^3)|=|z^7+z-1/2|
\leq1+1+\frac12=\frac52<4=|-4z^3|.
$$
Rouché's theorem applies because both polynomials are
holomorphic on a neighborhood of the closed disk [@SS03].
It gives the same number of zeros for $p$ and $-4z^3$
in that disk. The latter has a zero of multiplicity three
at zero and no other zero. The strict inequality also
gives $|p|\geq4-5/2>0$ on the boundary.
:::

<1>2. The leading term determines the radius-two count.
::: proof
For $|z|=2$,
$$
|p(z)-z^7|=|-4z^3+z-1/2|
\leq32+2+\frac12=\frac{69}{2}<128=|z^7|.
$$
Another application of Rouché's theorem gives seven
zeros in $|z|<2$, counted with multiplicity, the same
count as for $z^7$ [@SS03]. The strict comparison excludes
zeros on $|z|=2$. Thus the two counts refer to the open
disks specified in the question, with no boundary ambiguity.
:::
:::
