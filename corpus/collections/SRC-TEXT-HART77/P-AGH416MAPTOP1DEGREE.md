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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 4.1.6, printed p. 84,
    rendered as a page image from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne IV.1.6, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed
    l(gP) >= 1 and l((g+1)P) >= 2 by Riemann-Roch, the elliptic case
    l(P) = 1, and the degree bound the exercise asks for. Not checked: Yang's Solutions outside printed pp. 84-85; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now names Yang Pi-Yeh's Solution 4.1.6 at printed
    p. 84 beside the entry already there. No step, statement or
    hypothesis of the card changes.
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

::: pf

::: {.pf-step #s1}

One has
$$
\ell(D)\ge2.
$$

::: pf-proof

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

:::

::: {.pf-step #s2}

There is a nonconstant rational function $f\in K(X)$ whose pole divisor satisfies
$$
(f)_\infty\le D.
$$

::: pf-proof

By definition,
$$
L(D)=H^0(X,\mco_X(D))
=
\{f\in K(X) \st \divisorof(f)+D\ge0\}\cup\{0\}.
$$
The constants form a one-dimensional subspace of $L(D)$, while step [](#s1){.pf-ref} gives $\dim_kL(D)\ge2$. Hence there is a nonconstant $f\in L(D)$.

The inequality
$$
\divisorof(f)+D\ge0
$$
says precisely that the polar divisor of $f$ is bounded by $D$:
$$
(f)_\infty\le D.
$$

:::

:::

::: {.pf-step #s3}

The function $f$ defines a finite morphism
$$
f:X\longrightarrow\PP^1
$$
of degree at most $g+1$.

::: pf-proof

A nonconstant rational function on the smooth projective curve $X$ defines a nonconstant morphism to $\PP^1$. A nonconstant morphism between projective integral curves is finite.

Its degree equals the degree of its polar divisor:
$$
\deg f=\deg (f)_\infty
$$
by the degree formula for a rational function on a projective curve. By step [](#s2){.pf-ref},
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

:::

::: pf-qed

Step [](#s3){.pf-ref} gives the required finite morphism.

:::

:::

:::

::: {.remark title="Published solution"}
A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.1.6, text version `tmp/sources/hartshorne-solutions-egbert.md`, produces the finite morphism to $\PP^1$ from the linear system $\linearsystem{K}$; the degree count and finiteness use (II, 6.8).

Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.1.6, takes the divisor $gP$ and applies Riemann--Roch. Two things in it need care. With $D=gP$ the bound is only $\ell(D)\ge\deg D+1-g=1$, which does not produce a nonconstant function: for $g=1$ one has $\ell(P)=1+\ell(K-P)=1$, so the only sections are constants, and a degree-one map would make $X$ rational. With $D=(g+1)P$ instead, $\ell(D)\ge(g+1)+1-g=2$, so there is a nonconstant $f$ whose only pole is at $P$, of order at most $g+1$, and the morphism $X\to\PP^1$ it defines has degree at most $g+1$ — the exercise's bound. The entry's closing "$\deg f=\deg D=g$" therefore states an equality where only the inequality holds, and its divisor is one short.
:::
