---
schema: qual/card@1
id: PR-TLBPS
kind: proposition
title: "Derivative completely detects separability"
classification:
  areas:
  - algebra
  topics:
  - separability
  - polynomials
  - characteristic
relations: []
review: draft
---
:::{.proposition title="Derivative completely detects separability"}
\envlist

- For any field $k$, $f\in k[x]$ is separable $\iff f'\not\equiv 0 \in k[x]$.
- For $\ch k = 0$, irreducible implies separable.
- For $\ch k = p$, irreducibles $f(x)$ are inseparable iff $f(x) = g(x^p)$ for some $g\in k[x]$.


Thus for an irreducible polynomial $f$,
\[
f\text{ separable} \iff \gcd(f, f')=1 \iff f'\not\equiv 0 \iff_{\ch k = p} f(x) = g(x^p)
.\]
:::
