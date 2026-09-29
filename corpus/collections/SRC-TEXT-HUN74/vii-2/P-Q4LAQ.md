---
schema: qual/card@1
id: P-Q4LAQ
kind: problem
title: Smith normal form as a canonical matrix form
classification:
  areas:
  - algebra
  topics:
  - Smith Normal Form
  - Canonical Forms
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hungerford VII.2.5 in an independent exercise reproduction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $R$ be a PID. For each positive integer $r$ and sequence of nonzero ideals $I_1 \supset I_2 \supset \cdots \supset I_r$, choose a sequence $d_i \in R$ such that $(d_i) = I_i$ and $d_i \mid d_{i+1}$.

For a given pair of positive integers $n, m$, let $S$ be the set of all $n\times m$ matrices of the form $\left(\begin{array}{ll}{L_{r}} & {0} \\ {0} & {0}\end{array}\right)$ where $r=1,2,\cdots,\min(m,n)$ and $L_r$ is a diagonal $r\times r$ matrix with main diagonal $d_i$.

Show that $S$ is a set of canonical forms under equivalence for the set of all $n\times m$ matrices over $R$.
:::

::: {.solution}
Two \(n\times m\) matrices over \(R\) are equivalent when one is obtained from
the other by multiplication on the left and right by invertible matrices.
We prove that every equivalence class contains exactly one matrix in \(S\).

::: pf

::: {.pf-step #s1}

Every \(n\times m\) matrix over \(R\) is equivalent to an element of
\(S\).

::: pf-proof

By the Smith normal form theorem over a PID, every matrix \(A\) is equivalent
to a diagonal matrix
\[
D=\operatorname{diag}(a_1,\ldots,a_r,0,\ldots,0),
\]
where each \(a_i\ne0\) and
\[
a_1\mid a_2\mid\cdots\mid a_r.
\]
Put \(I_i=(a_i)\). Then
\[
I_1\supseteq I_2\supseteq\cdots\supseteq I_r.
\]
By the choice made in the statement, there are generators \(d_i\) of these
ideals with \(d_i\mid d_{i+1}\). Since \(a_i\) and \(d_i\) generate the same
principal ideal, they differ by a unit. Multiplying suitable rows (or columns)
by these units changes \(D\) to the corresponding matrix in \(S\). Hence every
equivalence class meets \(S\).

:::

:::

::: {.pf-step #s2}

For \(1\le j\le\min(m,n)\), let \(\Delta_j(A)\) be the ideal generated
by all \(j\times j\) minors of \(A\). Then \(\Delta_j(A)\) is invariant under
matrix equivalence.

::: pf-proof

Let \(P\) be any \(n\times n\) matrix over \(R\). By the Cauchy--Binet formula,
each \(j\times j\) minor of \(PA\) is an \(R\)-linear combination of
\(j\times j\) minors of \(A\), so
\[
\Delta_j(PA)\subseteq\Delta_j(A).
\]
If \(P\) is invertible, applying this to \(P^{-1}\) and \(PA\) gives the reverse
inclusion. The same argument applies to right multiplication by an invertible
\(m\times m\) matrix \(Q\). Hence \(\Delta_j(PAQ)=\Delta_j(A)\).

:::

:::

::: {.pf-step #s3}

If
\[
D=\operatorname{diag}(d_1,\ldots,d_r,0,\ldots,0)
\]
with \(d_1\mid\cdots\mid d_r\), then for \(1\le j\le r\),
\[
\Delta_j(D)=(d_1d_2\cdots d_j),
\]
and for \(j>r\), \(\Delta_j(D)=0\).

::: pf-proof

Every nonzero \(j\times j\) minor of \(D\) is a product
\(d_{i_1}\cdots d_{i_j}\) with
\(1\le i_1<\cdots<i_j\le r\). Divisibility of the diagonal entries implies
\[
d_1\cdots d_j\mid d_{i_1}\cdots d_{i_j},
\]
so every such minor lies in \((d_1\cdots d_j)\). The leading \(j\times j\)
minor equals \(d_1\cdots d_j\), giving equality. If \(j>r\), every \(j\times j\)
minor vanishes.

:::

:::

::: {.pf-step #s4}

Two matrices in \(S\) that are equivalent are equal.

::: pf-proof

Let their nonzero diagonal entries be
\[
d_1,\ldots,d_r
\quad\text{and}\quad
e_1,\ldots,e_s.
\]
By steps [](#s2){.pf-ref} and [](#s3){.pf-ref}, the largest index for which \(\Delta_j\ne0\) is both \(r\)
and \(s\), hence \(r=s\). Moreover, for each \(j\le r\),
\[
(d_1\cdots d_j)=(e_1\cdots e_j).
\]
For \(j=1\) this gives \((d_1)=(e_1)\). Inductively, if
\((d_i)=(e_i)\) for \(i<j\), cancellation in the PID gives
\((d_j)=(e_j)\). Thus the two Smith forms determine the same chain of ideals
\[
(d_1)\supseteq\cdots\supseteq(d_r).
\]
The statement fixed once and for all the chosen generator \(d_i\) for each such
chain, so the representatives in \(S\) have exactly the same diagonal entries.
Hence the matrices are equal.

:::

:::

::: pf-step

Therefore \(S\) is a set of canonical forms for matrix equivalence.

::: pf-proof

By step [](#s1){.pf-ref} every equivalence class contains an element of \(S\), and by step [](#s4){.pf-ref} it
contains at most one.

:::

:::

:::

:::
