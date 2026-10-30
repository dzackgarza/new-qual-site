---
schema: qual/card@1
id: P-GRECH2-37
kind: problem
title: Limit of $(\cos x)^{\cot^2 x}$ at $0$
classification:
  areas: [prelim]
  topics:
  - Limits
  - L'Hopital's Rule
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 37 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Evaluate the following limit:

$$
\lim_{x \to 0} (\cos x)^{\cot^2 x}
$$

(A) $\frac{1}{2}$
(B) $\frac{1}{\sqrt{e}}$
(C) $\frac{\sqrt{e}}{2}$
(D) $1$
(E) $\sqrt{e}$
:::

::: {.solution}

For $x$ sufficiently close to $0$, one has $\cos x>0$, so define
$$
y(x)=(\cos x)^{\cot^2x}.
$$

::: pf

::: {.pf-step #s1-1}

The logarithm satisfies
$$
\log y(x)=\frac{\log(\cos x)}{\tan^2x}.
$$


::: pf-proof

Taking logarithms gives
$$
\log y(x)=\cot^2x\,\log(\cos x).
$$
Since $\cot^2x=1/\tan^2x$, this is the displayed quotient.

:::

:::

::: {.pf-step #s1-2}

One has
$$
\lim_{x\to0}\log y(x)=-\frac12.
$$


::: pf-proof

The quotient in step [](#s1-1){.pf-ref} has the form $0/0$. By L'Hôpital's rule,
$$
\begin{aligned}
\lim_{x\to0}\frac{\log(\cos x)}{\tan^2x}
&=\lim_{x\to0}\frac{-\tan x}{2\tan x\sec^2x}\\
&=\lim_{x\to0}-\frac{\cos^2x}{2}\\
&=-\frac12.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{\lim_{x\to0}(\cos x)^{\cot^2x}=\frac1{\sqrt e}},
$$
so the answer is (B).


::: pf-proof

By step [](#s1-2){.pf-ref} and continuity of the exponential function,
$$
\lim_{x\to0}y(x)
=\exp\left(-\frac12\right)
=\frac1{\sqrt e}.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested limit and corresponding choice.

:::

:::

:::
