---
schema: qual/card@1
id: P-AGHTWCUBIC
kind: problem
title: The twisted cubic is an affine variety of dimension one
classification:
  areas:
  - algebraic-geometry
  topics:
  - Twisted Cubic
  - Dimension
  - Coordinate Rings
relations:
- kind: uses
  target: D-5LJUX
- kind: uses
  target: PR-7OT2Z
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry, §I.1 Exercise 1.2 (scan page 22
    of the retained PDF). What was checked: the printed text against the card's
    statement, wording by wording — the set Y = {(t, t^2, t^3) : t in k}, the three
    tasks (affine variety of dimension 1; generators for I(Y); A(Y) isomorphic to
    a polynomial ring in one variable), and the closing sentence defining the
    parametric representation. No difference was found and no repair was needed;
    the exercise carries no star. What was not checked: the solution was read only
    for consistency with the statement, not re-derived.
---

::: {.problem}
Let $Y \subseteq \AA^3$ be the set $Y = \theset{ (t, t^2, t^3) \st t \in k }$.

- Show that $Y$ is an affine variety of dimension $1$.

- Find generators for the ideal $I(Y)$.

- Show that $A(Y)$ is isomorphic to a polynomial ring in one variable over $k$.

We say $Y$ is given by the \dfn{parametric representation} $x = t,\ y = t^2,\ z = t^3$.
:::

::: {.solution}
**The ideal.** Let $\mathfrak a = \generators{y - x^2,\ z - x^3}$. Clearly $\mathfrak a \subseteq I(Y)$.
Modulo $\mathfrak a$ every polynomial is congruent to a polynomial $g(x)$, so if $h \in I(Y)$ then $h \equiv g(x)$ with $g(t) = h(t,t^2,t^3) = 0$ for every $t \in k$.
Since $k$ is infinite, $g = 0$, so $h \in \mathfrak a$. Hence $I(Y) = \generators{y - x^2,\ z - x^3}$.

**The coordinate ring.** The same reduction shows that $x \mapsto t,\ y \mapsto t^2,\ z \mapsto t^3$ induces an isomorphism
$$
A(Y) = k[x,y,z]/I(Y) \cong k[t] .
$$

**That $Y$ is a variety of dimension $1$.** The set $Y = Z(y - x^2,\ z - x^3)$ is closed, and $I(Y)$ is prime because $A(Y) \cong k[t]$ is a domain, so $Y$ is irreducible.
Finally $\dim Y = \krulldim A(Y) = \krulldim k[t] = 1$.
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 1.2, PDF p. 1, and Jinhyun Park, *Algebraic Geometry by Robin Hartshorne: Exercises solutions*, Exercise 1.2, PDF p. 2, and William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 1.2, PDF p. 2: all three compute $k[x,y,z]/(y-x^2,z-x^3)\cong k[x]$, conclude that $(y-x^2,z-x^3)$ is radical because $k[x]$ is a domain, and read off $I(Y)$, $A(Y)\cong k[x]$ and $\dim Y=1$; Borcherds states the two results in one line and omits the dimension count.
The proof above takes the steps in the opposite order: it proves $I(Y)=(y-x^2,z-x^3)$ first, by reducing modulo that ideal and using that a polynomial vanishing at every $t\in k$ is zero, and then gets $A(Y)\cong k[t]$ and the dimension from the resulting presentation.
The same reduction is the main step in both, and both identify the quotient with $k[t]$; agree.
:::
