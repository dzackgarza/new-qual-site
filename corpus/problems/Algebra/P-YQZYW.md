---
schema: qual/card@1
id: P-YQZYW
kind: problem
title: Intermediate fields of $\QQ(\sqrt{2},\sqrt{3})$ and $\QQ(\sqrt{2}+\sqrt{3})$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Polynomials
relations: []
review: draft
---

::: problem
Compute all intermediate fields of
\[
L=\QQ(\sqrt2,\sqrt3)/\QQ.
\]
Show that
\[
L=\QQ(\sqrt2+\sqrt3)
\]
and find the minimal polynomial of $\sqrt2+\sqrt3$ over $\QQ$.
:::

::: solution
The extension is biquadratic:
\[
[L:\QQ]=4,
\qquad
\operatorname{Gal}(L/\QQ)\cong C_2\times C_2.
\]
The three subgroups of order $2$ correspond to the three quadratic intermediate fields
\[
\QQ(\sqrt2),
\qquad
\QQ(\sqrt3),
\qquad
\QQ(\sqrt6).
\]
Together with $\QQ$ and $L$, these are all intermediate fields.

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
\alpha^{-1}=\sqrt3-\sqrt2.
\]
Therefore
\[
\sqrt3=\frac{\alpha+\alpha^{-1}}2,
\qquad
\sqrt2=\frac{\alpha-\alpha^{-1}}2,
\]
so
\[
\QQ(\alpha)=\QQ(\sqrt2,\sqrt3)=L.
\]

Now
\[
\alpha^2=5+2\sqrt6,
\]
so
\[
(\alpha^2-5)^2=24.
\]
Hence
\[
\alpha^4-10\alpha^2+1=0.
\]
Thus $\alpha$ is a root of
\[
f(x)=x^4-10x^2+1.
\]
Because $\QQ(\alpha)=L$ has degree $4$ over $\QQ$, this degree-$4$ polynomial is the minimal polynomial.
:::
