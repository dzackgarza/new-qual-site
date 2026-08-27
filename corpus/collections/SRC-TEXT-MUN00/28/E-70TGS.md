---
schema: qual/card@1
id: E-70TGS
kind: exercise
title: Shrinking maps and contractions on compact metric spaces
subtitle: Munkres §28.7
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
---

::: {.exercise}

Let $(X, d)$ be a metric space.
If $f$ satisfies the condition

$$
d(f(x), f(y)) < d(x, y)
$$

for all $x, y \in X$ with $x \neq y$, then $f$ is called a shrinking map.
If there is a number $\alpha < 1$ such that

$$
d(f(x), f(y)) \leq \alpha d(x, y)
$$

for all $x, y \in X$, then $f$ is called a contraction.
A fixed point of $f$ is a point $x$ such that $f(x) = x$.

(a) If $f$ is a contraction and $X$ is compact, show $f$ has a unique fixed point.
[Hint: Define $f^1 = f$ and $f^{n+1} = f \circ f^n$. Consider the intersection $A$ of the sets $A_n = f^n(X)$.]

(b) Show more generally that if $f$ is a shrinking map and $X$ is compact, then $f$ has a unique fixed point.
[Hint: Let $A$ be as before. Given $x \in A$, choose $x_n$ so that $x = f^{n+1}(x_n)$. If $a$ is the limit of some subsequence of the sequence $y_n = f^n(x_n)$, show that $a \in A$ and $f(a) = x$. Conclude that $A = f(A)$, so that $\operatorname{diam} A = 0$.]

(c) Let $X = [0, 1]$.
Show that $f(x) = x - x^2/2$ maps $X$ into $X$ and is a shrinking map that is not a contraction.
[Hint: Use the mean-value theorem of calculus.]

(d) The result in (a) holds if $X$ is a complete metric space, such as $\mathbb{R}$; see the exercises of §43. The result in (b) does not: show that the map $f: \mathbb{R} \to \mathbb{R}$ given by $f(x) = [x + (x^2 + 1)^{1/2}]/2$ is a shrinking map that is not a contraction and has no fixed point.
:::
