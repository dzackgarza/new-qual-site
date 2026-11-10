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
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 17.18, printed pp. 171--172** (`tmp/sources/munkres-solutions-whitman.pdf`); the five answers are his, and "positron0802", *Solutions to Topology, Chapter 2*, Exercise 17.18, PDF p. 9, gives the same five. His reduction to the limit points of a horizontal slice is stated below in a form that separates the two exceptional heights $0$ and $1$, which is where the dictionary order behaves differently from a product.

The answers, in the ordered square $I_{o}^{2}=[0,1]\times[0,1]$ with the dictionary order,
$$
\overline{A}=A\cup\{(0,1)\},\qquad \overline{B}=B\cup\{(1,0)\},
$$
$$
\overline{C}=C\cup\{(1,0)\}\cup\big(\{x\}\times\{1\}:0\le x<1\big),\qquad
\overline{D}=D\cup\big(\{x\}\times\{0\}:0<x\le1\big)\cup\big(\{x\}\times\{1\}:0\le x<1\big),
$$
$$
\overline{E}=\{\tfrac12\}\times[0,1].
$$

**Lemma.** Let $A\subset[0,1]$, $b\in[0,1]$ and $B=\{x\times b\mid x\in A\}$. Then $x\times y$ is a limit point of $B$ if and only if either $y=1$ and $x$ is a limit point of $A$ from above, or $y=0$ and $x$ is a limit point of $A$ from below.

*Proof.* In the dictionary order on $I_{o}^{2}$ the interval with endpoints $x\times c$ and $x\times d$ is contained in the fibre $\{x\}\times[0,1]$. Consequently:

If $0<y<1$ and $y\ne b$, the fibre interval between $x\times y$ and $x\times b$ has an endpoint at distance $\abs{y-b}$ from $y$, and the fibre interval $(x\times(y-\varepsilon),x\times(y+\varepsilon))$ with $\varepsilon<\min(y,1-y,\abs{y-b})$ is a basis element containing $x\times y$ and no point of $B$. If $y=b$ with $0<b<1$, the same fibre interval with $\varepsilon<\min(b,1-b)$ contains $x\times y$ and meets $B$ only possibly at $x\times y$ itself, so $x\times y$ is not a limit point. If $y<b$ (respectively $y>b$) the fibre interval $(x\times(y-\varepsilon),x\times(y+\varepsilon))$ with $\varepsilon<\abs{y-b}$ and $\varepsilon<\min(y,1-y)$ avoids $B$ unless $y\in\{0,1\}$, because at $y=0$ no basis element containing $x\times0$ is contained in the fibre: its lower endpoint would have to be strictly below $x\times 0$, so its first coordinate is $<x$, and the interval then contains every point with first coordinate strictly between that and $x$. Symmetrically, at $y=1$ every basis element containing $x\times1$ has upper endpoint with first coordinate $>x$ and so contains every point whose first coordinate lies strictly between $x$ and that endpoint.

So a limit point must have $y=0$ or $y=1$. For $y=0$: a basis element containing $x\times0$ contains some set $\{x'\}\times[0,1)$ with $c<x'\le x$ (take the upper endpoint at first coordinate $x$), and it meets $B$ in a point other than $x\times0$ exactly when $A$ has a point with first coordinate in $(c,x)$. Hence $x\times0$ is a limit point of $B$ exactly when every $c<x$ admits such a point, that is, when $x$ is a limit point of $A$ from below. For $y=1$ the same reasoning with the roles of above and below exchanged gives: $x\times1$ is a limit point exactly when every $d>x$ admits a point of $A$ with first coordinate in $(x,d)$, that is, when $x$ is a limit point of $A$ from above. $\square$

Now the five sets, in each case as $S\cup(\text{limit points of }S)$:

*$A=\{1/n\}\times\{0\}$.* Here $A$ is the slice over $\{1/n\mid n\in\ZZ_{+}\}$ at height $0$; its only limit point is $0$, and only from above, so the only limit point of $A$ in the square is $0\times1$, by the lemma. Hence $\overline{A}=A\cup\{(0,1)\}$.

*$B=\{(1-1/n)\times\tfrac12\}$.* The slice is over $\{1-1/n\}$ at height $\tfrac12$; its only limit point is $1$, from below, so by the lemma the only limit point of $B$ is $1\times0$ and $\overline{B}=B\cup\{(1,0)\}$.

*$C=\{x\times0\mid0<x<1\}$.* The slice is over $(0,1)$ at height $0$. Every $x\in(0,1)$ is a limit point of $(0,1)$ from below, $0$ is a limit point from above, and $1$ is a limit point from below. By the lemma the limit points of $C$ are $\{x\times0\mid0<x\le1\}\cup\{x\times1\mid0\le x<1\}$, and since $C$ already contains $\{x\times0\mid0<x<1\}$,
$$
\overline{C}=C\cup\{(1,0)\}\cup\{x\times1\mid0\le x<1\}.
$$

*$D=\{x\times\tfrac12\mid0<x<1\}$.* The slice is over $(0,1)$ at height $\tfrac12$, so by the lemma the limit points are $\{x\times0\mid0<x\le1\}\cup\{x\times1\mid0\le x<1\}$, and
$$
\overline{D}=D\cup\{x\times0\mid0<x\le1\}\cup\{x\times1\mid0\le x<1\}.
$$

*$E=\{\tfrac12\}\times(0,1)$.* Here $E$ is a vertical fibre, not a horizontal slice. A point $x\times y$ with $x\ne\tfrac12$ has a neighbourhood avoiding $E$: if $x<\tfrac12$ the basis element $[0\times0,\tfrac12\times0)$ contains it and no point of $E$, and if $x>\tfrac12$ the basis element $(\tfrac12\times1,1\times1]$ does. So all limit points have $x=\tfrac12$. Points $\tfrac12\times y$ with $0<y<1$ lie in $E$. For $y=0$: a basis element containing $\tfrac12\times0$ contains $\{\tfrac12\}\times[0,\varepsilon)$ for some $\varepsilon>0$, which meets $E$ in a point other than $\tfrac12\times0$. For $y=1$: a basis element containing $\tfrac12\times1$ contains $\{\tfrac12\}\times(\varepsilon,1]$ for some $\varepsilon<1$, which meets $E$ in a point other than $\tfrac12\times1$. Hence $\overline{E}=\{\tfrac12\}\times[0,1]$.
:::
