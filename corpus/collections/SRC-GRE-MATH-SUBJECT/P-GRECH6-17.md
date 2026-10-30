---
schema: qual/card@1
id: P-GRECH6-17
kind: problem
title: Which listed rings are integral domains
classification:
  areas:
  - algebra
  topics:
  - Integral Domains
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Re-transcribed from Chapter 6 review Question 17 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), compared with assets/attachments/chapter-6_extracted.md, replacing the earlier paraphrased transcription. The book extraction garbles the ring in item III as Z_p^b; the chapter-6.md extraction reads Z_{p^2}, and the book's Chapter 8 solution discusses Z_{p^2}."
---

::: {.problem}
Which of the following rings are integral domains?

I. $\ZZ \oplus \ZZ$

II. $\ZZ_p$, where $p$ is a prime

III. $\ZZ_{p^2}$, where $p$ is a prime

(A) I and II only
(B) II only
(C) II and III only
(D) III only
(E) I and III only
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The ring $\ZZ\oplus\ZZ$ is not an integral domain.


::: pf-proof

The nonzero elements $(1,0)$ and $(0,1)$ satisfy
$$
(1,0)(0,1)=(0,0),
$$
so $\ZZ\oplus\ZZ$ has zero divisors.

:::

:::

::: {.pf-step #s1-2}

The ring $\ZZ_p$ is an integral domain when $p$ is prime.


::: pf-proof

Suppose $\overline a\,\overline b=\overline0$ in $\ZZ_p$. Then $p\mid ab$. Since $p$ is prime, Euclid's lemma gives $p\mid a$ or $p\mid b$, so $\overline a=\overline0$ or $\overline b=\overline0$. Thus $\ZZ_p$ has no zero divisors. It is commutative and has identity, so it is an integral domain.

:::

:::

::: {.pf-step #s1-3}

The ring $\ZZ_{p^2}$ is not an integral domain.


::: pf-proof

The residue class $\overline p$ is nonzero modulo $p^2$, but
$$
\overline p\,\overline p=\overline{p^2}=\overline0.
$$
Hence $\overline p$ is a nonzero zero divisor.

:::

:::

::: {.pf-step #s1-4}

Therefore the only integral domain listed is
$$
\boxed{\text{II only}},
$$
so the answer is (B).


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} show that I and III are not integral domains and II is an integral domain.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required choice.

:::

:::

:::
