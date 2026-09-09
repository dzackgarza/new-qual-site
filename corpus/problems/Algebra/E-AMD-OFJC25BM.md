---
schema: qual/card@1
id: E-AMD-OFJC25BM
kind: problem
title: Intermediate fields of $\QQ(\sqrt{2},\sqrt{3})=\QQ(\sqrt{2}+\sqrt{3})$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
  note: Checked against the Qual Algebra extra-problems Galois computations list.
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
Compute all intermediate field extensions of $\QQ(\sqrt 2, \sqrt 3)$, show it is equal to $\QQ(\sqrt 2 + \sqrt 3)$, and find a corresponding minimal polynomial.
:::

::: {.solution}
<1>1. Let
\[
K=\mathbb Q(\sqrt2,\sqrt3).
\]
Then \([K:\mathbb Q]=4\).
::: {.proof}
We have \([\mathbb Q(\sqrt2):\mathbb Q]=2\). Also \(\sqrt3\notin\mathbb Q(\sqrt2)\): if \(\sqrt3=a+b\sqrt2\) with \(a,b\in\mathbb Q\), then squaring gives
\[
3=a^2+2b^2+2ab\sqrt2.
\]
Hence \(ab=0\). If \(b=0\), then \(\sqrt3\in\mathbb Q\), impossible; if \(a=0\), then \(3=2b^2\), so \(b^2=3/2\), impossible for \(b\in\mathbb Q\). Thus adjoining \(\sqrt3\) gives another quadratic extension, and the tower law yields degree \(4\).
:::

<1>2. The extension \(K/\mathbb Q\) is Galois with
\[
\operatorname{Gal}(K/\mathbb Q)\cong C_2\times C_2.
\]
::: {.proof}
The field \(K\) is the splitting field over \(\mathbb Q\) of \((x^2-2)(x^2-3)\), which is separable in characteristic \(0\). Its four automorphisms independently choose the signs of \(\sqrt2\) and \(\sqrt3\). Hence the Galois group is the Klein four group.
:::

<1>3. The complete list of intermediate fields is
\[
\mathbb Q,
\quad
\mathbb Q(\sqrt2),
\quad
\mathbb Q(\sqrt3),
\quad
\mathbb Q(\sqrt6),
\quad
K.
\]
::: {.proof}
By <1>2 and the fundamental theorem of Galois theory, intermediate fields correspond bijectively to subgroups of \(C_2\times C_2\). Besides the whole group and the trivial subgroup, there are exactly three subgroups of order \(2\). Their fixed fields are respectively the quadratic fields obtained by fixing \(\sqrt2\), fixing \(\sqrt3\), or fixing \(\sqrt6=\sqrt2\sqrt3\). Thus the three proper nontrivial intermediate fields are exactly the displayed ones.
:::

<1>4. If
\[
\alpha=\sqrt2+\sqrt3,
\]
then \(K=\mathbb Q(\alpha)\).
::: {.proof}
Clearly \(\alpha\in K\), so \(\mathbb Q(\alpha)\subseteq K\). Moreover
\[
\alpha^2=5+2\sqrt6,
\]
so \(\sqrt6=(\alpha^2-5)/2\in\mathbb Q(\alpha)\). Also
\[
(\sqrt3+\sqrt2)(\sqrt3-\sqrt2)=1,
\]
so \(\alpha^{-1}=\sqrt3-\sqrt2\). Therefore
\[
\sqrt3=\frac{\alpha+\alpha^{-1}}2,
\qquad
\sqrt2=\frac{\alpha-\alpha^{-1}}2,
\]
and both generators of \(K\) lie in \(\mathbb Q(\alpha)\). Hence equality holds.
:::

<1>5. The minimal polynomial of \(\alpha\) over \(\mathbb Q\) is
\[
m_\alpha(x)=x^4-10x^2+1.
\]
::: {.proof}
From \(\alpha^2=5+2\sqrt6\),
\[
(\alpha^2-5)^2=24,
\]
so
\[
\alpha^4-10\alpha^2+1=0.
\]
Thus \(\alpha\) is a root of \(x^4-10x^2+1\). By <1>1 and <1>4,
\[
[\mathbb Q(\alpha):\mathbb Q]=[K:\mathbb Q]=4.
\]
Hence the minimal polynomial has degree \(4\), so the displayed monic quartic that annihilates \(\alpha\) is exactly the minimal polynomial.
:::
:::
