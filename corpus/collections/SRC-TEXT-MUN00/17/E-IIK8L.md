---
schema: qual/card@1
id: E-IIK8L
kind: problem
title: Closures in the ordered square
classification:
  areas:
  - topology
  topics:
  - Closure
  - Order Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 18, printed p. 102, the ordered
    square being the dictionary order square of §16; the five sets are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 17.18, printed pp.
    171-172. The five answers are his, and positron0802 PDF p. 9 gives the same five. His
    reduction to the limit points of a horizontal slice is stated with the two exceptional
    heights 0 and 1 separated, since that is where the dictionary order differs from a
    product: at height 0 no basis element containing a point is confined to its fibre from
    below, and at height 1 none is confined from above. (tmp/sources/munkres-solutions-
    whitman.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into STYLE-08 as the slice lemma and the five closure computations. The lemma's separation of the two exceptional heights $0$ and $1$ was re-checked against the dictionary order, as were the five answers. No statement change.
---

::: {.exercise}

Determine the **closures** of the following subsets of the **ordered square** $I_o^2 = [0, 1] \times [0, 1]$ equipped with the dictionary order topology:

$$
A = \left\{ \frac{1}{n} \times 0 \;\st\; n \in \ZZ_+ \right\},
$$

$$
B = \left\{ \left(1 - \frac{1}{n}\right) \times \frac{1}{2} \;\st\; n \in \ZZ_+ \right\},
$$

$$
C = \{ x \times 0 \mid 0 < x < 1 \},
$$

$$
D = \left\{ x \times \frac{1}{2} \;\st\; 0 < x < 1 \right\},
$$

$$
E = \left\{ \frac{1}{2} \times y \;\st\; 0 < y < 1 \right\}.
$$
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 17.18** (`tmp/sources/munkres-solutions-whitman.pdf`); the five answers are his, and "positron0802", *Solutions to Topology, Chapter 2*, Exercise 17.18, gives the same five. His reduction to the limit points of a horizontal slice is stated below in a form that separates the two exceptional heights $0$ and $1$, which is where the dictionary order behaves differently from a product.

Let $I_{o}^{2}=[0,1]\times[0,1]$ carry the dictionary order topology, and let
$$
A=\Big\{\tfrac1n\times 0\Big\},\quad B=\Big\{\big(1-\tfrac1n\big)\times\tfrac12\Big\},\quad C=\{x\times0\mid0<x<1\},\quad D=\Big\{x\times\tfrac12\mid0<x<1\Big\},\quad E=\Big\{\tfrac12\times y\mid0<y<1\Big\}.
$$

::: pf

::: {.pf-step #slice}

Let $A_{0}\subset[0,1]$, let $b\in[0,1]$ and let $S=\{x\times b\mid x\in A_{0}\}$. Then $x\times y$ is a limit point of $S$ if and only if either $y=1$ and $x$ is a limit point of $A_{0}$ from above, or $y=0$ and $x$ is a limit point of $A_{0}$ from below.

::: pf-proof

In the dictionary order on $I_{o}^{2}$ the interval with endpoints $x\times c$ and $x\times d$ is contained in the fibre $\{x\}\times[0,1]$. If $0<y<1$ and $y\ne b$, the fibre interval $(x\times(y-\varepsilon),x\times(y+\varepsilon))$ with $\varepsilon<\min(y,1-y,\abs{y-b})$ is a basis element containing $x\times y$ and no point of $S$; if $y=b$ with $0<b<1$, the same fibre interval with $\varepsilon<\min(b,1-b)$ meets $S$ at most in $x\times y$ itself; and if $y<b$, respectively $y>b$, the fibre interval with $\varepsilon<\min(\abs{y-b},y,1-y)$ avoids $S$. So a limit point must have $y=0$ or $y=1$, because at those heights no basis element containing $x\times y$ is contained in the fibre: a basis element at $x\times0$ has lower endpoint strictly below $x\times0$, hence first coordinate $<x$, and then it contains every point whose first coordinate lies strictly between that and $x$; symmetrically, a basis element at $x\times1$ has upper endpoint with first coordinate $>x$ and contains every point whose first coordinate lies strictly between $x$ and that endpoint.

For $y=0$: a basis element containing $x\times0$ contains some set $\{x'\}\times[0,1)$ with $c<x'\le x$, and it meets $S$ in a point other than $x\times0$ exactly when $A_{0}$ has a point with first coordinate in $(c,x)$. Hence $x\times0$ is a limit point of $S$ exactly when every $c<x$ admits such a point, that is, exactly when $x$ is a limit point of $A_{0}$ from below. For $y=1$ the same reasoning with the roles of above and below exchanged gives: $x\times1$ is a limit point exactly when every $d>x$ admits a point of $A_{0}$ with first coordinate in $(x,d)$, that is, exactly when $x$ is a limit point of $A_{0}$ from above.

:::

:::

::: pf-step

$\overline{A}=A\cup\{(0,1)\}$.

::: pf-proof

$A$ is the slice over $\{1/n\mid n\in\ZZ_{+}\}$ at height $0$. That set has $0$ as its only limit point, and only from above, so by step [](#slice){.pf-ref} the only limit point of $A$ in the square is $0\times1$.

:::

:::

::: pf-step

$\overline{B}=B\cup\{(1,0)\}$.

::: pf-proof

$B$ is the slice over $\{1-1/n\mid n\in\ZZ_{+}\}$ at height $\tfrac12$. That set has $1$ as its only limit point, and only from below, so by step [](#slice){.pf-ref} the only limit point of $B$ is $1\times0$.

:::

:::

::: pf-step

$\overline{C}=C\cup\{(1,0)\}\cup\{x\times1\mid0\le x<1\}$.

::: pf-proof

$C$ is the slice over $(0,1)$ at height $0$. Every $x\in(0,1)$ is a limit point of $(0,1)$ from below, the point $0$ is a limit point of $(0,1)$ from above, and $1$ is a limit point of $(0,1)$ from below; by step [](#slice){.pf-ref} the limit points of $C$ are $\{x\times0\mid0<x\le1\}\cup\{x\times1\mid0\le x<1\}$, and $C$ already contains $\{x\times0\mid0<x<1\}$.

:::

:::

::: pf-step

$\overline{D}=D\cup\{x\times0\mid0<x\le1\}\cup\{x\times1\mid0\le x<1\}$.

::: pf-proof

$D$ is the slice over $(0,1)$ at height $\tfrac12$, so by step [](#slice){.pf-ref} its limit points are exactly $\{x\times0\mid0<x\le1\}\cup\{x\times1\mid0\le x<1\}$.

:::

:::

::: pf-step

$\overline{E}=\{\tfrac12\}\times[0,1]$.

::: pf-proof

$E$ is a vertical fibre, not a horizontal slice. A point $x\times y$ with $x\ne\tfrac12$ has a neighbourhood avoiding $E$: if $x<\tfrac12$ the basis element $[0\times0,\tfrac12\times0)$ contains it and no point of $E$, and if $x>\tfrac12$ the basis element $(\tfrac12\times1,1\times1]$ does. So all limit points have $x=\tfrac12$. The points $\tfrac12\times y$ with $0<y<1$ lie in $E$. For $y=0$: a basis element containing $\tfrac12\times0$ contains $\{\tfrac12\}\times[0,\varepsilon)$ for some $\varepsilon>0$, which meets $E$ in a point other than $\tfrac12\times0$. For $y=1$: a basis element containing $\tfrac12\times1$ contains $\{\tfrac12\}\times(\varepsilon,1]$ for some $\varepsilon<1$, which meets $E$ in a point other than $\tfrac12\times1$.

:::

:::

:::
:::
