---
schema: qual/card@1
id: P-4DRTY
kind: problem
title: Normal closure and Galois theory of $\QQ(\sqrt[3]{21})$
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Galois Theory
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Is $\mathbb{Q}(\sqrt[3]{21})$ normal?
What is its splitting field?
What is its Galois group?
Describe the lattice of subfields.
:::

::: solution
Let $\alpha=\sqrt[3]{21}$ and let $\omega$ be a primitive cube root of unity. The polynomial
\[
f(x)=x^3-21
\]
is irreducible over $\mathbb Q$ by Eisenstein at $3$ (or $7$). Its roots are $\alpha,\omega\alpha,\omega^2\alpha$.

Since $\mathbb Q(\alpha)\subset\mathbb R$, it contains only the real root, so it is not normal over $\mathbb Q$. The splitting field is
\[
K=\mathbb Q(\alpha,\omega)=\mathbb Q(\alpha,\sqrt{-3}).
\]
Now $[\mathbb Q(\alpha):\mathbb Q]=3$ and $\omega\notin\mathbb R$, so $[K:\mathbb Q(\alpha)]=2$; hence $[K:\mathbb Q]=6$.

The discriminant of $x^3-21$ is
\[
-27\cdot 21^2,
\]
which is not a square in $\mathbb Q$. Therefore the Galois group of the irreducible cubic is
\[
\operatorname{Gal}(K/\mathbb Q)\cong S_3.
\]
One may take generators
\[
\sigma(\alpha)=\omega\alpha,\quad \sigma(\omega)=\omega,
\qquad
\tau(\alpha)=\alpha,\quad \tau(\omega)=\omega^2,
\]
with $\sigma^3=\tau^2=1$ and $\tau\sigma\tau=\sigma^{-1}$.

By Galois correspondence, the intermediate fields are:
\[
\mathbb Q,
\quad \mathbb Q(\omega),
\quad \mathbb Q(\alpha),\quad \mathbb Q(\omega\alpha),\quad \mathbb Q(\omega^2\alpha),
\quad K.
\]
The quadratic field $\mathbb Q(\omega)=\mathbb Q(\sqrt{-3})$ corresponds to $A_3$, and the three cubic fields correspond to the three subgroups of order $2$ in $S_3$.
:::
