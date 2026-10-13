---
schema: qual/card@1
id: P-TRIV-RA02
kind: problem
title: Derivative of $x^x$
classification:
  areas: [real-analysis]
  topics: []
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

<1>1. Write
$$
f(x)=x^x=e^{x\log x}.
$$

::: {.proof}
For $x>0$,
$$
x^x=e^{\log(x^x)}=e^{x\log x}.
$$
:::

<1>2. Differentiate the exponent:
$$
\frac{d}{dx}(x\log x)=\log x+1.
$$

::: {.proof}
By the product rule,
$$
\frac{d}{dx}(x\log x)
=
\log x+x\frac1x
=
\log x+1.
$$
:::

<1>3. Therefore
$$
\boxed{f'(x)=x^x(\log x+1)}.
$$

::: {.proof}
Apply the chain rule to the representation in step <1>1 and use step <1>2:
$$
f'(x)
=
e^{x\log x}(\log x+1)
=
x^x(\log x+1).
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required derivative.
:::
:::
