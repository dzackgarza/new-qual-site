---
schema: qual/card@1
id: E-C0ZWV
kind: problem
title: Homotopy classes into an interval and out of a path-connected space
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-corrected
  by: gpt-6.1-sol
  date: 2026-10-31
  note: 'The claim that [I,Y] has one class requires Y nonempty if path connectedness is allowed to hold vacuously for the empty space.'
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 51: Problem 2 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-51-homotopy-of-paths/problem-2-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-51-homotopy-of-paths/problem-2-solution.txt),
    and against Munkres, Topology (2000), Section 51 Exercise 2, printed p. 330. dbFin gives (a) as the straight-line homotopy into the convex interval and (b) in one sentence, that a segment of a path is homotopic to the path and that path-connectedness lets one join the two; the card writes both out. What was corrected: the stored statement had added the word nonempty to part (b). The book prints "Show that if Y is path connected, the set [I,Y] has a single element", and Munkres's definition of path connected quantifies over pairs of points, so the empty space satisfies it vacuously while [I,empty] is empty, not a singleton. The printed wording is restored and the solution now names the point of Y that the argument needs and records that Y empty is the one exception.
---

::: {.exercise}

Given spaces $X$ and $Y$, let $[X, Y]$ denote the set of homotopy classes of maps of $X$ into $Y$.

(a) Let $I = [0, 1]$.
Show that for any $X$, the set $[X, I]$ has a single element.

(b) Show that if $Y$ is path connected, the set $[I, Y]$ has a single element.
:::

::: {.solution}
(a) Let $f,g:X\to I$ be arbitrary. Since $I=[0,1]$ is convex, define
$$
H(x,t)=(1-t)f(x)+tg(x).
$$
Then $H:X\times I\to I$ is continuous, $H(x,0)=f(x)$, and $H(x,1)=g(x)$. Thus every two maps $X\to I$ are homotopic, so $[X,I]$ has one element.

(b) Let $f,g:I\to Y$. Since $Y$ is path connected, choose a path $\alpha:I\to Y$ from $f(0)$ to $g(0)$. Every map from an interval is homotopic to the constant map at its initial value: for $f$,
$$
F(s,t)=f((1-t)s)
$$
is a homotopy from $f$ to the constant map $c_{f(0)}$, and similarly $g\simeq c_{g(0)}$. The constants $c_{f(0)}$ and $c_{g(0)}$ are homotopic by
$$
A(s,t)=\alpha(t),
$$
independent of $s$. Hence
$$
f\simeq c_{f(0)}\simeq c_{g(0)}\simeq g.
$$
Therefore $[I,Y]$ also has a single element.

The printed statement of (b) carries no nonemptiness hypothesis, and it needs none except for one space: Munkres defines a path connected space by a condition on pairs of points (§24), so the empty space is path connected vacuously, while $[I,\varnothing]$ is empty rather than a singleton. For every nonempty path connected $Y$ the argument above applies, and it begins exactly there, with the points $f(0)$ and $g(0)$ of a pair of maps $f,g: I \to Y$.
:::
