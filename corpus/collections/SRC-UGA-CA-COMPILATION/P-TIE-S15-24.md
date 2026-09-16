---
schema: qual/card@1
id: P-TIE-S15-24
kind: problem
title: Integrals of $|\psi_\alpha'|^2$ and $|\psi_\alpha'|$ over the disk for a Blaschke factor
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 24.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Absorbed the duplicate P-TIE-S15-30, which the source prints again as Spring 2015, question 30, page 14 of Questions_from_Tie.pdf, and took over its typed statement and remark.
---

::: {.problem}
Let $\psi_\alpha(z) = \frac{\alpha - z}{1 - \bar{\alpha}z}$ with $\abs{\alpha} < 1$ and $\mathbb{D} = \{z : \abs{z} < 1\}$. Prove that

(a) $\displaystyle\frac{1}{\pi}\iint_{\mathbb{D}} \abs{\psi_\alpha'}^2\,dx\,dy = 1$.

(b) $\displaystyle\frac{1}{\pi}\iint_{\mathbb{D}} \abs{\psi_\alpha'}\,dx\,dy = \frac{1 - \abs{\alpha}^2}{\abs{\alpha}^2}\log\frac{1}{1 - \abs{\alpha}^2}$.
:::

::: {.remark}
The source prints this problem twice, as questions 24 and 30 of Spring 2015.
Under question 30 it also prints "Prove that $f(z) = -\frac{1}{2}\left(z + \frac{1}{z}\right)$ is a conformal map from half disc $\{z = x + iy : \abs{z} < 1,\ y > 0\}$ to upper half plane $\mathbb{H} = \{z = x + iy : y > 0\}$", which is question 25 of the same list.
It is a separate problem, carried by its own card.
:::
