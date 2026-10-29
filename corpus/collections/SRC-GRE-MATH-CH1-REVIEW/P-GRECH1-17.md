---
schema: qual/card@1
id: P-GRECH1-17
kind: problem
title: Simplify an expression with logarithmic exponents
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
  note: Re-transcribed from Chapter 1 review Question 17 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription. The book extraction read log_x x; the chapter-1.pdf extraction and the definition A = a^2 give log_A x.
---

::: {.problem}
If $a$ and $x$ are positive numbers and $A = a^2$, express the following in its simplest form in terms of $x$:

$$
a^{(\log_a x) + (\log_A x)}
$$

(A) $2x$
(B) $x^2$
(C) $\sqrt{x}$
(D) $x^3$
(E) $x\sqrt{x}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

$\log_A x=\frac12\log_a x$.


::: pf-proof

Since $A=a^2$, the change-of-base formula gives
$$
\log_A x
=\frac{\log_a x}{\log_a(a^2)}
=\frac{\log_a x}{2}.
$$
Here the logarithms are understood on their usual domains, so in particular $a\ne1$.

:::

:::

::: {.pf-step #s1-2}

The exponent simplifies to
$$
(\log_a x)+(\log_A x)=\frac32\log_a x.
$$


::: pf-proof

Substitute the identity from step [](#s1-1){.pf-ref}:
$$
\log_a x+\frac12\log_a x=\frac32\log_a x.
$$

:::

:::

::: {.pf-step #s1-3}

The expression is
$$
\boxed{x\sqrt{x}},
$$
so the answer is (E).


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
a^{(\log_a x)+(\log_A x)}
=a^{\frac32\log_a x}
=\left(a^{\log_a x}\right)^{3/2}
=x^{3/2}
=x\sqrt{x},
$$
where $x>0$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested simplified form and corresponding choice.

:::

:::

:::
