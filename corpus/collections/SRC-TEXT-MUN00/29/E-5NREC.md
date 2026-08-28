---
schema: qual/card@1
id: E-5NREC
kind: exercise
title: Images of locally compact spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $X$ be a locally compact space.
If $f: X \to Y$ is continuous, does it follow that $f(X)$ is locally compact?
What if $f$ is both continuous and open?
Justify your answer.
:::

::: solution
**Goal:** Determine whether the continuous image (and continuous open image) of a locally compact space is locally compact.

<1>1. Question 1: Continuous images of locally compact spaces need NOT be locally compact.
    *Proof:*
    <2>1. Let $X = \mathbb{R}$ with the discrete topology.
    <2>2. Since every singleton in $X$ is an open and compact neighborhood of itself, $X$ is locally compact.
    <2>3. Let $Y = \mathbb{Q}$ with the standard subspace topology inherited from $\mathbb{R}$.
    <2>4. Let $f: X \to Y$ be any surjective function (for example, mapping $\mathbb{R} \setminus \mathbb{Q}$ onto $0$ and acting as the identity on $\mathbb{Q}$).
    <2>5. Since $X$ has the discrete topology, $f$ is continuous, and $f(X) = \mathbb{Q}$.
    <2>6. The rational numbers $\mathbb{Q}$ are not locally compact at any point: every compact subset of $\mathbb{Q}$ has empty interior, so no point of $\mathbb{Q}$ possesses a compact neighborhood.
    <2>7. Thus the continuous image $f(X)$ is not locally compact.

<1>2. Question 2: If $f$ is continuous and open, then $f(X)$ IS locally compact.
    *Proof:*
    <2>1. Let $y \in f(X)$. Since $f: X \to f(X)$ is surjective, choose $x \in X$ such that $f(x) = y$.
    <2>2. Because $X$ is locally compact, there exists a compact subspace $C \subseteq X$ containing an open neighborhood $U \subseteq X$ of $x$, so $x \in U \subseteq C$.
    <2>3. Since $f$ is continuous, the image $f(C)$ is a compact subset of $f(X)$.
    <2>4. Since $f: X \to f(X)$ is an open map, $f(U)$ is an open subset of $f(X)$.
    <2>5. We have $y = f(x) \in f(U) \subseteq f(C)$, which exhibits $f(C)$ as a compact neighborhood of $y$ in $f(X)$.
    <2>6. Since $y \in f(X)$ was arbitrary, $f(X)$ is locally compact. Q.E.D.
:::
