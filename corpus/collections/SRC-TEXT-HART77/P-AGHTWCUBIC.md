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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. Checked: the reduction modulo (y - x^2, z - x^3) by replacing each monomial x^i y^j z^m with x^(i+2j+3m); the identification I(Y) = (y - x^2, z - x^3) from k infinite (a nonzero polynomial has finitely many roots); the isomorphism A(Y) = k[t] via the kernel computation; closedness of Y as the common zero set of the two generators; primality of I(Y) from A(Y) being a domain; and the dimension, now computed from the Krull dimension of k[t] with both inequalities (the chain (0) subset (t), and every nonzero prime maximal because k[t] is a PID). Two gaps filled: the prose asserted dim k[t] = 1 without the chain argument, and it asserted Y = Z(y - x^2, z - x^3) without checking the zero set is exactly Y rather than only containing it. The retained solutions are cited with their pages in the remark below, and their text versions were re-read this turn (Borcherds 1.2 states both results in a line, Park 1.2 identifies the quotient, Troiani 1.2 concludes I(Y) from k[x] having no nilpotents).
---

::: {.problem}
Let $Y \subseteq \AA^3$ be the set $Y = \theset{ (t, t^2, t^3) \st t \in k }$.

- Show that $Y$ is an affine variety of dimension $1$.

- Find generators for the ideal $I(Y)$.

- Show that $A(Y)$ is isomorphic to a polynomial ring in one variable over $k$.

We say $Y$ is given by the \dfn{parametric representation} $x = t,\ y = t^2,\ z = t^3$.
:::

::: {.solution}
The argument is the card's own, and it takes the same two steps as the three retained solutions cited in the remark below: **Borcherds, Exercise 1.2**, **Park, Exercise 1.2**, **Troiani, Exercise 1.2**. The exercise is Hartshorne, *Algebraic Geometry*, §I.1 Exercise 1.2, where $k$ is algebraically closed, hence infinite.

Put $\mathfrak a=\generators{y-x^2,z-x^3}$ and $Y=\theset{(t,t^2,t^3)\st t\in k}$.

::: pf

::: {.pf-step #reduce}
$\mathfrak a\subseteq I(Y)$, and every element of $k[x,y,z]$ is congruent modulo $\mathfrak a$ to a polynomial in $x$ alone.

::: pf-proof
$y-x^2$ and $z-x^3$ vanish at $(t,t^2,t^3)$ for every $t$, so $\mathfrak a\subseteq I(Y)$. Modulo $\mathfrak a$ one has $y\equiv x^2$ and $z\equiv x^3$, so the monomial $x^iy^jz^m$ is congruent to $x^{i+2j+3m}$; replacing each monomial of a polynomial $h$ in this way gives $h\equiv g(x)$ for some $g\in k[x]$.
:::

:::

::: {.pf-step #ideal}
$I(Y)=\mathfrak a$.

::: pf-proof
Let $h\in I(Y)$ and let $g\in k[x]$ be as in step [](#reduce){.pf-ref}, so $h-g(x)\in\mathfrak a\subseteq I(Y)$ and hence $g(x)\in I(Y)$. Evaluating at $(t,t^2,t^3)$ gives $g(t)=0$ for every $t\in k$. A nonzero polynomial over a field has at most as many roots as its degree, so $g=0$ because $k$ is infinite; hence $h\equiv0$ modulo $\mathfrak a$, i.e. $h\in\mathfrak a$. With the reverse inclusion from step [](#reduce){.pf-ref}, $I(Y)=\mathfrak a$.
:::

:::

::: {.pf-step #coordinate}
$A(Y)=k[x,y,z]/I(Y)\cong k[t]$, by $x\mapsto t$, $y\mapsto t^2$, $z\mapsto t^3$.

::: pf-proof
The $k$-algebra map $\phi:k[x,y,z]\to k[t]$ with $x\mapsto t$, $y\mapsto t^2$, $z\mapsto t^3$ is surjective since $t=\phi(x)$. Its kernel consists of the $h$ with $h(t,t^2,t^3)=0$ for all $t$, which by steps [](#reduce){.pf-ref} and [](#ideal){.pf-ref} is exactly $\mathfrak a=I(Y)$. So $\phi$ induces an isomorphism $A(Y)\to k[t]$.
:::

:::

::: {.pf-step #variety}
$Y$ is an affine variety, i.e. an irreducible closed subset of $\AA^3$.

::: pf-proof
$Y$ is closed because $Y$ is the common zero set of $y-x^2$ and $z-x^3$: a point $(a,b,c)$ satisfies both equations exactly when $b=a^2$ and $c=a^3$, i.e. lies in $Y$. Its ideal $I(Y)$ is prime, because $A(Y)\cong k[t]$ by step [](#coordinate){.pf-ref} is a domain and a quotient $k[x,y,z]/\mathfrak a$ is a domain exactly when $\mathfrak a$ is prime. A closed set whose ideal is prime is irreducible. So $Y$ is an affine variety.
:::

:::

::: {.pf-step #dimension}
$\dim Y=1$.

::: pf-proof
For an affine variety Hartshorne defines $\dim Y=\dim A(Y)$, the Krull dimension. By step [](#coordinate){.pf-ref} this is $\dim k[t]$. The chain $(0)\subsetneq(t)$ of prime ideals has length $1$, so $\dim k[t]\ge1$. For the reverse inequality, $k[t]$ is a principal ideal domain, so every nonzero prime ideal is maximal: if $(0)\subsetneq\mathfrak p_1\subsetneq\cdots\subsetneq\mathfrak p_n$ is a chain of primes, then $\mathfrak p_1\ne0$ is maximal, so $n=1$. Hence $\dim k[t]=1$ and $\dim Y=1$.
:::

:::

::: {.pf-step}
$Y$ is an affine variety of dimension $1$, $I(Y)=\generators{y-x^2,z-x^3}$, and $A(Y)\cong k[t]$.

::: pf-proof
Steps [](#variety){.pf-ref} and [](#dimension){.pf-ref} give the first two assertions about $Y$, step [](#ideal){.pf-ref} the generators, and step [](#coordinate){.pf-ref} the isomorphism with a polynomial ring in one variable. This is the twisted cubic, with parametric representation $x=t$, $y=t^2$, $z=t^3$.
:::

:::

:::
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 1.2, text version `tmp/sources/hartshorne-solutions-borcherds.md`, and Jinhyun Park, *Algebraic Geometry by Robin Hartshorne: Exercises solutions*, Exercise 1.2, text version `tmp/sources/hartshorne-solutions-park.md`, and William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 1.2, text version `tmp/sources/hartshorne-solutions-troiani.md`: all three compute $k[x,y,z]/(y-x^2,z-x^3)\cong k[x]$, conclude that $(y-x^2,z-x^3)$ is radical because $k[x]$ is a domain, and read off $I(Y)$, $A(Y)\cong k[x]$ and $\dim Y=1$; Borcherds states the two results in one line and omits the dimension count.
The proof above takes the steps in the opposite order: it proves $I(Y)=(y-x^2,z-x^3)$ first, by reducing modulo that ideal and using that a polynomial vanishing at every $t\in k$ is zero, and then gets $A(Y)\cong k[t]$ and the dimension from the resulting presentation.
The same reduction is the main step in both, and both identify the quotient with $k[t]$; agree.
:::
