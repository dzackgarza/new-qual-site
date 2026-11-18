---
schema: qual/card@1
id: P-CASP04C
kind: problem
title: 'Meromorphic functions with $\abs{f+g}\leq\abs{g}$ are proportional'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The g = 0 case is now argued from the isolatedness of poles rather than asserted. The main case separates four things the prose ran together: that f/g is meromorphic with the stated exceptional set, that |h| <= 2 off it, that each exceptional point is removable by Riemann's theorem using that bound on a punctured disc, and that the bound then propagates to all of C by continuity on a dense set. The final identification f = cg uses the identity theorem for meromorphic functions. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The g = 0 case is now argued from the isolatedness of poles rather than asserted. The main case separates four things the prose ran together: that f/g is meromorphic with the stated exceptional set, that |h| <= 2 off it, that each exceptional point is removable by Riemann's theorem using that bound on a punctured disc, and that the bound then holds on all of C by density and continuity. The identification f = cg in the last step invokes the identity theorem for meromorphic functions, which the prose also used without naming. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair.
---

::: {.problem}
Let $f$ and $g$ be meromorphic functions in $\CC$.
Assume that $\abs{f(z) + g(z)} \leq \abs{g(z)}$ for every $z \in \CC$ which is not a pole of either $f$ or $g$.
Show that there is a constant $c$ with $\abs{c + 1} \leq 1$ such that $f(z) = cg(z)$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #zerog}
If $g\equiv0$ then $f\equiv0$, and $c=0$ satisfies the conclusion.

::: pf-proof
With $g\equiv0$ the hypothesis reads $\abs{f(z)}\le0$ at every $z$ that is not a pole of $f$, so $f$ vanishes at every finite point; the poles of a meromorphic function are isolated, so $f$ is the zero function. Then $f=0\cdot g$ and $\abs{c+1}=1\le1$.
:::

:::

::: {.pf-step #quotient}
Assume $g\not\equiv0$ and put $h=f/g$. Then $h$ is meromorphic on $\CC$, and $\abs{h(z)+1}\le1$ at every point where $f$ and $g$ are finite and $g(z)\ne0$.

::: pf-proof
The zeros of the nonzero meromorphic function $g$ are isolated, so the quotient $f/g$ is meromorphic on $\CC$, its poles lying among the zeros of $g$ and the poles of $f$ and of $g$. Dividing the hypothesis by the nonzero number $\abs{g(z)}$ gives $\abs{(f/g)(z)+1}\le1$ at each point where $f$ and $g$ are finite and $g(z)\ne0$.
:::

:::

::: {.pf-step #bounded}
$\abs{h(z)}\le2$ at every point where $f$ and $g$ are finite and $g(z)\ne0$.

::: pf-proof
There $\abs{h(z)}=\abs{(h(z)+1)-1}\le\abs{h(z)+1}+1\le2$, by step [](#quotient){.pf-ref} and the triangle inequality.
:::

:::

::: {.pf-step #removable}
$h$ extends to an entire function, still written $h$, with $\abs{h+1}\le1$ everywhere.

::: pf-proof
Let $E$ be the union of the pole sets of $f$ and $g$ and the zero set of $g$. Each of those three sets is discrete in $\CC$ (a meromorphic function's poles and zeros are isolated), so $E$ is a discrete closed set, and $h$ is holomorphic on the open set $\CC\setminus E$. Take $z_0\in E$ and a disc $D$ about $z_0$ with $D\cap E=\{z_0\}$; then $h$ is holomorphic on the punctured disc $D\setminus\{z_0\}$ and bounded there by step [](#bounded){.pf-ref}, so $z_0$ is a removable singularity (Riemann's removable singularity theorem) and $h$ extends holomorphically over $z_0$. Doing this at each point of $E$ gives an entire $h$. The inequality $\abs{h+1}\le1$ holds on $\CC\setminus E$ by step [](#quotient){.pf-ref}, and $\CC\setminus E$ is dense, so by continuity of $\abs{h+1}$ it holds on $\CC$.
:::

:::

::: {.pf-step #constant}
$h$ is constant.

::: pf-proof
$h+1$ is entire and $\abs{h+1}\le1$ on $\CC$ by step [](#removable){.pf-ref}, so it is bounded; Liouville's theorem makes it constant, hence so is $h$.
:::

:::

::: {.pf-step}
There is a constant $c$ with $\abs{c+1}\le1$ and $f=cg$.

::: pf-proof
By step [](#constant){.pf-ref}, $h\equiv c$ for some $c\in\CC$. Then $f=cg$ at every point where $f$ and $g$ are finite and $g\ne0$, a set that accumulates at every point of $\CC$; two meromorphic functions agreeing on such a set agree identically, since their difference divided by the product of their pole-free parts is holomorphic and vanishes on a set with a limit point. The bound $\abs{c+1}\le1$ is step [](#removable){.pf-ref}.
:::

:::

:::
:::
