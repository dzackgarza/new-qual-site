---
schema: qual/card@1
id: P-BKF09-9B
kind: problem
title: Functions with positive Laplacian have no local maximum
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
    assets/attachments/f09solutions.pdf, page 9, Problem 9B: "If f is a smooth
    real valued function of x, y, z such that the sum of second partials is > 0
    for all x, y, z, show that f does not have a local maximum." The card states
    exactly this.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The card carried the retained answer, "at a local maximum all second
    derivatives must be at most 0", which asserts the one-variable second
    derivative test for each coordinate direction without naming it. The
    solution written here reduces to the one-variable test by restricting f to
    the three coordinate lines through a putative maximum and adds the three
    conclusions; the continuum many other directions are deliberately not
    needed, only the coordinate ones.
---

::: {.problem}
If $f$ is a smooth real valued function of $x$, $y$, $z$ such that
$$
\frac{\partial^2f}{\partial x^2}+\frac{\partial^2f}{\partial y^2}+\frac{\partial^2f}{\partial z^2}>0
$$
for all $x$, $y$, $z$, show that $f$ does not have a local maximum.
:::

::: {.solution}

::: pf

::: {.pf-step #one-variable}

Suppose $f$ has a local maximum at $p=(x_{0},y_{0},z_{0})$. Then along each
coordinate line through $p$ the one-variable function has a local maximum at
$0$.

::: pf-proof

By definition of local maximum there is $r>0$ with $f(q)\le f(p)$ for all $q$
within distance $r$ of $p$. The function $g(t)=f(x_{0}+t,y_{0},z_{0})$ is defined
on $(-r,r)$ and satisfies $g(t)\le g(0)$ there, so $g$ has a local maximum at
$t=0$. The same holds for $h(t)=f(x_{0},y_{0}+t,z_{0})$ and
$k(t)=f(x_{0},y_{0},z_{0}+t)$.

:::

:::

::: {.pf-step #second-derivative-test}

Hence the three unmixed second partials of $f$ at $p$ are all at most $0$.

::: pf-proof

$g$ is twice differentiable with $g''(t)=f_{xx}(p+t e_{1})$ and $g$ has a local
maximum at $0$, so the second derivative test gives
$g''(0)=f_{xx}(p)\le 0$. The same test applied to $h$ and $k$ gives
$f_{yy}(p)\le 0$ and $f_{zz}(p)\le 0$. Differentiability of $f$ is used only to
justify differentiating under the restriction to the line.

:::

:::

::: {.pf-step #contradiction}

The sum of the three is then at most $0$, contradicting
$f_{xx}+f_{yy}+f_{zz}>0$ everywhere.

::: pf-proof

A sum of three numbers each $\le 0$ is $\le 0$, so
$f_{xx}(p)+f_{yy}(p)+f_{zz}(p)\le 0$, whereas the hypothesis states that this sum
is positive at every point, in particular at $p$. So no point $p$ can be a local
maximum, which is the assertion.

:::

:::

:::

:::
