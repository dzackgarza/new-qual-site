---
schema: qual/card@1
id: E-26ELV
kind: exercise
title: Second countable locally compact Hausdorff spaces of finite dimension imbed as closed subspaces
classification:
  areas:
  - topology
  topics:
  - Dimension Theory
relations: []
review: draft
solved: false
---

::: {.exercise title="Munkres §50.6"}


Prove the following.

Theorem. Let $X$ be a locally compact Hausdorff space with a countable basis, such that every compact subspace of $X$ has topological dimension at most $m$. Then $X$ is homeomorphic to a closed subspace of $\mathbb{R}^{2m+1}$.

If $f: X \to \mathbb{R}^N$ is a continuous map, we say $f(x) \to \infty$ as $x \to \infty$ if given $n$, there is a compact subspace $C$ of $X$ such that $f(x) > n$ for $x \in X - C$.

(a) Let $\bar{\rho}$ be the uniform metric on $\mathcal{C}(X, \mathbb{R}^N)$. Show that if $f(x) \to \infty$ as $x \to \infty$ and $\bar{\rho}(f, g) < 1$, then $g(x) \to \infty$ as $x \to \infty$.

(b) Show that if $f(x) \to \infty$ as $x \to \infty$, then $f$ extends to a continuous map of one-point compactifications. Conclude that if $f$ is injective as well, then $f$ is a homeomorphism of $X$ with a closed subspace of $\mathbb{R}^N$.

(c) Given $f: X \to \mathbb{R}^N$ and given a compact subspace $C$ of $X$, let

$$
U_\epsilon(C) = \ts{f \mid \Delta(f \mid C) < \epsilon}.
$$

Show that $U_\epsilon(C)$ is open in $\mathcal{C}(X, \mathbb{R}^N)$.

(d) Show that if $N = 2m + 1$, then $U_\epsilon(C)$ is dense in $\mathcal{C}(X, \mathbb{R}^N)$. [Hint: Given $f$ and given $\epsilon, \delta > 0$, choose $g: C \to \mathbb{R}^N$ so that $d(f(x), g(x)) < \delta$ for $x \in C$, and $\Delta(g) < \epsilon$. Extend $f - g$ to $h: X \to [-\delta, \delta]^N$ using the Tietze theorem.]

(e) Show there exists a map $f: X \to \mathbb{R}^N$ such that $f(x) \to \infty$ as $x \to \infty$. [Hint: Write $X$ as the union of compact subspaces $C_n$ such that $C_n \subset \operatorname{Int} C_{n+1}$ for each $n$.]

(f) Let $C_n$ be as in (e). Use the fact that $\bigcap U_{1/n}(C_n)$ is dense in $\mathcal{C}(X, \mathbb{R}^N)$ to complete the proof.
:::
