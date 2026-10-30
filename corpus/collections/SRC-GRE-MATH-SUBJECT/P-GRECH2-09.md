---
schema: qual/card@1
id: P-GRECH2-09
kind: problem
title: Derivative of $\arcsin(\log\sqrt x)$ at $x=e$
classification:
  areas: [prelim]
  topics:
  - Differentiation
  - Chain Rule
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 9 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Evaluate the derivative of the following function at $x = e$:

$$
f(x) = \arcsin(\log \sqrt{x})
$$

(A) $\frac{1}{e\sqrt{3}}$
(B) $\frac{e}{\sqrt{2}}$
(C) $\frac{\pi e}{2}$
(D) $\sqrt{2e}$
(E) $\frac{3e}{\sqrt{2}}$
:::

::: {.solution}

Set $u(x)=\log\sqrt{x}$.

::: pf

::: {.pf-step #s1-1}

For interior points of the domain,
$$
f'(x)=\frac{1}{2x\sqrt{1-[\log\sqrt{x}]^2}}.
$$


::: pf-proof

The chain rule gives
$$
f'(x)=\frac{u'(x)}{\sqrt{1-u(x)^2}}.
$$
Since
$$
u(x)=\log(x^{1/2})=\frac12\log x,
$$
one has $u'(x)=1/(2x)$. Substitution gives the displayed derivative.

:::

:::

::: {.pf-step #s1-2}

At $x=e$,
$$
f'(e)=\frac{1}{e\sqrt3}.
$$


::: pf-proof

Because
$$
\log\sqrt e=\frac12,
$$
step [](#s1-1){.pf-ref} gives
$$
f'(e)
=\frac{1}{2e\sqrt{1-(1/2)^2}}
=\frac{1}{2e(\sqrt3/2)}
=\frac{1}{e\sqrt3}.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore the requested value is
$$
\boxed{\frac{1}{e\sqrt3}},
$$
so the answer is (A).


::: pf-proof

This is exactly the evaluation established in step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested derivative value and corresponding choice.

:::

:::

:::
