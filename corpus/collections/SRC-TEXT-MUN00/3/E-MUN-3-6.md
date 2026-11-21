---
schema: qual/card@1
id: E-MUN-3-6
kind: problem
title: Ordering the plane by the translates of the parabola $y=x^2$
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
    Read against Munkres, Topology (2000), §3 Exercise 6, printed p. 29: (x_0,y_0) <
    (x_1,y_1) if y_0 - x_0^2 < y_1 - x_1^2, or the two are equal and x_0 < x_1; show
    this is an order relation and describe it geometrically. The stored statement
    matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.6,
    printed pp. 25-26 (tmp/sources/munkres-solutions-whitman.pdf). The three properties
    and the geometric description by the level curves y - x^2 = c, with c compared first
    and x breaking ties, are his.
---

::: {.exercise}

Define a relation on the plane by setting
$$
(x_0, y_0) < (x_1, y_1)
$$
if either $y_0 - x_0^2 < y_1 - x_1^2$, or $y_0 - x_0^2 = y_1 - x_1^2$ and $x_0 < x_1$. Show that this is an order relation on the plane, and describe it geometrically.
:::

::: {.solution}

The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.6, printed pp. 25--26** (`tmp/sources/munkres-solutions-whitman.pdf`); the three properties and the geometric description are his. Write $\varphi(x,y)=y-x^{2}$ and declare $(x_{0},y_{0})<(x_{1},y_{1})$ when $\varphi(x_{0},y_{0})<\varphi(x_{1},y_{1})$, or when $\varphi$ takes equal values there and $x_{0}<x_{1}$.

::: pf

::: {.pf-step #comparability}

Any two distinct points are comparable.

::: pf-proof

Let $(x_{0},y_{0})\ne(x_{1},y_{1})$. If $\varphi(x_{0},y_{0})\ne\varphi(x_{1},y_{1})$ then one of the two strict inequalities holds, and the point with the smaller value of $\varphi$ is the smaller one. Otherwise $\varphi(x_{0},y_{0})=\varphi(x_{1},y_{1})$; if also $x_{0}=x_{1}$ then $y_{0}=x_{0}^{2}+\varphi(x_{0},y_{0})=x_{1}^{2}+\varphi(x_{1},y_{1})=y_{1}$ and the points coincide, contrary to hypothesis, so $x_{0}\ne x_{1}$ and exactly one of $x_{0}<x_{1}$, $x_{1}<x_{0}$ holds, making one point smaller than the other.

:::

:::

::: {.pf-step #irreflexive}

No point is less than itself.

::: pf-proof

For a point $(x,y)$ we have $\varphi(x,y)=\varphi(x,y)$, so the first alternative of the definition fails, and the second requires $x<x$, which is false. Hence $(x,y)<(x,y)$ is false, which together with step [](#comparability){.pf-ref} makes $<$ a strict order.

:::

:::

::: {.pf-step #transitive}

If $(x_{0},y_{0})<(x_{1},y_{1})$ and $(x_{1},y_{1})<(x_{2},y_{2})$ then $(x_{0},y_{0})<(x_{2},y_{2})$.

::: pf-proof

Write $c_{i}=\varphi(x_{i},y_{i})$. If $c_{0}<c_{1}$ then either $c_{1}<c_{2}$, giving $c_{0}<c_{2}$, or $c_{1}=c_{2}$, giving $c_{0}<c_{2}$ again; in both cases the first alternative holds for the pair $(0,2)$. If $c_{0}=c_{1}$ and $x_{0}<x_{1}$, then either $c_{1}<c_{2}$, giving $c_{0}<c_{2}$, or $c_{1}=c_{2}$ and $x_{1}<x_{2}$, giving $c_{0}=c_{2}$ and $x_{0}<x_{1}<x_{2}$; in both cases $(x_{0},y_{0})<(x_{2},y_{2})$.

:::

:::

::: {.pf-step #geometric}

Geometrically the order stacks the translates $y=x^{2}+c$ of the parabola and orders each translate by its $x$-coordinate.

::: pf-proof

The level set $\{(x,y):\varphi(x,y)=c\}$ is exactly the translate $y=x^{2}+c$ of the standard parabola, and the translates for different $c$ are disjoint and fill the plane, so every point lies on exactly one of them. The first clause of the definition compares the parameters $c$ of the two translates, the smaller $c$ lying below; the second clause, applied when $c$ is the same, compares the horizontal positions on that one parabola, the point further to the right being larger. Thus the plane is ordered as the family of parabolas $y=x^{2}+c$ ordered by $c$, each parabola being ordered left to right.

:::

:::

::: {.pf-step #conclusion}

The relation is an order relation on the plane.

::: pf-proof

An order relation is a relation that is transitive and satisfies the comparability and nonreflexivity conditions. Steps [](#comparability){.pf-ref}, [](#irreflexive){.pf-ref} and [](#transitive){.pf-ref} verify the three, so
$$
\boxed{< \text{is an order relation on } \RR^{2},\text{ ordered like the translates } y=x^{2}+c \text{ of the parabola, each read left to right.}}
$$

:::

:::

:::

:::
