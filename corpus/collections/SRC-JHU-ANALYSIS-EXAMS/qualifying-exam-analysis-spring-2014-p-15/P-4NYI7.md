---
schema: qual/card@1
id: P-4NYI7
kind: problem
title: Measurable set with dense complement and no isolated points
classification:
  areas:
  - real-analysis
  topics:
  - Lebesgue Measure
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 2 of the JHU Spring 2014 Analysis Qualifying Exam appearance in the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Does there exist a nonempty measurable set $E \subset \mathbb{R}$ satisfying the following two properties:

(a) given $x, y \in E$, there exists $z \notin E$ that lies between $x$ and $y$;

(b) $E$ has no isolated points?

::: solution
<1>1. Take the middle-thirds Cantor set.
::: proof
Let $E=C$, the standard middle-thirds Cantor subset of $[0,1]$. Then $C$ is closed, hence Lebesgue measurable, and it is nonempty.
:::

<1>2. Verify property (a).
::: proof
The Cantor set has empty interior; equivalently, its complement is dense in $[0,1]$. Therefore, if $x,y\in C$ are distinct, say $x<y$, then the open interval
\[
(x,y)
\]
contains a point $z\notin C$. Thus there is a point outside $E$ lying strictly between any two distinct points of $E$.
:::

<1>3. Verify property (b).
::: proof
The Cantor set is perfect: every point of $C$ is a limit point of $C$. Hence $C$ has no isolated points.

Therefore the answer is yes; the standard Cantor set satisfies both requested properties.
:::
:::
