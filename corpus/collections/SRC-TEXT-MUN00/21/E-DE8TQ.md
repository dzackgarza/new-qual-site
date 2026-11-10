---
schema: qual/card@1
id: E-DE8TQ
kind: problem
title: Isometric imbeddings
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §21 Exercise 2, printed p. 133, with the
    definition of imbedding on printed p. 105; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 21.2, PDF p. 23. The preimage of a ball around
    f(x) is the ball of the same radius around x, which gives injectivity, continuity, and
    openness onto the image, hence an imbedding. (tmp/sources/munkres-solutions-positron-
    ch2.pdf).
---

::: {.exercise}

Let $X$ and $Y$ be metric spaces with metrics $d_X$ and $d_Y$, respectively.
Let $f: X \to Y$ have the property that for every pair of points $x_1, x_2$ of $X$,

$$
d_Y(f(x_1), f(x_2)) = d_X(x_1, x_2).
$$

Show that $f$ is an imbedding.
It is called an isometric imbedding of $X$ in $Y$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.2, PDF p. 23** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the argument is theirs. Whitman's printed p. 235 runs the same three steps.

Let $f:X\to Y$ satisfy $d_{Y}(f(x_{1}),f(x_{2}))=d_{X}(x_{1},x_{2})$ for all $x_{1},x_{2}\in X$.

*Injectivity.* If $f(x)=f(y)$ then $d_{X}(x,y)=d_{Y}(f(x),f(y))=0$, so $x=y$.

*Continuity.* Let $x\in X$ and let $V$ be a neighbourhood of $f(x)$ in $Y$; choose $r>0$ with $B_{d_{Y}}(f(x),r)\subset V$. Then
$$
f^{-1}\big(B_{d_{Y}}(f(x),r)\big)=\{y\in X\mid d_{Y}(f(y),f(x))<r\}=\{y\in X\mid d_{X}(y,x)<r\}=B_{d_{X}}(x,r),
$$
which is a neighbourhood of $x$ mapped into $V$. So $f$ is continuous, and so is its restriction $f':X\to f(X)$ (range restricted).

*$f'$ is open onto its image.* Let $U\subset X$ be open and let $f(x)\in f'(U)$ with $x\in U$; choose $r>0$ with $B_{d_{X}}(x,r)\subset U$. Then
$$
f'\big(B_{d_{X}}(x,r)\big)=B_{d_{Y}}(f(x),r)\cap f(X),
$$
because $d_{Y}(f(y),f(x))<r\iff d_{X}(y,x)<r$. So the image of $U$ contains the trace on $f(X)$ of an open ball of $Y$ around $f(x)$: $f'(U)$ is open in the subspace $f(X)$.

Hence $f'$ is a continuous bijection onto $f(X)$ whose inverse carries each $f'(U)$ to an open set, that is, $f'$ is a homeomorphism and $f$ an imbedding.
:::
