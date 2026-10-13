---
schema: qual/card@1
id: P-UCLARA15F-04
kind: problem
title: Completeness of orthonormal systems close to an orthonormal basis
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
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2015 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 4 on page 1 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $\mathcal{H}$ be a separable infinite-dimensional Hilbert space and assume that $(e_n)$ is an orthonormal system in $\mathcal{H}$. Let $(f_n)$ be another orthonormal system which is complete, i.e. the closure of the span of the $(f_n)$ is all of $\mathcal{H}$.

(a) Show that if $\sum_{n=1}^{\infty} \|f_n - e_n\|^2 < 1$ then the orthonormal system $(e_n)$ is also complete.

(b) Assume that we only have $\sum_{n=1}^{\infty} \|f_n - e_n\|^2 < \infty$. Prove that it is still true that $(e_n)$ is complete.
:::

::: {.solution}
Let
\[
F:\ell^2(\mathbb N)\to\mathcal H,
\qquad
F(a_1,a_2,\dots)
=
\sum_{n=1}^\infty a_n f_n,
\]
and
\[
E:\ell^2(\mathbb N)\to\mathcal H,
\qquad
E(a_1,a_2,\dots)
=
\sum_{n=1}^\infty a_n e_n.
\]

Because \((f_n)\) is a complete orthonormal system, \(F\) is unitary. Because
\((e_n)\) is orthonormal, \(E\) is an isometry onto the closed subspace
\[
\overline{\operatorname{span}}\{e_n:n\ge1\}.
\]

## Part (a)

Assume
\[
\sum_{n=1}^\infty \|f_n-e_n\|^2<1.
\]

<1>1. Suppose, toward a contradiction, that \((e_n)\) is not complete.

::: {.proof}
Then its closed linear span is a proper closed subspace of \(\mathcal H\).
:::

<1>2. There exists a unit vector
\[
x\in\mathcal H
\]
such that
\[
\boxed{\langle x,e_n\rangle=0}
\]
for every \(n\).

::: {.proof}
Take a nonzero vector in the orthogonal complement of
\[
\overline{\operatorname{span}}\{e_n\}
\]
and normalize it.
:::

<1>3. Since \((f_n)\) is a complete orthonormal system, Parseval's identity gives
\[
\boxed{
1=\|x\|^2
=
\sum_{n=1}^\infty
|\langle x,f_n\rangle|^2}.
\]

::: {.proof}
Apply Parseval to the orthonormal basis \((f_n)\).
:::

<1>4. For every \(n\),
\[
\langle x,f_n\rangle
=
\langle x,f_n-e_n\rangle.
\]

::: {.proof}
By step <1>2,
\[
\langle x,e_n\rangle=0.
\]
:::

<1>5. Hence
\[
|\langle x,f_n\rangle|
\le
\|x\|\,
\|f_n-e_n\|
=
\|f_n-e_n\|.
\]

::: {.proof}
Use step <1>4, Cauchy--Schwarz, and \(\|x\|=1\).
:::

<1>6. Therefore
\[
1
=
\sum_{n=1}^\infty
|\langle x,f_n\rangle|^2
\le
\sum_{n=1}^\infty
\|f_n-e_n\|^2
<1.
\]

::: {.proof}
Use steps <1>3 and <1>5 and the hypothesis.
:::

<1>7. This contradiction shows that
\[
\boxed{(e_n)\text{ is complete}.}
\]

::: {.proof}
The assumption in step <1>1 is impossible.
:::

## Part (b)

Assume now only that
\[
\sum_{n=1}^\infty
\|f_n-e_n\|^2
<
\infty.
\]

<1>8. The operator
\[
K=E-F:\ell^2\to\mathcal H
\]
is Hilbert--Schmidt.

::: {.proof}
Let \((\delta_n)\) be the standard orthonormal basis of \(\ell^2\). Then
\[
K\delta_n
=
e_n-f_n.
\]
Therefore
\[
\sum_{n=1}^\infty
\|K\delta_n\|^2
=
\sum_{n=1}^\infty
\|e_n-f_n\|^2
<
\infty.
\]
This is exactly the Hilbert--Schmidt condition.
:::

<1>9. Hence \(K\) is compact.

::: {.proof}
Every Hilbert--Schmidt operator between Hilbert spaces is compact.
:::

<1>10. Define
\[
A=F^{-1}E:\ell^2\to\ell^2.
\]
Then
\[
\boxed{
A-I=F^{-1}(E-F)}
\]
is compact.

::: {.proof}
Since \(F\) is unitary,
\[
A-I
=
F^{-1}E-F^{-1}F
=
F^{-1}(E-F).
\]
The operator \(E-F\) is compact by step <1>9, and composition with the bounded operator \(F^{-1}\) preserves compactness.
:::

<1>11. The operator \(A\) is an isometry.

::: {.proof}
For \(u\in\ell^2\),
\[
\|Au\|
=
\|F^{-1}Eu\|
=
\|Eu\|
=
\|u\|,
\]
because \(F^{-1}\) is unitary and \(E\) is an isometry.
:::

<1>12. Hence
\[
\boxed{\ker A=\{0\}}
\]
and
\[
\boxed{\operatorname{ran}A\text{ is closed}.}
\]

::: {.proof}
An isometry is injective. Also, if \(Au_j\) converges, then
\[
\|u_j-u_k\|
=
\|Au_j-Au_k\|,
\]
so \((u_j)\) is Cauchy and converges to some \(u\), giving
\[
Au_j\to Au.
\]
Thus the range is closed.
:::

<1>13. Since \(A=I+\text{compact}\), \(A\) is Fredholm of index \(0\).

::: {.proof}
The identity operator is Fredholm with index \(0\), and compact perturbations preserve Fredholmness and the Fredholm index.
:::

<1>14. Therefore
\[
\dim\ker A
-
\operatorname{codim}\operatorname{ran}A
=
0.
\]

::: {.proof}
This is the definition of the Fredholm index, using step <1>13.
:::

<1>15. Since \(\ker A=\{0\}\),
\[
\boxed{
\operatorname{codim}\operatorname{ran}A=0}.
\]

::: {.proof}
Substitute
\[
\dim\ker A=0
\]
from step <1>12 into the index formula in step <1>14.
:::

<1>16. Because \(\operatorname{ran}A\) is closed and has codimension \(0\),
\[
\boxed{\operatorname{ran}A=\ell^2}.
\]

::: {.proof}
A closed subspace of codimension \(0\) is the whole Hilbert space.
:::

<1>17. Hence \(A\) is unitary.

::: {.proof}
By step <1>11, \(A\) is an isometry, and by step <1>16 it is surjective.
:::

<1>18. Therefore
\[
E=FA
\]
is surjective onto \(\mathcal H\).

::: {.proof}
Both \(F\) and \(A\) are surjective by completeness of \((f_n)\) and step <1>17.
:::

<1>19. Thus
\[
\boxed{
\overline{\operatorname{span}}\{e_n:n\ge1\}
=
\mathcal H}.
\]

::: {.proof}
The range of the synthesis isometry \(E\) is precisely the closed span of the orthonormal system \((e_n)\). Step <1>18 says this range is all of \(\mathcal H\).
:::

<1>20. Therefore \((e_n)\) is complete.

::: {.proof}
This is exactly step <1>19.
:::

<1>21. Q.E.D.

::: {.proof}
Step <1>7 proves part (a), and step <1>20 proves part (b).
:::
:::
