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
::: {.proof}
standard classification of automorphisms of $\HH$.
:::

<1>2. Derivation.
<2>1. The Cayley transform $\phi(z) = \frac{z - i}{z + i}$ maps $\HH$ biholomorphically onto the unit disk $\DD$.
::: {.proof}
$\phi$ is a Möbius map sending the real axis to the unit circle and $i$ to $0$.
:::
<2>2. The automorphisms of $\DD$ are $w \mapsto e^{i\theta}\frac{w - a}{1 - \overline{a}w}$ with $|a| < 1$, $\theta \in \RR$.
::: {.proof}
Schwarz lemma (standard classification of disk automorphisms).
:::
<2>3. Conjugating <2>2 by $\phi$ gives the automorphisms of $\HH$.
::: {.proof}
$\operatorname{Aut}(\HH) = \phi^{-1} \operatorname{Aut}(\DD) \phi$.
:::
<2>4. This conjugation yields exactly the maps $z \mapsto \frac{az+b}{cz+d}$ with $a,b,c,d \in \RR$ and $ad - bc = 1$.
::: {.proof}
Let $T = \phi^{-1} \circ g \circ \phi$ with $g(w) = e^{i\theta}\frac{w-a}{1-\bar a w}$. A composition of Möbius transformations is Möbius, so $T(z) = \frac{az+b}{cz+d}$ for some $a,b,c,d\in\CC$, unique up to a common scalar. The real axis $\RR\cup\{\infty\}$ is the fixed boundary of $\HH$, and $\phi$ maps it onto the unit circle while $g$ preserves the circle; hence $T$ preserves $\RR\cup\{\infty\}$. A Möbius map preserving $\RR\cup\{\infty\}$ has a real representative: its values on $0, 1, \infty$ are three points of $\RR\cup\{\infty\}$, and the map is uniquely determined by these three images — solving $\frac{a\cdot 0 + b}{c\cdot 0 + d} = r_0$, $\frac{a+b}{c+d} = r_1$, $\frac{a}{c} = r_\infty$ for real $r_0, r_1, r_\infty$ determines $a:b:c:d$ as a ratio in $\RR$ (each equation is homogeneous linear with real coefficients, and the system has a unique solution line through the origin, which must therefore be real). So after rescaling, $a,b,c,d \in \RR$, and dividing by $\sqrt{|ad-bc|}$ gives $ad - bc = \pm 1$. For real coefficients, $\Im T(i) = \Im\frac{ai+b}{ci+d} = \frac{ad-bc}{c^2+d^2}$, and since $T(\HH) = \HH$ we have $\Im T(i) > 0$, hence $ad - bc > 0$ and the sign is $+1$. Conversely every matrix in $\mathrm{PSL}_2(\RR)$ preserves $\RR\cup\{\infty\}$ (real coefficients) and sends $i$ into $\HH$ (the computation just displayed); since $T$ preserves the boundary $\RR\cup\{\infty\}$ of $\HH$ and maps the component containing $i$ to the component containing $T(i)$, it restricts to a holomorphic map $\HH \to \HH$, which is a biholomorphism since its inverse has the same form.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
