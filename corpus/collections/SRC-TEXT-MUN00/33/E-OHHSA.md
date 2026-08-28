---
schema: qual/card@1
id: E-OHHSA
kind: exercise
title: A regular space that is not completely regular
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
---

::: {.exercise}

Define a set $X$ as follows.
For each even integer $m$, let $L_m$ denote the line segment $m \times [-1, 0]$ in the plane.
For each odd integer $n$ and each integer $k \geq 2$, let $C_{n,k}$ denote the union of the line segments $(n + 1 - 1/k) \times [-1, 0]$ and $(n - 1 + 1/k) \times [-1, 0]$ and the semicircle

$$
\ts{x \times y \mid (x - n)^2 + y^2 = (1 - 1/k)^2 \text{ and } y \geq 0}
$$

in the plane.
Let $p_{n,k}$ denote the topmost point $n \times (1 - 1/k)$ of this semicircle.
Let $X$ be the union of all the sets $L_m$ and $C_{n,k}$, along with two extra points $a$ and $b$.
Topologize $X$ by taking sets of the following four types as basis elements:

(i) The intersection of $X$ with a horizontal open line segment that contains none of the points $p_{n,k}$.

(ii) A set formed from one of the sets $C_{n,k}$ by deleting finitely many points.

(iii) For each even integer $m$, the union of $\ts{a}$ and the set of points $x \times y$ of $X$ for which $x < m$.

(iv) For each even integer $m$, the union of $\ts{b}$ and the set of points $x \times y$ of $X$ for which $x > m$.

(a) Sketch $X$; show that these sets form a basis for a topology on $X$.

(b) Let $f$ be a continuous real-valued function on $X$.
Show that for any $c$, the set $f^{-1}(c)$ is a $G_\delta$ set in $X$.
(This is true for any space $X$.)
Conclude that the set $S_{n,k}$ consisting of those points $p$ of $C_{n,k}$ for which $f(p) \neq f(p_{n,k})$ is countable.
Choose $d \in [-1, 0]$ so that the line $y = d$ intersects none of the sets $S_{n,k}$.
Show that for $n$ odd,

$$
f((n - 1) \times d) = \lim_{k \to \infty} f(p_{n,k}) = f((n + 1) \times d).
$$

Conclude that $f(a) = f(b)$.

(c) Show that $X$ is regular but not completely regular.
:::
