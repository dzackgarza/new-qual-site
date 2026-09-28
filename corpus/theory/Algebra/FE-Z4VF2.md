---
schema: qual/card@1
id: FE-Z4VF2
kind: example
title: $\QQ(\sqrt[3]{2})/\QQ$ is not Galois
prompts:
- Give a field extension that is not Galois.
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Counterexamples
relations: []
review: draft
---

::: {.example}
Let $\sqrt[3]{2}\in\RR$ be the real cube root of $2$.
The extension $\QQ(\sqrt[3]{2})/\QQ$ has degree $3$ and trivial automorphism group, so it is not [[D-5JYEI|Galois]].

The polynomial $x^3-2$ is irreducible over $\QQ$ by [[FT-2P5VV|Eisenstein's criterion]] at $p=2$, so $[\QQ(\sqrt[3]{2}):\QQ]=3$.
An automorphism $\sigma$ of $\QQ(\sqrt[3]{2})$ fixing $\QQ$ sends $\sqrt[3]{2}$ to a root of $x^3-2$ lying in $\QQ(\sqrt[3]{2})\subseteq\RR$.
The only real root of $x^3-2$ is $\sqrt[3]{2}$, so $\sigma=\id$.
Hence $\abs{\Aut(\QQ(\sqrt[3]{2})/\QQ)}=1\ne3$, and $\QQ(\sqrt[3]{2})/\QQ$ is not Galois by [[FT-3WWKN]].
:::
