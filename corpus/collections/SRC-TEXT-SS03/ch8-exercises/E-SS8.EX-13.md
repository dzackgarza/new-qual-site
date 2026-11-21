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
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    The card's statement omitted the bracketed hint the book prints at PDF page 268, printed p.249: "[Hint: Consider the automorphism ψα (z) = (z − α)/(1 − αz) and apply the Schwarz lemma to ψ −1 f (w) ◦ f ◦ ψw .]"
    A completeness audit of the collection against the book flagged the omission; the hint
    is restored verbatim from the print. The mathematics of the statement is unchanged.

- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose argument into numbered steps without changing the mathematics, and
    re-checked each step against the definitions and theorems it invokes. What was not checked: no
    copy of Stein and Shakarchi and no solution set for it is retained in tmp/sources (the
    collection provenance is the Google Books ISBN link), so the printed statement and page were
    not re-read; the exercise number is the one the collection index records. No published
    solution is transcribed; the argument remains the card's own, as its solution section says.
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
[Hint: Consider the automorphism $\psi_\alpha(z)=(z-\alpha)/(1-\bar\alpha z)$ and apply the Schwarz lemma to $\psi_{f(w)}^{-1}\circ f\circ\psi_w$.]
:::

::: {.solution}

The argument is the card's own: the book is retained in this repository as `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, and no published solution set of this exercise is retained, so nothing below is transcribed. The statement is the exercise the collection index records as Stein and Shakarchi, *Complex Analysis* (2003), Ch. 8, Exercise 13. Here $\DD=\theset{\abs{z}<1}$, $\rho(z,w)=\abs{\frac{z-w}{1-\overline{w}z}}$, and for $a\in\DD$ the disk automorphism is $\phi_a(\zeta)=\frac{\zeta-a}{1-\overline{a}\zeta}$ with inverse $\phi_a^{-1}(\zeta)=\frac{\zeta+a}{1+\overline{a}\zeta}$; Schwarz's lemma is that a holomorphic $g:\DD\to\DD$ with $g(0)=0$ satisfies $\abs{g(\zeta)}\leq\abs{\zeta}$ and $\abs{g'(0)}\leq1$.

::: pf

::: {.pf-step #phi}

$\rho(z,w)=\abs{\phi_w(z)}$ and $\phi_w$ is an automorphism of $\DD$.

::: pf-proof

Substituting $a=w$, $\zeta=z$ in the definition of $\phi_w$ gives exactly $(z-w)/(1-\overline{w}z)$. The denominator does not vanish for $\abs{z}<1$, $\abs{w}<1$ since $\abs{\overline{w}z}<1$, and $\phi_w$ is a bijection of $\DD$ with the displayed inverse, which is holomorphic for the same reason.

:::

:::

::: {.pf-step #a}

(a) $\rho(f(z),f(w))\leq\rho(z,w)$ for holomorphic $f:\DD\to\DD$.

::: pf-proof

Fix $w\in\DD$ and put $g=\phi_{f(w)}\circ f\circ\phi_w^{-1}$, holomorphic $\DD\to\DD$ with $g(0)=\phi_{f(w)}(f(w))=0$. Schwarz's lemma gives $\abs{g(\zeta)}\leq\abs{\zeta}$; at $\zeta=\phi_w(z)$ this reads $\abs{\phi_{f(w)}(f(z))}\leq\abs{\phi_w(z)}$, which is the inequality by step [](#phi){.pf-ref}.

:::

:::

::: {.pf-step #aut}

(a) An automorphism $f$ preserves $\rho$.

::: pf-proof

Apply step [](#a){.pf-ref} to $f^{-1}$, which is holomorphic $\DD\to\DD$, and to the pair $f(z),f(w)$: $\rho(z,w)=\rho(f^{-1}(f(z)),f^{-1}(f(w)))\leq\rho(f(z),f(w))$. With step [](#a){.pf-ref} applied to $f$ itself, the two are equal.

:::

:::

::: {.pf-step #b}

(b) $\frac{\abs{f'(z)}}{1-\abs{f(z)}^{2}}\leq\frac{1}{1-\abs{z}^{2}}$.

::: pf-proof

Schwarz's lemma also gives $\abs{g'(0)}\leq1$. Since $\phi_a'(\zeta)=\frac{1-\abs{a}^{2}}{(1-\overline{a}\zeta)^{2}}$, we have $\phi_{f(w)}'(f(w))=\frac{1}{1-\abs{f(w)}^{2}}$ and $(\phi_w^{-1})'(0)=1-\abs{w}^{2}$; the chain rule in $g=\phi_{f(w)}\circ f\circ\phi_w^{-1}$ gives $g'(0)=\frac{1-\abs{w}^{2}}{1-\abs{f(w)}^{2}}f'(w)$, so the inequality $\abs{g'(0)}\leq1$ is the displayed one at $w$, and renaming $w$ as $z$ gives it everywhere.

:::

:::

:::

:::
