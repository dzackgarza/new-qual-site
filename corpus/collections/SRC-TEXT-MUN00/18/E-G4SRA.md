---
schema: qual/card@1
id: E-G4SRA
kind: problem
title: Products of continuous maps are continuous
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 10, printed p. 112, with Theorem
    18.1 and the product topology of §15; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 18.10, PDF p. 13. The content is theirs: the
    inverse image of a product basis element U x V is f^{-1}(U) x g^{-1}(V), open in A x C.
    (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Let $f: A \to B$ and $g: C \to D$ be continuous functions.
Let us define a map $f \times g: A \times C \to B \times D$ by the equation

$$
(f \times g)(a \times c) = f(a) \times g(c).
$$

Show that $f \times g$ is continuous.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 18.10, PDF p. 13** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the computation of the inverse image is theirs. Whitman, printed p. 187, proves the same by checking Theorem 18.1 at each point and neighbourhood.

Let $U\subset B$ and $V\subset D$ be open, so that $U\times V$ is a basis element of $B\times D$. For $a\in A$, $c\in C$,
$$
(f\times g)(a\times c)\in U\times V
\iff f(a)\in U \text{ and } g(c)\in V
\iff a\in f^{-1}(U) \text{ and } c\in g^{-1}(V),
$$
hence
$$
(f\times g)^{-1}(U\times V)=f^{-1}(U)\times g^{-1}(V),
$$
which is open in $A\times C$ because $f$ and $g$ are continuous. Since the inverse images of a basis of $B\times D$ are open, $f\times g$ is continuous (Theorem 18.1 and the definition of a basis for a topology).
:::
