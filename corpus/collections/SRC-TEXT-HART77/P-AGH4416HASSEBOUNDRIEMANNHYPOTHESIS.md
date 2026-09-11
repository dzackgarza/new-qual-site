---
schema: qual/card@1
id: P-AGH4416HASSEBOUNDRIEMANNHYPOTHESIS
kind: problem
title: Hasse's bound $\abs{a} \leq 2\sqrt{q}$ for $N = \size X(\FF_q)$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
  - Curves
relations: []
review: draft
---

::: problem
Again let $X$ be an elliptic curve over $k$ of characteristic $p$, and suppose $X$ is defined over the field $\FF_q$ of $q=p^r$ elements, i.e., $X \subseteq \PP^2$ can be defined by an equation with coefficients in $\FF_q$. Assume also that $X$ has a rational point over $\FF_q$. Let $F': X_q \to X$ be the $k$-linear Frobenius with respect to $q$.

a. Show that $X_q \cong X$ as schemes over $k$, and that under this identification, $F': X \to X$ is the map obtained by the $q$-th power map on the coordinates of points of $X$, embedded in $\PP^2$.

b. Show that $1_X-F'$ is a separable morphism and its kernel is just the set $X(\FF_q)$ of points of $X$ with coordinates in $\FF_q$.

c. Using (Ex. 4.7), show that $F'+\hat{F}'=a_X$ for some integer $a$, and that $N=q-a+1$, where $N=\size X(\FF_q)$.

d. Use the fact that $\deg(m+n F')>0$ for all $m, n \in \ZZ$ to show that $\abs{a} \leq 2 \sqrt{q}$. This is Hasse's proof of the analogue of the Riemann hypothesis for elliptic curves (App. C, Ex. 5.6).

e. Now assume $q=p$, and show that the Hasse invariant of $X$ is 0 if and only if $a \equiv 0 \pmod p$. Conclude for $p \geq 5$ that $X$ has Hasse invariant 0 if and only if $N=p+1$.
:::
