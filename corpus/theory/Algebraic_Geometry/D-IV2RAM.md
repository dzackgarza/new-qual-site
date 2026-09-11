---
schema: qual/card@1
id: D-IV2RAM
kind: definition
title: Ramification index, tame and wild ramification
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ramification
  - Riemann-Hurwitz
  - Differentials
relations:
- kind: uses
  target: D-MORUNR
- kind: related-to
  target: T-LKT0U
review: draft
prompts:
- Define the ramification index of a morphism of curves at a point.
- What is the difference between tame and wild ramification?
- What is the length of $(\Omega_{X/Y})_p$, and how does it depend on that difference?
- Give a wildly ramified map and compute its ramification divisor.
---

::: {.definition title="Ramification index"}
Let $f : X \to Y$ be a finite morphism of curves, $p \in X$, $q = f(p)$, and $t$ a uniformizer of the discrete valuation ring $\OO_{Y,q}$.
The **ramification index** is
\[
e_p \definedas v_p(f^\sharp t) ,
\]
the valuation at $p$ of the pulled-back uniformizer.
$f$ is **ramified** at $p$ if $e_p > 1$ and **unramified** there if $e_p = 1$; the image $q$ of a ramification point is a **branch point**.
:::

::: {.definition title="Tame and wild"}
Let $\characteristic k = p_0$.
The ramification at $p$ is **tame** if $p_0 \nmid e_p$, and **wild** if $p_0 \mid e_p$.
In characteristic $0$ all ramification is tame.
:::

::: {.proposition title="The length formula"}
For $f$ finite separable, $\Omega_{X/Y}$ is a torsion sheaf supported exactly on the ramification locus, its stalks are principal $\OO_p$-modules, and
\[
\length (\Omega_{X/Y})_p
\begin{cases}
= e_p - 1 & \text{at a tamely ramified } p, \\
> e_p - 1 & \text{at a wildly ramified } p .
\end{cases}
\]
The ramification divisor is $R = \sum_{p \in X} \length (\Omega_{X/Y})_p \cdot [p]$.
:::

::: {.remark title="Where the dichotomy comes from"}
The stalk length is computed by one derivative.
With $u$ a uniformizer at $p$ and $t$ one at $q$, write $f^\sharp t = c u^{e_p}(1 + \cdots)$; then
\[
f^* dt = \left( e_p \, c \, u^{e_p - 1} + \cdots \right) du ,
\]
and $\length(\Omega_{X/Y})_p$ is the valuation of that coefficient.
If $p_0 \nmid e_p$ the leading term survives and the valuation is $e_p - 1$.
If $p_0 \mid e_p$ the leading term is killed, the valuation is determined by whatever comes next, and it is strictly larger.
So the tame/wild split is not a bookkeeping convention: it is the single question of whether $e_p$ is invertible in $k$.

$t \mapsto u^n$ with $p_0 \nmid n$ is the tame model, contributing $n-1$.
For a wild example take $\characteristic k = p_0$ and $f : \PP^1 \to \PP^1$ with $t = u^{p_0} - u$, which is separable since $dt = -du$.
It is unramified on the affine line and totally ramified at infinity with $e = p_0$, which is wild, and the local computation there gives length $2p_0 - 2 > p_0 - 1$.
Riemann--Hurwitz confirms it: $-2 = p_0 \cdot (-2) + \deg R$ forces $\deg R = 2p_0 - 2$, carried by that one point.
:::

::: {.remark title="Why this is the notion Riemann--Hurwitz needs"}
[[T-LKT0U]] is stated with $\deg R = \sum_p \length (\Omega_{X/Y})_p$ and only becomes $\sum_p (e_p - 1)$ under tameness, and the word "tame" in that statement is defined here.
The formula with $e_p - 1$ is the one everyone memorises, so the examiner's question is whether one knows it is the special case, and whether one can say which way the inequality runs: wild ramification makes $\deg R$ *larger*, hence makes $g(X)$ larger than the naive count.
The example above is the cleanest evidence, since a degree-$p_0$ self-map of $\PP^1$ with one branch point is impossible under the tame formula.

The unramified condition $e_p = 1$ for all $p$ is the same one appearing in [[D-MORUNR]], and for curves it upgrades to étale for free, since a nonconstant morphism of smooth curves is automatically flat.
:::
