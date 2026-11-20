---
schema: qual/card@1
id: E-A0UGQ
kind: problem
title: A function continuous at exactly one point
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 6, printed p. 111; the stored
    statement is the printed request and the card answers it with one function and the proof
    that its set of continuity is a single point.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 18.6, printed p. 181.
    The function, zero on the rationals and the identity on the irrationals, is his, as is
    the epsilon-delta verification: continuous at 0 with delta = epsilon, and at x != 0 the
    point y chosen rational or irrational within delta of x forces |f(y)-f(x)| > |x|/2. The
    epsilon-delta definition is admissible here because it implies the open set definition
    by Exercise 18.1. (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

Find a function $f: \RR \to \RR$ that is continuous at precisely one point.
:::

::: {.solution}

The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 18.6, printed p. 181** (`tmp/sources/munkres-solutions-whitman.pdf`); the function and the proof are his, with the two cases of the discontinuity argument separated below. The same answer is recorded by "positron0802", *Solutions to Topology, Chapter 2*, Exercise 18.6.

::: pf

::: {.pf-step #definition}
Define $f:\RR\to\RR$ by $f(x)=0$ for $x\in\QQ$ and $f(x)=x$ for $x\notin\QQ$; then $f(0)=0$. Continuity at a point is the $\varepsilon$-$\delta$ condition (Exercise 18.1).

::: pf-proof
$0\in\QQ$, so $f(0)=0$; and for metric spaces the $\varepsilon$-$\delta$ condition at a point is equivalent to continuity there, which is the content of Exercise 18.1.
:::

:::

::: {.pf-step #at-zero}
$f$ is continuous at $0$.

::: pf-proof
Given $\varepsilon>0$ take $\delta=\varepsilon$. If $\abs{y}<\delta$ and $y\in\QQ$, then $\abs{f(y)-f(0)}=\abs{0-0}=0<\varepsilon$; if $y\notin\QQ$, then $\abs{f(y)-f(0)}=\abs{y}<\delta=\varepsilon$. So the condition holds at $0$.
:::

:::

::: {.pf-step #not-elsewhere}
$f$ is continuous at no point $x\ne0$.

:::: {.pf-proof}

::: {.pf-step #rational-point}
If $x\in\QQ$, $x\ne0$, then $f$ is discontinuous at $x$.

::: pf-proof
Let $\varepsilon=\abs{x}/2>0$ and let $\delta>0$ be arbitrary. Since the irrationals are dense there is an irrational $y$ with $\abs{y-x}<\min\theset{\varepsilon,\delta}$. Then $f(x)=0$, $f(y)=y$, and $\abs{y}\ge\abs{x}-\abs{x-y}>\abs{x}-\varepsilon=\varepsilon$, so $\abs{f(y)-f(x)}>\varepsilon$ while $\abs{y-x}<\delta$. Hence no $\delta$ works for this $\varepsilon$.
:::

:::

::: {.pf-step #irrational-point}
If $x\notin\QQ$, then $f$ is discontinuous at $x$.

::: pf-proof
Let $\varepsilon=\abs{x}/2>0$ and let $\delta>0$ be arbitrary. By density of $\QQ$ there is a rational $y$ with $\abs{y-x}<\delta$. Then $f(y)=0$ and $f(x)=x$, so $\abs{f(y)-f(x)}=\abs{x}=2\varepsilon>\varepsilon$. Hence no $\delta$ works for this $\varepsilon$.
:::

:::

::::

:::

::: {.pf-qed}
$f$ is continuous at $0$ by step [](#at-zero){.pf-ref} and at no other point by step [](#not-elsewhere){.pf-ref}, so $0$ is precisely the set of points where $f$ is continuous.
:::

:::

:::
