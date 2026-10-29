---
schema: qual/card@1
id: P-GRECH6-10
kind: problem
title: Inverse under a logarithmic group operation
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
  note: "Re-transcribed from Chapter 6 review Question 10 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), compared with assets/attachments/chapter-6_extracted.md, replacing the earlier paraphrased transcription."
---

::: {.problem}
If $S = \{a \in \RR^+ : a \neq 1\}$, with the binary operation $\bullet$ defined by the equation $a \bullet b = a^{\log b}$ (where $\log b = \log_e b$), then $(S, \bullet)$ is a group. What is the inverse of $a \in S$?

(A) $\frac{1}{e \log a}$
(B) $\frac{e}{\log a}$
(C) $e^{-\log a}$
(D) $e^{\log(1/a)}$
(E) $e^{1/\log a}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The identity element of $(S,\bullet)$ is $e$.


::: pf-proof

For every $a\in S$,
$$
a\bullet e=a^{\log e}=a
$$
and
$$
e\bullet a=e^{\log a}=a.
$$
Thus $e$ is a two-sided identity.

:::

:::

::: {.pf-step #s1-2}

If $b$ is the inverse of $a$, then
$$
\log b=\frac1{\log a}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, an inverse must satisfy $a\bullet b=e$. Taking natural logarithms in
$$
a^{\log b}=e
$$
gives
$$
(\log a)(\log b)=1.
$$
Because $a\ne1$, one has $\log a\ne0$, so division by $\log a$ yields the displayed equation.

:::

:::

::: {.pf-step #s1-3}

The inverse of $a$ is
$$
\boxed{e^{1/\log a}},
$$
so the answer is (E).


::: pf-proof

Step [](#s1-2){.pf-ref} gives $b=e^{1/\log a}$. Since $1/\log a\ne0$, this number is positive and not equal to $1$, so $b\in S$. Moreover,
$$
a\bullet b
=\exp\bigl((\log a)(\log b)\bigr)
=e,
$$
and the same symmetric expression gives $b\bullet a=e$. Hence $b$ is the inverse of $a$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives and verifies the required inverse.

:::

:::

:::
