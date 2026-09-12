---
schema: qual/card@1
id: E-SS8.EX-13
kind: problem
title: "SS 8.13: The pseudo-hyperbolic metric and the Schwarz-Pick inequality"
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09

---

::: exercise
The **pseudo-hyperbolic distance** between two points $z, w \in \mathbb{D}$ is defined by:
$$\rho(z, w) = \left| \frac{z - w}{1 - \bar{w} z} \right|.$$

(a) Prove that if $f: \mathbb{D} \to \mathbb{D}$ is holomorphic, then:
$$\rho(f(z), f(w)) \le \rho(z, w) \quad \text{for all } z, w \in \mathbb{D}.$$
Moreover, prove that if $f \in \operatorname{Aut}(\mathbb{D})$ is a conformal automorphism of $\mathbb{D}$, then $f$ preserves the pseudo-hyperbolic distance:
$$\rho(f(z), f(w)) = \rho(z, w) \quad \text{for all } z, w \in \mathbb{D}.$$

(b) Prove the **Schwarz-Pick Lemma**: for any holomorphic function $f: \mathbb{D} \to \mathbb{D}$,
$$\frac{|f'(z)|}{1 - |f(z)|^2} \le \frac{1}{1 - |z|^2} \quad \text{for all } z \in \mathbb{D}.$$
:::

::: solution
For $a\in\mathbb D$, define the disk automorphism
\[
\phi_a(\zeta)=\frac{\zeta-a}{1-\overline a\zeta}.
\]
Then
\[
\rho(z,w)=|\phi_w(z)|.
\]

Fix $w\in\mathbb D$ and set
\[
g=\phi_{f(w)}\circ f\circ\phi_w^{-1}.
\]
Then $g:\mathbb D\to\mathbb D$ is holomorphic and $g(0)=0$. Schwarz's lemma gives
\[
|g(\zeta)|\le|\zeta|.
\]
Taking $\zeta=\phi_w(z)$ yields
\[
\rho(f(z),f(w))
=|\phi_{f(w)}(f(z))|
\le|\phi_w(z)|
=\rho(z,w).
\]
If $f$ is an automorphism, apply the same inequality to $f^{-1}$ and the pair $f(z),f(w)$ to obtain the reverse inequality. Hence automorphisms preserve $\rho$ exactly.

For the infinitesimal form, Schwarz's lemma also gives $|g'(0)|\le1$. Since
\[
\phi_a'(a)=\frac1{1-|a|^2}
\]
and, because $\phi_w^{-1}(\zeta)=(\zeta+w)/(1+\overline w\zeta)$,
\[
(\phi_w^{-1})'(0)=1-|w|^2,
\]
the chain rule gives
\[
g'(0)
=
\frac{1-|w|^2}{1-|f(w)|^2}f'(w).
\]
Therefore
\[
\frac{|f'(w)|}{1-|f(w)|^2}
\le
\frac1{1-|w|^2}.
\]
Renaming $w$ as $z$ gives the Schwarz-Pick inequality.
:::
