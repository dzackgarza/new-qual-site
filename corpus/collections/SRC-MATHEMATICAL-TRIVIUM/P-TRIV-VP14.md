---
schema: qual/card@1
id: P-TRIV-VP14
kind: problem
title: Q-ball ansatz in the Euler--Lagrange equations of a complex scalar field
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Variational Principle, Problem 14, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash concatenates the `14.` marker to the end of Problem 13; source order unambiguously separates this as Problem 14.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed a stray extraction digit against Variational Principle Problem 14 on page 21 of the source PDF and added a remark on the source's variable x for r.
---

::: problem
Consider the functional $S[\phi, \phi^*] = 4\pi \int_{-\infty}^{\infty} dt \int_0^\infty dr\, r^2 \left(\dot{\phi}\dot{\phi}^* - \phi'\phi'^* - U(\phi\phi^*)\right)$, where $U \in C^1(\mathbb{R})$ and $\phi$ is a $C^2(\mathbb{R} \times [0, \infty))$ complex-valued function of $t$ and $x$.

(a) Varying with respect to $\phi$ and $\phi^*$, obtain the Euler-Lagrange equation and its conjugated.
Substituting the *ansatz* $\phi(r, t) = f(r) e^{i\omega t}$, rewrite them as an equation on a function $f$ of a single variable $r$.

(b) Substitute the ansatz $\phi(r, t) = f(r) e^{i\omega t}$ into the functional $S[\phi, \phi^*]$ first, and, varying with respect to $f$, obtain the Euler-Lagrange equation on $f$.
Compare with the result of the previous point.
:::

::: {.remark}
The source says $\phi$ is a function "of $t$ and $x$", but the functional and the ansatz use the radial variable $r \in [0, \infty)$, with $\dot{\phi} = \partial_t \phi$ and $\phi' = \partial_r \phi$; the intended variables are $t$ and $r$.
:::
