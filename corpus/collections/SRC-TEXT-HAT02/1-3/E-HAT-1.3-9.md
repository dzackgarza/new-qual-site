---
schema: qual/card@1
id: E-HAT-1.3-9
kind: exercise
title: "Maps to $S^1$ from spaces with finite fundamental group"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

Show that if a path-connected, locally path-connected space $X$ has $\pi_1(X)$ finite, then every map $X \to S^1$ is nullhomotopic.

::: solution
**Goal:** Use the induced map on $\pi_1$ to force a trivial map into $\pi_1(S^1)=\mathbb Z$.

<1> Let $f\colon X\to S^1$ be any map.
    Choose basepoints $x_0\in X$, $s_0\in S^1$.
    The induced group map
    $$
    f_\*:\pi_1(X,x_0)\to \pi_1(S^1,s_0)\cong\mathbb Z
    $$
    has finite image because the domain is finite.

<1> Every finite subgroup of $\mathbb Z$ is trivial.
    Hence $f_\*=0$.

<1> Since $f_\*=0$, the covering-lifting criterion gives a lift
    $\tilde f\colon X\to\mathbb R$ of $f$ through $\exp\colon\mathbb R\to S^1$.
    Here $\mathbb R$ is contractible, so $\tilde f$ is nullhomotopic.
    Composing with $\exp$ shows $f$ is nullhomotopic.

Authored by **Codex 5.3 Spark Extra High**.
:::
