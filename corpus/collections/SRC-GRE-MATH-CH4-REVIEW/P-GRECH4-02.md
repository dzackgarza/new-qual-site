---
schema: qual/card@1
id: P-GRECH4-02
kind: problem
title: Exponential bacterial growth constant
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 4 review Question 2 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch4-review/, replacing the earlier chapter-4.pdf transcription.
---

::: {.problem}
A population of bacteria grows at a rate proportional to the number present. After two hours, the population has tripled. After two more hours elapse, the population will have increased by a factor of $k$. What is the value of $k$?

(A) $6$
(B) $8$
(C) $9$
(D) $27$
(E) $81$
:::

::: pf

::: pf-step

If $N(t)$ denotes the population at time $t$, then
$$
N(t)=N(0)e^{ct}
$$
for some constant $c$.


::: pf-proof

The hypothesis that the growth rate is proportional to the population means
$$
N'(t)=cN(t)
$$
for a constant $c$. Separating variables and integrating gives
$$
\frac{dN}{N}=c\,dt,
\qquad
\log N=ct+C,
$$
and hence $N(t)=Ae^{ct}$. Evaluating at $t=0$ gives $A=N(0)$.

:::

:::

::: pf-step

The tripling condition implies
$$
e^{2c}=3.
$$


::: pf-proof

By step <1>1,
$$
3N(0)=N(2)=N(0)e^{2c}.
$$
Since the population is nonzero, division by $N(0)$ gives the displayed identity.

:::

:::

::: pf-step

After four hours the population has increased by the factor
$$
\boxed{k=9},
$$
so the answer is (C).


::: pf-proof

Using steps <1>1 and <1>2,
$$
\frac{N(4)}{N(0)}
=e^{4c}
=(e^{2c})^2
=3^2
=9.
$$

:::

:::

::: pf-qed

Step <1>3 gives the requested growth factor and corresponding choice.

:::

:::
