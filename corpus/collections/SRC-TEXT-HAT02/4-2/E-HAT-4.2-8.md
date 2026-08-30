---
schema: qual/card@1
id: E-HAT-4.2-8
kind: exercise
title: "Suspension of acyclic CW complex is contractible"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

Show the suspension of an acyclic CW complex is contractible.

::: solution
**Goal:** Show the suspension $\Sigma X$ is contractible when $X$ is acyclic.

<1>1. Use reduced homology of suspension.
    <2>1. For reduced homology of a suspension, $\widetilde H_n(\Sigma X)\cong \widetilde H_{n-1}(X)$ for $n\ge2$.
    <2>2. Since $X$ is acyclic, $\widetilde H_{n-1}(X)=0$ for all $n-1\ge0$, so $\widetilde H_n(\Sigma X)=0$ for all $n\ge2$.
    <2>3. The space $\Sigma X$ is nonempty and connected, hence $\widetilde H_0(\Sigma X)=0$.
    <2>4. Therefore $\widetilde H_n(\Sigma X)=0$ for every $n\ge0$.

<1>2. Check simple connectivity.
    <2>1. A suspension is path-connected, and in fact simply connected for any nonempty $X$, because every loop can be pushed into the union of two cones and then contracted to one endpoint.
    <2>2. Hence $\Sigma X$ is simply connected.

<1>3. Apply Whitehead’s theorem for CW complexes.
    <2>1. $\Sigma X$ is a CW complex (suspension of a CW complex).
    <2>2. A simply connected CW complex with all reduced homology zero is contractible.
    <2>3. Therefore $\Sigma X$ is contractible.
:::
