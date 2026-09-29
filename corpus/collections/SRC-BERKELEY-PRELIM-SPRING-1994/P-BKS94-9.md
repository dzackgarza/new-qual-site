---
schema: qual/card@1
id: P-BKS94-9
kind: problem
title: Proper analytic maps between planar domains are surjective
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 1994 preliminary examination.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Proved the proper map has closed image by compactness, used the open
    mapping theorem for the analytic case, and gave z mapsto |z| on C as a
    proper continuous nonsurjective counterexample.
---

::: {.problem}
1. Let U and V be open connected subsets of the complex plane, and let f be an analytic function in U such that $f ( U ) \subset V$ . Assume $f ^ { - 1 } ( K )$ is compact whenever K is a compact subset of V . Prove that $f ( U ) = V$

2. Prove that the last equality can fail if analytic is replaced by continuous in the preceding statement.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Under the hypotheses of part 1, the analytic function $f$ is
nonconstant.

::: pf-proof

If $f$ were constant with value $w\in V$, then for the compact set
$$
K=\{w\}
$$
one would have
$$
f^{-1}(K)=U.
$$
The hypothesis would then make $U$ compact. But a nonempty open subset of
$\CC$ is not compact. Hence $f$ is nonconstant.

:::

:::

::: {.pf-step #s2}

The set $f(U)$ is open in $V$.

::: pf-proof

By step [](#s1){.pf-ref}, $f$ is a nonconstant analytic function on the connected open
set $U$. The open mapping theorem therefore implies that $f(U)$ is open in
$\CC$, and hence open as a subset of $V$.

:::

:::

::: {.pf-step #s3}

The set $f(U)$ is closed in $V$.

::: pf-proof

Let
$$
y_j\in f(U),
\qquad
y_j\longrightarrow y\in V.
$$
Choose $x_j\in U$ with
$$
f(x_j)=y_j.
$$
The set
$$
K\coloneqq\{y\}\cup\{y_j:j\geq1\}
$$
is compact and lies in $V$. By hypothesis,
$$
f^{-1}(K)
$$
is compact. Hence some subsequence $x_{j_\ell}$ converges to a point
$x\in f^{-1}(K)\subseteq U$. Continuity gives
$$
f(x)
=
\lim_{\ell\to\infty}f(x_{j_\ell})
=
\lim_{\ell\to\infty}y_{j_\ell}
=
y.
$$
Thus $y\in f(U)$, proving that $f(U)$ is closed in $V$.

:::

:::

::: {.pf-step #s4}

One has
$$
f(U)=V.
$$

::: pf-proof

The image $f(U)$ is nonempty, open in $V$ by step [](#s2){.pf-ref}, and closed in $V$
by step [](#s3){.pf-ref}. Since $V$ is connected, the only nonempty subset both open and
closed in $V$ is $V$ itself.

:::

:::

::: {.pf-step #s5}

The conclusion can fail for a continuous proper map.

::: pf-proof

Take
$$
U=V=\CC
$$
and define
$$
F(z)=\abs{z}.
$$
Then $F$ is continuous and
$$
F(\CC)=[0,\infty)\neq\CC.
$$

It remains to check the compact-preimage property. Let $K\subseteq\CC$ be
compact. Then
$$
F^{-1}(K)
=
\{z\in\CC:\abs{z}\in K\cap[0,\infty)\}.
$$
This set is closed because $F$ is continuous. Since
$K\cap[0,\infty)$ is bounded, there is $R>0$ such that every
$z\in F^{-1}(K)$ satisfies $\abs{z}\leq R$. Hence $F^{-1}(K)$ is closed and
bounded in $\CC\cong\RR^2$, and therefore compact.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves part 1, and step [](#s5){.pf-ref} supplies the counterexample required
for part 2.

:::

:::

:::
