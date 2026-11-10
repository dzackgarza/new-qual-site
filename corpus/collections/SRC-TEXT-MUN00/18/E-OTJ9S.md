---
schema: qual/card@1
id: E-OTJ9S
kind: problem
title: Coordinate slices are imbeddings
classification:
  areas:
  - topology
  topics:
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 4, printed p. 111, with Theorem
    18.2, Theorem 18.4 and the definition of imbedding on printed pp. 105-110; the stored
    statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 18.4, printed p. 180.
    His proof for f, which is the same for g: injective, continuous because both components
    are (identity and constant), and an imbedding because on its image it is inverse to the
    projection pi_1, which is continuous by Theorem 18.4. (tmp/sources/munkres-solutions-
    whitman.pdf).
---

::: {.exercise}

Given $x_0 \in X$ and $y_0 \in Y$, show that the maps $f: X \to X \times Y$ and $g: Y \to X \times Y$ defined by

$$
f(x) = x \times y_0 \quad \text{and} \quad g(y) = x_0 \times y
$$

are imbeddings.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 18.4, printed p. 180** (`tmp/sources/munkres-solutions-whitman.pdf`); the proof for $f$ is his, and $g$ is the same argument. "positron0802", *Solutions to Topology, Chapter 2*, Exercise 18.4, PDF p. 11, states the same in one line.

We show that $f:X\to X\times Y$, $f(x)=x\times y_{0}$, is an imbedding; the argument for $g$ is the same with the factors exchanged.

*$f$ is injective*: $f(x)=f(x')$ forces $x=x'$ in the first coordinate.

*$f$ is continuous*: its components are the identity $x\mapsto x$ and the constant map $x\mapsto y_{0}$, both continuous (Theorem 18.2), so $f$ is continuous by Theorem 18.4 (maps into products, printed p. 110).

*$f$ is an imbedding*: let $f':X\to f(X)$ be $f$ with its range restricted. It is a bijection, it is continuous because $f$ is (Theorem 18.2(e)), and its inverse is the restriction to $f(X)$ of the projection $\pi_{1}:X\times Y\to X$, which is continuous (Theorem 18.4); hence $f'$ is a homeomorphism and $f$ is an imbedding.
:::
