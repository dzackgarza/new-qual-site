---
schema: qual/card@1
id: P-FOXHV
kind: problem
title: The disk automorphism $z\mapsto\frac{w-z}{1-\bar{w}z}$
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Schwarz Lemma
  - Biholomorphisms
relations: []
review: draft
---

::: problem
a. Let $z, w \in \CC$ with $\bar z w \neq 1$.
Prove that
\[
\abs{w-z \over 1 - \bar w z} < 1 \quad\text{ if } \abs{z}<1,~ \abs{w} < 1
\]
with equality when $\abs{z} = 1$ or $\abs{w} = 1$.

b. Prove that for a fixed $w\in \DD$, the mapping $F: z\mapsto {w-z \over 1 - \bar w z}$ satisfies

- $F$ maps $\DD$ to itself and is holomorphic.

- $F(0) = w$ and $F(w) = 0$.

- $\abs{z} = 1$ implies $\abs{F(z)} = 1$.

- $F: \DD \to \DD$ is bijective.

> Hint: Calculate $F \circ F$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** (a) Show $\abs{\frac{w - z}{1 - \bar w z}} < 1$ for $\abs z, \abs w < 1$ (with equality when $\abs z = 1$ or $\abs w = 1$), for $\bar z w \neq 1$; (b) show $F(z) = \frac{w - z}{1 - \bar w z}$ maps $\DD$ to itself, is holomorphic, sends $0 \mapsto w$, $w \mapsto 0$, the circle to the circle, and is bijective.

<1>1. Compute $\abs{w - z}^2 - \abs{1 - \bar w z}^2 = (\abs w^2 - 1)(1 - \abs z^2)$.
Proof: $\abs{w - z}^2 = \abs w^2 + \abs z^2 - w\bar z - \bar w z$ and $\abs{1 - \bar w z}^2 = 1 + \abs w^2 \abs z^2 - \bar w z - w \bar z$; subtracting gives $\abs w^2 + \abs z^2 - 1 - \abs w^2\abs z^2 = (\abs w^2 - 1)(1 - \abs z^2)$.

<1>2. (a): For $\abs z, \abs w < 1$, $\abs{\frac{w - z}{1 - \bar w z}} < 1$.
Proof: By <1>1, $\abs{w - z}^2 - \abs{1 - \bar w z}^2 = (\abs w^2 - 1)(1 - \abs z^2) < 0$ (both factors negative), so $\abs{w - z} < \abs{1 - \bar w z}$; dividing by the positive $\abs{1 - \bar w z}$ (nonzero because $\abs{\bar w z} = \abs w \abs z < 1$) gives the claim.

<1>3. (a): If $\abs z = 1$ or $\abs w = 1$, then $\abs{\frac{w - z}{1 - \bar w z}} = 1$.
Proof: If $\abs z = 1$, then $\abs{1 - \bar w z} = \abs z \abs{1 - \bar w z} = \abs{z - \bar w z^2}$... more directly: $\abs{1 - \bar w z} = \abs{\bar z - \bar w} = \abs{z - w}$ since $\bar z = 1/z$; indeed $\abs{1 - \bar w z} = \abs{\overline{1 - \bar w z}} = \abs{1 - w\bar z}$, and $\abs{1 - w\bar z} = \abs{z - w}$ because $\abs z = 1$ (multiply by $\abs z$: $\abs{z - w\abs z^2} = \abs{z - w}$). So numerator and denominator have equal modulus.
The case $\abs w = 1$ is symmetric: $\abs{1 - \bar w z} = \abs{w - z\abs w^2} = \abs{w - z}$.

<1>4. (b): $F$ is holomorphic on $\DD$.
Proof: $F$ is a rational function whose denominator $1 - \bar w z$ does not vanish on $\DD$ (as $\abs{\bar w z} \leq \abs w \abs z < 1$ for $\abs w < 1$, $\abs z < 1$); hence it is holomorphic there.

<1>5. (b): $F(0) = w$ and $F(w) = 0$.
Proof: $F(0) = \frac{w - 0}{1 - 0} = w$, and $F(w) = \frac{w - w}{1 - \bar w w} = \frac{0}{1 - \abs w^2} = 0$ (valid since $\abs w < 1$).

<1>6. (b): $F$ maps $\DD$ into itself and $\abs z = 1 \implies \abs{F(z)} = 1$.
Proof: By <1>2, $\abs{F(z)} < 1$ for $\abs z < 1$; by <1>3 with the roles as given, $\abs{F(z)} = 1$ for $\abs z = 1$ (equality case $\abs z = 1$).

<1>7. (b): $F: \DD \to \DD$ is bijective.
Proof: $F(F(z)) = \frac{w - F(z)}{1 - \bar w F(z)}$.
Clearing the inner denominator $1 - \bar w z$ gives
\[
F(F(z)) = \frac{w(1 - \bar w z) - (w - z)}{(1 - \bar w z) - \bar w(w - z)} = \frac{z(1 - \abs w^2)}{1 - \abs w^2} = z
\]
for $\abs w < 1$.
Thus $F \circ F = \mathrm{id}_{\DD}$, so $F$ is a bijection.

<1>8. Q.E.D. Proof: <1>2–<1>3 prove (a) and <1>4–<1>7 prove (b).
:::
