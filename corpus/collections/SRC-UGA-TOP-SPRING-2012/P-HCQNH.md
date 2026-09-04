---
schema: qual/card@1
id: P-HCQNH
kind: problem
title: A formula for $\chi(X)$ in terms of $\chi(U)$, $\chi(V)$, and $\chi(U\cap V)$
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Mayer-Vietoris
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Restored the official problem statement verbatim; the source omits the finiteness hypothesis needed for ordinary Euler characteristic.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Reproved inclusion-exclusion from the finite Mayer--Vietoris exact sequence under an explicit finite-type hypothesis.
---

::: problem
Suppose that $U$ and $V$ are open subsets of a space $X$, with $X = U \cup V$.
Find, with proof, a general formula relating the Euler characteristics of $X, U, V$, and $U \cap V$.
:::

::: {.solution}
<1>1. As stated in the official source, the problem needs the usual proviso that the ordinary Euler characteristics involved are defined.
Assume, for example, that with rational coefficients
\[
H_k(X;\mathbb Q),\quad
H_k(U;\mathbb Q),\quad
H_k(V;\mathbb Q),\quad
H_k(U\cap V;\mathbb Q)
\]
are finite-dimensional for every \(k\) and vanish for all sufficiently large \(k\). Then
\[
\boxed{
\chi(X)=\chi(U)+\chi(V)-\chi(U\cap V)}.
\]
::: {.proof}
Under this finite-type hypothesis,
\[
\chi(Y)=\sum_{k\ge0}(-1)^k\dim_{\mathbb Q}H_k(Y;\mathbb Q)
\]
is a finite sum for each of the four spaces.
Without such a hypothesis, the ordinary Euler characteristic in the source statement need not be defined, so no unrestricted numerical identity can be asserted.
:::

<1>2. The open cover \(X=U\cup V\) gives the Mayer--Vietoris long exact sequence
\[
\cdots\longrightarrow
H_k(U\cap V)
\longrightarrow
H_k(U)\oplus H_k(V)
\longrightarrow
H_k(X)
\longrightarrow
H_{k-1}(U\cap V)
\longrightarrow\cdots,
\]
with all homology groups taken over \(\mathbb Q\).
::: {.proof}
This is the singular-homology Mayer--Vietoris theorem for an open cover.
The openness of \(U\) and \(V\) is the standard hypothesis in this formulation.
:::

<1>3. Under the finite-type hypothesis in <1>1, the Mayer--Vietoris sequence truncates to a finite exact sequence of finite-dimensional vector spaces.
::: {.proof}
Choose \(N\) so large that all four homology groups vanish in degrees greater than \(N\). Then the portion of the Mayer--Vietoris sequence from degree \(N\) down through degree \(0\) has zeros at both ends:
\[
0\to H_N(U\cap V)
\to H_N(U)\oplus H_N(V)
\to H_N(X)
\to\cdots
\to H_0(U)\oplus H_0(V)
\to H_0(X)
\to0.
\]
Every term is finite-dimensional by hypothesis.
:::

<1>4. The alternating sum of the dimensions of the terms in this finite exact sequence is zero.
::: {.proof}
For any finite exact sequence
\[
0\to E_m\to E_{m-1}\to\cdots\to E_0\to0
\]
of finite-dimensional vector spaces,
\[
\sum_{j=0}^m(-1)^j\dim E_j=0.
\]
Indeed, if \(I_j\) denotes the image of \(E_j\to E_{j-1}\), exactness gives short exact sequences
\[
0\to I_{j+1}\to E_j\to I_j\to0,
\]
so
\[
\dim E_j=\dim I_{j+1}+\dim I_j.
\]
The alternating sum telescopes, with the end images zero.
:::

<1>5. Applying <1>4 to the sequence in <1>3 gives
\[
\chi(U\cap V)-\chi(U)-\chi(V)+\chi(X)=0.
\]
::: {.proof}
In each degree \(k\), the three consecutive types of terms are
\[
H_k(U\cap V),
\qquad
H_k(U)\oplus H_k(V),
\qquad
H_k(X).
\]
Accounting for the one-step shift between degree \(k\) and degree \(k-1\), the zero alternating sum from <1>4 is, up to an irrelevant overall sign,
\[
\sum_{k\ge0}(-1)^k
\left(
\dim H_k(U\cap V)
-\dim H_k(U)
-\dim H_k(V)
+\dim H_k(X)
\right)=0.
\]
Using
\[
\dim(H_k(U)\oplus H_k(V))
=
\dim H_k(U)+\dim H_k(V)
\]
and the definition of Euler characteristic yields the displayed identity.
:::

<1>6. Therefore, whenever the ordinary Euler characteristics in the source problem are defined under the preceding finite-type condition,
\[
\boxed{\chi(X)=\chi(U)+\chi(V)-\chi(U\cap V)}.
\]
::: {.proof}
Rearrange the equality in <1>5.
:::
:::
