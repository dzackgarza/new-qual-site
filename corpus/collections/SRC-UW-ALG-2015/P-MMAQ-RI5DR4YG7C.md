---
schema: qual/card@1
id: P-MMAQ-RI5DR4YG7C
kind: problem
title: Minimal polynomial of $\sqrt{2}+\sqrt{3}$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Find the minimal polynomial of $\sqrt2+\sqrt3$ over $\mathbb Q$.
Justify your answer.
:::


::: solution
<1>1. Let
\[
\alpha=\sqrt2+\sqrt3.
\]
Then \(\alpha\) is a root of
\[
f(x)=x^4-10x^2+1.
\]
::: {.proof}
We have
\[
\alpha^2=5+2\sqrt6,
\]
so
\[
\alpha^2-5=2\sqrt6.
\]
Squaring gives
\[
(\alpha^2-5)^2=24,
\]
hence
\[
\alpha^4-10\alpha^2+1=0.
\]
:::

<1>2. The field \(\mathbb Q(\alpha)\) contains both \(\sqrt2\) and \(\sqrt3\).
::: {.proof}
Since
\[
(\sqrt2+\sqrt3)(\sqrt3-\sqrt2)=1,
\]
we have
\[
\alpha^{-1}=\sqrt3-\sqrt2\in\mathbb Q(\alpha).
\]
Therefore
\[
\sqrt3=\frac{\alpha+\alpha^{-1}}2,
\qquad
\sqrt2=\frac{\alpha-\alpha^{-1}}2.
\]
Thus \(\mathbb Q(\sqrt2,\sqrt3)\subseteq\mathbb Q(\alpha)\), while the reverse inclusion is immediate from the definition of \(\alpha\).
:::

<1>3. We have
\[
[\mathbb Q(\alpha):\mathbb Q]=4.
\]
::: {.proof}
By <1>2,
\[
\mathbb Q(\alpha)=\mathbb Q(\sqrt2,\sqrt3).
\]
Now \([\mathbb Q(\sqrt2):\mathbb Q]=2\), and \(\sqrt3\notin\mathbb Q(\sqrt2)\). Indeed, if \(\sqrt3=a+b\sqrt2\) with \(a,b\in\mathbb Q\), squaring gives
\[
3=a^2+2b^2+2ab\sqrt2,
\]
so \(ab=0\); either case is impossible. Hence adjoining \(\sqrt3\) gives another quadratic extension, and the total degree is \(4\).
:::

<1>4. Therefore the minimal polynomial of \(\sqrt2+\sqrt3\) over \(\mathbb Q\) is
\[
\boxed{x^4-10x^2+1}.
\]
::: {.proof}
The polynomial in <1>1 is monic of degree \(4\) and annihilates \(\alpha\). By <1>3, the minimal polynomial of \(\alpha\) has degree \(4\), so it must equal this polynomial.
:::
:::
