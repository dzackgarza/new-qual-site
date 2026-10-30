---
schema: qual/card@1
id: P-GRECH2-23
kind: problem
title: Rate of change of a circle's area with shrinking radius
classification:
  areas: [prelim]
  topics:
  - Related Rates
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 23 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
The radius of a circle is decreasing at a rate of 0.5 cm per second. At what rate, in cm$^2$/sec, is the circle's area decreasing when the radius is 4 cm?

(A) $4\pi$
(B) $2\pi$
(C) $\pi$
(D) $\frac{1}{2}\pi$
(E) $\frac{1}{4}\pi$
:::

::: {.solution}

Let $r(t)$ be the radius and $A(t)=\pi r(t)^2$ the area.

::: pf

::: {.pf-step #s1-1}

The area satisfies
$$
\frac{dA}{dt}=2\pi r\frac{dr}{dt}.
$$


::: pf-proof

Differentiate the identity $A=\pi r^2$ with respect to time and apply the chain rule.

:::

:::

::: {.pf-step #s1-2}

When $r=4$ cm,
$$
\frac{dA}{dt}=-4\pi\ \mathrm{cm}^2/\mathrm{sec}.
$$


::: pf-proof

Because the radius is decreasing at $0.5$ cm/sec,
$$
\frac{dr}{dt}=-0.5=-\frac12.
$$
Substituting $r=4$ and this value into step [](#s1-1){.pf-ref} gives
$$
\frac{dA}{dt}=2\pi(4)\left(-\frac12\right)=-4\pi.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore the circle's area is decreasing at the rate
$$
\boxed{4\pi\ \mathrm{cm}^2/\mathrm{sec}},
$$
so the answer is (A).


::: pf-proof

Step [](#s1-2){.pf-ref} gives the signed rate of change as $-4\pi$. Thus the positive magnitude of the rate of decrease is $4\pi$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested rate of decrease and corresponding choice.

:::

:::

:::
