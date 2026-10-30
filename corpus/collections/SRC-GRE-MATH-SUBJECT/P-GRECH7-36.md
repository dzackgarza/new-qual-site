---
schema: qual/card@1
id: P-GRECH7-36
kind: problem
title: Cauchy integral of $(3z^2+z-4)/(z-3)$ over $\abs{z}=5$
classification:
  areas: [complex-analysis]
  topics:
  - Cauchy Integral Formula
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 36 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Let $C$ be the counterclockwise-oriented circle $\abs{z} = 5$. If $h(a) = \int_C \frac{3z^2 + z - 4}{z - a}$, what is $h(3)$?

(A) $2\pi i$
(B) $16\pi i$
(C) $26\pi i$
(D) $52\pi i$
(E) $56\pi i$
:::

::: {.solution}

Let
$$
f(z)=3z^2+z-4.
$$
Interpreting the displayed contour integral in the standard form $h(a)=\int_C f(z)/(z-a)\,dz$, one has the following.

::: pf

::: {.pf-step #s1-1}

The point $a=3$ lies inside $C$, and $f$ is holomorphic on and inside $C$.


::: pf-proof

The contour is the circle $\abs{z}=5$, so $\abs{3}<5$. The function $f$ is a polynomial, hence entire.

:::

:::

::: {.pf-step #s1-2}

The Cauchy integral formula gives
$$
h(3)=2\pi i\,f(3).
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, all hypotheses of the Cauchy integral formula apply to the positively oriented contour $C$. Therefore
$$
\frac{1}{2\pi i}\int_C\frac{f(z)}{z-3}\,dz=f(3),
$$
which is equivalent to the displayed identity.

:::

:::

::: {.pf-step #s1-3}

One has
$$
f(3)=26.
$$


::: pf-proof

Direct substitution gives
$$
f(3)=3(3^2)+3-4=27+3-4=26.
$$

:::

:::

::: {.pf-step #s1-4}

Hence
$$
\boxed{h(3)=52\pi i},
$$
so the answer is (D).


::: pf-proof

Substitute step [](#s1-3){.pf-ref} into step [](#s1-2){.pf-ref}:
$$
h(3)=2\pi i\cdot26=52\pi i.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested value.

:::

:::

:::
