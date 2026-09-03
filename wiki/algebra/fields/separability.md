---
title: Separability
order: 30
problems:
  topics:
  - Separability
---

# Separability

The hypothesis that is automatic in characteristic zero and over finite fields, and therefore the one a problem is testing whenever it is stated in characteristic $p$.

[[D-ZT46D]]

[[D-JGYLA]]

[[FD-6WSIA]] [[FD-OUWGL]]

[[PR-ENHVC]]

[[PR-OMKPN]]

[[PR-TLBPS]]

[[C-C2GYX]]

::: {.remark title="The derivative test"}
$f$ is separable exactly when $\gcd(f, f') = 1$, which is a computation rather than a search for roots.
In characteristic $p$ this is how inseparability appears: $f' = 0$ identically when $f$ is a polynomial in $x^p$, and then every root is repeated.
The canonical inseparable extension is $\FF_p(t^{1/p})/\FF_p(t)$, where $x^p - t = (x - t^{1/p})^p$.
:::

## Permanence and the Galois condition

For finite extensions, separability is the condition that the embedding count has the expected size: no degree is lost to repeated roots.
Over a perfect base field it is automatic for algebraic extensions, which is why characteristic zero and finite fields usually let a Galois problem focus on normality.
Separability is also stable through towers and composita, so once the pieces of a construction are separable the combined extension remains in the separable regime.

[[PR-3VQBI]]

[[PR-ZCKLJ]]

[[PR-MK2W6]]

[[PR-25FLW]]

[[PR-XB3O7]]

[[D-WB4M5]]

[[PR-YCTNC]]

[[PR-KFQJG]]

A finite extension is Galois when normality and separability hold together.
In practice, constructing an extension as a splitting field supplies normality; the derivative/perfect-field tests above supply separability.
Keeping those two checks separate prevents the common mistake of treating "splitting field" alone as a synonym for "Galois" in positive characteristic.
