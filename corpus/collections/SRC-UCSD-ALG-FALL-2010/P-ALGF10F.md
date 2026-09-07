---
schema: qual/card@1
id: P-ALGF10F
kind: problem
title: "Splitting fields and degrees of x^6 + 1 and x^6 - 1 over Q"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 6 of the official UCSD Algebra Qualifying Examination, Fall 2010; both polynomials and the requested splitting-field degrees agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the cyclotomic descriptions Q(zeta_6) and Q(zeta_12), their explicit quadratic generators, and degrees 2 and 4.
---

::: {.problem}
Explicitly determine the splitting fields over the rationals of the following two polynomials and their degrees over $\mathbb{Q}$:

(a) $x^6 + 1$

(b) $x^6 - 1$
:::


::: {.solution}
<1>1. The splitting field of \(x^6-1\) is
\[
\mathbb Q(\zeta_6)=\mathbb Q(\sqrt{-3}),
\]
and it has degree \(2\) over \(\mathbb Q\).
::: {.proof}
The roots of \(x^6-1\) are exactly the sixth roots of unity
\[
1,\zeta_6,\zeta_6^2,\ldots,\zeta_6^5,
\]
where \(\zeta_6=e^{2\pi i/6}\).
Thus the splitting field is \(\mathbb Q(\zeta_6)\).
Since
\[
\zeta_6=\frac{1+\sqrt{-3}}2,
\]
we have
\[
\mathbb Q(\zeta_6)=\mathbb Q(\sqrt{-3}).
\]
The element \(\sqrt{-3}\notin\mathbb Q\), so
\[
[\mathbb Q(\zeta_6):\mathbb Q]=2.
\]
Equivalently, this degree is \(\varphi(6)=2\).
:::

<1>2. The roots of \(x^6+1\) are twelfth roots of unity, and a primitive twelfth root occurs among them.
::: {.proof}
If \(z^6=-1\), then
\[
z^{12}=1.
\]
Thus every root is a twelfth root of unity.
Conversely, if \(\zeta_{12}=e^{2\pi i/12}\), then
\[
\zeta_{12}^6=-1,
\]
so \(\zeta_{12}\) itself is a root of \(x^6+1\).
The six roots are
\[
\zeta_{12}^{1},\zeta_{12}^{3},\zeta_{12}^{5},
\zeta_{12}^{7},\zeta_{12}^{9},\zeta_{12}^{11}.
\]
Therefore the splitting field is
\[
\mathbb Q(\zeta_{12}).
\]
:::

<1>3. One has
\[
\mathbb Q(\zeta_{12})=\mathbb Q(i,\sqrt3)
\]
and
\[
[\mathbb Q(\zeta_{12}):\mathbb Q]=4.
\]
::: {.proof}
Using
\[
\zeta_{12}=e^{\pi i/6}=\frac{\sqrt3+i}{2},
\]
we get
\[
\zeta_{12}\in\mathbb Q(i,\sqrt3).
\]
Conversely,
\[
i=\zeta_{12}^3
\]
and
\[
\sqrt3=2\zeta_{12}-i,
\]
so \(i,\sqrt3\in\mathbb Q(\zeta_{12})\).
Hence the two fields are equal.

Now \([\mathbb Q(i):\mathbb Q]=2\), while \(\sqrt3\notin\mathbb Q(i)\): if \(\sqrt3=a+bi\) with \(a,b\in\mathbb Q\), comparison with its complex conjugate gives \(b=0\), contradicting \(\sqrt3\notin\mathbb Q\).
Thus
\[
[\mathbb Q(i,\sqrt3):\mathbb Q]=4.
\]
Equivalently, this is \(\varphi(12)=4\).
:::

<1>4. Therefore the requested splitting fields and degrees are
\[
\operatorname{Spl}_{\mathbb Q}(x^6-1)=\mathbb Q(\sqrt{-3}),
\qquad [\operatorname{Spl}:\mathbb Q]=2,
\]
and
\[
\operatorname{Spl}_{\mathbb Q}(x^6+1)=\mathbb Q(i,\sqrt3),
\qquad [\operatorname{Spl}:\mathbb Q]=4.
\]
::: {.proof}
This is the combination of <1>1 and <1>3.
:::
:::
