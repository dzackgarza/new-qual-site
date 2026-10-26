---
schema: qual/card@1
id: P-SERIES-A2-04
kind: problem
title: Subsequence criteria for convergence of a sequence
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
(a) Let $\{a_n\}$ be a bounded sequence with the property that every convergent subsequence converges to the same limit $a$. Show that the entire sequence converges to $a$.

(b) Now assume that $\{a_n\}$ has the property that every subsequence has a further subsequence that converges to the same limit $a$. Show that the entire sequence converges to $a$.
:::

## Part (a)

Assume \((a_n)\) is bounded and every convergent subsequence converges to
the same limit \(a\).

::: pf

::: pf-step

Suppose, toward a contradiction, that
\[
a_n\not\to a.
\]


::: pf-proof

This is the negation of the desired conclusion.

:::

:::

::: pf-step

Then there exists
\[
\varepsilon>0
\]
such that for every \(N\), there is some \(n\ge N\) with
\[
\boxed{|a_n-a|\ge\varepsilon}.
\]


::: pf-proof

This is the negation of the \(\varepsilon\)-\(N\) definition of convergence
to \(a\).

:::

:::

::: pf-step

Therefore one can choose a subsequence
\[
(a_{n_k})
\]
such that
\[
\boxed{
|a_{n_k}-a|\ge\varepsilon}
\]
for every \(k\).


::: pf-proof

Choose \(n_1\) using step <1>2 with \(N=1\). After choosing \(n_k\), apply
step <1>2 with \(N=n_k+1\) to choose \(n_{k+1}>n_k\) satisfying the same
inequality.

:::

:::

::: pf-step

The subsequence \((a_{n_k})\) is bounded.


::: pf-proof

Every subsequence of a bounded sequence is bounded.

:::

:::

::: pf-step

By Bolzano--Weierstrass, \((a_{n_k})\) has a convergent
subsubsequence
\[
a_{n_{k_j}}\to b
\]
for some \(b\in\mathbb R\).


::: pf-proof

Bolzano--Weierstrass states that every bounded real sequence has a convergent
subsequence.

:::

:::

::: pf-step

By the hypothesis of part (a),
\[
\boxed{b=a}.
\]


::: pf-proof

The sequence \((a_{n_{k_j}})\) is a convergent subsequence of the original
sequence, and every such subsequence is assumed to converge to \(a\).

:::

:::

::: pf-step

On the other hand,
\[
\boxed{|b-a|\ge\varepsilon}.
\]


::: pf-proof

Every term of the convergent subsubsequence satisfies
\[
|a_{n_{k_j}}-a|\ge\varepsilon
\]
by step <1>3. Passing to the limit and using continuity of
\(x\mapsto|x-a|\) gives
\[
|b-a|\ge\varepsilon.
\]

:::

:::

::: pf-step

Steps <1>6 and <1>7 contradict one another.


::: pf-proof

If \(b=a\), then
\[
|b-a|=0,
\]
but step <1>7 gives
\[
|b-a|\ge\varepsilon>0.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{a_n\to a}.
\]


::: pf-proof

The assumption of nonconvergence in step <1>1 led to a contradiction.

:::

:::

::: pf-step

Suppose, toward a contradiction, that
\[
a_n\not\to a.
\]


::: pf-proof

Again this is the negation of the desired conclusion.

:::

:::

::: pf-step

Then there are
\[
\varepsilon>0
\]
and a subsequence \((a_{n_k})\) such that
\[
\boxed{
|a_{n_k}-a|\ge\varepsilon}
\]
for every \(k\).


::: pf-proof

Repeat the construction in steps <1>2--<1>3.

:::

:::

::: pf-step

By the hypothesis of part (b), the subsequence \((a_{n_k})\) has a
further subsequence
\[
a_{n_{k_j}}\to a.
\]


::: pf-proof

The stated property applies to every subsequence, including the one chosen in
step <1>11.

:::

:::

::: pf-step

Since
\[
a_{n_{k_j}}\to a,
\]
there exists \(J\) such that for all \(j\ge J\),
\[
|a_{n_{k_j}}-a|<\varepsilon.
\]


::: pf-proof

Apply the definition of convergence with the same positive
\(\varepsilon\) from step <1>11.

:::

:::

::: pf-step

This contradicts
\[
|a_{n_{k_j}}-a|\ge\varepsilon
\]
from step <1>11.


::: pf-proof

The further subsequence is still a subsequence of \((a_{n_k})\), so every
one of its terms satisfies the lower bound from step <1>11.

:::

:::

::: pf-step

Therefore
\[
\boxed{a_n\to a}.
\]


::: pf-proof

The nonconvergence assumption in step <1>10 leads to the contradiction in
step <1>14.

:::

:::

::: pf-qed

Step <1>9 proves part (a), and step <1>15 proves part (b).

:::

:::
