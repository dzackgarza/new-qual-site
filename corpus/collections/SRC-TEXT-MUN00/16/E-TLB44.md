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
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 16.3, printed pp. 150--151** (`tmp/sources/munkres-solutions-whitman.pdf`); the answer, the four decompositions and every argument for the five sets are his.

**Answer.** $A$ is open in both $\RR$ and $Y$; $B$ is open in $Y$ but not in $\RR$; $C$ and $D$ are open in neither; $E$ is open in both.

Two facts are used. First, for $0\le a<b$,
$$
\{x\mid a<\abs{x}<b\}=(-b,-a)\cup(a,b),\quad
\{x\mid a<\abs{x}\le b\}=[-b,-a)\cup(a,b],
$$
$$
\{x\mid a\le\abs{x}<b\}=(-b,-a]\cup[a,b),\quad
\{x\mid a\le\abs{x}\le b\}=[-b,-a]\cup[a,b],
$$
each proved by splitting into $x\ge0$, where $\abs{x}=x$, and $x<0$, where $\abs{x}=-x$. Second, if $U\subset Y$ is open in $\RR$ then $U=Y\cap U$ is open in the subspace $Y$.

*$A$.* By the first decomposition, $A=(-1,-\tfrac12)\cup(\tfrac12,1)$, a union of open intervals, so $A$ is open in $\RR$; and $A\subset Y$, so $A$ is open in $Y$.

*$B$.* By the second decomposition, $B=[-1,-\tfrac12)\cup(\tfrac12,1]$. The sets $(-2,-\tfrac12)$ and $(\tfrac12,2)$ are open in $\RR$, so
$$
B=\big((-2,-\tfrac12)\cap Y\big)\cup\big((\tfrac12,2)\cap Y\big)
$$
is open in $Y$. It is not open in $\RR$: $-1\in B$, and for any basis element $(a,b)$ of $\RR$ with $-1\in(a,b)$ we have $a<-1<b$, so $a<(a-1)/2<-1<b$ gives $(a-1)/2\in(a,b)$ while $(a-1)/2<-1$, hence $(a-1)/2\notin B$ and $(a,b)\not\subset B$.

*$C$ and $D$.* By the third and fourth decompositions, $C=(-1,-\tfrac12]\cup[\tfrac12,1)$ and $D=[-1,-\tfrac12]\cup[\tfrac12,1]$. Let $B_{Y}$ be a basis element of the subspace $Y$ containing $\tfrac12$, so $B_{Y}=Y\cap(a,b)$ with $a<\tfrac12<b$. Put $a_{0}=\max(a,-\tfrac12)$ and $y=(a_{0}+\tfrac12)/2$. Then $a\le a_{0}<y<\tfrac12<b$, so $y\in(a,b)$, and $-1<-\tfrac12\le a_{0}<y<\tfrac12<1$, so $y\in Y$; hence $y\in B_{Y}$. But $\abs{y}<\tfrac12$, so $y\notin C$ and $y\notin D$. Thus no basis element of $Y$ containing $\tfrac12$ lies inside $C$ or inside $D$, and neither set is open in $Y$. Since each is a subset of $Y$, neither is open in $\RR$ either: a set open in $\RR$ and contained in $Y$ would be open in $Y$.

*$E$.* For $x<0$ we have $1/x<0$, so $1/x\notin\ZZ_{+}$; for $x>0$ we have $1/x\in\ZZ_{+}$ exactly when $x=1/n$ for some $n$. Hence
$$
E=\big((-1,0)\cup(0,1)\big)-K,\qquad K=\{1/n\mid n\in\ZZ_{+}\}.
$$
The interval $(-1,0)$ is open in $\RR$. If $x\in(0,1)-K$, then $1/x>1$ and $1/x\notin\ZZ_{+}$, so by Exercise 4.9(b) there is a unique $n\in\ZZ_{+}$ with $n<1/x<n+1$, which gives $\tfrac1{n+1}<x<\tfrac1n$; and for any $y\in(\tfrac1{n+1},\tfrac1n)$ we have $n<1/y<n+1$, so $1/y\notin\ZZ_{+}$ and $y\in E$. So each point of $E$ lies in an open interval contained in $E$, and $E$ is open in $\RR$ (Exercise 13.1); as $E\subset Y$, $E$ is open in $Y$ as well.
:::
