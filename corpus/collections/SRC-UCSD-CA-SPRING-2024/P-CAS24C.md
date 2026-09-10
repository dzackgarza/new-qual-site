---
schema: qual/card@1
id: P-CAS24C
kind: problem
title: Schwarz–Pick type bound for positive real part on the disc
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
---

::: problem
Let $f : \mathbb{D} \to \mathbb{C}$ be holomorphic.
Assume $\operatorname{Re} f(z) > 0$ for all $z \in \mathbb{D}$.
Show that
\[
|f'(0)| \le 2\operatorname{Re} f(0).
\]
:::

::: solution
Let $a=f(0)$, so $\operatorname{Re}a>0$. The Möbius map
\[
\Phi(w)=\frac{w-a}{w+\overline a}
\]
maps the right half-plane to the unit disk and sends $a$ to $0$. Hence
\[
g=\Phi\circ f:\mathbb D\to\mathbb D
\]
is holomorphic and $g(0)=0$. Schwarz's lemma yields $|g'(0)|\le1$.
Since
\[
\Phi'(a)=\frac1{a+\overline a}
=\frac1{2\operatorname{Re}a},
\]
we get
\[
\frac{|f'(0)|}{2\operatorname{Re}f(0)}
=|g'(0)|\le1.
\]
Therefore
\[
\boxed{|f'(0)|\le2\operatorname{Re}f(0).}
\]
:::
