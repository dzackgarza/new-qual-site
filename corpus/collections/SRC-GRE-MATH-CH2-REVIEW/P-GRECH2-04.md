---
schema: qual/card@1
id: P-GRECH2-04
kind: problem
title: Limit of $(\arcsin x-x)/x^3$ at $0$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 4 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Evaluate the following limit:

$$
\lim_{x \to 0} \frac{\arcsin x - x}{x^3}
$$

(A) $0$
(B) $\frac{1}{6}$
(C) $\frac{1}{3}$
(D) $\frac{1}{2}$
(E) $1$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

After one application of L'Hôpital's rule, the limit becomes
$$
\lim_{x\to0}
\frac{(1-x^2)^{-1/2}-1}{3x^2}.
$$


::: pf-proof

Both numerator and denominator of the original quotient tend to $0$. Differentiating them gives
$$
\frac{d}{dx}(\arcsin x-x)
=\frac1{\sqrt{1-x^2}}-1
$$
and
$$
\frac{d}{dx}(x^3)=3x^2.
$$
Thus L'Hôpital's rule gives the displayed limit.

:::

:::

::: {.pf-step #s1-2}

The limit in step [](#s1-1){.pf-ref} equals $1/6$.


::: pf-proof

The quotient in step [](#s1-1){.pf-ref} again has the indeterminate form $0/0$. A second application of L'Hôpital's rule gives
$$
\lim_{x\to0}
\frac{x(1-x^2)^{-3/2}}{6x}.
$$
For $x\ne0$ this quotient equals
$$
\frac{(1-x^2)^{-3/2}}6,
$$
whose limit at $0$ is $1/6$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{\lim_{x\to0}\frac{\arcsin x-x}{x^3}=\frac16},
$$
so the answer is (B).


::: pf-proof

Combine steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested limit and corresponding choice.

:::

:::

:::
