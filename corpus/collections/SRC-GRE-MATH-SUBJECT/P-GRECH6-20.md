---
schema: qual/card@1
id: P-GRECH6-20
kind: problem
title: Which listed subsets are subfields of $\CC$
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Subfields
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Re-transcribed from Chapter 6 review Question 20 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), compared with assets/attachments/chapter-6_extracted.md, replacing the earlier paraphrased transcription. The book extraction prints item I as a + b sqrt(3); the chapter-6.md extraction and the book's Chapter 8 solution read a + b sqrt(2/3), which is kept."
---

::: {.problem}
Which of the following are subfields of $\CC$?

I. $K_1 = \{a + b\sqrt{2/3} : a, b \in \QQ\}$

II. $K_2 = \{a + b\sqrt{2} : a, b \in \QQ \text{ and } ab < \sqrt{2}\}$

III. $K_3 = \{a + bi : a, b \in \ZZ \text{ and } i = \sqrt{-1}\}$

(A) I only
(B) I and II only
(C) III only
(D) I and III only
(E) None of the $K_i$ are subfields of $\CC$.
:::

::: {.solution}

::: pf

::: pf-step

The set $K_1$ equals $\QQ(\sqrt6)=\{a+b\sqrt6:a,b\in\QQ\}$.


::: pf-proof

Since
$$
\sqrt{\frac23}=\frac{\sqrt6}{3},
$$
every element $a+b\sqrt{2/3}$ can be written as $a+(b/3)\sqrt6$. Conversely,
$$
a+c\sqrt6=a+(3c)\sqrt{\frac23},
$$
so the two displayed sets coincide.

:::

:::

::: {.pf-step #s1-2}

The set $K_1$ is a subfield of $\CC$.


::: pf-proof

It contains $0$ and $1$, and it is closed under addition, subtraction, and multiplication because
$$
(a+b\sqrt6)(c+d\sqrt6)
=(ac+6bd)+(ad+bc)\sqrt6.
$$
If $a+b\sqrt6\ne0$, then
$$
\frac1{a+b\sqrt6}
=\frac{a-b\sqrt6}{a^2-6b^2}.
$$
The denominator is nonzero: otherwise, if $b\ne0$, then $(a/b)^2=6$, contradicting the irrationality of $\sqrt6$, while if $b=0$ then $a=0$, contrary to the element being nonzero. Thus the inverse again has rational coefficients and lies in $K_1$.

:::

:::

::: {.pf-step #s1-3}

The set $K_2$ is not a subfield of $\CC$.


::: pf-proof

The element
$$
u=1+\sqrt2
$$
lies in $K_2$ because its coefficients satisfy $1\cdot1<\sqrt2$. But
$$
u+u=2+2\sqrt2
$$
does not lie in $K_2$, since $2\cdot2=4>\sqrt2$. Hence $K_2$ is not closed under addition.

:::

:::

::: {.pf-step #s1-4}

The set $K_3$ is not a subfield of $\CC$.


::: pf-proof

The nonzero element $1+i$ lies in $K_3$, but
$$
(1+i)^{-1}=\frac{1-i}{2}=\frac12-\frac12 i
$$
does not lie in $K_3$ because its real and imaginary coefficients are not integers. Thus $K_3$ is not closed under inverses of nonzero elements.

:::

:::

::: {.pf-step #s1-5}

Therefore the listed subfields are
$$
\boxed{\text{I only}},
$$
so the answer is (A).


::: pf-proof

Step [](#s1-2){.pf-ref} proves that $K_1$ is a subfield, while steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} rule out $K_2$ and $K_3$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the required choice.

:::

:::

:::
