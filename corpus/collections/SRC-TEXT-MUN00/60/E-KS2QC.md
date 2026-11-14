---
schema: qual/card@1
id: E-KS2QC
kind: problem
title: The projective line and its covering
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 60 Exercise 4, printed p. 375,
    with Theorem 60.3 and the compact-to-Hausdorff argument of Theorem 26.6. $P^1=S^1/(x\sim-x)$ and $z\mapsto z^2$ factors through a continuous bijection from the compact quotient onto the Hausdorff circle, hence a homeomorphism; the standard covering is exactly $z\mapsto z^2$. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    A published answer has now been located: Pearse, *Topology (2nd ed.) — James R. Munkres*,
    solutions, Cornell 2005, §60 Exercise 4, his p. 27, read in the MinerU extraction
    tmp/sources/cornell-erin-munkres.md. The solution is that answer transcribed and checked:
    $P^1$ is a circle and the covering map is $z\mapsto z^2$, the map the book itself uses as a
    covering map in the proof of Theorem 57.1. The source is correct and needed no repair; it
    quotes the covering property from earlier work, and the card cites the place in the book.
    Checked against the book: the exercise on printed p. 375, the definition of $P^n$ on printed
    p. 373, the covering and quotient properties of $q(z)=z^2$ on printed p. 356, Theorem 26.5 on
    printed p. 166 and Theorem 26.6 on printed p. 167. Not claimed: that the source identifies
    $P^1$ with $S^1$ by a proof -- it writes "so $P^1=S^1$", and the card supplies the compact-to-
    Hausdorff step.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the answer above, in Lamport form, with the source and the book's
    pages named in its own text.
---

::: {.exercise}

The space $P^1$ and the covering map $p: S^1 \to P^1$ are familiar ones.
What are they?
:::

::: {.solution}
The exercise is §60 Exercise 4, printed p. 375, and $P^1$ is defined as for
$n\ge2$ on printed p. 373: the space obtained from $S^1$ by identifying each point
with its antipode.

The answer is transcribed from Pearse, *Topology (2nd ed.) — James R. Munkres*,
solutions, Cornell 2005, §60 Exercise 4, his p. 27, read in
`tmp/sources/cornell-erin-munkres.md`: $P^1$ is a circle, and the covering map
$p:S^1\to P^1$ is $p(z)=z^2$, the two-sheeted covering of the circle by itself.
The source says that this map is a covering map because it was met earlier; in
this book it is the map $q(z)=z^2$ whose quotient and covering properties are
established in the proof of Theorem 57.1 (printed p. 356).

::: pf

::: {.pf-step #constant-on-antipodes}
$q(z)=z^2$ is continuous, surjective, and satisfies $q(-z)=q(z)$; and
$q(z)=q(w)$ exactly when $w=z$ or $w=-z$.

::: pf-proof
The map $q$ is continuous as a product of continuous maps into the group $S^1$,
and $(-z)^2=z^2$. If $z^2=w^2$ then $(w/z)^2=1$, so $w/z\in\theset{\pm1}$ and
$w=\pm z$. And $q$ is surjective, because $e^{i\theta}=(e^{i\theta/2})^2$.
:::

:::

::: {.pf-step #quotient}
There is a continuous bijection $\bar q:P^1\to S^1$ with
$\bar q(\theset{z,-z})=z^2$, and it is a homeomorphism.

::: pf-proof
The quotient map of $S^1$ onto its orbit space under $z\mapsto-z$ is
$P^1$. By step [](#constant-on-antipodes){.pf-ref} the map $q$ is constant on the
orbits of that identification and separates distinct orbits, so it induces a
bijection $\bar q$ with $\bar q(\theset{z,-z})=z^2$, and $\bar q$ is continuous by
the universal property of the quotient map. The space $P^1$ is compact, being a
continuous image of the compact space $S^1$ (Theorem 26.5, printed p. 166), and
$S^1$ is Hausdorff, so $\bar q$ is a homeomorphism by Theorem 26.6 (printed
p. 167).
:::

:::

::: {.pf-step}
$\boxed{P^1\cong S^1}$, and the covering map $p:S^1\to P^1$ is $z\mapsto
\theset{z,-z}$, which is $q(z)=z^2$ read through that homeomorphism.

::: pf-proof
The first assertion is step [](#quotient){.pf-ref}. The quotient map
$z\mapsto\theset{z,-z}$ is the covering map of the definition of $P^1$, and
composing it with $\bar q$ gives $q$; so under the identification of $P^1$ with
$S^1$ the covering map is $z\mapsto z^2$, a two-sheeted covering whose sheets are
the two halves of the circle. This is the space and covering the exercise asks for,
up to the homeomorphism of step [](#quotient){.pf-ref}.
:::

:::

:::
:::
