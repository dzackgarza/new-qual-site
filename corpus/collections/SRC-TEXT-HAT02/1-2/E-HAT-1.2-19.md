---
schema: qual/card@1
id: E-HAT-1.2-19
kind: exercise
title: Union of spheres of radius $1/n$ centered at $(1/n, 0, 0)$ is simply-connected
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Simply Connected
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

Show that the subspace of $\mathbb{R}^3$ that is the union of the spheres of radius ${^1/_n}$ and center $({^1/_n}, 0, 0)$ for $n = 1, 2, \cdots$ is simply-connected.

::: solution
**Goal:** Show the union $X$ is path-connected and has trivial $\pi_1$.

<1> Describe the geometry.
    *Proof:*
    <2>1. Let
        $$
        S_n=\{x\in\RR^3:\|x-(1/n,0,0)\|=1/n\}.
        $$
    <2>2. The point $0=(0,0,0)$ lies in every $S_n$.
    <2>3. The distance between centers is
        $$
        \left\|\frac1n,0,0-\frac1{n+1},0,0\right\|=\frac1{n(n+1)}
        $$
        which equals $1/n-1/(n+1)$, so $S_{n+1}$ lies in the closed unit ball of $S_n$ and $S_{n+1}\cap S_n=\{0\}$.
    <2>4. Hence $X=\bigcup_{n\ge1}S_n$ is a wedge of spheres with basepoint $0$.

<1> Build the finite subunions.
    *Proof:*
    <2>1. Let $X_m=\bigcup_{n=1}^m S_n$.
    <2>2. $X_m$ is a finite wedge $\bigvee_{n=1}^m S^2$, so $\pi_1(X_m)=0$.

<1> Handle an arbitrary loop in $X$.
    *Proof:*
    <2>1. Let $\gamma:S^1\to X$ be a loop based at $0$.
    <2>2. A continuous image of $S^1$ is compact and meets only finitely many spheres away from $0$.
    <2>3. Therefore $\gamma(S^1)\subseteq X_m$ for some $m$.
    <2>4. Since $X_m$ is simply-connected, $\gamma$ is null-homotopic in $X_m\subseteq X$.

<1> Conclude $\pi_1(X)=0$, so $X$ is simply-connected.

Authored by **Codex 5.3 Spark Extra High**.
:::
