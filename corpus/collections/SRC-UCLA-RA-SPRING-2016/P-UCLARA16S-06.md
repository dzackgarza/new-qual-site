---
schema: qual/card@1
id: P-UCLARA16S-06
kind: problem
title: Orthonormal systems with $\|f\|_\infty\le C\|f\|_2$ on their span are finite
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Suppose that $\{\phi_n\}$ is an orthonormal system of continuous functions in $L^2([0,1])$ and let $S$ be the closure of the span of $\{\phi_n\}$. If
$$
\sup_{f\in S\setminus\{0\}}\frac{\lVert f\rVert_\infty}{\lVert f\rVert_2}<\infty,
$$
prove that $S$ is finite dimensional.
:::

::: {.solution}

Choose $M<\infty$ such that
$$
\|f\|_\infty
\le
M\|f\|_2
\qquad
(f\in S).
$$

::: pf

::: {.pf-step #s1-1}

For every positive integer $N$ and every $x\in[0,1]$,
$$
\sum_{n=1}^N|\phi_n(x)|^2
\le
M^2.
$$


::: pf-proof

Fix $N$ and $x$. For arbitrary scalars $a_1,\dots,a_N$, set
$$
f_a
\coloneqq
\sum_{n=1}^N a_n\phi_n.
$$
Then $f_a\in S$, and orthonormality gives
$$
\|f_a\|_2^2
=
\sum_{n=1}^N|a_n|^2.
$$
Because $f_a$ is continuous on $[0,1]$, its ordinary supremum norm equals its $L^\infty$ norm. Hence
$$
\left|
\sum_{n=1}^N a_n\phi_n(x)
\right|
\le
\|f_a\|_\infty
\le
M
\left(
\sum_{n=1}^N|a_n|^2
\right)^{1/2}.
$$
Taking the supremum over all coefficient vectors with
$$
\sum_{n=1}^N|a_n|^2=1
$$
and using the Euclidean dual-norm identity yields
$$
\left(
\sum_{n=1}^N|\phi_n(x)|^2
\right)^{1/2}
\le M.
$$
Squaring proves the claim.

:::

:::

::: {.pf-step #s1-2}

Every finite orthonormal subfamily of $\{\phi_n\}$ has cardinality at most $M^2$.


::: pf-proof

Integrating the inequality from step [](#s1-1){.pf-ref} over $[0,1]$ and using Tonelli's theorem,
$$
\begin{aligned}
N
&=
\sum_{n=1}^N\|\phi_n\|_2^2\\
&=
\int_0^1
\sum_{n=1}^N|\phi_n(x)|^2\,dx\\
&\le
\int_0^1 M^2\,dx
=M^2.
\end{aligned}
$$
Thus no finite orthonormal subfamily can contain more than $M^2$ elements.

:::

:::

::: {.pf-step #s1-3}

The orthonormal system $\{\phi_n\}$ is finite.


::: pf-proof

If the system were infinite, then for every positive integer $N$ it would contain $N$ distinct elements. Choosing an integer $N>M^2$ would contradict step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

$S$ is finite dimensional.


::: pf-proof

By step [](#s1-3){.pf-ref} there are only finitely many functions in the orthonormal system. Their span is therefore finite dimensional, hence closed in $L^2([0,1])$. Since $S$ is defined as the closure of that span, $S$ equals the span itself and is finite dimensional.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the desired conclusion.

:::

:::

:::
