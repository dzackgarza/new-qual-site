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

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 24.8, PDF pp. 5--6** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); all four parts are theirs, and (d) uses the pasting lemma explicitly where their sentence stops at "concatenation".

Part (c) is proved first, since the counterexample of (b) uses it.

Recall that a space is path connected when any two of its points are joined by a path, a path in $X$ being a continuous map $[0,1]\to X$.

::: pf

::: {.pf-step #image}
(c) Yes: the continuous image of a path-connected space is path connected.

::: pf-proof
Let $f:X\to Y$ be continuous with $X$ path connected, and let $x=f(p)$, $y=f(q)$ be points of $f(X)$. Choose a path $\gamma:[0,1]\to X$ from $p$ to $q$; then $f\circ\gamma$ is continuous, being a composite of continuous maps (Theorem 18.2(c)), with $(f\circ\gamma)(0)=x$ and $(f\circ\gamma)(1)=y$. So $f(X)$ is path connected.
:::

:::

::: {.pf-step #product}
(a) Yes: a product of path-connected spaces is path connected.

::: pf-proof
Let $\mathbf{x},\mathbf{y}\in\prod_{\alpha\in J}X_{\alpha}$ with each $X_{\alpha}$ path connected, and choose a path $\gamma_{\alpha}:[0,1]\to X_{\alpha}$ from $x_{\alpha}$ to $y_{\alpha}$. Define $\gamma(t)=\big(\gamma_{\alpha}(t)\big)_{\alpha}$. Its coordinate function $\pi_{\alpha}\circ\gamma=\gamma_{\alpha}$ is continuous for every $\alpha$, so $\gamma$ is continuous (Theorem 19.6), and $\gamma(0)=\mathbf{x}$, $\gamma(1)=\mathbf{y}$.
:::

:::

::: {.pf-step #closure}
(b) No: the closure of a path-connected subspace need not be path connected.

::: pf-proof
Let $A=\theset{x\times\sin(1/x)\mid 0<x\le1}\subseteq\RR^{2}$. The interval $(0,1]$ is path connected — for $s,t\in(0,1]$ the straight-line path $u\mapsto(1-u)s+ut$ stays in $(0,1]$ — and $A$ is its image under the continuous map $x\mapsto\big(x,\sin(1/x)\big)$, so $A$ is path connected by step [](#image){.pf-ref}. Its closure $\overline A=A\cup\big(\{0\}\times[-1,1]\big)$ is the topologist's sine curve, which is connected but not path connected (Example 7). So $\overline A$ is a counterexample.
:::

:::

::: {.pf-step #union}
(d) Yes: a union of path-connected subspaces with a common point is path connected.

::: pf-proof
Let $z\in\bigcap_{\alpha}A_{\alpha}$ and let $x,y\in\bigcup_{\alpha}A_{\alpha}$, say $x\in A_{\beta}$ and $y\in A_{\gamma}$. As $A_{\beta}$ is path connected there is a path $\gamma_{1}:[0,1]\to A_{\beta}$ from $x$ to $z$, and as $A_{\gamma}$ is path connected there is a path $\gamma_{2}:[0,1]\to A_{\gamma}$ from $z$ to $y$. Define $\gamma:[0,1]\to\bigcup_{\alpha}A_{\alpha}$ by $\gamma(s)=\gamma_{1}(2s)$ for $0\le s\le1/2$ and $\gamma(s)=\gamma_{2}(2s-1)$ for $1/2\le s\le1$. On the closed sets $[0,1/2]$ and $[1/2,1]$ these formulas are continuous and they agree at $s=1/2$, both giving $z$, so $\gamma$ is continuous by the pasting lemma (Theorem 18.3). It joins $x$ to $y$, so the union is path connected.
:::

:::

::: {.pf-qed}
The answers are: yes by step [](#product){.pf-ref}, no by step [](#closure){.pf-ref}, yes by step [](#image){.pf-ref}, and yes by step [](#union){.pf-ref}.
:::

:::

:::
