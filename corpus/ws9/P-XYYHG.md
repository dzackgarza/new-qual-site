---
schema: qual/card@1
id: P-XYYHG
kind: problem
title: "Determine all holomorphic automorphisms of the upper half\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - fractional-linear-transformations
  - conformal-maps
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Determine all holomorphic automorphisms of the upper half plane $\mathcal{U} = \{z : \operatorname{Im} z > 0\}$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Determine all holomorphic automorphisms of the upper half-plane $\mcu = \{z : \Im z > 0\}$.

<1>1. Every map $z \mapsto \frac{az + b}{cz + d}$ with $a, b, c, d \in \RR$, $ad - bc > 0$, is an automorphism of $\mcu$.
Proof: for $z = x + iy$, $y > 0$: $\Im\frac{az+b}{cz+d} = \frac{(ad - bc)y}{|cz + d|^2} > 0$; the inverse is again of the same form (with matrix inverse), so the map is a biholomorphism of $\mcu$.

<1>2. Conversely, let $f \in \Aut(\mcu)$; it suffices to show $f$ is a Möbius map.
<2>1. Conjugate by the Cayley map $C(z) = \frac{z - i}{z + i}: \mcu \to D$.
Proof: $C$ is a biholomorphism (its inverse is $C^{-1}(w) = i\frac{1 + w}{1 - w}$). <2>2. $g := C \circ f \circ C^{-1} \in \Aut(D)$.
Proof: composition of biholomorphisms.
<2>3. $g$ is a Möbius transformation: $g(w) = e^{i\theta}\frac{w - \alpha}{1 - \bar\alpha w}$, $|\alpha| < 1$.
Proof: automorphisms of the unit disk are exactly these (standard Schwarz-lemma argument).
<2>4. $f = C^{-1} \circ g \circ C$ is a Möbius transformation with real coefficients and positive determinant.
Proof: $C$ and $C^{-1}$ are Möbius maps with real coefficients (up to the constant $i$: concretely, unwinding gives $f(z) = \frac{az + b}{cz + d}$ with $a,b,c,d \in \RR$ and $ad - bc > 0$; the reality follows from $f(\RR \cup \{\infty\}) \subseteq \RR \cup \{\infty\}$, and positivity of $ad - bc$ from $f(\mcu) \subseteq \mcu$ as in <1>1).

<1>3. Q.E.D. Proof: <1>1 and <1>2 show $\Aut(\mcu) = \ts{z \mapsto \frac{az+b}{cz+d} \st a,b,c,d \in \RR,\, ad - bc > 0}$, i.e. $\PSL_2(\RR)$.
:::
