---
schema: qual/card@1
id: P-TGGYQ
kind: problem
title: $[\QQ(\sqrt{2}+\sqrt{3}):\QQ]$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
---

::: problem
Compute
\[
[\QQ(\sqrt2+\sqrt3):\QQ].
\]
:::

::: solution
Set
\[
\alpha=\sqrt2+\sqrt3.
\]
Since
\[
(\sqrt3+\sqrt2)(\sqrt3-\sqrt2)=1,
\]
we have
\[
\alpha^{-1}=\sqrt3-\sqrt2\in\QQ(\alpha).
\]
Therefore
\[
\sqrt3=\frac{\alpha+\alpha^{-1}}2,
\qquad
\sqrt2=\frac{\alpha-\alpha^{-1}}2,
\]
so
\[
\QQ(\alpha)=\QQ(\sqrt2,\sqrt3).
\]

Now
\[
[\QQ(\sqrt2):\QQ]=2,
\]
and $\sqrt3\notin\QQ(\sqrt2)$; otherwise writing $\sqrt3=a+b\sqrt2$ with $a,b\in\QQ$ and squaring would force $2ab=0$ and then either $3=a^2$ or $3=2b^2$, impossible in $\QQ$. Hence
\[
[\QQ(\sqrt2,\sqrt3):\QQ(\sqrt2)]=2.
\]
By the tower law,
\[
[\QQ(\sqrt2+\sqrt3):\QQ]=4.
\]

Indeed, $\alpha$ satisfies
\[
x^4-10x^2+1=0,
\]
which is therefore its minimal polynomial.
:::
