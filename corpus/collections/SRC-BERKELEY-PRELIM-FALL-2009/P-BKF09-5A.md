---
schema: qual/card@1
id: P-BKF09-5A
kind: problem
title: Minkowski sum of closed connected subsets of $\RR^2$ need not be closed
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the retained exam with solutions,
    assets/attachments/f09solutions.pdf, page 3, Problem 5A: "Is it possible to
    find two closed and connected subsets A and B in R2 such that A + B =
    {(x1 + x2, y1 + y2) in R2 | (x1, y1) in A, (x2, y2) in B} is not closed?"
    The card states exactly this.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The card carried the retained answer, "take A the x-axis and B a component
    of xy = 1, so that A + B is an open half-plane", which states the identity
    without proof. The solution written here proves each of the three claims:
    A and B are closed and connected, A + B is exactly the open upper half plane
    (both inclusions, with the parameter t = 1/v exhibited), and that half plane
    is not closed because (0, 0) is a limit point outside it.
---

::: {.problem}
Is it possible to find two closed and connected subsets $A$ and $B$ in $\RR^2$ such that
$$
A+B=\{(x_1+x_2,y_1+y_2)\in\RR^2\mid(x_1,y_1)\in A,\ (x_2,y_2)\in B\}
$$
is not closed?
:::

::: {.solution}

Yes. Take $A=\{(x,0)\mid x\in\RR\}$, the $x$-axis, and
$B=\{(t,1/t)\mid t>0\}$, one component of the hyperbola $xy=1$. Then $A+B$ is
the open upper half plane, which is not closed.

::: pf

::: {.pf-step #a-closed-connected}

$A$ is closed and connected.

::: pf-proof

$A=\{(x,y)\mid y=0\}$ is the zero set of the continuous function $y$, hence
closed in $\RR^{2}$, and it is homeomorphic to $\RR$ via $x\mapsto(x,0)$, hence
connected.

:::

:::

::: {.pf-step #b-closed-connected}

$B$ is closed and connected.

::: pf-proof

Connected: $B$ is the image of the interval $(0,\infty)$ under the continuous map
$t\mapsto(t,1/t)$, and a continuous image of a connected set is connected.
Closed: $B=\{xy=1\}\cap\{x\ge 0\}$, since $xy=1$ with $x=0$ is impossible, so the
condition $x\ge 0$ is equivalent to $x>0$ on the hyperbola. The set $\{xy=1\}$
is closed, being the preimage of the closed set $\{1\}$ under the continuous map
$(x,y)\mapsto xy$, and $\{x\ge 0\}$ is closed, so $B$ is the intersection of two
closed sets.

:::

:::

::: {.pf-step #sum}

$A+B=\{(u,v)\mid v>0\}$.

::: pf-proof

If $(x,0)\in A$ and $(t,1/t)\in B$ with $t>0$, then their sum is
$(x+t,\,1/t)$ with second coordinate $1/t>0$, so $A+B\subseteq\{v>0\}$.
Conversely let $v>0$ and put $t=1/v>0$; then $(u,v)=(u-1/v,\,0)+(1/v,\,v)$ with
$(u-1/v,0)\in A$ and $(1/v,v)=(t,1/t)\in B$, so $(u,v)\in A+B$. Hence $A+B$ is
exactly the open upper half plane.

:::

:::

::: {.pf-step #not-closed}

$A+B$ is not closed, so the answer is yes.

::: pf-proof

The points $(0,1/n)=(0,0)+(1/n,n)\in A+B$ converge to $(0,0)$, whose second
coordinate is $0$, so $(0,0)\notin A+B$. A closed set contains the limits of its
convergent sequences, so $A+B$ is not closed, and $A$ and $B$ are the required
closed connected sets.

:::

:::

:::

:::
