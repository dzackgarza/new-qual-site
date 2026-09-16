---
schema: qual/card@1
id: C-Q6BSL
kind: corollary
title: Residue of $g/h$ at a simple zero of $h$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Poles
relations: []
review: draft
---

::: {.corollary}
Let $g$ and $h$ be [[D-E7A5W|holomorphic]] near $z_0$, with $h(z_0)=0$ and $h'(z_0)\neq0$.
Then
$$
\Res_{z=z_0}\frac{g(z)}{h(z)}=\frac{g(z_0)}{h'(z_0)}.
$$
:::

::: {.proof}
Write $h(z)=(z-z_0)h_1(z)$ with $h_1$ holomorphic near $z_0$ and $h_1(z_0)=h'(z_0)\neq0$.
Then $g/h$ has at most a simple [[D-AUD6K|pole]] at $z_0$, and its [[D-C3JIU|residue]] is $\lim_{z\to z_0}(z-z_0)\frac{g(z)}{h(z)}=\frac{g(z_0)}{h_1(z_0)}=\frac{g(z_0)}{h'(z_0)}$.
:::
