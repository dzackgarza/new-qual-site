---
schema: qual/card@1
id: E-B3WXJ
kind: problem
title: Fixed points for maps of retracts of the disk
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 55: Problem 1 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-55-retractions-and-fixed-points/problem-1-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-55-retractions-and-fixed-points/problem-1-solution.txt), and against Munkres,
    Topology (2000), Section 55 Exercise 1, printed p. 353. dbFin's is the same composition $i\circ f\circ r$ and Theorem 55.6; the card writes the three steps out. Nothing needed repair.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Rewrote the solution on 2026-11-19. Its two steps opened with run-in titles
    ("Retraction and map extension", "Existence of a fixed point via Brouwer's
    Fixed Point Theorem") instead of claims, their content was a sequence of
    unlabelled fragments, and the page carried no citation. It is now two
    labelled steps — the composite j o f o r is a self-map of the disc, and its
    fixed point lies in A and is fixed by f — and it cites the published solution
    it transcribes, dbFin, "Section 55: Problem 1 Solution"
    (https://dbfin.com/topology/munkres/chapter-9/section-55-retractions-and-fixed-points/problem-1-solution/),
    kept at tmp/sources/dbfin/section-55-retractions-and-fixed-points/problem-1-solution.txt
    and read on 2026-11-11. Checked against the book in
    tmp/sources/munkres-2000-topology.md and the retained PDF: the exercise on
    printed p. 353 (PDF p. 368, printed page = PDF page - 15) and Theorem 55.6 on
    printed p. 351 (PDF p. 366). No statement changes.

---

::: {.exercise}

Show that if $A$ is a retract of $B^2$, then every continuous map $f: A \to A$ has a fixed point.
:::

::: {.solution}
The argument is that of the published solution of dbFin, "Section 55: Problem 1 Solution": compose the retraction, the given map and the inclusion into a self-map of the disc, apply Brouwer's theorem to that self-map, and read the fixed point back on $A$. The exercise is Munkres, *Topology* (2000), Section 55, Exercise 1, printed p. 353, and Brouwer's fixed-point theorem for the disc is Theorem 55.6, printed p. 351.

Let $r\colon B^2\to A$ be a retraction, so that $r$ is continuous and $r(a)=a$ for every $a\in A$, and let $j\colon A\to B^2$ be the inclusion.

::: pf

::: {.pf-step #self-map}
For every continuous $f\colon A\to A$ the composite $g=j\circ f\circ r$ is a continuous map of $B^2$ into itself.

::: pf-proof
The maps $r$, $f$ and $j$ are continuous, so their composite is continuous, and its values lie in $j(A)\subseteq B^2$.
:::

:::

::: {.pf-step #fixed-point}
$g$ has a fixed point $x$, and every fixed point $x$ of $g$ lies in $A$ and satisfies $f(x)=x$.

::: pf-proof
By Theorem 55.6, printed p. 351, there is a point $x\in B^2$ with $g(x)=x$. Now $g(x)=j(f(r(x)))$ lies in $j(A)=A$, so $x\in A$; since $r$ is a retraction, $r(x)=x$, and therefore $f(x)=f(r(x))=x$, which is the same equation $g(x)=j(f(r(x)))=x$ read in $B^2$.
:::

:::

:::

:::
