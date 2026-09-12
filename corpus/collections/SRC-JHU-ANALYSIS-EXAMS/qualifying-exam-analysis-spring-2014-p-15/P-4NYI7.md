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
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Read Fall 2013 problem 2 on PDF page 16. The source omits distinctness of x and y; the equality case makes the literal nonempty-set assertion impossible."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Made the distinct-point hypothesis explicit, retained the Cantor-set example, and proved its nonemptiness, measurability, empty interior and absence of isolated points from the interval construction."
---

::: problem
Does there exist a nonempty measurable set $E \subset \mathbb{R}$ satisfying the following two properties:

(a) given distinct $x,y\in E$, there exists $z\notin E$ strictly between $x$ and $y$;

(b) $E$ has no isolated points?
:::

::: remark
The distinctness requirement is necessary. If $x=y\in E$,
there is no point outside $E$ between them, whether
"between" is interpreted strictly or inclusively. Without
that qualification no nonempty set can satisfy (a).
:::

::: solution
<1>1. Take the middle-thirds Cantor set.
::: proof
Start with $C_0=[0,1]$ and obtain $C_{n+1}$ by removing
the open middle third of each component interval of $C_n$.
Then $C_n$ is a union of $2^n$ disjoint closed intervals,
each of length $3^{-n}$, by induction. Set
$E=C=\bigcap_{n\geq0}C_n$. This is closed, hence Lebesgue
measurable [@Fol13], and nonempty since $0\in C_n$ for every $n$.
:::

<1>2. Verify property (a).
::: proof
Let $x<y$ belong to $C$ and choose $n$ with $3^{-n}<y-x$.
If $(x,y)\subset C$, it is contained in $C_n$. An interval
contained in the disjoint union defining $C_n$ must lie
in a single component interval: meeting two components
would force it to contain the gap between them. But a
component of length $3^{-n}$ cannot contain $(x,y)$.
This contradiction shows that some $z\in(x,y)$ lies
outside $C$, proving (a).
:::

<1>3. Verify property (b).
::: proof
Every endpoint of a component interval of $C_n$ survives
all later stages, because only open middle thirds are
removed; it therefore belongs to $C$. For $x\in C$ and
$\varepsilon>0$, choose $n$ with $3^{-n}<\varepsilon$ and
let $J$ be the component interval of $C_n$ containing $x$.
At least one of the two endpoints of $J$ is different
from $x$, lies in $C$, and is at distance at most
$3^{-n}<\varepsilon$ from $x$. Thus $x$ is not isolated.

Therefore the answer is yes; the standard Cantor set satisfies both requested properties.
:::
:::
