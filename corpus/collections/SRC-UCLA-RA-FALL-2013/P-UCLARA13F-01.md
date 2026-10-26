---
schema: qual/card@1
id: P-UCLARA13F-01
kind: problem
title: Proper holomorphic maps between plane domains are surjective
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Fall 2013 section.
---

::: {.problem}
Let $U,V\subset\mathbb C$ be open and connected, and let $f:U\to\mathbb C$ be holomorphic with $f(U)\subset V$.
Suppose $f:U\to V$ is proper: $f^{-1}(K)$ is compact in $U$ whenever $K\subset V$ is compact.
Show that $f$ is surjective.
:::

::: pf

::: pf-step

The map $f$ is not constant.


::: pf-proof

If $f\equiv c\in V$, then the compact set $K=\{c\}\subset V$ would have
\[
f^{-1}(K)=U.
\]
Properness would make $U$ compact. But a nonempty open subset of $\mathbb C$ is not compact. Hence $f$ cannot be constant.

:::

:::

::: pf-step

By the open mapping theorem,
\[
f(U)
\]
is open in $V$.


::: pf-proof

A nonconstant holomorphic function on a connected open subset of $\mathbb C$ is an open map. Step <1>1 gives nonconstancy, and $f(U)\subset V$ by hypothesis.

:::

:::

::: pf-step

The image $f(U)$ is closed in $V$.


::: pf-proof

Let $(y_j)$ be a sequence in $f(U)$ converging to $y\in V$. Choose $x_j\in U$ with
\[
f(x_j)=y_j.
\]
The set
\[
K=\{y\}\cup\{y_j:j\geq1\}
\]
is compact in $V$: it is a convergent sequence together with its limit. Properness gives that
\[
f^{-1}(K)
\]
is compact in $U$. Hence $(x_j)$ has a subsequence $x_{j_k}\to x\in U$. Continuity of $f$ gives
\[
f(x)=\lim_k f(x_{j_k})=\lim_k y_{j_k}=y.
\]
Thus $y\in f(U)$. Since $V\subset\mathbb C$ is metrizable, sequential closedness is closedness.

:::

:::

::: pf-step

The set $f(U)$ is nonempty, open, and closed in the connected space $V$.


::: pf-proof

It is nonempty because $U$ is nonempty; openness is step <1>2 and closedness is step <1>3.

:::

:::

::: pf-step

Therefore
\[
f(U)=V.
\]


::: pf-proof

The only subsets of a connected space that are both open and closed are the empty set and the whole space. Step <1>4 excludes the empty set.

:::

:::

::: pf-step

Hence
\[
\boxed{f:U\to V\text{ is surjective}.}
\]


::: pf-proof

This is exactly the equality $f(U)=V$ from step <1>5.

:::

:::

::: pf-qed

Step <1>6 proves the claim.

:::

:::
