---
schema: qual/card@1
id: P-GRECH1-12
kind: problem
title: A polynomial with root $\sqrt3-\sqrt2$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 1 review Question 12 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription.
---

::: {.problem}
Which one of the following polynomials $p(x)$ has the property that $\sqrt{3} - \sqrt{2}$ is a root of the equation $p(x) = 0$?

(A) $2x^2 + 6x + 3$
(B) $x^3 - 2x + 6$
(C) $x^4 + 2x^2 - 3$
(D) $x^4 - 10x^2 + 1$
(E) $x^4 - 5x^2 + 6$
:::

::: {.solution}

Set $\alpha=\sqrt3-\sqrt2$.

::: pf

::: {.pf-step #s1-1}

$\alpha^2-5=-2\sqrt6$.


::: pf-proof

Directly,
$$
\alpha^2=(\sqrt3-\sqrt2)^2=3+2-2\sqrt6=5-2\sqrt6.
$$
Rearranging gives the claim.

:::

:::

::: {.pf-step #s1-2}

$\alpha$ satisfies
$$
\alpha^4-10\alpha^2+1=0.
$$


::: pf-proof

Squaring the equality in step [](#s1-1){.pf-ref} gives
$$
(\alpha^2-5)^2=24.
$$
Expanding and moving $24$ to the left yields
$$
\alpha^4-10\alpha^2+25-24=0,
$$
which is the claimed relation.

:::

:::

::: {.pf-step #s1-3}

The required polynomial is
$$
\boxed{p(x)=x^4-10x^2+1},
$$
so the answer is (D).


::: pf-proof

Step [](#s1-2){.pf-ref} states exactly that substituting $x=\alpha$ into the polynomial in choice (D) gives zero.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} identifies the requested listed polynomial.

:::

:::

:::
