---
schema: qual/card@1
id: P-GRECH1-22
kind: problem
title: Domain of $\log(\sin x)$
classification:
  areas:
  - algebra
  topics:
  - Trigonometric Functions
  - Exponential and Logarithmic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 1 review Question 22 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription. The book extraction read '1111 is just slightly greater than 353.64 x pi'; the chapter-1.pdf extraction and the book's solution read '111 is just slightly greater than 35 pi'.
---

::: {.problem}
Which one of the following is in the domain of the function $f(x) = \log(\sin x)$? (You may use the fact that $111$ is just slightly greater than $35\pi$.)

(A) $11$
(B) $111$
(C) $1111$
(D) 11,111
(E) None of these
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A real number $t$ lies in the domain of $f$ exactly when $\sin t>0$.


::: pf-proof

The real logarithm $\log u$ is defined exactly for $u>0$. Therefore $\log(\sin t)$ is defined exactly when $\sin t>0$.

:::

:::

::: {.pf-step #s1-2}

The four candidates lie in the intervals
$$
3\pi<11<4\pi,\qquad
35\pi<111<36\pi,
$$
$$
353\pi<1111<354\pi,\qquad
3536\pi<11111<3537\pi.
$$


::: pf-proof

Using the standard decimal bounds $3.1415<\pi<3.1416$ gives
$$
3\pi<9.4248<11<12.566<4\pi,
$$
$$
35\pi<109.956<111<113.094<36\pi,
$$
$$
353\pi<1108.9848<1111<1112.091<354\pi,
$$
and
$$
3536\pi<11108.6976<11111<11111.4855<3537\pi.
$$

:::

:::

::: {.pf-step #s1-3}

Among the listed numbers, only $11111$ has positive sine.


::: pf-proof

Sine is negative on $(m\pi,(m+1)\pi)$ when $m$ is odd and positive there when $m$ is even. In step [](#s1-2){.pf-ref}, the first three left endpoints have odd indices $3$, $35$, and $353$, while the last has even index $3536$. Hence the first three sines are negative and $\sin(11111)>0$.

:::

:::

::: {.pf-step #s1-4}

The answer is
$$
\boxed{11111},
$$
namely choice (D).


::: pf-proof

Combine step [](#s1-1){.pf-ref} with step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} identifies the unique listed input in the domain of $f$.

:::

:::

:::
