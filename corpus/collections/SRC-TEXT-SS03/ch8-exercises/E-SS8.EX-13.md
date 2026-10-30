---
schema: qual/card@1
id: E-SS8.EX-13
kind: problem
title: The pseudo-hyperbolic metric and the Schwarz--Pick inequality
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Automorphisms
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

::: {.exercise}
The **pseudo-hyperbolic distance** between two points $z, w \in \DD$ is defined by:
$$\rho(z, w) = \abs{ \frac{z - w}{1 - \bar{w} z} }.$$

(a) Prove that if $f: \DD \to \DD$ is holomorphic, then:
$$\rho(f(z), f(w)) \le \rho(z, w) \quad \text{for all } z, w \in \DD.$$
Moreover, prove that if $f \in \operatorname{Aut}(\DD)$ is a conformal automorphism of $\DD$, then $f$ preserves the pseudo-hyperbolic distance:
$$\rho(f(z), f(w)) = \rho(z, w) \quad \text{for all } z, w \in \DD.$$

(b) Prove the **Schwarz-Pick Lemma**: for any holomorphic function $f: \DD \to \DD$,
$$\frac{\abs{f'(z)}}{1 - \abs{f(z)}^2} \le \frac{1}{1 - \abs{z}^2} \quad \text{for all } z \in \DD.$$
:::

::: {.solution}
For $a\in\DD$, define the disk automorphism
$$
\phi_a(\zeta)=\frac{\zeta-a}{1-\overline a\zeta}.
$$
Then
$$
\rho(z,w)=\abs{\phi_w(z)}.
$$

Fix $w\in\DD$ and set
$$
g=\phi_{f(w)}\circ f\circ\phi_w^{-1}.
$$
Then $g:\DD\to\DD$ is holomorphic and $g(0)=0$. Schwarz's lemma gives
$$
\abs{g(\zeta)}\le\abs{\zeta}.
$$
Taking $\zeta=\phi_w(z)$ yields
$$
\rho(f(z),f(w))
=\abs{\phi_{f(w)}(f(z))}
\le\abs{\phi_w(z)}
=\rho(z,w).
$$
If $f$ is an automorphism, apply the same inequality to $f^{-1}$ and the pair $f(z),f(w)$ to obtain the reverse inequality. Hence automorphisms preserve $\rho$ exactly.

For the infinitesimal form, Schwarz's lemma also gives $\abs{g'(0)}\le1$. Since
$$
\phi_a'(a)=\frac1{1-\abs{a}^2}
$$
and, because $\phi_w^{-1}(\zeta)=(\zeta+w)/(1+\overline w\zeta)$,
$$
(\phi_w^{-1})'(0)=1-\abs{w}^2,
$$
the chain rule gives
$$
g'(0)
=
\frac{1-\abs{w}^2}{1-\abs{f(w)}^2}f'(w).
$$
Therefore
$$
\frac{\abs{f'(w)}}{1-\abs{f(w)}^2}
\le
\frac1{1-\abs{w}^2}.
$$
Renaming $w$ as $z$ gives the Schwarz-Pick inequality.
:::
