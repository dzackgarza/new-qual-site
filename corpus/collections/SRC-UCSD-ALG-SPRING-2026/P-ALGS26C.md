---
schema: qual/card@1
id: P-ALGS26C
kind: problem
title: "Conjugacy classes of GL_3(F_q)"
classification:
  areas:
  - algebra
  topics:
  - Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Find the number of conjugacy classes of $\operatorname{GL}_3(\mathbb{F}_q)$, where $q$ is a power of a prime number.
:::


::: {.solution}
<1>1. Conjugacy classes in \(\operatorname{GL}_3(\mathbb F_q)\) are classified by rational canonical form, equivalently by assigning to each monic irreducible polynomial \(\phi\neq x\) a partition \(\lambda_\phi\), with
\[
\sum_\phi (\deg\phi)|\lambda_\phi|=3.
\]
::: {.proof}
This is the primary rational-canonical-form classification of similarity classes over a field. The condition \(\phi\neq x\) is exactly the invertibility condition: an invertible matrix has no \(x\)-primary part.
:::

<1>2. The classes whose characteristic polynomial splits completely over \(\mathbb F_q\) contribute
\[
\binom{q-1}{3}+2(q-1)(q-2)+3(q-1).
\]
::: {.proof}
There are \(q-1\) possible nonzero eigenvalues.

If there are three distinct eigenvalues, the unordered set of eigenvalues determines the class, giving
\[
\binom{q-1}{3}.
\]

If there are exactly two distinct eigenvalues, choose the eigenvalue of multiplicity \(2\) in \(q-1\) ways and the other eigenvalue in \(q-2\) ways. For the multiplicity-\(2\) primary part there are the two partitions of \(2\), namely \((2)\) and \((1,1)\). Hence this case contributes
\[
2(q-1)(q-2).
\]

If there is only one eigenvalue, its multiplicity is \(3\), and the three partitions
\[
(3),\qquad (2,1),\qquad (1,1,1)
\]
give three conjugacy classes for each nonzero eigenvalue. Hence this case contributes \(3(q-1)\).
:::

<1>3. The number of monic irreducible quadratic polynomials over \(\mathbb F_q\) is
\[
N_2=\frac{q^2-q}{2}.
\]
::: {.proof}
Every element of \(\mathbb F_{q^2}\setminus\mathbb F_q\) has degree \(2\) over \(\mathbb F_q\), and each monic irreducible quadratic has exactly two roots in \(\mathbb F_{q^2}\). Thus
\[
2N_2=q^2-q.
\]
:::

<1>4. Classes with one irreducible quadratic primary factor and one linear factor contribute
\[
(q-1)N_2=(q-1)\frac{q^2-q}{2}.
\]
::: {.proof}
Choose the monic irreducible quadratic in \(N_2\) ways and the nonzero linear eigenvalue in \(q-1\) ways. Since both primary components occur with multiplicity one, there is one rational canonical form for each such pair.
:::

<1>5. The number of monic irreducible cubic polynomials over \(\mathbb F_q\) is
\[
N_3=\frac{q^3-q}{3}.
\]
::: {.proof}
Because \(3\) is prime, the only proper subfield of \(\mathbb F_{q^3}\) containing \(\mathbb F_q\) is \(\mathbb F_q\). Hence the \(q^3-q\) elements of \(\mathbb F_{q^3}\setminus\mathbb F_q\) all have degree \(3\) over \(\mathbb F_q\). Each monic irreducible cubic has three roots in \(\mathbb F_{q^3}\), so
\[
3N_3=q^3-q.
\]
:::

<1>6. Classes with irreducible cubic characteristic polynomial contribute
\[
N_3=\frac{q^3-q}{3}.
\]
::: {.proof}
For an irreducible cubic \(\phi\), the only possible partition is \((1)\), so its companion matrix gives exactly one similarity class.
:::

<1>7. Summing all five disjoint types gives
\[
\begin{aligned}
k(\operatorname{GL}_3(\mathbb F_q))
&=\binom{q-1}{3}+2(q-1)(q-2)+3(q-1)\\
&\qquad +(q-1)\frac{q^2-q}{2}+\frac{q^3-q}{3}\\
&=q^3-q.
\end{aligned}
\]
::: {.proof}
The cases in <1>2, <1>4, and <1>6 exhaust the degree partitions \(3=1+1+1=1+2=3\), and within the split case <1>2 exhausts the possible multiplicity partitions. Direct simplification of the displayed sum gives \(q^3-q\).
:::
:::
