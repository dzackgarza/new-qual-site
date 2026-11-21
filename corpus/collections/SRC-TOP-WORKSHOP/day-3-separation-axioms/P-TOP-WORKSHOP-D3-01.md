---
schema: qual/card@1
id: P-TOP-WORKSHOP-D3-01
kind: problem
title: A Hausdorff quotient without a countable basis
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Hausdorff Spaces
  - Countability
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: the classes are the collapsed axis and
    the off-axis singletons, so saturated open sets are easy to exhibit; Hausdorffness uses
    saturated balls inside a half-plane and, for the collapsed point, a strip about the axis disjoint
    from a small ball at the other point; and the failure of a countable neighbourhood basis is the
    diagonal construction $z_n=(t_n,n)\in V_n$, whose set $F$ is closed because the second
    coordinates are distinct integers, so $W=\RR^2\setminus F$ is a saturated open set containing
    the axis but omitting $z_n\in V_n$. Added: the classification of the equivalence classes, the
    saturation check for $W$, and the step from 'not first countable at $p$' to 'no countable
    basis', which the prose stated without its reason. No defect found in the statement (Wisconsin
    January 1998). The collection's provenance is the worksheet, so no retained solution set covers
    the item.
---

::: {.problem}
Let $X=\RR^2$ and define an equivalence relation on $X$ by $(x_1,x_2)\sim(y_1,y_2)$ if and only if they are equal or $x_1=y_1=0$.
Set $Y=X/\sim$.
Show that $Y$ is Hausdorff but does not have a countable basis for its topology.
:::

::: {.solution}
No retained solution set covers this item, the collection's provenance being the worksheet, so the argument is the card's own. Let $q\colon\RR^2\to Y$ be the quotient map, $L=\{0\}\times\RR$ the collapsed axis and $p=q(L)$.

::: pf

::: {.pf-step #classes}
The equivalence classes are $L$ and the singletons of $\RR^2\setminus L$.

::: pf-proof
The relation identifies $(x_1,x_2)$ with $(y_1,y_2)$ either when they are equal or when $x_1=y_1=0$. In the second case both points lie on $L$, and any two points of $L$ satisfy it; so the class of a point of $L$ is all of $L$, and a point off $L$ has $x_1\ne0$, so it is equivalent only to itself.
:::

:::

::: {.pf-step #hausdorff}
$Y$ is Hausdorff.

::: pf-proof
Let two distinct points of $Y$ be represented by $x,y$. If both lie off $L$, then $x_1,y_1\ne0$ and small disjoint Euclidean balls about them, taken inside the half-planes $x_1>0$ or $x_1<0$ that contain them, are saturated and open with disjoint images, which therefore separated the two points. If one of them is $p$, say the other is $x$ with $x_1\ne0$, choose $0<\delta<\abs{x_1}/3$; the strip $S=\{(u,v):\abs u<\delta\}$ is open and saturated, hence $q(S)$ is open and contains $p$, while a small ball about $x$ is disjoint from $S$ and from $L$, so its saturated image is a disjoint open neighbourhood. Hence any two points are separated.
:::

:::

::: {.pf-step #not-first-countable}
$p$ has no countable neighbourhood basis, so $Y$ is not first countable and hence not second countable.

::: pf-proof
Suppose $U_1,U_2,\ldots$ is a countable neighbourhood basis at $p$ and put $V_n=q^{-1}(U_n)$, an open set containing $L$. For each $n$ the point $(0,n)$ lies in $V_n$, so there is $r_n>0$ with $B((0,n),r_n)\subseteq V_n$; choose $0<t_n<\min\{r_n,\tfrac12\}$ and put $z_n=(t_n,n)\in V_n$. The set $F=\{z_n:n\ge1\}$ is closed in $\RR^2$: its second coordinates are distinct integers, so it has no accumulation point in $\RR^2$ and no limit at infinity inside the plane. Hence $W=\RR^2\setminus F$ is open, contains $L$, and is saturated because $F$ misses $L$ and has no two points in a common class; so $q(W)$ is an open neighbourhood of $p$. But $z_n\in V_n\setminus W$ gives $q(z_n)\in U_n\setminus q(W)$, so $U_n\not\subseteq q(W)$ for every $n$, contradicting that the $U_n$ form a neighbourhood basis at $p$. A space with a countable basis is first countable, so $Y$ has no countable basis.
:::

:::

:::
:::
