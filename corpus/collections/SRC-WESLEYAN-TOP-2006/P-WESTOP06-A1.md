---
schema: qual/card@1
id: P-WESTOP06-A1
kind: problem
title: Density character bounds the cardinality of $C(X)$
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
For a space $X$, define its density character by
\[
\delta X=\min\{m:X\text{ has a dense subset of cardinality }m\}.
\]

1. Explain why this minimum exists.
2. Let
   \[
   C(X)=\{f\in\RR^X:f\text{ is continuous}\}.
   \]
   If $m$ is infinite, prove that
   \[
   \delta X\le m\quad\Longrightarrow\quad |C(X)|\le2^m.
   \]
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The minimum in the definition of \(\delta X\) exists.


::: pf-proof

The space \(X\) is dense in itself, so the collection
\[
\mathcal K=\{|D|:D\subseteq X,\ \overline D=X\}
\]
of cardinalities of dense subsets is nonempty. Cardinals are well ordered, so every nonempty collection of cardinals has a least element. Therefore
\[
\delta X=\min\mathcal K
\]
is defined.

:::

:::

::: {.pf-step #s1-2}

If \(D\subseteq X\) is dense, then the restriction map
\[
\rho:C(X)\to\RR^D,
\qquad
\rho(f)=f|_D,
\]
is injective.


::: pf-proof

Suppose \(f,g\in C(X)\) satisfy \(f|_D=g|_D\). The equalizer
\[
E=\{x\in X:f(x)=g(x)\}
\]
is closed: it is the inverse image of the diagonal
\[
\Delta_{\RR}\subseteq\RR^2
\]
under the continuous map \(x\mapsto(f(x),g(x))\), and \(\RR\) is Hausdorff, so \(\Delta_{\RR}\) is closed. Since \(D\subseteq E\) and \(D\) is dense, one has
\[
X=\overline D\subseteq E.
\]
Thus \(f=g\), proving injectivity.

:::

:::

::: {.pf-step #s1-3}

If \(m\) is infinite and \(\delta X\le m\), then
\[
|C(X)|\le2^m.
\]


::: pf-proof

Choose a dense subset \(D\subseteq X\) with
\[
|D|=\delta X\le m.
\]
By step [](#s1-2){.pf-ref},
\[
|C(X)|\le|\RR^D|=|\RR|^{|D|}.
\]
Since \(m\) is infinite,
\[
|\RR|=2^{\aleph_0}\le2^m,
\]
and therefore
\[
|\RR|^{|D|}
\le
(2^m)^m
=
2^{m\cdot m}
=
2^m.
\]
Hence
\[
\boxed{|C(X)|\le2^m.}
\]

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves existence of the density character, and step [](#s1-3){.pf-ref} proves the required cardinal bound.

:::

:::

:::
