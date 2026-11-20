---
schema: qual/card@1
id: C-Q6BSL
kind: corollary
title: Residue of $g/h$ at a simple zero of $h$
slogan: 'At a simple zero of the denominator, the residue is numerator over derivative: $g(z_0)/h''(z_0)$.'
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
In particular, $\Res_{z=z_0}\frac{1}{h(z)}=\frac{1}{h'(z_0)}$.

This is the simple-pole rule of [@Ahl73, ch. 4, §5.1, The Residue Theorem], that the residue at a simple pole $\alpha$ equals the value of $(z-\alpha)f(z)$ at $z=\alpha$: for $f=g/h$ with $h(z_0)=0$, $h'(z_0)\neq0$, that value is $\lim_{z\to z_0}(z-z_0)g(z)/h(z)=g(z_0)/h'(z_0)$, because $h(z)=(z-z_0)h'(z_0)+O\qty{(z-z_0)^2}$. The section's worked example $\frac{e^z}{(z-a)(z-b)}$, whose residue at $a$ it gives as $e^a/(a-b)$, is the case $g=e^z$ and $h=(z-a)(z-b)$.
:::
