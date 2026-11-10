---
schema: qual/card@1
id: E-MUN-3-10
kind: problem
title: An order isomorphism of the interval $(-1,1)$ with the real line
classification:
  areas:
  - topology
  topics:
  - Relations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §3 Exercise 10, printed p. 29, and against
    Example 9 of §3, which defines f(x) = x/(1 - x^2) on (-1,1) and asserts it is an
    order-preserving bijection. The card states f from Example 9 so that the exercise
    stands alone.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.10,
    printed pp. 28-30 (tmp/sources/munkres-solutions-whitman.pdf). His (a) is the case
    split x >= 0 and x < 0 with f odd; the card keeps it. For (b) the card replaces his
    expansion of (f o g)(y) by the identity 1 - g(y)^2 = 2/(1 + sqrt(1 + 4y^2)), from
    which both g(y) in (-1,1) and f(g(y)) = y follow in one line; his verification of
    g o f = id is kept as it stands, through 1 + 4f(x)^2 = (1+x^2)^2/(1-x^2)^2.
---

::: {.exercise}

(a) Show that the map $f: (-1, 1) \to \RR$ of Example 9, that is $f(x) = x/(1-x^2)$, is order preserving.

(b) Show that the equation $g(y) = 2y/[1 + (1 + 4y^2)^{1/2}]$ defines a function $g: \RR \to (-1, 1)$ that is both a left and a right inverse for $f$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.10, printed pp. 28--30** (`tmp/sources/munkres-solutions-whitman.pdf`); part (a) is his, and part (b) is his with the square completion below.

Throughout, $\abs{t}<1$ gives $t^2<1$ and hence $1-t^2>0$.

(a) Let $-1<x<y<1$. If $x\ge0$ then $0\le x<y$, so $x^2<y^2$ and therefore $0<1-y^2<1-x^2$, whence
$$
\frac{1}{1-x^2}<\frac{1}{1-y^2}.
$$
Then
$$
f(x)=\frac{x}{1-x^2}\le\frac{y}{1-x^2}<\frac{y}{1-y^2}=f(y),
$$
the middle inequality because $y>0$ and the two denominators are positive, and it is strict because $y>0$.

If $x<0$: when $y\le0$ we have $0\le-y<-x<1$, so the previous case gives $f(-y)<f(-x)$; since $f(-t)=-t/(1-t^2)=-f(t)$, this is $-f(y)<-f(x)$, that is $f(x)<f(y)$. When $y>0$, $f(x)<0<f(y)$ because $x<0$ and $y>0$ while both denominators are positive.

So $f$ is order preserving on $(-1,1)$.

(b) First, $g$ is defined on all of $\RR$, since $1+(1+4y^2)^{1/2}>0$. Next, put $s=(1+4y^2)^{1/2}\ge1$ and compute
$$
1-g(y)^2
=1-\frac{4y^2}{(1+s)^2}
=\frac{(1+s)^2-4y^2}{(1+s)^2}
=\frac{1+2s+s^2-4y^2}{(1+s)^2}
=\frac{1+2s+(1+4y^2)-4y^2}{(1+s)^2}
=\frac{2(1+s)}{(1+s)^2}
=\frac{2}{1+s}>0 .
$$
Hence $\abs{g(y)}<1$, so $g$ maps $\RR$ into $(-1,1)$.

For $x\in(-1,1)$ we have $f(x)=x/(1-x^2)$ and
$$
1+4f(x)^2
=1+\frac{4x^2}{(1-x^2)^2}
=\frac{(1-x^2)^2+4x^2}{(1-x^2)^2}
=\frac{(1+x^2)^2}{(1-x^2)^2},
$$
so $(1+4f(x)^2)^{1/2}=(1+x^2)/(1-x^2)$, and therefore
$$
(g\circ f)(x)=\frac{2f(x)}{1+(1+4f(x)^2)^{1/2}}
=\frac{2x/(1-x^2)}{1+(1+x^2)/(1-x^2)}
=\frac{2x}{(1-x^2)+(1+x^2)}
=x .
$$
So $g$ is a left inverse of $f$.

For $y\in\RR$, using $1-g(y)^2=2/(1+s)$ from above,
$$
(f\circ g)(y)=\frac{g(y)}{1-g(y)^2}
=\frac{2y}{1+s}\cdot\frac{1+s}{2}
=y .
$$
So $g$ is a right inverse of $f$ as well, and $g=f^{-1}$ by [[E-MUN-2-5]](e).
:::
