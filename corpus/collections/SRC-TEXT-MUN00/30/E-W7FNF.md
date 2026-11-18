---
schema: qual/card@1
id: E-W7FNF
kind: problem
title: The lower limit line and the ordered square are not metrizable
classification:
  areas:
  - topology
  topics:
  - Metrizability
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Ana Emilia de Orellana, "Solutions -
    Topology Munkres", Section 30 Exercise 6, printed p. 31
    (tmp/sources/munkres-solutions-anadeore.pdf), checked against Munkres, Topology (2000),
    Section 30 Exercise 6, printed p. 194, and against Example 3 (printed p. 192, R_l is Lindelof)
    and Example 5 (printed p. 193, I_o^2 is compact). Orellana's route is the one on the card:
    R_l is separable and Lindelof and not second countable, so by Exercise 30.5 it is not
    metrizable; and I_o^2 is compact, so a metrization would make it second countable and hence
    separable, which it is not. What was corrected: Orellana writes only "I_o^2 is compact ...
    then it also cannot be metrizable, because it is not separable", leaving the non-separability
    unproved; the card exhibits the uncountably many pairwise disjoint open vertical intervals
    {x} x (0,1) that no countable set can meet. Note that the rational points of I_o^2 are not
    dense: an interval {x} x (0,1) with x irrational meets Q x Q in no point.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured both arguments into numbered steps. Converted two assertions into proofs: that the
    vertical intervals of the ordered square are open (each is the interval (x x 0, x x 1) of the
    dictionary order) and that uncountably many pairwise disjoint nonempty open sets prevent
    separability; and, for the compact half, that a compact metric space is separable, proved here by
    taking a finite (1/n)-net for each n and collecting the centres. Kept as citations the two book
    facts the transcription used: Example 3 of Section 30 for the Lindelof property of R_l and
    Example 5 for the compactness of I_o^2. Not re-read this session: the Orellana page and Munkres
    printed pp. 192-194.
---

::: {.exercise}

Show that $\RR_\ell$ and $I_o^2$ are not metrizable.
:::

::: {.solution}

The route is that of **Ana Emilia de Orellana, "Solutions - Topology Munkres", Section 30 Exercise 6, printed p. 31** (`tmp/sources/munkres-solutions-anadeore.pdf`), with the non-separability of the ordered square proved rather than asserted. The statement was checked against Munkres, *Topology* (2000), §30 Exercise 6, printed p. 194.

::: pf

::: {.pf-step #rl-separable}
$\RR_{\ell}$ is separable.

::: pf-proof
$\QQ$ is countable, and every basis element $[a,b)$ with $a<b$ contains the rational points of $(a,b)$, which is nonempty because $\QQ$ is dense in $\RR$. A set meeting every basis element meets every nonempty open set, so $\QQ$ is dense in $\RR_{\ell}$.
:::

:::

::: {.pf-step #rl-not-second}
$\RR_{\ell}$ is not second countable.

::: pf-proof
Let $\mathcal{B}$ be a basis. For $x\in\RR$ the set $[x,x+1)$ is a neighbourhood of $x$, so there is $B_{x}\in\mathcal{B}$ with $x\in B_{x}\subset[x,x+1)$. A basis element of $\RR_{\ell}$ is $[a,b)$; from $x\in[a,b)\subset[x,x+1)$ we get $x\geq a$, and since $a\in[a,b)\subset[x,x+1)$ also $a\geq x$, so $a=x$. Thus $B_{x}$ has left endpoint $x$, and distinct $x$ give distinct basis elements: $x\mapsto B_{x}$ injects $\RR$ into $\mathcal{B}$, so $\mathcal{B}$ is uncountable.
:::

:::

::: {.pf-step #rl-not-metrizable}
$\RR_{\ell}$ is not metrizable.

::: pf-proof
A metrizable separable space is second countable, which is Exercise 5 of §30. Steps [](#rl-separable){.pf-ref} and [](#rl-not-second){.pf-ref} contradict this, so $\RR_{\ell}$ is not metrizable.
:::

:::

::: {.pf-step #square-not-separable}
$I_{o}^{2}$ is not separable.

::: pf-proof
For $x\in[0,1]$ the set $V_{x}=\{x\}\times(0,1)$ is the open interval $\bigl(x\times0,\,x\times1\bigr)$ of the dictionary order, hence open and nonempty, and the family $\{V_{x}\}$ is uncountable and pairwise disjoint: $V_{x}$ consists of the points of first coordinate $x$. A dense set meets every $V_{x}$, and a point of $V_{x}$ lies in no $V_{y}$ with $y\neq x$, so a dense set has at least one point for each $x$ and is uncountable.
:::

:::

::: {.pf-step #compact-separable}
Every compact metric space is separable.

::: pf-proof
Let $(Z,d)$ be compact. For each $n$ the balls $B(z,1/n)$ with $z\in Z$ cover $Z$, so finitely many cover, say those with centres $z_{n,1},\dots,z_{n,k_{n}}$. Let $S$ be the set of all centres over all $n$, which is a countable union of finite sets and so countable. It is dense: for $z\in Z$ and $\varepsilon>0$ choose $n$ with $1/n<\varepsilon$; some centre $z_{n,j}$ satisfies $d(z,z_{n,j})<1/n<\varepsilon$, so $S$ meets $B(z,\varepsilon)$.
:::

:::

::: {.pf-step #square-not-metrizable}
$I_{o}^{2}$ is not metrizable.

::: pf-proof
$I_{o}^{2}$ is compact, this being Example 5 of §30 (printed p. 193). Were it metrizable, step [](#compact-separable){.pf-ref} would make it separable, contradicting step [](#square-not-separable){.pf-ref}.
:::

:::

::: {.pf-step}
Neither $\RR_{\ell}$ nor $I_{o}^{2}$ is metrizable.

::: pf-proof
Steps [](#rl-not-metrizable){.pf-ref} and [](#square-not-metrizable){.pf-ref}.
:::

:::

:::

:::
