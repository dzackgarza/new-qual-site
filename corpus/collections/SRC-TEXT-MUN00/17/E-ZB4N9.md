---
schema: qual/card@1
id: E-ZB4N9
kind: problem
title: Boundaries and interiors of plane regions
classification:
  areas:
  - topology
  topics:
  - Boundary
  - Interior
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 20, printed p. 102, with the
    boundary of Exercise 17.19; the six sets are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 17.20, printed pp.
    174-175. The six interiors and boundaries are his, and positron0802 PDF p. 9 gives the
    same six. Both texts leave the verification to the reader, so the card proves each
    answer: which points have a ball inside the set, which are limits of points of the set,
    and for the open sets B and F the boundary as the closure minus the set (Exercise
    17.19(c)). (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

Find the boundary and the interior of each of the following subsets of $\RR^2$.

(a) $A = \theset{x \times y \mid y = 0}$

(b) $B = \theset{x \times y \mid x > 0 \text{ and } y \neq 0}$

(c) $C = A \cup B$

(d) $D = \theset{x \times y \mid x \text{ is rational}}$

(e) $E = \theset{x \times y \mid 0 < x^2 + y^2 \leq 1}$

(f) $F = \theset{x \times y \mid x \neq 0 \text{ and } y \leq 1/x}$
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 17.20, printed pp. 174--175** (`tmp/sources/munkres-solutions-whitman.pdf`); the six answers are his, and "positron0802", *Solutions to Topology, Chapter 2*, Exercise 17.20, PDF p. 9, gives the same six. Both texts state the answers with the verification abbreviated ("it is easy to show", "would be tedious"); the verifications are supplied below, since the card's obligation is a proof.

The answers are
$$
\begin{aligned}
&\operatorname{Int}A=\varnothing,\quad \overline{A}=A,\quad \operatorname{Bd}A=A;\\
&\operatorname{Int}B=B,\quad \overline{B}=\{x\ge0\},\quad \operatorname{Bd}B=\{x=0\}\cup\{x>0,\ y=0\};\\
&\operatorname{Int}C=\{x>0\},\quad \overline{C}=\{x\ge0\}\cup\{y=0\},\quad \operatorname{Bd}C=\{x=0\}\cup\{x<0,\ y=0\};\\
&\operatorname{Int}D=\varnothing,\quad \overline{D}=\RR^{2},\quad \operatorname{Bd}D=\RR^{2};\\
&\operatorname{Int}E=\{0<x^{2}-y^{2}<1\},\quad \operatorname{Bd}E=\{x^{2}=y^{2}\}\cup\{x^{2}-y^{2}=1\};\\
&\operatorname{Int}F=\{x\ne0,\ y<1/x\},\quad \overline{F}=\{x=0\}\cup\{x\ne0,\ y\le1/x\},\quad \operatorname{Bd}F=\{x=0\}\cup\{x\ne0,\ y=1/x\},
\end{aligned}
$$
where a condition such as $x>0$ abbreviates $\{(x,y)\in\RR^{2}:x>0\}$, and $\operatorname{Bd}$ is as in Exercise 17.19.

We use throughout that a point is interior exactly when some ball around it is contained in the set, and that a point is in the closure of a set exactly when every ball around it meets the set; a ball around $(x,y)$ contains points $(x',y')$ with $x'$ and $y'$ arbitrarily close to $x$ and $y$.

(a) $A=\{y=0\}$. No ball around a point of $A$ is contained in $A$, since it contains points with $y\ne0$: so $\operatorname{Int}A=\varnothing$. The complement $\{y\ne0\}$ is open, so $A$ is closed and $\overline{A}=A$. Every ball meets both $A$ and its complement, so $\overline{\RR^{2}-A}=\RR^{2}$ and $\operatorname{Bd}A=A$.

(b) $B=\{x>0,\ y\ne0\}=(0,\infty)\times(\RR-\{0\})$ is a product of open sets, hence open, so $\operatorname{Int}B=B$. For the closure: if $x>0$ and $y\ne0$ the point is in $B$; if $x>0$ and $y=0$, every ball contains points $(x,y')$ with $0\ne y'$ close to $0$ and $x>0$, which lie in $B$; if $x=0$, every ball contains points with $0<x'<\varepsilon$ and $y'$ close to $y$ and $\ne0$ (for $y=0$ take $y'$ small and nonzero), again in $B$; while if $x<0$ a small ball around $(x,y)$ lies in $\{x'<0\}$, which misses $B$. So $\overline{B}=\{x\ge0\}$, and by Exercise 17.19(c), as $B$ is open, $\operatorname{Bd}B=\overline{B}-B=\{x=0\}\cup\{x>0,\ y=0\}$.

(c) $C=\{x>0\}\cup\{y=0\}$. The set $\{x>0\}$ is open and contained in $C$, so $\{x>0\}\subset\operatorname{Int}C$; a point with $x\le0$ has every ball meeting $\{x<0,\ y\ne0\}$, which misses $C$, so no such point is interior. Hence $\operatorname{Int}C=\{x>0\}$. Since $C=\{x>0\}\cup\{y=0\}$ with the first set dense in $\{x\ge0\}$ and the second closed, $\overline{C}=\{x\ge0\}\cup\{y=0\}$. And $\RR^{2}-C=\{x\le0,\ y\ne0\}$ has closure $\{x\le0\}$, so
$$
\operatorname{Bd}C=\big(\{x\ge0\}\cup\{y=0\}\big)\cap\{x\le0\}=\{x=0\}\cup\{x<0,\ y=0\}.
$$

(d) $D=\QQ\times\RR$. Every ball around any point of $\RR^{2}$ contains points with rational first coordinate and points with irrational first coordinate, so every point is in $\overline{D}$ and no point is in $\operatorname{Int}D$: $\overline{D}=\RR^{2}$ and $\operatorname{Int}D=\varnothing$. By Exercise 17.19(a), $\RR^{2}=\operatorname{Int}D\cup\operatorname{Bd}D=\operatorname{Bd}D$.

(e) $E=\{0<x^{2}-y^{2}\le1\}$. The function $f(x,y)=x^{2}-y^{2}$ is continuous, so $\{0<x^{2}-y^{2}<1\}=f^{-1}((0,1))$ is open and lies in $E$; hence it is contained in $\operatorname{Int}E$. A point with $x^{2}-y^{2}=1$ is not interior: there $x\ne0$, and the points $(x+t,y)$ with $t$ of the sign of $x$ and $\abs{t}$ small have $(x+t)^{2}-y^{2}=1+2xt+t^{2}>1$, so they lie outside $E$ and are arbitrarily close. So $\operatorname{Int}E=\{0<x^{2}-y^{2}<1\}$. The set $f^{-1}([0,1])=\{0\le x^{2}-y^{2}\le1\}$ is closed and contains $E$, so it contains $\overline{E}$. Conversely every point $p=(x,y)$ with $0\le x^{2}-y^{2}\le1$ is a limit of points of $E$: if $0<x^{2}-y^{2}<1$ then $p\in E$; if $x^{2}-y^{2}=1$ then $x\ne0$, and the points $(x-st,y)$ with $s=\operatorname{sign}x$ and $t>0$ small have $x^{2}-y^{2}$ replaced by $1-2\abs{x}t+t^{2}$, which lies in $(0,1)$; and if $x^{2}-y^{2}=0$ then either $p=(0,0)$, and the points $(t,0)$ with $0<t^{2}\le1$ lie in $E$, or $x\ne0$, and the points $(x+st,y)$ have $x^{2}-y^{2}$ replaced by $2\abs{x}t+t^{2}\in(0,1]$. So $\overline{E}=f^{-1}([0,1])$, and $\operatorname{Bd}E=\overline{E}-\operatorname{Int}E=\{x^{2}=y^{2}\}\cup\{x^{2}-y^{2}=1\}$.

(f) $F=\{x\ne0,\ y\le1/x\}$. On the open set $\{x\ne0\}$ the function $g(x,y)=y-1/x$ is continuous, so $\{x\ne0,\ y<1/x\}=g^{-1}((-\infty,0))$ is open and contained in $F$, hence in $\operatorname{Int}F$; a point with $y=1/x$ is not interior, since the points $(x,1/x+t)$ with $t>0$ small lie outside $F$. So $\operatorname{Int}F=\{x\ne0,\ y<1/x\}$. For the closure: points of $F$ are in it; a point $(0,y)$ is in it, because for small $x>0$ one has $1/x>y$ and $(x,y)\in F$ arbitrarily close to $(0,y)$; and a point with $x\ne0$ and $y>1/x$ is not in it, because $g$ is continuous at that point and $g>0$ there, so a small ball around it lies in $\{g>0\}$, which misses $F$. So $\overline{F}=\{x=0\}\cup\{x\ne0,\ y\le1/x\}$, and $\operatorname{Bd}F=\overline{F}-\operatorname{Int}F=\{x=0\}\cup\{x\ne0,\ y=1/x\}$.
:::
