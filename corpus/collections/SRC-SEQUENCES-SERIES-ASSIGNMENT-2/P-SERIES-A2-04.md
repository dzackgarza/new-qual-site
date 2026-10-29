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

::: {.solution}

## Part (a)

Assume \((a_n)\) is bounded and every convergent subsequence converges to
the same limit \(a\).

::: pf

::: {.pf-step #s1-1}

Suppose, toward a contradiction, that
\[
a_n\not\to a.
\]


::: pf-proof

This is the negation of the desired conclusion.

:::

:::

::: {.pf-step #s1-2}

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

::: {.pf-step #s1-3}

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

Choose \(n_1\) using step [](#s1-2){.pf-ref} with \(N=1\). After choosing \(n_k\), apply
step [](#s1-2){.pf-ref} with \(N=n_k+1\) to choose \(n_{k+1}>n_k\) satisfying the same
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
for some \(b\in\RR\).


::: pf-proof

Bolzano--Weierstrass states that every bounded real sequence has a convergent
subsequence.

:::

:::

::: {.pf-step #s1-6}

By the hypothesis of part (a),
\[
\boxed{b=a}.
\]


::: pf-proof

The sequence \((a_{n_{k_j}})\) is a convergent subsequence of the original
sequence, and every such subsequence is assumed to converge to \(a\).

:::

:::

::: {.pf-step #s1-7}

On the other hand,
\[
\boxed{|b-a|\ge\varepsilon}.
\]


::: pf-proof

Every term of the convergent subsubsequence satisfies
\[
|a_{n_{k_j}}-a|\ge\varepsilon
\]
by step [](#s1-3){.pf-ref}. Passing to the limit and using continuity of
\(x\mapsto|x-a|\) gives
\[
|b-a|\ge\varepsilon.
\]

:::

:::

::: pf-step

Steps [](#s1-6){.pf-ref} and [](#s1-7){.pf-ref} contradict one another.


::: pf-proof

If \(b=a\), then
\[
|b-a|=0,
\]
but step [](#s1-7){.pf-ref} gives
\[
|b-a|\ge\varepsilon>0.
\]

:::

:::

::: {.pf-step #s1-9}

Therefore
\[
\boxed{a_n\to a}.
\]


::: pf-proof

The assumption of nonconvergence in step [](#s1-1){.pf-ref} led to a contradiction.

:::

:::

::: {.pf-step #s1-10}

Suppose, toward a contradiction, that
\[
a_n\not\to a.
\]


::: pf-proof

Again this is the negation of the desired conclusion.

:::

:::

::: {.pf-step #s1-11}

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

Repeat the construction in steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}.

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
step [](#s1-11){.pf-ref}.

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
\(\varepsilon\) from step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-14}

This contradicts
\[
|a_{n_{k_j}}-a|\ge\varepsilon
\]
from step [](#s1-11){.pf-ref}.


::: pf-proof

The further subsequence is still a subsequence of \((a_{n_k})\), so every
one of its terms satisfies the lower bound from step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-15}

Therefore
\[
\boxed{a_n\to a}.
\]


::: pf-proof

The nonconvergence assumption in step [](#s1-10){.pf-ref} leads to the contradiction in
step [](#s1-14){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} proves part (a), and step [](#s1-15){.pf-ref} proves part (b).

:::

:::

:::
