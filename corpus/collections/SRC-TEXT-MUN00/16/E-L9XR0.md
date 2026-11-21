---
schema: qual/card@1
id: E-L9XR0
kind: problem
title: Subspace topologies on lines in the Sorgenfrey plane
classification:
  areas:
  - topology
  topics:
  - Subspace Topology
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §16 Exercise 8, printed p. 92, with Lemma 16.1 on
    printed p. 89; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 16.8, PDF p. 5, with each entry proved on the card
    from the traces of the bases [a,b) x (c,d) and [a,b) x [c,d). The answer: over R_l x R a
    vertical line gives R and any other line gives R_l directed rightward and R_u directed
    leftward; over R_l x R_l a vertical line gives R_l upward and R_u downward, a line of
    non-negative slope gives R_l or R_u according to direction, and a negative-slope line
    gives the discrete topology, since a small product basis element at a point of it meets
    the line in that point alone. Two source defects are recorded: positron0802 misprints
    the leftward negative-slope case, and Whitman, printed pp. 154-155, states that his
    argument is informal. (tmp/sources/munkres-solutions-positron-ch2.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Structured the answer as Lamport steps and checked every entry of the table against
    Munkres §16 Exercise 8, printed p. 92, with Lemma 16.1: the traces of [a,b) x (c,d) and
    of [a,b) x [c,d) on a vertical line, on a non-vertical line (an interval meeting a half-
    open interval, hence a union of half-open intervals), on a line of slope m >= 0 (a trace
    [max(a,gamma), min(b,delta))) and on a line of negative slope (the singleton trace). The
    table is positron0802's, PDF p. 5; the arguments for the entries are this card's own,
    which the card says. Two source defects are recorded: positron0802 reads the negative-
    slope case off the direction of the line, and Whitman says his argument is informal.
---

::: {.exercise}

If $L$ is a straight line in the plane, describe the topology $L$ inherits as a subspace of $\RR_\ell \times \RR$ and as a subspace of $\RR_\ell \times \RR_\ell$.
In each case it is a familiar topology.
:::

::: {.solution}
The table of answers is that of **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 16.8, PDF p. 5** (`tmp/sources/munkres-solutions-positron-ch2.pdf`). The arguments below, one for each entry, are the card's own: they are the traces of the two bases, computed from Lemma 16.1, printed p. 89, and are not a transcription. One misprint in the source is corrected: for a line of negative slope it reads the answer off the direction of the line, whereas the discreteness comes from the negative slope and holds in either direction. Whitman, printed pp. 154--155, gives the same table but states on p. 154 that his argument is informal, so nothing is taken from him.

Identify $L$ with $\RR$ by a coordinate $x$ increasing in a chosen direction of $L$; reversing the direction is the homeomorphism $x\mapsto-x$ of $\RR_{\ell}$ with $\RR_{u}$, so it suffices to treat one direction in each case. The basis of $\RR_{\ell}\times\RR$ is the collection of sets $[a,b)\times(c,d)$ and that of $\RR_{\ell}\times\RR_{\ell}$ is the collection of sets $[a,b)\times[c,d)$, with $a<b$, $c<d$; by Lemma 16.1 a basis for the topology $L$ inherits is the collection of traces $L\cap\big([a,b)\times I\big)$, where $I$ runs over the second-coordinate basis elements. For a non-vertical line $L=\{y=mx+k\}$ and $p<q$, write
$$
\mu(p,q)=\min\{mp+k,\ mq+k\},\qquad M(p,q)=\max\{mp+k,\ mq+k\},
$$
so that $\mu(p,q)\le mx+k\le M(p,q)$ for $p\le x\le q$, because $x\mapsto mx+k$ is monotone.

::: pf

::: {.pf-step #half-open-traces}
For a non-vertical $L$ and any $p<q$, the half-open interval $[p,q)$ of $L$ is a trace on $L$, in $\RR_{\ell}\times\RR$ and in $\RR_{\ell}\times\RR_{\ell}$.

::: pf-proof
For the half-open interval take the interval $[p,q)$ in the first coordinate. In $\RR_{\ell}\times\RR$ use $[p,q)\times(\mu(p,q)-1,\ M(p,q)+1)$: a point of $L$ over $x\in[p,q)$ has second coordinate between $\mu(p,q)$ and $M(p,q)$, hence lies in the trace, and a point of $L$ over $x\notin[p,q)$ does not. In $\RR_{\ell}\times\RR_{\ell}$ use $[p,q)\times[\mu(p,q),\ M(p,q)+1)$, which likewise contains every point of $L$ over $x\in[p,q)$ by the displayed inequality and no other point of $L$. So in both products $[p,q)$ is a trace, and the open interval $(p,q)$ is a union of the traces $[p',q)$ with $p<p'<q$.
:::

:::

::: {.pf-step #vertical-first}
In $\RR_{\ell}\times\RR$ the trace on a vertical line is that of $\RR$.

::: pf-proof
Let $L=\{x_{0}\}\times\RR$. The trace of $[a,b)\times(c,d)$ is $\{x_{0}\}\times(c,d)$ if $x_{0}\in[a,b)$ and is empty otherwise, and for every $x_{0}$ and every $c<d$ there is such a basis element with $x_{0}\in[a,b)$, for instance $a=x_{0}$, $b=x_{0}+1$. So the traces are exactly the intervals $\{x_{0}\}\times(c,d)$ together with $\varnothing$, which is a basis for the usual topology of $\RR$ in the second coordinate.
:::

:::

::: {.pf-step #nonvertical-first}
In $\RR_{\ell}\times\RR$ the trace on a non-vertical line is the topology of $\RR_{\ell}$ when $L$ is directed to the right, and that of $\RR_{u}$ when it is directed to the left.

::: pf-proof
Let $L=\{y=mx+k\}$. For a basis element $[a,b)\times(c,d)$ the trace is
$$
\{x\in[a,b)\mid c<mx+k<d\}=[a,b)\cap J,\qquad J=\{x\mid c<mx+k<d\}.
$$
Since $x\mapsto mx+k$ is injective with $m\neq0$, the two inequalities $c<mx+k$ and $mx+k<d$ are equivalent to $x$ lying on one side of $(c-k)/m$ and on the other side of $(d-k)/m$, so $J$ is the open interval with those two endpoints, or is empty; in either case $J$ is an interval. If $J=(\alpha,\beta)$ then $[a,b)\cap(\alpha,\beta)$ is $[a,\min\{b,\beta\})$ when $a\ge\alpha$, and $(\alpha,\min\{b,\beta\})$ when $a<\alpha$; in either case it is a union of half-open intervals $[p,q)$, hence open in $\RR_{\ell}$. So every trace is open in $\RR_{\ell}$, and by step [](#half-open-traces){.pf-ref} every half-open interval is a trace, so the inherited topology is that of $\RR_{\ell}$ in the direction of increasing $x$; with the opposite direction the coordinate $x\mapsto-x$ identifies it with $\RR_{u}$.
:::

:::

::: {.pf-step #vertical-second}
In $\RR_{\ell}\times\RR_{\ell}$ the trace on a vertical line is that of $\RR_{\ell}$ when the line is directed upward and that of $\RR_{u}$ when it is directed downward.

::: pf-proof
Let $L=\{x_{0}\}\times\RR$. The trace of $[a,b)\times[c,d)$ is $\{x_{0}\}\times[c,d)$ if $x_{0}\in[a,b)$ and empty otherwise, and every $c<d$ occurs with $x_{0}\in[a,b)$, so the traces are exactly the half-open intervals of the second coordinate. They form a basis for the lower limit topology in the direction of increasing second coordinate, and reversing that coordinate gives the upper limit topology.
:::

:::

::: {.pf-step #nonneg-second}
In $\RR_{\ell}\times\RR_{\ell}$ the trace on a line of slope $m\ge0$ is the topology of $\RR_{\ell}$ when the line is directed to the right, and that of $\RR_{u}$ when it is directed to the left.

::: pf-proof
Let $L=\{y=mx+k\}$ with $m\ge0$; the horizontal case $m=0$ is included. The trace of $[a,b)\times[c,d)$ is
$$
\{x\in[a,b)\mid c\le mx+k<d\}=[a,b)\cap[\gamma,\delta),
$$
where for $m>0$ one has $\gamma=(c-k)/m$ and $\delta=(d-k)/m$, and for $m=0$ the trace is $[a,b)$ if $c\le k<d$ and empty otherwise. For $m>0$ the set $[a,b)\cap[\gamma,\delta)$ is empty or $[\max\{a,\gamma\},\min\{b,\delta\})$, a half-open interval. So every trace is open in $\RR_{\ell}$, and by step [](#half-open-traces){.pf-ref} every half-open interval is a trace; hence the inherited topology is that of $\RR_{\ell}$ in the direction of increasing $x$, and that of $\RR_{u}$ in the opposite direction.
:::

:::

::: {.pf-step #negative-second}
In $\RR_{\ell}\times\RR_{\ell}$ the trace on a line of negative slope is the discrete topology, in either direction.

::: pf-proof
Let $L=\{y=mx+k\}$ with $m<0$ and let $(x_{0},y_{0})\in L$. The trace of $[x_{0},x_{0}+1)\times[y_{0},y_{0}+1)$ is the set of points of $L$ with $x_{0}\le x<x_{0}+1$ and $y_{0}\le y<y_{0}+1$. For such a point $y=mx+k=y_{0}+m(x-x_{0})$, and $x\ge x_{0}$ with $m<0$ gives $y\le y_{0}$, so $y_{0}\le y\le y_{0}$ forces $y=y_{0}$ and hence $x=x_{0}$. Thus the trace is the singleton $\{(x_{0},y_{0})\}$, which is therefore open in $L$. As $(x_{0},y_{0})$ was an arbitrary point of $L$, every subset of $L$ is a union of open singletons and is open, so $L$ is discrete.
:::

:::

::: {.pf-step}
The answer. As a subspace of $\RR_{\ell}\times\RR$: a vertical line gives $\RR$; every other line gives $\RR_{\ell}$ when directed to the right and $\RR_{u}$ when directed to the left, whatever its slope. As a subspace of $\RR_{\ell}\times\RR_{\ell}$: a vertical line gives $\RR_{\ell}$ directed upward and $\RR_{u}$ directed downward; a horizontal or positive-slope line gives $\RR_{\ell}$ directed to the right and $\RR_{u}$ directed to the left; a negative-slope line gives the discrete topology $\RR_{d}$.

::: pf-proof
Steps [](#vertical-first){.pf-ref} and [](#nonvertical-first){.pf-ref} settle the first product, steps [](#vertical-second){.pf-ref}, [](#nonneg-second){.pf-ref} and [](#negative-second){.pf-ref} settle the second, and every straight line is vertical, horizontal, of positive slope or of negative slope.
:::

:::

:::
:::
