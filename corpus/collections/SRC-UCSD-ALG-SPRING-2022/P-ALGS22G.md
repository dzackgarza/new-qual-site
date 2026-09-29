---
schema: qual/card@1
id: P-ALGS22G
kind: problem
title: "Simple finitely generated k-algebras are finite-dimensional, and artinian iff finite-dimensional"
classification:
  areas:
  - algebra
  topics:
  - Ring Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: {.problem}
Let $k$ be a field and let $A$ be a finitely generated commutative $k$-algebra.

(a) Suppose that $A$ is simple as an $A$-module. Prove that $A$ is a finite-dimensional
$k$-vector space.

(b) Show that $A$ is an Artinian ring if and only if $A$ is a finite-dimensional
$k$-vector space.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If \(A\) is simple as an \(A\)-module, then \(A\) is a field.

::: pf-proof

The \(A\)-submodules of the regular module \(A\) are exactly the ideals of \(A\).
Simplicity therefore says that the only ideals are \(0\) and \(A\). Since \(A\neq0\),
this is equivalent to every nonzero element being a unit, so \(A\) is a field.

:::

:::

::: pf-step

Under the hypothesis of part (a), \(A\) is finite-dimensional over \(k\).

::: pf-proof

By step [](#s1){.pf-ref}, \(A\) is a field. By hypothesis it is finitely generated as a \(k\)-algebra.
Zariski's lemma therefore implies that \([A:k]<\infty\).

:::

:::

::: {.pf-step #s3}

If \(A\) is finite-dimensional as a \(k\)-vector space, then \(A\) is Artinian.

::: pf-proof

Every ideal of \(A\) is in particular a \(k\)-subspace. A descending chain of ideals is
therefore a descending chain of subspaces of the finite-dimensional vector space \(A\),
so the dimensions can decrease only finitely many times. Hence every descending chain of
ideals stabilizes.

:::

:::

::: {.pf-step #s4}

Suppose conversely that \(A\) is Artinian. Then \(A\), regarded as a module over
itself, has finite length.

::: pf-proof

For a commutative ring, Artinianity is equivalent to finite length of the regular
module; in particular every Artinian ring is Noetherian and admits a finite composition
series as an \(A\)-module.

:::

:::

::: {.pf-step #s5}

Every composition factor of the regular module \(A\) is of the form
\(A/\mathfrak m\) for a maximal ideal \(\mathfrak m\subset A\), and each such field is
finite-dimensional over \(k\).

::: pf-proof

A simple \(A\)-module is isomorphic to \(A/\mathfrak m\) for some maximal ideal
\(\mathfrak m\). Because \(A\) is a finitely generated \(k\)-algebra, so is every
quotient \(A/\mathfrak m\). Since \(A/\mathfrak m\) is a field, Zariski's lemma gives
\([A/\mathfrak m:k]<\infty\).

:::

:::

::: {.pf-step #s6}

Hence an Artinian finitely generated commutative \(k\)-algebra \(A\) is
finite-dimensional over \(k\).

::: pf-proof

Choose a composition series
\[
0=M_0\subset M_1\subset\cdots\subset M_\ell=A.
\]
By step [](#s5){.pf-ref}, each quotient \(M_i/M_{i-1}\) is finite-dimensional over \(k\). Repeatedly
using
\[
\dim_k M_i=\dim_k M_{i-1}+\dim_k(M_i/M_{i-1})
\]
shows that \(\dim_k A<\infty\).

:::

:::

::: pf-step

Therefore
\[
A\text{ is Artinian}\quad\Longleftrightarrow\quad \dim_k A<\infty.
\]

::: pf-proof

The forward implication is steps [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref}, and the reverse implication is step [](#s3){.pf-ref}.

:::

:::

:::

:::
