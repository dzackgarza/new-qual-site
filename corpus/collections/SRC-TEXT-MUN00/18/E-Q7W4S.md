---
schema: qual/card@1
id: E-Q7W4S
kind: problem
title: Separate continuity does not imply continuity
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 12, printed p. 112; the function and
    the three parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 18.12, PDF p. 13. From them: the slices are
    constant when y_0 = 0 and rational otherwise, so separately continuous; g is 1/2 off 0
    and 0 at 0; and the neighbourhood (-1/2,1/2) of F(0 x 0) contains no image of a
    neighbourhood of 0 x 0, since every such neighbourhood contains points x x x with F =
    1/2. (tmp/sources/munkres-solutions-positron-ch2.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked all three parts against Munkres §18 Exercise
    12, printed p. 112: separate continuity of the two one-variable maps (constant for 0, a
    quotient with nonvanishing denominator otherwise), g = 1/2 off the origin, and the
    failure of continuity at (0,0) via the neighbourhood (-1/2,1/2) and the diagonal point
    inside any product neighbourhood. positron0802, Exercise 18.12, PDF p. 13; Whitman,
    printed pp. 188-189, agrees. The printed statement needed no repair.
---

::: {.exercise}

Let $F: \RR \times \RR \to \RR$ be defined by the equation

$$
F(x \times y) =
\begin{cases}
xy/(x^2 + y^2) & \text{if } x \times y \neq 0 \times 0, \\
0 & \text{if } x \times y = 0 \times 0.
\end{cases}
$$

(a) Show that $F$ is continuous in each variable separately.

(b) Compute the function $g: \RR \to \RR$ defined by $g(x) = F(x \times x)$.

(c) Show that $F$ is not continuous.
:::

::: {.solution}
The published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 18.12** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the three parts below are theirs, and Whitman, gives the same, proving (c) by composing with the diagonal map instead of testing a neighbourhood directly.

Recall that $F(x,y)=xy/(x^{2}+y^{2})$ for $(x,y)\neq(0,0)$ and $F(0,0)=0$. Throughout, $x\times y$ is written $(x,y)$.

::: pf

::: {.pf-step #part-a}
(a) $F$ is continuous in each variable separately.

:::: pf-proof

::: {.pf-step #a-first}
For each $y_{0}\in\RR$ the map $h(x)=F(x,y_{0})$ is continuous.

::: pf-proof
If $y_{0}=0$ then $h(0)=F(0,0)=0$ by the second clause of the definition, and $h(x)=x\cdot 0/(x^{2}+0)=0$ for $x\neq0$, so $h$ is the constant map $0$, which is continuous. If $y_{0}\neq0$ then $x^{2}+y_{0}^{2}\ge y_{0}^{2}>0$ for every $x$, so $h(x)=xy_{0}/(x^{2}+y_{0}^{2})$ is a quotient of polynomials whose denominator never vanishes; sums, products and such quotients of continuous real functions are continuous, so $h$ is continuous.
:::

:::

::: {.pf-step #a-second}
For each $x_{0}\in\RR$ the map $k(y)=F(x_{0},y)$ is continuous.

::: pf-proof
The formula defining $F$ is symmetric in its two arguments, so the computation of step [](#a-first){.pf-ref} applies with the variables exchanged: $k$ is constant when $x_{0}=0$ and is the quotient $yx_{0}/(y^{2}+x_{0}^{2})$ with nonvanishing denominator otherwise.
:::

:::

::: {.pf-step}
$F$ is continuous in each variable separately.

::: pf-proof
That is the definition: the maps $h$ of step [](#a-first){.pf-ref} and $k$ of step [](#a-second){.pf-ref} are continuous for every choice of the fixed coordinate.
:::

:::

:::

:::

::: {.pf-step #part-b}
(b) For $g(x)=F(x,x)$,
$$
g(x)=\begin{cases}\tfrac12,&x\neq0,\\ 0,&x=0.\end{cases}
$$

::: pf-proof
If $x\neq0$ then $(x,x)\neq(0,0)$ and $g(x)=x\cdot x/(x^{2}+x^{2})=x^{2}/(2x^{2})=\tfrac12$. If $x=0$ then $g(0)=F(0,0)=0$ by the second clause of the definition.
:::

:::

::: {.pf-step #part-c}
(c) $F$ is not continuous.

:::: pf-proof

::: {.pf-step #c-neighbourhood}
The set $V=(-\tfrac12,\tfrac12)$ is a neighbourhood of $F(0,0)$ that contains no image of a non-diagonal point of any neighbourhood of $(0,0)$.

::: pf-proof
$F(0,0)=0\in V$ and $V$ is open in $\RR$, so $V$ is a neighbourhood of $F(0,0)$. Let $U$ be a neighbourhood of $(0,0)$ in $\RR^{2}$. Since $\RR^{2}$ has the product topology, $U$ contains a basis element $(a,b)\times(c,d)$ with $a<0<b$ and $c<0<d$. Choose $x\neq0$ with $\abs{x}<\min\{-a,b,-c,d\}$; then $a<x<b$ and $c<x<d$, so $(x,x)\in U$. By step [](#part-b){.pf-ref}, $F(x,x)=\tfrac12\notin V$.
:::

:::

::: {.pf-step}
$F$ is not continuous at $(0,0)$.

::: pf-proof
A map is continuous at a point when the preimage of every neighbourhood of the image contains a neighbourhood of the point. By step [](#c-neighbourhood){.pf-ref}, the neighbourhood $V$ of $F(0,0)$ has the property that no neighbourhood $U$ of $(0,0)$ is mapped into $V$, so $F^{-1}(V)$ contains no neighbourhood of $(0,0)$.
:::

:::

:::

:::

::: {.pf-step}
All three parts hold: $F$ is continuous in each variable separately, $g$ takes the value $\tfrac12$ off $0$ and $0$ at $0$, and $F$ is discontinuous at $(0,0)$.

::: pf-proof
Steps [](#part-a){.pf-ref}, [](#part-b){.pf-ref} and [](#part-c){.pf-ref} are the three assertions of the exercise.
:::

:::

:::
:::
