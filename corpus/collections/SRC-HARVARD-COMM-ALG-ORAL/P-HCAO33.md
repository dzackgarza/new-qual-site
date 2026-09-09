---
schema: qual/card@1
id: P-HCAO33
kind: problem
title: Integral ring extensions
classification:
  areas:
  - algebra
  topics:
  - Integral Extensions
  - Prime Ideals
  - Integral Closure
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard commutative-algebra oral extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Define an integral ring extension and state its principal properties.
:::


::: solution
Let \(A\subseteq B\) be rings.

<1>1. An element \(b\in B\) is **integral over \(A\)** if it satisfies a monic
polynomial
\[
b^n+a_{n-1}b^{n-1}+\cdots+a_0=0,
\qquad a_i\in A.
\]
The extension \(B/A\) is integral if every element of \(B\) is integral over
\(A\).
::: proof
This is the definition.
:::

<1>2. For \(b\in B\), the following are equivalent:

- \(b\) is integral over \(A\);
- \(A[b]\) is a finitely generated \(A\)-module;
- there is a faithful finitely generated \(A[b]\)-submodule of \(B\) that is
  finitely generated over \(A\).
::: proof
If \(b\) satisfies a monic equation of degree \(n\), every power \(b^m\) with
\(m\ge n\) reduces to an \(A\)-linear combination of
\(1,b,\ldots,b^{n-1}\), so \(A[b]\) is finite over \(A\).

The second condition implies the third by taking \(A[b]\) itself.

For the third implication, let \(M\) be generated over \(A\) by
\(m_1,\ldots,m_r\). Multiplication by \(b\) gives an \(A\)-linear endomorphism
of \(M\), represented by a matrix \(C\in M_r(A)\). Cayley--Hamilton gives a
monic polynomial \(p\in A[x]\) with \(p(b)M=0\). Faithfulness as an
\(A[b]\)-module forces \(p(b)=0\), so \(b\) is integral.
:::

<1>3. Integral elements are stable under addition and multiplication, and
integrality is transitive.
::: proof
If \(b_1,\ldots,b_r\) are integral over \(A\), repeated use of <1>2 shows
\[
A[b_1,\ldots,b_r]
\]
is a finite \(A\)-module. Every element of this ring, in particular sums and
products of the \(b_i\), acts on this finite module, so <1>2 shows it is
integral over \(A\). Thus the elements of \(B\) integral over \(A\) form a
subring.

If \(A\subseteq B\subseteq C\), with \(B\) integral over \(A\) and \(c\in C\)
integral over \(B\), the coefficients of a monic equation for \(c\) involve
only finitely many elements \(b_1,\ldots,b_r\in B\). The ring
\(A[b_1,\ldots,b_r,c]\) is finite over \(A\), so <1>2 implies that \(c\) is
integral over \(A\).
:::

<1>4. Integrality is preserved by localization and quotient, and a finite-type
integral algebra is module-finite.
::: proof
A monic equation remains monic after applying a quotient map or localization,
which proves the first assertion. If
\[
B=A[b_1,\ldots,b_r]
\]
with each \(b_i\) integral, then repeated use of <1>2 shows \(B\) is a finite
\(A\)-module.
:::

<1>5. If \(B\) is integral over \(A\), then the map
\[
\operatorname{Spec}B\longrightarrow\operatorname{Spec}A,
\qquad \mathfrak q\longmapsto\mathfrak q\cap A,
\]
has the following principal properties:

- **lying over:** every prime of \(A\) is the contraction of a prime of \(B\);
- **going up:** if \(\mathfrak p_1\subseteq\mathfrak p_2\) in \(A\) and
  \(\mathfrak q_1\) lies over \(\mathfrak p_1\), there is
  \(\mathfrak q_2\supseteq\mathfrak q_1\) lying over \(\mathfrak p_2\);
- **incomparability:** two comparable primes of \(B\) with the same contraction
  are equal;
- consequently, a prime \(\mathfrak q\subseteq B\) is maximal if and only if
  \(\mathfrak q\cap A\) is maximal, and
  \(\dim B=\dim A\).
::: proof
For lying over, quotient by \(\mathfrak p\subseteq A\) and localize at
\(A\setminus\mathfrak p\). This reduces to an integral extension of a field
\(k\) by a nonzero ring \(C\). A maximal ideal of \(C\) contracts to \(0\),
since any nonzero element of the contraction is invertible in \(k\).

Going up follows by applying lying over to the integral extension
\[
A/\mathfrak p_1\subseteq B/\mathfrak q_1
\]
and then localizing at the image of \(\mathfrak p_2\).

For incomparability, suppose
\(\mathfrak q_1\subsetneq\mathfrak q_2\) have common contraction
\(\mathfrak p\). Quotient by \(\mathfrak q_1\) and localize at
\(A\setminus\mathfrak p\). One obtains an integral domain integral over the
field \(\operatorname{Frac}(A/\mathfrak p)\). An integral domain integral over
a field is a field: for \(0\ne x\), a monic equation of least degree with
nonzero constant term expresses \(x^{-1}\) as a polynomial in \(x\). Hence no
nonzero prime can remain above \(0\), contradiction.

The maximal-ideal assertion follows from lying over and incomparability.
Going up lifts chains of primes from \(A\) to \(B\), while incomparability shows
that contraction cannot shorten a chain in \(B\); hence the Krull dimensions
are equal.
:::
:::
