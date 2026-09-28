---
schema: qual/card@1
id: E-HAT-4.1-4
kind: problem
title: "Deck transformation action on $\\pi_n$ of universal cover"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

::: {.problem}
Let $p: \tilde{X} \to X$ be the universal cover of a path-connected space $X$.
Show that under the isomorphism $\pi_n(X) \approx \pi_n(\tilde{X})$, which holds for $n \geq 2$, the action of $\pi_1(X)$ on $\pi_n(X)$ corresponds to the action of $\pi_1(X)$ on $\pi_n(\tilde{X})$ induced by the action of $\pi_1(X)$ on $\tilde{X}$ as deck transformations.
More precisely, prove a formula like $\gamma p_*(\alpha) = p_*\bigl(\beta_{\tilde{\gamma}}(\gamma_*(\alpha))\bigr)$ where $\gamma \in \pi_1(X, x_0)$, $\alpha \in \pi_n(\tilde{X}, \tilde{x}_0)$, and $\gamma_*$ denotes the homomorphism induced by the action of $\gamma$ on $\tilde{X}$.
:::

::: {.solution}
Let \(\widetilde x_0\in p^{-1}(x_0)\), and let \(\gamma\) be a loop at \(x_0\). Lift \(\gamma\) to a path
\[
\widetilde\gamma:I\to\widetilde X,
\qquad
\widetilde\gamma(0)=\widetilde x_0.
\]
Its endpoint is \(T_\gamma(\widetilde x_0)\), where \(T_\gamma\) is the deck transformation corresponding to \(\gamma\).

Take
\[
\alpha\in\pi_n(\widetilde X,\widetilde x_0),\qquad n\ge2.
\]
Applying \(T_\gamma\) gives
\[
(T_\gamma)_*(\alpha)\in
\pi_n(\widetilde X,T_\gamma\widetilde x_0).
\]
Change the basepoint back along \(\widetilde\gamma\). With the convention that
\(\beta_{\widetilde\gamma}:\pi_n(\widetilde X,T_\gamma\widetilde x_0)\to
\pi_n(\widetilde X,\widetilde x_0)\), the resulting class is
\[
\beta_{\widetilde\gamma}(T_\gamma)_*(\alpha).
\]

Projecting to \(X\), the path \(\widetilde\gamma\) projects to \(\gamma\), while
\(pT_\gamma=p\). Hence the defining construction of the \(\pi_1(X)\)-action on \(\pi_n(X)\) gives the commutative formula
\[
\boxed{
\gamma\cdot p_*(\alpha)
=p_*\!\left(\beta_{\widetilde\gamma}(T_\gamma)_*(\alpha)\right).
}
\]
If the opposite convention for change-of-basepoint maps is used, the same formula is written with \(\beta_{\widetilde\gamma}^{-1}\); the content is unchanged. Thus under
\(p_*:\pi_n(\widetilde X)\cong\pi_n(X)\), the usual \(\pi_1(X)\)-action is precisely the action induced by deck transformations, with the necessary basepoint correction.
:::
