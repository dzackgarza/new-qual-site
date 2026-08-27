---
schema: qual/card@1
id: E-MVB8P
kind: exercise
title: Sigma-compact Hausdorff spaces of finite dimension
subtitle: Munkres §50.8
classification:
  areas:
  - topology
  topics:
  - Dimension Theory
relations: []
review: draft
---

::: {.exercise}

Recall that $X$ is said to be $\sigma$-compact if there is a countable collection of compact subspaces of $X$ whose interiors cover $X$.

Theorem.
Let $X$ be a $\sigma$-compact Hausdorff space.
If every compact subspace of $X$ has topological dimension at most $m$, then so does $X$.

Let $\mathcal{A}$ be an open cover of $X$.
Find an open cover $\mathcal{B}$ of $X$ refining $\mathcal{A}$ that has order at most $m + 1$, as follows:

(a) Show that $X = \bigcup X_n$, where $X_n$ is compact and $X_n \subset \operatorname{Int} X_{n+1}$ for each $n$.
Let $X_0 = \varnothing$.

(b) Find an open covering $\mathcal{B}_0$ of $X$ refining $\mathcal{A}$ such that for each $n$, each element of $\mathcal{B}_0$ that intersects $X_n$ lies in $X_{n+1}$.

(c) Suppose $n \geq 0$ and $\mathcal{B}_n$ is an open covering of $X$ refining $\mathcal{B}_0$ such that $\mathcal{B}_n$ has order at most $m + 1$ at points of $X_n$.
Choose an open covering $\mathcal{C}$ of $X$ refining $\mathcal{B}_n$ that has order at most $m + 1$ at points of $X_{n+1}$.
Choose $f: \mathcal{C} \to \mathcal{B}_n$ so that $C \subset f(C)$.
For $B \in \mathcal{B}_n$, let $D(B)$ be the union of those $C$ for which $f(C) = B$.
Let $\mathcal{B}_{n+1}$ consist of all sets $B \in \mathcal{B}_n$ for which $B \cap X_{n-1} \neq \varnothing$, along with all sets $D(B)$ for which $B \in \mathcal{B}_n$ and $B \cap X_{n-1} = \varnothing$.
Show that $\mathcal{B}_{n+1}$ is an open covering of $X$ that refines $\mathcal{B}_n$ and has order at most $m + 1$ at points of $X_{n+1}$.

(d) Define $\mathcal{B}$ as follows.
Given a set $B$, it belongs to $\mathcal{B}$ if there is an $N$ such that $B \in \mathcal{B}_n$ for all $n \geq N$.
:::
