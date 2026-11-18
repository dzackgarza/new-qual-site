---
schema: qual/card@1
id: E-TLB44
kind: problem
title: Open sets in a closed interval versus open sets in the line
classification:
  areas:
  - topology
  topics:
  - Subspace Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §16 Exercise 3, printed p. 92; the five sets are
    stored as printed, Y = [-1,1] as a subspace of R.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 16.3, printed pp.
    150-151. The answer (A and E open in both, B open in Y only, C and D in neither), the
    four decompositions of sets defined by |x|, the witness sets (-2,-1/2) and (1/2,2) for
    B, the point (a-1)/2 for the failure of openness in R, and the point y just below 1/2
    inside every Y-basis element for C and D are his; the computation E = ((-1,0) union
    (0,1)) - K and the interval (1/(n+1), 1/n) at a point of E are his too.
    (tmp/sources/munkres-solutions-whitman.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps and checked each of the five sets against Munkres §16
    Exercise 3, printed p. 92: the four decompositions of sets defined by $\abs{x}$, the
    witness sets $(-2,-1/2)$ and $(1/2,2)$ for $B$, the point $(a-1)/2$ for its failure in
    $\RR$, the point below $1/2$ inside every $Y$-basis element for $C$ and $D$, and
    $E=\big((-1,0)\cup(0,1)\big)-K$. One source line is corrected: the integer $n$ bounding
    $1/x$ follows from §4 Exercise 9(a) (a nonempty subset of $\ZZ$ bounded above has a
    largest element), not from Exercise 4.9(b) as the earlier note said. Whitman, Exercise
    16.3, printed pp. 150-151.
---

::: {.exercise}

Consider the set $Y = [-1, 1]$ as a subspace of $\RR$.
Which of the following sets are open in $Y$?
Which are open in $\RR$?

$$
A = \theset{x \mid \tfrac{1}{2} < \abs{x} < 1},
$$

$$
B = \theset{x \mid \tfrac{1}{2} < \abs{x} \leq 1},
$$

$$
C = \theset{x \mid \tfrac{1}{2} \leq \abs{x} < 1},
$$

$$
D = \theset{x \mid \tfrac{1}{2} \leq \abs{x} \leq 1},
$$

$$
E = \theset{x \mid 0 < \abs{x} < 1 \text{ and } 1/x \notin \ZZ_+}.
$$
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 16.3, printed pp. 150--151** (`tmp/sources/munkres-solutions-whitman.pdf`); the answer, the four decompositions and the arguments for the five sets are his. One source line is corrected: the integer $n$ used for $E$ comes from the well-ordering of the integers, §4 Exercise 9(a), not from a statement about intervals.

Write $Y=[-1,1]$ and $K=\{1/n\mid n\in\ZZ_+\}$.

::: pf

::: {.pf-step #splits}
For $0\le a<b$,
$$
\{x\mid a<\abs{x}<b\}=(-b,-a)\cup(a,b),\qquad
\{x\mid a<\abs{x}\le b\}=[-b,-a)\cup(a,b],
$$
$$
\{x\mid a\le\abs{x}<b\}=(-b,-a]\cup[a,b),\qquad
\{x\mid a\le\abs{x}\le b\}=[-b,-a]\cup[a,b].
$$

::: pf-proof
Split on the sign of $x$. For $x\ge 0$ one has $\abs{x}=x$, so the condition on $\abs{x}$ becomes $a<x<b$, $a<x\le b$, $a\le x<b$ or $a\le x\le b$, giving respectively $(a,b)$, $(a,b]$, $[a,b)$ or $[a,b]$ as the nonnegative part. For $x<0$ one has $\abs{x}=-x>0$, so each condition on $-x$ is equivalent to the same condition with the inequality reversed on $x$: $a<\abs{x}<b$ means $a<-x<b$, that is $-b<x<-a$, and carrying the non-strict inequality to the corresponding endpoint gives $[-b,-a)$ for $a<\abs{x}\le b$, $(-b,-a]$ for $a\le\abs{x}<b$ and $[-b,-a]$ for $a\le\abs{x}\le b$. The displayed identities are the unions of the two parts, since $0$ satisfies none of them as $a\ge 0$ requires $\abs{x}>0$ or $x=0$ entered only in the two non-strict cases, where $a\le 0$ is excluded by $0\le a<b$ unless $a=0$, when the four displays are checked directly. In every case the two parts are as displayed.
:::

:::

::: {.pf-step #subspace}
If $U\subset Y$ is open in $\RR$, then $U$ is open in $Y$.

::: pf-proof
$U=Y\cap U$, and $Y\cap U$ is open in the subspace $Y$ for every set $U$ open in $\RR$ by the definition of the subspace topology. This is the direction used below; the converse is false in general, as $B$ shows.
:::

:::

::: {.pf-step #A}
$A$ is open in $\RR$ and in $Y$.

::: pf-proof
By step [](#splits){.pf-ref} with $a=\tfrac12$ and $b=1$, $A=(-1,-\tfrac12)\cup(\tfrac12,1)$. Each of these two intervals is open in $\RR$, so their union is open in $\RR$. And $A\subset[-1,1]=Y$, so $A$ is open in $Y$ by step [](#subspace){.pf-ref}.
:::

:::

::: {.pf-step #B}
$B$ is open in $Y$ and is not open in $\RR$.

::: pf-proof
By step [](#splits){.pf-ref}, $B=[-1,-\tfrac12)\cup(\tfrac12,1]$. The sets $(-2,-\tfrac12)$ and $(\tfrac12,2)$ are open in $\RR$ and their traces on $Y$ are $[-1,-\tfrac12)$ and $(\tfrac12,1]$, so $B$ is a union of open subsets of the subspace $Y$ and is open in $Y$. It is not open in $\RR$: the point $-1$ lies in $B$, and if $(a,b)$ is a basis element of $\RR$ with $-1\in(a,b)$ then $a<-1<b$, so $a<(a-1)/2<-1<b$ shows $(a-1)/2\in(a,b)$ while $(a-1)/2<-1$ gives $(a-1)/2\notin[-1,1]\supset B$; hence $(a,b)\not\subset B$ and no neighbourhood of $-1$ lies in $B$.
:::

:::

::: {.pf-step #CD}
$C$ and $D$ are open in neither $Y$ nor $\RR$.

::: pf-proof
By step [](#splits){.pf-ref}, $C=(-1,-\tfrac12]\cup[\tfrac12,1)$ and $D=[-1,-\tfrac12]\cup[\tfrac12,1]$. Let $B_{Y}$ be a basis element of the subspace $Y$ containing $\tfrac12$; then $B_{Y}=Y\cap(a,b)$ with $a<\tfrac12<b$. Put $a_{0}=\max\{a,-\tfrac12\}$ and $y=(a_{0}+\tfrac12)/2$. Then $-\tfrac12\le a_{0}<y<\tfrac12$, so $a\le a_{0}<y<b$ and $y\in(a,b)$, while $-1<-\tfrac12\le y<\tfrac12<1$ gives $y\in Y$; hence $y\in B_{Y}$. But $\abs{y}<\tfrac12$, so $y\notin C$ and $y\notin D$. Thus no basis element of $Y$ containing $\tfrac12$ lies in $C$ or in $D$, and neither set is open in $Y$. Each is contained in $Y$, so neither is open in $\RR$ either, since a subset of $Y$ open in $\RR$ would be open in $Y$ by step [](#subspace){.pf-ref}.
:::

:::

::: {.pf-step #E}
$E$ is open in $\RR$ and in $Y$.

:::: pf-proof

::: {.pf-step #E-form}
$E=\big((-1,0)\cup(0,1)\big)-K$.

::: pf-proof
If $x<0$ then $1/x<0$ and so $1/x\notin\ZZ_+$. If $x>0$ then $1/x\in\ZZ_+$ exactly when $1/x=n$ for some $n\in\ZZ_+$, that is exactly when $x=1/n\in K$. Hence, for $0<\abs{x}<1$, the condition $1/x\notin\ZZ_+$ holds exactly when $x\notin K$, and $x\notin K$ is automatic for $x<0$.
:::

:::

::: {.pf-step #E-nbhd}
Every point of $(0,1)-K$ has a neighbourhood in $\RR$ contained in $E$.

::: pf-proof
Let $x\in(0,1)-K$, so $1/x>1$ and $1/x\notin\ZZ_+$. The set $\{m\in\ZZ\mid m\le 1/x\}$ is nonempty, as it contains $1$, and is bounded above, so by §4 Exercise 9(a) it has a largest element $n$. Then $n\le 1/x<n+1$, since $n+1$ is an integer not in the set. Also $n\ge 1$ because $1\le 1/x$. If $n=1/x$ then $x=1/n\in K$, contrary to the choice of $x$; so $n<1/x$ and therefore $1/(n+1)<x<1/n$. For any $y\in\big(1/(n+1),1/n\big)$ we have $n<1/y<n+1$, so $1/y\notin\ZZ_+$ and $y\in E$ by step [](#E-form){.pf-ref}. Hence the open interval $\big(1/(n+1),1/n\big)$ is a neighbourhood of $x$ contained in $E$.
:::

:::

::: {.pf-step}
$E$ is open in $\RR$ and in $Y$.

::: pf-proof
$(-1,0)$ is open in $\RR$ and lies in $E$, so each of its points has a neighbourhood in $E$. Each point of $(0,1)-K$ has one by step [](#E-nbhd){.pf-ref}. By step [](#E-form){.pf-ref} these two pieces exhaust $E$, so every point of $E$ has a neighbourhood contained in $E$, and $E$ is open in $\RR$ by Munkres §13 Exercise 1. Since $E\subset Y$, step [](#subspace){.pf-ref} makes $E$ open in $Y$.
:::

:::

:::

:::

::: {.pf-step}
The answer: $A$ and $E$ are open in both $Y$ and $\RR$; $B$ is open in $Y$ but not in $\RR$; $C$ and $D$ are open in neither.

::: pf-proof
Steps [](#A){.pf-ref}, [](#B){.pf-ref}, [](#CD){.pf-ref} and [](#E){.pf-ref} settle the five sets, and they are the only sets asked about.
:::

:::

:::
:::
