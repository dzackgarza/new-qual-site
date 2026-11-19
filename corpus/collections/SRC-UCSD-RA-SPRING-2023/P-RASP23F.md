---
schema: qual/card@1
id: P-RASP23F
kind: problem
title: "Interpolation of weak-type bounds"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 6 of the official UCSD Spring 2023 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the layer-cake interpolation already on the card, which
    is correct: the distribution-function bounds are combined as a minimum, split at the scale
    where the two exponentials cross, and integrated with the layer-cake identity. Added: the
    layer-cake identity itself with its Tonelli justification and the measurability of Tf; the
    derivation of the crossing scale alpha_0 by taking roots, including which bound is smaller
    on each side; the convergence of the two integrals from q1 < q < q2; and the substitution
    written out, including the check that the bracket is a constant times ||f||_p^q only because
    alpha_0 is a constant times ||f||_p. Not claimed: a retained solution set; the collection's
    provenance is the examination paper only.
---

::: {.problem}
Let $1 \leq p < \infty$.
Recall that $\lambda_g(\alpha) = \mu(\{x : \abs{g(x)} > \alpha\})$.
Assume that $T$ is a linear operator from $L^p$ into $L^{q_1}$ and $L^{q_2}$ with $1 \leq q_1 < q_2$ such that $\lambda_{Tf}(\alpha) \leq (C_1 \norm{f}_p / \alpha)^{q_1}$ and $\lambda_{Tf}(\alpha) \leq (C_2 \norm{f}_p / \alpha)^{q_2}$.
Prove that for any $q_1 < q < q_2$, $\norm{Tf}_q \leq C_q \norm{f}_p$.
Here $C_q$ depends on $q, q_1, q_2$ and $C_1, C_2$.
:::


::: {.solution}
Throughout $1 \le p < \infty$ and $1 \le q_{1} < q < q_{2}$, $\lambda_{g}(\alpha) = \mu\bigl(\theset{x \mid \abs{g(x)} > \alpha}\bigr)$ for $\alpha > 0$, and the two hypotheses are the weak-type bounds $\lambda_{Tf}(\alpha) \le (A/\alpha)^{q_{1}}$ and $\lambda_{Tf}(\alpha) \le (B/\alpha)^{q_{2}}$ with $A \coloneqq C_{1}\norm{f}_{p}$ and $B \coloneqq C_{2}\norm{f}_{p}$. The collection's `provenance` is the Spring 2023 examination paper, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #layer}
$\norm{Tf}_{q}^{q} = q\int_{0}^{\infty}\alpha^{q-1}\lambda_{Tf}(\alpha)\\,d\alpha$.

::: pf-proof
This is the layer-cake identity for a nonnegative measurable $g = Tf$: $\abs{g}^{q} = q\int_{0}^{\infty}\alpha^{q-1}\mathbf{1}_{\theset{\abs{g} > \alpha}}d\alpha$ pointwise, and integrating over the measure space with Tonelli's theorem (all integrands nonnegative) interchanges the two integrals. $Tf$ is measurable because $T$ maps $L^{p}$ into the space of measurable functions by hypothesis.

:::

:::

::: {.pf-step #degenerate}
If $A = 0$ or $B = 0$ then $Tf = 0$ almost everywhere and the conclusion holds.

::: pf-proof
$\lambda_{Tf}(\alpha) \le (A/\alpha)^{q_{1}} = 0$ for every $\alpha > 0$ when $A = 0$, so the set where $\abs{Tf} > \alpha$ is null for every $\alpha$, and $\theset{\abs{Tf} > 0}$ is the union of these over $\alpha = 1/n$; the same with $B$ and $q_{2}$. Hence assume $A, B > 0$.

:::

:::

::: {.pf-step #min}
$\lambda_{Tf}(\alpha) \le \min\bigl\\{(A/\alpha)^{q_{1}}, (B/\alpha)^{q_{2}}\bigr\\}$ for every $\alpha > 0$.

::: pf-proof
Both weak-type bounds hold for every $\alpha > 0$, so the smaller of the two bounds is a bound as well.

:::

:::

::: {.pf-step #scale}
The two bounds agree exactly at $\alpha_{0} = \bigl(B^{q_{2}}/A^{q_{1}}\bigr)^{1/(q_{2}-q_{1})}$; for $\alpha < \alpha_{0}$ the bound $(A/\alpha)^{q_{1}}$ is the smaller and for $\alpha > \alpha_{0}$ the bound $(B/\alpha)^{q_{2}}$ is.

::: pf-proof
$(A/\alpha)^{q_{1}} \le (B/\alpha)^{q_{2}}$ is equivalent to $A^{q_{1}}\alpha^{q_{2}-q_{1}} \le B^{q_{2}}$, that is to $\alpha \le \alpha_{0}$, since $q_{2} - q_{1} > 0$ and $A, B > 0$; equality at $\alpha = \alpha_{0}$ follows by taking the $(q_{2}-q_{1})$-th root.

:::

:::

::: {.pf-step #split}
$\norm{Tf}_{q}^{q} \le \frac{q}{q-q_{1}}A^{q_{1}}\alpha_{0}^{q-q_{1}} + \frac{q}{q_{2}-q}B^{q_{2}}\alpha_{0}^{q-q_{2}}$.

::: pf-proof
By steps [](#layer){.pf-ref} and [](#scale){.pf-ref}, the bound of step [](#min){.pf-ref} splits as $\norm{Tf}_{q}^{q} \le qA^{q_{1}}\int_{0}^{\alpha_{0}}\alpha^{q-q_{1}-1}d\alpha + qB^{q_{2}}\int_{\alpha_{0}}^{\infty}\alpha^{q-q_{2}-1}d\alpha$, using the smaller exponent on each side of $\alpha_{0}$. Both integrals converge: on $(0,\alpha_{0})$ the exponent is $q - q_{1} - 1 > -1$ because $q > q_{1}$, so the integrand is integrable at $0$; on $(\alpha_{0},\infty)$ the exponent is $q - q_{2} - 1 < -1$ because $q < q_{2}$, so the integrand is integrable at infinity. Evaluating, $\int_{0}^{\alpha_{0}}\alpha^{q-q_{1}-1}d\alpha = \alpha_{0}^{q-q_{1}}/(q-q_{1})$ and $\int_{\alpha_{0}}^{\infty}\alpha^{q-q_{2}-1}d\alpha = \alpha_{0}^{q-q_{2}}/(q_{2}-q)$, which are the two displayed terms.

:::

:::

::: {.pf-step #substitute}
Substituting $\alpha_{0}$ gives $\norm{Tf}_{q}^{q} \le C_{q}^{q}\norm{f}_{p}^{q}$, with $C_{q}$ depending only on $q, q_{1}, q_{2}, C_{1}, C_{2}$.

::: pf-proof
Write $\alpha_{0} = \kappa\norm{f}_{p}$ with $\kappa \coloneqq \bigl(C_{2}^{q_{2}}/C_{1}^{q_{1}}\bigr)^{1/(q_{2}-q_{1})}$, which is the displayed form of step [](#scale){.pf-ref} after substituting $A = C_{1}\norm{f}_{p}$ and $B = C_{2}\norm{f}_{p}$. Then $A^{q_{1}}\alpha_{0}^{q-q_{1}} = C_{1}^{q_{1}}\kappa^{q-q_{1}}\norm{f}_{p}^{q}$ and $B^{q_{2}}\alpha_{0}^{q-q_{2}} = C_{2}^{q_{2}}\kappa^{q-q_{2}}\norm{f}_{p}^{q}$, so the bound of step [](#split){.pf-ref} reads $\norm{Tf}_{q}^{q} \le \bigl[\frac{q}{q-q_{1}}C_{1}^{q_{1}}\kappa^{q-q_{1}} + \frac{q}{q_{2}-q}C_{2}^{q_{2}}\kappa^{q-q_{2}}\bigr]\norm{f}_{p}^{q}$, and the bracket is $C_{q}^{q}$.

:::

:::

::: pf-step
$\norm{Tf}_{q} \le C_{q}\norm{f}_{p}$ for every $q_{1} < q < q_{2}$, with $C_{q}$ as in step [](#substitute){.pf-ref}.

::: pf-proof
Take $q$-th roots in step [](#substitute){.pf-ref}: the bracket depends only on $q, q_{1}, q_{2}$ and the two constants, and $\norm{f}_{p}^{q}$ has $q$-th root $\norm{f}_{p}$. The degenerate case is step [](#degenerate){.pf-ref}.

:::

:::

:::
:::
