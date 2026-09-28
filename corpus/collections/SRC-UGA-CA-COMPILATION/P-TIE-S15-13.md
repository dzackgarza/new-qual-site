---
schema: qual/card@1
id: P-TIE-S15-13
kind: problem
title: 'Residue computations: rational, trigonometric, and Fourier-type integrals'
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 13.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rebuilt the run-together integral list with consecutive labels (the source repeats (v)) and added an erratum for a = 0 in (ii), against Spring 2015, question 13, page 12 of Questions_from_Tie.pdf (read from the page image).
---

::: {.problem}
Compute the following integrals.

(i) $\displaystyle\int_0^\infty \frac{1}{(1+x^n)^2}\,dx$, $n \ge 1$

(ii) $\displaystyle\int_0^\infty \frac{\cos x}{(x^2+a^2)^2}\,dx$, $a \in \mathbb{R}$

(iii) $\displaystyle\int_0^\pi \frac{1}{a + \sin\theta}\,d\theta$, $a > 1$

(iv) $\displaystyle\int_0^{\frac{\pi}{2}} \frac{d\theta}{a + \sin^2\theta}$, $a > 0$.

(v) $\displaystyle\int_{\abs{z}=2} \frac{1}{(z^5-1)(z-3)}\,dz$

(vi) $\displaystyle\int_{-\infty}^\infty \frac{\sin \pi a}{\cosh \pi x + \cos \pi a}\,e^{-ix\xi}\,dx$, $0 < a < 1$, $\xi \in \mathbb{R}$

(vii) $\displaystyle\int_{\abs{z}=1} \cot^2 z\,dz$.
:::

::: {.remark}
The source labels these integrals (i), (ii), (iii), (iv), (v), (v), (vi); here they are numbered consecutively, so the source's second (v) is (vi) and its (vi) is (vii).
:::

::: {.remark}
Erratum: integral (ii) diverges for $a = 0$, where the integrand is $\cos x / x^4$, which is not integrable at $0$.
The hypothesis should be $a \in \mathbb{R}$, $a \ne 0$.
:::
