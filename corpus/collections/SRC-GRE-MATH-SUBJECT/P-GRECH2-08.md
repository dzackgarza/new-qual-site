---
schema: qual/card@1
id: P-GRECH2-08
kind: problem
title: Domain of $\arcsin(\log\sqrt x)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 8 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Determine the domain of the following function:

$$
f(x) = \arcsin(\log \sqrt{x})
$$

(A) $[0, \frac{1}{e^2}]$
(B) $[\frac{1}{e^2}, 1]$
(C) $[e, e^2]$
(D) $[\frac{1}{e^2}, e^2]$
(E) $[1, e^2]$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The inverse-sine condition is
$$
-1\leq \log\sqrt{x}\leq1.
$$


::: pf-proof

The inner expression $\log\sqrt{x}$ first requires $x>0$. On that domain, the real function $\arcsin u$ is defined exactly for $u\in[-1,1]$, which gives the displayed inequalities. Step [](#s1-2){.pf-ref} will show that those inequalities force $x\ge e^{-2}>0$, so no additional domain restriction remains.

:::

:::

::: {.pf-step #s1-2}

The condition in step [](#s1-1){.pf-ref} is equivalent to
$$
e^{-2}\leq x\leq e^2.
$$


::: pf-proof

Exponentiation is increasing, so step [](#s1-1){.pf-ref} gives
$$
e^{-1}\leq\sqrt{x}\leq e.
$$
All three quantities are positive, hence squaring preserves the inequalities:
$$
e^{-2}\leq x\leq e^2.
$$

:::

:::

::: {.pf-step #s1-3}

The domain is
$$
\boxed{\left[\frac1{e^2},e^2\right]},
$$
so the answer is (D).


::: pf-proof

Step [](#s1-2){.pf-ref} gives exactly the set of real $x$ for which every operation in $f(x)$ is defined.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested domain and corresponding choice.

:::

:::

:::
