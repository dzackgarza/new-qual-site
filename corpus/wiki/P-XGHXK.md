---
schema: qual/card@1
id: P-XGHXK
kind: problem
title: "Main Idea: A linear homotopy projected onto the sphere\u2026"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
1. **Main Idea**: A linear homotopy projected onto the sphere works.

Let $f: X \to S^n \subset \RR^{n+1}$ be an arbitrary map that fails to be surjective. Then, by definition, there is at least one point $s_0 \in S^n - f(X)$.

Then, $\forall x\in X$, since $f(x) \neq s_0$, there is a unique geodesic $C$ connecting $f(x)$ and $s_0$. So a  variant of the straight line homotopy will work, by interpolating between $f(x)$ and $s_0$ along $C$.

So let $H:X \cross I \to S^n$ be defined by $H(x, t) = P(ts_0  + (1-t)f(x))$, where $P: \mathbb{R}^{n+1} \to S^n$ is given by $P(x) = x/\norm{x}$.
This is well defined, since the denominator is zero iff $f(x) = s_0$, which by assumption is not the case.
This is a homotopy, since $H(x, 0) =P(f(x)) = f(x)$ (since $P$ fixes $S^n$) and $H(x, 1) = P(s_0) = s_0$ (since $s_0 \in S^n$).

