---
schema: qual/card@1
id: E-2X3VM
kind: problem
title: Behavior of path connectedness under products, closures, images, and unions
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §24 Exercise 8, printed p. 158, with Theorem 19.6
    and Example 7; the four questions are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 24.8, PDF pp. 5-6. Products, images and unions
    with a common point are path connected; the closure of a path-connected set need not be,
    the topologist's sine curve being the example from Example 7. (tmp/sources/munkres-
    solutions-positron-ch3.pdf).
---

::: {.exercise}

(a) Is a product of path-connected spaces necessarily path connected?

(b) If $A \subset X$ and $A$ is path connected, is $\overline{A}$ necessarily path connected?

(c) If $f: X \to Y$ is continuous and $X$ is path connected, is $f(X)$ necessarily path connected?

(d) If $\theset{A_\alpha}$ is a collection of path-connected subspaces of $X$ and if $\bigcap A_\alpha \neq \varnothing$, is $\bigcup A_\alpha$ necessarily path connected?
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 24.8, PDF pp. 5--6** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); all four parts are theirs.

(a) **Yes.** If $\mathbf{x},\mathbf{y}\in\prod X_{\alpha}$ and $X_{\alpha}$ is path connected, choose paths $\gamma_{\alpha}:[0,1]\to X_{\alpha}$ from $x_{\alpha}$ to $y_{\alpha}$; then $\gamma(t)=(\gamma_{\alpha}(t))_{\alpha}$ is continuous into the product (Theorem 19.6: its coordinate functions are continuous) and joins $\mathbf{x}$ to $\mathbf{y}$.

(b) **No.** $A=\{x\times\sin(1/x)\mid 0<x\le1\}\subset\RR^{2}$ is path connected, being the continuous image of $(0,1]$; its closure, the topologist's sine curve, is not path connected (Example 7 of §24).

(c) **Yes.** If $x,y\in f(X)$ pick $p,q\in X$ with $f(p)=x,f(q)=y$ and a path $\gamma$ from $p$ to $q$; then $f\circ\gamma$ is a path from $x$ to $y$ in $f(X)$.

(d) **Yes.** Let $z\in\bigcap_{\alpha}A_{\alpha}$ and let $x,y\in\bigcup_{\alpha}A_{\alpha}$, say $x\in A_{\beta}$, $y\in A_{\gamma}$. Each $A_{\alpha}$ is path connected, so there are paths in $A_{\beta}$ from $x$ to $z$ and in $A_{\gamma}$ from $z$ to $y$; their concatenation is a path in the union from $x$ to $y$.
:::
