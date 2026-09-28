---
schema: qual/card@1
id: P-AGH416MAPTOP1DEGREE
kind: problem
title: Every curve of genus $g$ admits a finite map to $\PP^1$ of degree $\leq g+1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Riemann-Roch
  - Linear Systems
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.1.6 and independently derived the Riemann--Roch argument
    before comparing it with the retained solution transcription. The degree
    calculation agrees with the pole-divisor formula used in II.6.9.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $X$ be a curve of genus $g$.
Show that there is a finite morphism $f: X \to \PP^1$ of degree $\leq g+1$.

Recall that the degree of a finite morphism of curves $f: X \to Y$ is defined as the degree of the field extension $[K(X): K(Y)]$ (II.6).
:::

::: {.solution}
Choose a point $P\in X$ and put
$$
D=(g+1)P.
$$

<1>1. One has
$$
\ell(D)\ge2.
$$

::: {.proof}
By [[T-MWDVL|Riemann--Roch]],
$$
\ell(D)-\ell(K-D)
=
\deg D+1-g
=
2.
$$
Since $\ell(K-D)\ge0$, it follows that
$$
\ell(D)=2+\ell(K-D)\ge2.
$$
:::

<1>2. There is a nonconstant rational function $f\in K(X)$ whose pole divisor satisfies
$$
(f)_\infty\le D.
$$

::: {.proof}
By definition,
$$
L(D)=H^0(X,\mco_X(D))
=
\{f\in K(X):\operatorname{div}(f)+D\ge0\}\cup\{0\}.
$$
The constants form a one-dimensional subspace of $L(D)$, while step <1>1 gives $\dim_kL(D)\ge2$. Hence there is a nonconstant $f\in L(D)$.

The inequality
$$
\operatorname{div}(f)+D\ge0
$$
says precisely that the polar divisor of $f$ is bounded by $D$:
$$
(f)_\infty\le D.
$$
:::

<1>3. The function $f$ defines a finite morphism
$$
f:X\longrightarrow\PP^1
$$
of degree at most $g+1$.

::: {.proof}
A nonconstant rational function on the smooth projective curve $X$ defines a nonconstant morphism to $\PP^1$. A nonconstant morphism between projective integral curves is finite.

Its degree equals the degree of its polar divisor:
$$
\deg f=\deg (f)_\infty
$$
by the degree formula for a rational function on a projective curve. By step <1>2,
$$
\deg (f)_\infty
\le
\deg D
=
g+1.
$$
Therefore
$$
\boxed{\deg f\le g+1}.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the required finite morphism.
:::
:::
