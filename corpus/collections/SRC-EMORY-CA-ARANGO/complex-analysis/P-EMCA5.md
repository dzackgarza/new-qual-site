---
schema: qual/card@1
id: P-EMCA5
kind: problem
title: "Schwarz lemma and hyperbolic metric inequality"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
(a) State the Schwarz lemma for analytic functions in the unit disc.

(b) Let $f : \mathbf{D} \to \mathbf{D}$ be an analytic map from the unit disc $\mathbf{D}$ into itself.
Use the Schwarz lemma to show that for each $a \in \mathbf{D}$,
$$
\frac{|f'(a)|}{1 - |f(a)|^2} \leq \frac{1}{1 - |a|^2}.
$$

::: {.solution}
**(a).**

<1>1. The Schwarz lemma states: if $g : \mathbb{D} \to \mathbb{D}$ is analytic with $g(0) = 0$, then $|g(z)| \le |z|$ and $|g'(0)| \le 1$.
Proof: statement of the Schwarz lemma.

**(b).**

<1>1. Fix $a \in \mathbb{D}$ and define the disk automorphisms $\varphi_a(z) = \frac{z - a}{1 - \bar a z}$ and $\psi_{f(a)}(w) = \frac{w - f(a)}{1 - \overline{f(a)} w}$.
Proof: the Möbius automorphisms sending $a \mapsto 0$ and $f(a) \mapsto 0$.

<1>2. Define $g = \psi_{f(a)} \circ f \circ \varphi_a^{-1}$.
Proof: composition.

<1>3. $g : \mathbb{D} \to \mathbb{D}$ is analytic and $g(0) = 0$.
Proof: <1>1 and <1>2 ($\varphi_a^{-1}(0) = a$ and $\psi_{f(a)}(f(a)) = 0$).

<1>4. By the Schwarz lemma, $|g'(0)| \le 1$.
Proof: <1>3.

<1>5. $g'(0) = \psi_{f(a)}'(f(a)) \cdot f'(a) \cdot (\varphi_a^{-1})'(0)$.
Proof: chain rule.

<1>6. $\psi_{f(a)}'(f(a)) = \frac{1}{1 - |f(a)|^2}$ and $(\varphi_a^{-1})'(0) = 1 - |a|^2$.
Proof: compute the derivatives of the Möbius maps.

<1>7. Hence $|g'(0)| = \frac{|f'(a)|(1 - |a|^2)}{1 - |f(a)|^2} \le 1$.
Proof: <1>5 and <1>6.

<1>8. Therefore $\frac{|f'(a)|}{1 - |f(a)|^2} \le \frac{1}{1 - |a|^2}$.
Proof: <1>7.

<1>9. Q.E.D.
Proof: <1>1 (a) and <1>8 (b).
:::
:::
