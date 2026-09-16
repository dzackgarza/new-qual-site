---
schema: qual/card@1
id: P-MMAQ-6DSHSTLKLP
kind: problem
title: Galois groups of $x^4+4x^2+1$ and $x^4+4x^2-5$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Determine the Galois groups of the following polynomials over $\mathbb Q$.

- $f(x)=x^4+4x^2+1$

- $f(x)=x^4+4x^2-5$.
:::


::: {.solution}
<1>1. For
\[
f_1(x)=x^4+4x^2+1,
\]
let \(\alpha\) satisfy
\[
\alpha^2=-2+\sqrt3.
\]
Then the four roots of \(f_1\) are
\[
\pm\alpha,\qquad \pm\alpha^{-1}.
\]
::: {.proof}
Solving the quadratic equation in \(y=x^2\) gives
\[
y^2+4y+1=0,
\qquad
y=-2\pm\sqrt3.
\]
Since
\[
(-2+\sqrt3)(-2-\sqrt3)=1,
\]
we have
\[
\alpha^{-2}=-2-\sqrt3.
\]
Thus the square roots of the two values of \(y\) are exactly
\(\pm\alpha\) and \(\pm\alpha^{-1}\).
:::

<1>2. The splitting field of \(f_1\) is
\[
K_1=\mathbb Q(\alpha),
\qquad [K_1:\mathbb Q]=4.
\]
::: {.proof}
By <1>1, \(\mathbb Q(\alpha)\) already contains every root, so it is the splitting field. Moreover
\[
\sqrt3=\alpha^2+2\in\mathbb Q(\alpha),
\]
so
\[
\mathbb Q\subset \mathbb Q(\sqrt3)\subset \mathbb Q(\alpha).
\]
The first extension has degree \(2\). The element \(-2+\sqrt3\) is not a square in the real quadratic field \(\mathbb Q(\sqrt3)\): under the identity real embedding it is negative, whereas a square is nonnegative. Hence
\[
[\mathbb Q(\alpha):\mathbb Q(\sqrt3)]=2.
\]
Therefore \([K_1:\mathbb Q]=4\).
:::

<1>3. We have
\[
\operatorname{Gal}(K_1/\mathbb Q)\cong C_2\times C_2.
\]
::: {.proof}
Since \(K_1\) is the splitting field of a separable polynomial over \(\mathbb Q\), it is Galois of degree \(4\). Two nontrivial automorphisms are determined by
\[
\tau(\alpha)=-\alpha,
\qquad
\sigma(\alpha)=\alpha^{-1}.
\]
Both have order \(2\), and they commute because
\[
\sigma\tau(\alpha)=(-\alpha)^{-1}=-\alpha^{-1}
=\tau\sigma(\alpha).
\]
Thus the Galois group contains three nontrivial involutions and is therefore the Klein four group, not the cyclic group of order \(4\).
:::

<1>4. For
\[
f_2(x)=x^4+4x^2-5,
\]
we have
\[
f_2(x)=(x^2-1)(x^2+5).
\]
Hence its splitting field is
\[
K_2=\mathbb Q(\sqrt{-5}).
\]
::: {.proof}
The factorization is immediate:
\[
(x^2-1)(x^2+5)=x^4+4x^2-5.
\]
The roots are \(\pm1\) and \(\pm\sqrt{-5}\), so adjoining \(\sqrt{-5}\) gives all roots.
:::

<1>5. Therefore
\[
\operatorname{Gal}(K_2/\mathbb Q)\cong C_2.
\]
::: {.proof}
Since \(-5\) is not a square in \(\mathbb Q\), \([K_2:\mathbb Q]=2\). Every quadratic extension in characteristic \(0\) is Galois, with nontrivial automorphism
\[
\sqrt{-5}\longmapsto-\sqrt{-5}.
\]
:::
:::
