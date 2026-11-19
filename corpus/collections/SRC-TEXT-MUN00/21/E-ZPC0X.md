---
schema: qual/card@1
id: E-ZPC0X
kind: problem
title: Interchanging limits under uniform convergence
classification:
  areas:
  - topology
  topics:
  - Uniform Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §21 Exercise 8, printed p. 134, with Theorem
    21.6; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 21.8, PDF p. 25. The three-epsilon argument:
    uniform convergence bounds the distance from f_n(x_n) to f(x_n), continuity of the limit
    bounds the distance from f(x_n) to f(x), and the triangle inequality finishes.
    (tmp/sources/munkres-solutions-positron-ch2.pdf).
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2 and re-checked: uniform convergence gives the
    pointwise bound beyond $N_1$; a uniform limit of continuous functions is continuous, which the
    earlier solution asserted by Theorem 21.6 and which is now proved in the step by the
    $\varepsilon/3$ triangle inequality; continuity of $f$ and $x_n\to x$ give $N_2$; and the
    triangle inequality finishes. Added: the neighbourhood-base step from an arbitrary
    neighbourhood $V$ to a ball $B_d(f(x),\varepsilon)\subseteq V$, which the prose assumed.
    No defect found in the statement, §21 Exercise 8 on printed p. 134. Not claimed: a printed
    publication, the source being a posted solution set.
---

::: {.exercise}

Let $X$ be a topological space and let $Y$ be a metric space.
Let $f_n: X \to Y$ be a sequence of continuous functions.
Let $x_n$ be a sequence of points of $X$ converging to $x$.
Show that if the sequence $(f_n)$ converges uniformly to $f$, then $(f_n(x_n))$ converges to $f(x)$.
:::

::: {.solution}
The retained published solution is **positron0802, *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.8, PDF p. 25** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the three-$\varepsilon$ argument is its. Let $d$ be the metric of $Y$ and $B_d(y,\varepsilon)$ the ball of radius $\varepsilon$ about $y$.

::: pf

::: {.pf-step #uniform}
For every $\varepsilon>0$ there is $N_1$ with $d(f_n(t),f(t))<\varepsilon/2$ for all $t\in X$ and all $n\ge N_1$.

::: pf-proof
The sequence $(f_n)$ converges uniformly to $f$, which says exactly that for each $\eta>0$ there is $N$ beyond which $d(f_n(t),f(t))<\eta$ for every $t\in X$ simultaneously; take $\eta=\varepsilon/2$. In the uniform metric $\bar\rho(f_n,f)=\sup_t\min\{d(f_n(t),f(t)),1\}$ this is the statement that $\bar\rho(f_n,f)\to0$, and a bound on the supremum bounds every pointwise distance.
:::

:::

::: {.pf-step #limit-continuous}
$f$ is continuous.

::: pf-proof
A uniform limit of continuous functions is continuous, which is Theorem 21.6 of §21. Explicitly, given $\varepsilon>0$ and $x\in X$, take $n\ge N_1$ from step [](#uniform){.pf-ref} with $\varepsilon$ replaced by $\varepsilon/3$; since $f_n$ is continuous at $x$ there is a neighbourhood $U$ of $x$ with $d(f_n(t),f_n(x))<\varepsilon/3$ for $t\in U$, and then $d(f(t),f(x))<\varepsilon$ for $t\in U$ by the triangle inequality together with the uniform bound at $t$ and at $x$.
:::

:::

::: {.pf-step #along}
$f(x_n)\to f(x)$.

::: pf-proof
By step [](#limit-continuous){.pf-ref}, $f$ is continuous at $x$, so for $\varepsilon>0$ the set $U=f^{-1}\bigl(B_d(f(x),\varepsilon/2)\bigr)$ is a neighbourhood of $x$; since $x_n\to x$, there is $N_2$ with $x_n\in U$ for all $n\ge N_2$, and then $d(f(x_n),f(x))<\varepsilon/2$ for those $n$.
:::

:::

::: {.pf-step}
$\boxed{f_n(x_n)\to f(x)}$, that is, $f_n(x_n)\in V$ for every neighbourhood $V$ of $f(x)$ and all large $n$.

::: pf-proof
Let $V$ be a neighbourhood of $f(x)$ and choose $\varepsilon>0$ with $B_d(f(x),\varepsilon)\subseteq V$, which exists because the balls about a point form a neighbourhood base in a metric space. For $n\ge N=\max\{N_1,N_2\}$, with $N_1$ from step [](#uniform){.pf-ref} at this $\varepsilon$ and $N_2$ from step [](#along){.pf-ref},
$$
d(f_n(x_n),f(x))\le d(f_n(x_n),f(x_n))+d(f(x_n),f(x))<\tfrac{\varepsilon}{2}+\tfrac{\varepsilon}{2}=\varepsilon
$$
by the triangle inequality, so $f_n(x_n)\in B_d(f(x),\varepsilon)\subseteq V$. Since $V$ was arbitrary, $f_n(x_n)\to f(x)$.
:::

:::

:::
:::
