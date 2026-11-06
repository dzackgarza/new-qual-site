---
schema: qual/card@1
id: P-PRACT20-W3-16
kind: problem
title: Recovering $f(x,y)$ from its partial derivatives $2x+y$ and $x+2y$
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Partial Derivatives
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 5 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem gives the same pair of partial differential equations, and the printed solution gives the same family x^2 + xy + y^2 + C
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's two integrations are transcribed, with the constant-of-integration argument and the verification that every member of the family solves both equations.
---

::: {.problem}
Find all functions $f(x, y)$ satisfying $\frac{\partial f}{\partial x}(x, y) = 2x + y$, $\frac{\partial f}{\partial y}(x, y) = x + 2y$.
:::

::: {.solution}

We seek all differentiable $f$ on $\RR^2$ with $f_x=2x+y$ and $f_y=x+2y$.

::: pf

::: {.pf-step #integrate}

$f(x,y)=x^2+xy+g(y)$ for some differentiable $g$.

::: pf-proof

Integrating $f_x=2x+y$ with respect to $x$ at fixed $y$ gives
$f(x,y)=x^2+xy+g(y)$, where $g$ is the constant of integration with respect to
$x$, possibly depending on $y$; every such $f$ has $f_x=2x+y$.

:::

:::

::: {.pf-step #second}

$x+2y=f_y=x+g'(y)$, so $g'(y)=2y$ and $g(y)=y^2+C$.

::: pf-proof

Differentiating $f(x,y)=x^2+xy+g(y)$ in $y$ gives $x+g'(y)$, which must equal
$x+2y$; cancelling $x$ gives $g'(y)=2y$, so $g(y)=y^2+C$ on an interval, and
since the equation holds on all of $\RR^2$ the constant is the same
everywhere.

:::

:::

::: {.pf-step #solution}

$\boxed{f(x,y)=x^2+xy+y^2+C}$ for an arbitrary constant $C$, and these are all
the solutions.

::: pf-proof

Steps [](#integrate){.pf-ref} and [](#second){.pf-ref} show every solution has
that form, and substituting back gives $f_x=2x+y$ and $f_y=x+2y$, so every
such $f$ is a solution; $C$ is free because partial derivatives kill
constants. The two mixed partials agree, $f_{xy}=1=f_{yx}$, which is the
consistency condition for the pair of equations to have a solution at all.

:::

:::

:::


:::
