---
schema: qual/card@1
id: PR-TLBPS
kind: proposition
title: The derivative detects separability for irreducible polynomials
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Polynomials
  - Characteristic
relations: []
review: draft
---

:::{.proposition title="The derivative detects separability for irreducible polynomials"}
\envlist

- For any field $k$ and any $f\in k[x]$, $f$ is separable $\iff \gcd(f, f') = 1$.
- For $f$ **irreducible**, this simplifies to $f$ separable $\iff f'\not\equiv 0 \in k[x]$.
  Irreducibility is needed: $f(x) = x^2(x-1)$ over $\QQ$ has $f'\not\equiv 0$ and a repeated root.
- For $\ch k = 0$, irreducible implies separable.
- For $\ch k = p$, irreducibles $f(x)$ are inseparable iff $f(x) = g(x^p)$ for some $g\in k[x]$.


Thus for an irreducible polynomial $f$,
\[
f\text{ separable} \iff \gcd(f, f')=1 \iff f'\not\equiv 0 \iff_{\ch k = p} f(x) \neq g(x^p) \text{ for every } g
.\]
:::
