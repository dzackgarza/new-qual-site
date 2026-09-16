---
schema: qual/card@1
id: PR-I4YON
kind: proposition
title: Open sets are countable unions of disjoint intervals or almost disjoint cubes
classification:
  areas:
  - real-analysis
  topics:
  - Euclidean Spaces
  - Measure Theory
relations: []
review: draft
---

::: {.proposition}
(a) Every open set $U\subseteq\RR$ is a union of countably many pairwise disjoint open intervals, possibly unbounded, and these intervals are uniquely determined by $U$: they are the connected components of $U$.

(b) For $n\geq1$, every open set $U\subseteq\RR^n$ is a union of countably many pairwise [[FD-5T3HX|almost disjoint]] closed cubes.
:::

::: {.proof}
(a) Each connected component of $U$ is a connected open subset of $\RR$, hence an open interval, and distinct components are disjoint.
Each component contains a rational number, and distinct components contain distinct rationals, so there are countably many.
If $U$ is a disjoint union of open intervals, each of those intervals is connected and is relatively clopen in $U$, hence is a component; so the decomposition is unique.

(b) For $k\geq0$ let $\mathcal{Q}_k$ be the set of closed cubes $\prod_{i=1}^n[m_i2^{-k},(m_i+1)2^{-k}]$ with $m_1,\ldots,m_n\in\ZZ$, and put $\mathcal{Q}\coloneqq\bigcup_{k\geq0}\mathcal{Q}_k$, a countable set.
Two cubes in $\mathcal{Q}$ are either almost disjoint or one contains the other, and a cube in $\mathcal{Q}_k$ is contained in exactly one cube of $\mathcal{Q}_j$ for each $j\leq k$.
Let $\mathcal{C}$ be the set of cubes in $\mathcal{Q}$ that are contained in $U$ and maximal under inclusion among cubes of $\mathcal{Q}$ contained in $U$.
For $x\in U$ choose $r>0$ with the open ball $B(x,r)\subseteq U$ and $k$ with $\sqrt n\,2^{-k}<r$; a cube $Q\in\mathcal{Q}_k$ containing $x$ lies in $U$.
The cubes of $\mathcal{Q}$ containing $Q$ form a chain with at most $k+1$ elements, so its largest element contained in $U$ lies in $\mathcal{C}$.
Hence the cubes of $\mathcal{C}$ cover $U$; they are countably many, and pairwise almost disjoint because two distinct maximal cubes cannot be nested.
:::

::: {.remark}
The decomposition in (b) is not unique: replacing one cube of such a family by the $2^n$ closed cubes of half its side length obtained by bisecting each of its edges gives another countable family of pairwise almost disjoint closed cubes with union $U$.
:::
