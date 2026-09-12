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

::: problem
Let $k$ be a field and let $A$ be a finitely generated commutative $k$-algebra.

(a) Suppose that $A$ is simple as an $A$-module. Prove that $A$ is a finite-dimensional
$k$-vector space.

(b) Show that $A$ is an Artinian ring if and only if $A$ is a finite-dimensional
$k$-vector space.
:::

::: {.solution}
<1>1. If \(A\) is simple as an \(A\)-module, then \(A\) is a field.
::: {.proof}
The \(A\)-submodules of the regular module \(A\) are exactly the ideals of \(A\).
Simplicity therefore says that the only ideals are \(0\) and \(A\). Since \(A\neq0\),
this is equivalent to every nonzero element being a unit, so \(A\) is a field.
:::

<1>2. Under the hypothesis of part (a), \(A\) is finite-dimensional over \(k\).
::: {.proof}
By <1>1, \(A\) is a field. By hypothesis it is finitely generated as a \(k\)-algebra.
Zariski's lemma therefore implies that \([A:k]<\infty\).
:::

<1>3. If \(A\) is finite-dimensional as a \(k\)-vector space, then \(A\) is Artinian.
::: {.proof}
Every ideal of \(A\) is in particular a \(k\)-subspace. A descending chain of ideals is
therefore a descending chain of subspaces of the finite-dimensional vector space \(A\),
so the dimensions can decrease only finitely many times. Hence every descending chain of
ideals stabilizes.
:::

<1>4. Suppose conversely that \(A\) is Artinian. Then \(A\), regarded as a module over
itself, has finite length.
::: {.proof}
For a commutative ring, Artinianity is equivalent to finite length of the regular
module; in particular every Artinian ring is Noetherian and admits a finite composition
series as an \(A\)-module.
:::

<1>5. Every composition factor of the regular module \(A\) is of the form
\(A/\mathfrak m\) for a maximal ideal \(\mathfrak m\subset A\), and each such field is
finite-dimensional over \(k\).
::: {.proof}
A simple \(A\)-module is isomorphic to \(A/\mathfrak m\) for some maximal ideal
\(\mathfrak m\). Because \(A\) is a finitely generated \(k\)-algebra, so is every
quotient \(A/\mathfrak m\). Since \(A/\mathfrak m\) is a field, Zariski's lemma gives
\([A/\mathfrak m:k]<\infty\).
:::

<1>6. Hence an Artinian finitely generated commutative \(k\)-algebra \(A\) is
finite-dimensional over \(k\).
::: {.proof}
Choose a composition series
\[
0=M_0\subset M_1\subset\cdots\subset M_\ell=A.
\]
By <1>5, each quotient \(M_i/M_{i-1}\) is finite-dimensional over \(k\). Repeatedly
using
\[
\dim_k M_i=\dim_k M_{i-1}+\dim_k(M_i/M_{i-1})
\]
shows that \(\dim_k A<\infty\).
:::

<1>7. Therefore
\[
A\text{ is Artinian}\quad\Longleftrightarrow\quad \dim_k A<\infty.
\]
::: {.proof}
The forward implication is <1>4--<1>6, and the reverse implication is <1>3.
:::
:::
