---
schema: qual/card@1
id: P-3UTDH
kind: problem
title: Galois theory of $x^3-11$ and $11^{1/3}+\sqrt{2}$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $E\subset \CC$ denote the splitting field over $\QQ$ of the polynomial $x^3 - 11$.

a.
Prove that if $n>1$ is a squarefree positive integer, then $\sqrt{n}\not\in E$.

  > Hint: you can describe all quadratic extensions of $\QQ$ contained in $E$.

b.
Find the Galois group of $(x^3 - 11)(x^2 - 2)$ over $\QQ$.

c.
Prove that the minimal polynomial of $11^{1/3} + 2^{1/2}$ over $\QQ$ has degree 6.
:::

::: {.solution}
Let $a=11^{1/3}$ and let $\omega$ be a primitive cube root of unity. Then
\[
E=\mathbb Q(a,\omega).
\]
The polynomial $x^3-11$ is Eisenstein at $11$, so $[\mathbb Q(a):\mathbb Q]=3$. Since $\mathbb Q(a)\subset\mathbb R$ while $\omega\notin\mathbb R$, adjoining $\omega$ doubles the degree. Hence
\[
[E:\mathbb Q]=6,
\qquad
\operatorname{Gal}(E/\mathbb Q)\cong S_3.
\]
The unique subgroup of index $2$ in $S_3$ is $A_3$, so $E$ has a unique quadratic subfield. It is
\[
\mathbb Q(\omega)=\mathbb Q(\sqrt{-3}).
\]

For (a), let $n>1$ be squarefree and positive. Then $\mathbb Q(\sqrt n)$ is a real quadratic field, so it cannot equal the unique quadratic subfield $\mathbb Q(\sqrt{-3})$. Therefore $\sqrt n\notin E$.

For (b), the splitting field of
\[
(x^3-11)(x^2-2)
\]
is $E(\sqrt2)$. By part (a), $\sqrt2\notin E$, so
\[
[E(\sqrt2):E]=2
\]
and the total degree is $12$. Moreover
\[
E\cap\mathbb Q(\sqrt2)=\mathbb Q,
\]
because the intersection is either $\mathbb Q$ or the quadratic field $\mathbb Q(\sqrt2)$, and the latter is not contained in $E$. Both extensions are Galois, so restriction gives
\[
\operatorname{Gal}(E(\sqrt2)/\mathbb Q)
\cong S_3\times C_2.
\]

For (c), put
\[
\theta=a+\sqrt2.
\]
Since $[\mathbb Q(a):\mathbb Q]=3$, the field $\mathbb Q(a)$ cannot contain the quadratic field $\mathbb Q(\sqrt2)$; hence
\[
[\mathbb Q(a,\sqrt2):\mathbb Q]=6.
\]
It remains to show that $\theta$ generates this compositum. From $(\theta-\sqrt2)^3=11$ we obtain
\[
\theta^3-3\theta^2\sqrt2+6\theta-2\sqrt2=11,
\]
so
\[
\sqrt2=\frac{\theta^3+6\theta-11}{3\theta^2+2}.
\]
The denominator is nonzero because $\theta$ is real. Thus $\sqrt2\in\mathbb Q(\theta)$, and then $a=\theta-\sqrt2\in\mathbb Q(\theta)$. Therefore
\[
\mathbb Q(\theta)=\mathbb Q(a,\sqrt2)
\]
and the minimal polynomial of $\theta$ over $\mathbb Q$ has degree $6$.
:::
