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

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.2** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the three steps are theirs. Dan Whitman, *Solutions Manual*, runs the same three.

Let $f:X\to Y$ satisfy $d_{Y}\big(f(x_{1}),f(x_{2})\big)=d_{X}(x_{1},x_{2})$ for all $x_{1},x_{2}\in X$, and let $f':X\to f(X)$ be $f$ with its range restricted.

::: pf

::: {.pf-step #injective}
$f$ is injective.

::: pf-proof
If $f(x)=f(y)$ then $d_{X}(x,y)=d_{Y}\big(f(x),f(y)\big)=0$, and a metric vanishes only on the diagonal, so $x=y$.
:::

:::

::: {.pf-step #continuous}
$f$, and hence $f'$, is continuous.

::: pf-proof
Let $x\in X$ and let $V$ be a neighbourhood of $f(x)$ in $Y$; choose $r>0$ with $B_{d_{Y}}\big(f(x),r\big)\subseteq V$. Then $f^{-1}\big(B_{d_{Y}}(f(x),r)\big)=\theset{y\in X\mid d_{Y}(f(y),f(x))<r}=\theset{y\mid d_{X}(y,x)<r}=B_{d_{X}}(x,r)$, a neighbourhood of $x$ carried into $V$; so $f$ is continuous at $x$. The restriction of the range of a continuous map to a subspace containing its image is continuous (Theorem 18.2(e)), so $f'$ is continuous.
:::

:::

::: {.pf-step #open-image}
$f'$ carries open sets of $X$ to open sets of the subspace $f(X)$.

::: pf-proof
Let $U\subseteq X$ be open and let $f(x)\in f'(U)$ with $x\in U$; choose $r>0$ with $B_{d_{X}}(x,r)\subseteq U$. For $y\in X$ one has $d_{Y}(f(y),f(x))<r$ exactly when $d_{X}(y,x)<r$, so $f'\big(B_{d_{X}}(x,r)\big)=B_{d_{Y}}\big(f(x),r\big)\cap f(X)$. Hence $f'(U)\supseteq B_{d_{Y}}\big(f(x),r\big)\cap f(X)$, a neighbourhood of $f(x)$ in the subspace $f(X)$; so $f'(U)$ is open in $f(X)$.
:::

:::

::: {.pf-qed}
$f'$ is a bijection onto $f(X)$ by step [](#injective){.pf-ref}, continuous by step [](#continuous){.pf-ref}, and open onto $f(X)$ by step [](#open-image){.pf-ref}; so $f'$ is a homeomorphism and $f$ is an imbedding.
:::

:::

:::
