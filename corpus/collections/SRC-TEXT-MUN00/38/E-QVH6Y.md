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
A metrizable space $X$ has a metrizable compactification if and only if it is second countable. For metrizable spaces this is equivalent to separability.

Suppose first that $X$ is dense in a compact metrizable space $Y$. Every compact metrizable space is second countable, and every subspace of a second-countable space is second countable. Hence $X$ is second countable.

Conversely, suppose $X$ is metrizable and second countable. A metrizable space is regular, so by the Urysohn metrization/embedding theorem in its standard embedding form, a second-countable regular space admits a topological embedding
$$
e:X\hookrightarrow [0,1]^{\ZZ_+}.
$$
The Hilbert cube $[0,1]^{\ZZ_+}$ is compact metrizable. Therefore
$$
Y=\overline{e(X)}
$$
is a closed subspace of a compact metrizable space, hence is itself compact metrizable, and $e(X)$ is dense in $Y$. Thus $Y$ is a metrizable compactification of $X$.

Hence
$$
\boxed{X\text{ metrizable has a metrizable compactification}\iff X\text{ is second countable}.}
$$
:::
