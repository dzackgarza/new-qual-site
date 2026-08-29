---
schema: qual/card@1
id: P-XYYHG
kind: problem
title: Automorphisms of the upper half plane
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Question 2.1. Determine all holomorphic automorphisms of the upper half plane $u =$ $\lbrace z : I m z > 0 \rbrace$

::: {.solution}
<1>1. The holomorphic automorphisms of the upper half plane $\HH = \{z : \Im z > 0\}$ are exactly the maps
$$z \mapsto \frac{az + b}{cz + d},\qquad a,b,c,d \in \RR,\ ad - bc = 1,$$
i.e. the group $\operatorname{PSL}_2(\RR)$.
Proof: standard classification of automorphisms of $\HH$.

<1>2. Derivation.
<2>1. The Cayley transform $\phi(z) = \frac{z - i}{z + i}$ maps $\HH$ biholomorphically onto the unit disk $\DD$.
Proof: $\phi$ is a Möbius map sending the real axis to the unit circle and $i$ to $0$.
<2>2. The automorphisms of $\DD$ are $w \mapsto e^{i\theta}\frac{w - a}{1 - \overline{a}w}$ with $|a| < 1$, $\theta \in \RR$.
Proof: Schwarz lemma (standard classification of disk automorphisms).
<2>3. Conjugating <2>2 by $\phi$ gives the automorphisms of $\HH$.
Proof: $\operatorname{Aut}(\HH) = \phi^{-1} \operatorname{Aut}(\DD) \phi$.
<2>4. This conjugation yields exactly the maps $z \mapsto \frac{az+b}{cz+d}$ with $a,b,c,d \in \RR$ and $ad - bc = 1$.
Proof: a direct computation; the condition that the real axis maps to itself forces the coefficients to be real (up to a common real scalar).

<1>3. Q.E.D.
Proof: <1>1 and <1>2.
:::
