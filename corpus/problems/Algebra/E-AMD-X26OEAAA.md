---
schema: qual/card@1
id: E-AMD-X26OEAAA
kind: problem
title: $[\QQ(\sqrt{2}+\sqrt{3}):\QQ]=4$ and $\QQ(\sqrt{2}+\sqrt{3})=\QQ(\sqrt{2}-\sqrt{3})=\QQ(\sqrt{2},\sqrt{3})$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Recovered both square roots from the primitive element and computed the degree by the tower law.
---

::: {.exercise}
(1) Prove that
\[
\mathbb Q(\sqrt2+\sqrt3)=\mathbb Q(\sqrt2-\sqrt3)=\mathbb Q(\sqrt2,\sqrt3).
\]
(2) Prove that this extension has degree $4$ over $\mathbb Q$.
:::

::: {.solution}
Set
\[
\alpha=\sqrt2+\sqrt3.
\]
Since
\[
\alpha^{-1}=\sqrt3-\sqrt2,
\]
we have
\[
\sqrt2-\sqrt3=-\alpha^{-1}\in\mathbb Q(\alpha).
\]
Therefore
\[
\sqrt2=\frac{\alpha-\alpha^{-1}}2,
\qquad
\sqrt3=\frac{\alpha+\alpha^{-1}}2
\]
belong to $\mathbb Q(\alpha)$. The reverse inclusion is immediate, so
\[
\mathbb Q(\alpha)=\mathbb Q(\sqrt2,\sqrt3)=\mathbb Q(\sqrt2-\sqrt3).
\]

Now $[\mathbb Q(\sqrt2):\mathbb Q]=2$. Also $\sqrt3\notin\mathbb Q(\sqrt2)$: if
\[
\sqrt3=a+b\sqrt2\qquad(a,b\in\mathbb Q),
\]
then squaring gives
\[
3=a^2+2b^2+2ab\sqrt2.
\]
If $ab\ne0$, this would make $\sqrt2$ rational; if $a=0$ or $b=0$, it would force respectively $b^2=3/2$ or $a^2=3$, impossible in $\mathbb Q$. Hence
\[
[\mathbb Q(\sqrt2,\sqrt3):\mathbb Q(\sqrt2)]=2.
\]
By the tower law,
\[
[\mathbb Q(\alpha):\mathbb Q]=4.
\]
Equivalently, $\alpha$ has minimal polynomial
\[
x^4-10x^2+1.
\]
:::
