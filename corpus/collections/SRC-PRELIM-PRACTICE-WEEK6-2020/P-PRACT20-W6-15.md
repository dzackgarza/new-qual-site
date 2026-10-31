---
schema: qual/card@1
id: P-PRACT20-W6-15
kind: problem
title: Topology of the points of the unit square with an irrational coordinate
classification:
  areas:
  - prelim
  topics:
  - Connectedness
  - Path-Connectedness
relations: []
review: draft
---

::: {.problem}
Let $S \subset [0, 1] \times [0, 1]$ consist of all points $(x, y) \in [0, 1] \times [0, 1]$ such that $x$ or $y$ or both is irrational.
Which of the following is true (with respect to the standard topology on $\RR^{2}$)?

(A) $S$ is open

(B) $S$ is closed

(C) $S$ is connected

(D) $S$ is totally disconnected

(E) $S$ is compact
:::

::: {.solution}
Only (C) is true.

(A) is false. By density of $\QQ^2$ in $\RR^2$, every open ball centred at a point of $S$ contains a point with rational coordinates, which is not in $S$.

(B) is false. By density of $(\RR\setminus\QQ)^2$, there is a sequence of points of $S$ converging to a point of $[0,1]^2$ with rational coordinates, which is not in $S$.

(E) is false, since $S$ is not closed.

(C) is true; in fact $S$ is path-connected. Let $(x,y)\in S$. If $x$ is irrational, the vertical segment $V_x=\{(x,t):t\in[0,1]\}$ lies in $S$, so we can travel along it to $(x,\pi/4)$. The horizontal segment $H_{\pi/4}=\{(t,\pi/4):t\in[0,1]\}$ lies in $S$, so we can continue to $(\pi/4,\pi/4)$. If instead $y$ is irrational, travel along $H_y$ to $(\pi/4,y)$ and then along $V_{\pi/4}$ to $(\pi/4,\pi/4)$. So every point of $S$ is joined by a path to $(\pi/4,\pi/4)$, and composing paths joins any two points.

(D) is false, since $S$ is connected and has more than one point.
:::
