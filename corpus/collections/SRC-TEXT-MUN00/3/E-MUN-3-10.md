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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the two parts, which is what Queue D asks for on this card. Part (a) splits at the sign of x, with the non-negative case proved first and the negative case reduced to it by oddness of f, which is how the set's solution runs; part (b) has the interval computation, the left inverse and the right inverse as separate steps, and the two square completions the prose abbreviated are written out. Statement re-read against Munkres, Topology (2000), §3 Exercise 10, printed p. 29, and the argument against Dan Whitman's set, Exercise 3.10, printed pp. 28-30. No statement repair.
---

::: {.exercise}

(a) Show that the map $f: (-1, 1) \to \RR$ of Example 9, that is $f(x) = x/(1-x^2)$, is order preserving.

(b) Show that the equation $g(y) = 2y/[1 + (1 + 4y^2)^{1/2}]$ defines a function $g: \RR \to (-1, 1)$ that is both a left and a right inverse for $f$.
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.10, printed pp. 28--30** (`tmp/sources/munkres-solutions-whitman.pdf`); part (a) is his, and part (b) is his with the square completions written out below. The statement is Munkres, *Topology*, 2nd ed. (2000), §3 Exercise 10. Throughout, $\abs{t}<1$ gives $t^2<1$ and hence $1-t^2>0$.

::: pf

::: {.pf-step #part-a}
(a) $f(x)=x/(1-x^2)$ is order preserving on $(-1,1)$: if $-1<x<y<1$ then $f(x)<f(y)$.

::: pf-proof

::: {.pf-step #case-nonnegative}
If $0\le x<y$ then $f(x)<f(y)$.

::: pf-proof
Here $0\le x^2<y^2<1$, so $0<1-y^2<1-x^2$ and therefore $1/(1-x^2)<1/(1-y^2)$ as both denominators are positive. Hence
$$
f(x)=\frac{x}{1-x^2}\le\frac{y}{1-x^2}<\frac{y}{1-y^2}=f(y),
$$
the first inequality because $1-x^2>0$ and $x<y$, the second because $y>0$ and $0<1-y^2<1-x^2$.
:::

:::

::: {.pf-step #case-negative}
If $x<0$ then $f(x)<f(y)$ for every $y\in(x,1)$.

::: pf-proof
If $y\le0$ then $0\le-y<-x<1$, so step [](#case-nonnegative){.pf-ref} gives $f(-y)<f(-x)$; and $f(-t)=-t/(1-t^2)=-f(t)$ for every $t$, so $-f(y)<-f(x)$, that is $f(x)<f(y)$. If $y>0$ then $f(x)<0<f(y)$, because $x<0<y$ and both denominators are positive.
:::

:::

The two cases cover every pair $-1<x<y<1$, so $f$ is order preserving.
:::

:::

::: {.pf-step #part-b}
(b) $g(y)=2y/\bigl(1+(1+4y^2)^{1/2}\bigr)$ defines a map $g:\RR\to(-1,1)$ which is both a left and a right inverse for $f$.

::: pf-proof

::: {.pf-step #into-interval}
$g$ is defined on $\RR$ and $\abs{g(y)}<1$ for every $y$.

::: pf-proof
The denominator $1+(1+4y^2)^{1/2}$ is at least $2$, so $g(y)$ is defined for every real $y$. Put $s=(1+4y^2)^{1/2}\ge1$, so that $s^2=1+4y^2$. Then
$$
1-g(y)^2=1-\frac{4y^2}{(1+s)^2}=\frac{(1+s)^2-4y^2}{(1+s)^2}=\frac{1+2s+s^2-4y^2}{(1+s)^2}=\frac{1+2s+(1+4y^2)-4y^2}{(1+s)^2}=\frac{2(1+s)}{(1+s)^2}=\frac{2}{1+s}>0,
$$
so $g(y)^2<1$.
:::

:::

::: {.pf-step #left-inverse}
$(g\circ f)(x)=x$ for every $x\in(-1,1)$.

::: pf-proof
For $\abs{x}<1$ we have $1-x^2>0$ and
$$
1+4f(x)^2=1+\frac{4x^2}{(1-x^2)^2}=\frac{(1-x^2)^2+4x^2}{(1-x^2)^2}=\frac{1+2x^2+x^4}{(1-x^2)^2}=\frac{(1+x^2)^2}{(1-x^2)^2},
$$
so $(1+4f(x)^2)^{1/2}=(1+x^2)/(1-x^2)$, the positive root. Hence
$$
(g\circ f)(x)=\frac{2x/(1-x^2)}{1+(1+x^2)/(1-x^2)}=\frac{2x/(1-x^2)}{\bigl((1-x^2)+(1+x^2)\bigr)/(1-x^2)}=\frac{2x}{2}=x .
$$
:::

:::

::: {.pf-step #right-inverse}
$(f\circ g)(y)=y$ for every $y\in\RR$.

::: pf-proof
With $s=(1+4y^2)^{1/2}$, step [](#into-interval){.pf-ref} gives $1-g(y)^2=2/(1+s)>0$, and $g(y)=2y/(1+s)$. Hence
$$
(f\circ g)(y)=\frac{g(y)}{1-g(y)^2}=\frac{2y}{1+s}\cdot\frac{1+s}{2}=y .
$$
:::

:::

Steps [](#left-inverse){.pf-ref} and [](#right-inverse){.pf-ref} exhibit $g$ as a left and a right inverse of $f$, and step [](#into-interval){.pf-ref} shows it takes values in the codomain $(-1,1)$ named in the statement.
:::

:::

:::
:::
