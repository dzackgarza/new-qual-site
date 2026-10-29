---
schema: qual/card@1
id: P-GRECH7-38
kind: problem
title: Probability that one of two geometric-type variables exceeds $2$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 38 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. The two extractions read the domain as Z' and Z*; it is transcribed as the positive integers.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source calls $F_X(t)=1/3^t$ and $F_Y(t)=1/4^t$ distribution functions (they decrease, so they cannot be CDFs), names the second variable $W$, and does not state independence. The statement now gives these as tail probabilities $\Prob(X>t)$, $\Prob(Y>t)$ of independent $X$, $Y$, as the source solution uses them.
---

::: {.problem}
Let $X$ and $Y$ be independent random variables with values in $\ZZ^+$ whose tail probabilities are $\Prob(X>t)=1/3^t$ and $\Prob(Y>t)=1/4^t$ for $t\in\ZZ^+$. What is the probability that at least one of the variables $X$ and $Y$ is greater than $2$?

(A) $5/6$
(B) $64/81$
(C) $1/2$
(D) $17/81$
(E) $1/6$
:::

::: {.solution}

::: pf

::: pf-step

One has
$$
\Prob(X>2\text{ or }Y>2)=\boxed{\frac16},
$$
so the answer is (E).


::: pf-proof

By independence and the given tail probabilities,
$$
\begin{aligned}
\Prob(X>2\text{ or }Y>2)
&=1-\Prob(X\le2,Y\le2)\\
&=1-\Prob(X\le2)\Prob(Y\le2)\\
&=1-\frac89\cdot\frac{15}{16}\\
&=1-\frac56\\
&=\frac16.
\end{aligned}
$$

:::

:::

:::

:::
