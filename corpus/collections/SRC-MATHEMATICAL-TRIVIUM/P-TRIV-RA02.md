---
schema: qual/card@1
id: P-TRIV-RA02
kind: problem
title: Derivative of $x^x$
classification:
  areas: [real-analysis]
  topics:
  - Derivatives
  - Logarithmic Differentiation
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 2, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash reads `Find f(x), if f(x)=x^x`; any missing derivative mark in the source prompt is unresolved and is not silently supplied.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost prime in f'(x) against Real Analysis Problem 2 on page 8 of the source PDF.
---

::: {.problem}
Find $f'(x)$, if $f(x) = x^x$.
:::

::: {.solution}

Assume $x>0$ so that the real logarithm is defined.

::: pf

::: {.pf-step #s1-1}

Write
$$
f(x)=x^x=e^{x\log x}.
$$


::: pf-proof

For $x>0$,
$$
x^x=e^{\log(x^x)}=e^{x\log x}.
$$

:::

:::

::: {.pf-step #s1-2}

Differentiate the exponent:
$$
\frac{d}{dx}(x\log x)=\log x+1.
$$


::: pf-proof

By the product rule,
$$
\frac{d}{dx}(x\log x)
=
\log x+x\frac1x
=
\log x+1.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{f'(x)=x^x(\log x+1)}.
$$


::: pf-proof

Apply the chain rule to the representation in step [](#s1-1){.pf-ref} and use step [](#s1-2){.pf-ref}:
$$
f'(x)
=
e^{x\log x}(\log x+1)
=
x^x(\log x+1).
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required derivative.

:::

:::

:::
