---
schema: qual/card@1
id: E-QVH6Y
kind: problem
title: Metrizable spaces with metrizable compactifications
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metrizability
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "Solutions to exercises for Mathematics 205A"
    (University of California, Riverside, Fall 2014; the file names no author), file solutions5a.pdf,
    section VI.4 "Local compactness and compactifications", "Problems from Munkres, §38, pp. 241-242",
    Exercise 3, printed p. 9 of that file (tmp/sources/munkres-solutions-ucr-math205A-solutions5a.pdf).
    Checked against Munkres, Topology (2000), Section 38 Exercise 3, printed p. 241, Theorem 34.1 (the
    Urysohn imbedding theorem), Exercise 21.3(b) (a countable product of metrizable spaces is metrizable
    by the metric there) and Tychonoff's theorem (Theorem 37.3). The set's necessity is the card's: a
    dense subspace of a compact metrizable space is second countable, since compact metrizable spaces
    are second countable and a subspace of a second countable space is second countable. What was
    corrected: the sheet prints the exercise with the course's annotation "[Just give a necessary
    condition on the topology of the space.]" and says the sufficiency "was not assigned", giving it in
    a single sentence that leans on a compact metrizable ambient space; the card proves both directions,
    imbedding X in [0,1]^{Z_+} by Theorem 34.1, which is compact by Tychonoff and metrizable by Exercise
    21.3(b), and taking the closure of the image.
---

::: {.exercise}

Under what conditions does a metrizable space have a metrizable compactification?
:::

::: {.solution}

No retained solution set covers this exercise: the card's own characterisation follows, with each direction a step.

::: pf

::: {.pf-step #necessity}
If a metrizable space $X$ is dense in a compact metrizable space $Y$, then $X$ is second countable.

::: pf-proof
A compact metrizable space is second countable, and a subspace of a second-countable space is second countable (Theorem 30.2, printed p. 194). So $Y$ is second countable and $X$, a subspace of $Y$, is too.
:::

:::

::: {.pf-step #sufficiency}
If $X$ is metrizable and second countable, then $X$ has a metrizable compactification.

::: pf-proof
A metrizable space is normal (Theorem 32.2, printed p. 202), hence regular. By the Urysohn metrization theorem with its imbedding proof (Theorems 34.1 and 34.2) a second-countable regular space admits an imbedding $e:X\to[0,1]^{\ZZ_{+}}$ into the Hilbert cube. The Hilbert cube is a countable product of compact metrizable spaces, hence compact (Theorem 37.3, Tychonoff) and metrizable (Theorem 20.5, printed p. 125, applied coordinatewise); put $Y=\overline{e(X)}$. A closed subspace of a compact space is compact (Theorem 26.2, printed p. 165) and a subspace of a metrizable space is metrizable, so $Y$ is compact metrizable, and $e(X)$ is dense in $Y$ by construction. Then $e:X\to Y$ is an imbedding with dense image, so $Y$ is a metrizable compactification of $X$.
:::

:::

::: {.pf-step #separable}
For metrizable spaces, second countable is the same as separable.

::: pf-proof
A second-countable space has a countable dense subset (Theorem 30.3(a), printed p. 194), and a separable metrizable space has a countable basis (Exercise 30.5(a), printed p. 194).
:::

:::

::: {.pf-qed}
A metrizable space has a metrizable compactification exactly when it is second countable (steps [](#necessity){.pf-ref} and [](#sufficiency){.pf-ref}), and for metrizable spaces this is the same as being separable (step [](#separable){.pf-ref}).
:::

:::

:::
