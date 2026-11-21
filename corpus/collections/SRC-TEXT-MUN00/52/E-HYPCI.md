---
schema: qual/card@1
id: E-HYPCI
kind: problem
title: Star-convex sets are simply connected
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 52: Problem 1 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-52-the-fundamental-group/problem-1-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-52-the-fundamental-group/problem-1-solution.txt), and against Munkres, Topology (2000), Section 52
    Exercise 1, printed p. 334. dbFin proves (b) by the straight-line contraction to the star centre and refers to a figure for (a); the card supplies an explicit set in place of the figure, the cone over [-1,1] on [0,1] with the interval [1,2] attached, which is star convex at the origin and not convex because the midpoint of (1,1) and (2,0) is outside it. The rest of the card is dbFin's argument. Nothing needed repair.
---

::: {.exercise}

A subset $A$ of $\RR^n$ is said to be star convex if for some point $a_0$ of $A$, all the line segments joining $a_0$ to other points of $A$ lie in $A$.

(a) Find a star convex set that is not convex.

(b) Show that if $A$ is star convex, $A$ is simply connected.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the contractibility of a star convex set made into explicit homotopies.

::: pf

::: {.pf-step #example}
(a) The set $A=\theset{(x,y)\mid 0\le x\le1,\ \abs{y}\le x}\cup\theset{(x,0)\mid 1\le x\le2}\subseteq\RR^{2}$ is star convex but not convex.

:::: {.pf-proof}

::: {.pf-step #star}
$A$ is star convex with respect to $a_{0}=(0,0)$.

::: pf-proof
Let $(x,y)\in A$; a point of the segment from $a_{0}$ to $(x,y)$ is $t(x,y)=(tx,ty)$ with $0\le t\le1$. If $x\le1$ then $\abs{ty}=t\abs{y}\le tx$ and $0\le tx\le x\le1$, so $t(x,y)$ lies in the first piece. If $x>1$, then $y=0$ (second piece) and $t(x,y)=(tx,0)$; this lies in the first piece when $tx\le1$ and in the second when $1\le tx\le2$. So the whole segment lies in $A$.
:::

:::

::: {.pf-step #not-convex}
$A$ is not convex.

::: pf-proof
$(1,1)$ lies in $A$ ($\abs{1}\le1$) and $(2,0)$ lies in $A$ (second piece with $x=2$). The midpoint of the segment joining them is $(3/2,1/2)$, which is in $A$ only if $3/2\le1$ with $\abs{1/2}\le3/2$, or if its second coordinate is $0$ with $1\le3/2\le2$; neither holds. So $A$ is not convex.
:::

:::

::::

:::

::: {.pf-step #contractible}
(b) If $A$ is star convex with centre $a_{0}$, then $A$ is contractible.

::: pf-proof
Define $H:A\times I\to A$ by $H(x,t)=(1-t)x+t\,a_{0}$, the affine combination in $\RR^{n}$. It is continuous, taking values in $A$ because by star convexity the segment from $x$ to $a_{0}$ lies in $A$; and $H(x,0)=x$, $H(x,1)=a_{0}$ for every $x\in A$. So $H$ is a homotopy from the identity of $A$ to the constant map at $a_{0}$.
:::

:::

::: {.pf-step #simply}
$A$ is simply connected.

::: pf-proof
By step [](#contractible){.pf-ref} the space $A$ is contractible, hence path connected, so it has a fundamental group at $a_{0}$. A loop $f:I\to A$ with $f(0)=f(1)=a_{0}$ is homotopic to the constant loop by $F(s,t)=H\big(f(s),t\big)$, which satisfies $F(s,0)=f(s)$, $F(s,1)=a_{0}$, and $F(0,t)=F(1,t)=a_{0}$ since $f(0)=f(1)=a_{0}$. So every loop at $a_{0}$ is nullhomotopic and $\pi_{1}(A,a_{0})$ is trivial.
:::

:::

::: {.pf-qed}
Part (a) is step [](#example){.pf-ref} and part (b) is steps [](#contractible){.pf-ref} and [](#simply){.pf-ref}.
:::

:::

:::
