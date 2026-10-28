---
schema: qual/card@1
id: P-GRECH7-27
kind: problem
title: Contour integral of $(z+1)/((z+3)(z^2+1))$ over a drawn curve
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 27 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. The figure was not recovered by either extraction.
---

::: {.problem}
What's the value of the integral $\int_{C} \frac{z+1}{(z+3)(z^2+1)} dz$ where C is the curve shown below?

(A) $\frac{4}{5}\pi i$
(B) $\frac{2}{5}\pi i - \frac{1}{5}$
(C) $\frac{4}{5}\pi i - \frac{1}{5}$
(D) $\frac{2}{5}\pi i$
(E) $-\frac{2}{5}\pi i$
:::

::: {.remark}
The source shows the curve $C$ in a figure that is not reproduced here.
:::

::: {.solution}

Let
$$
f(z)=\frac{z+1}{(z+3)(z^2+1)}
=\frac{z+1}{(z+3)(z-i)(z+i)}.
$$

::: pf

::: {.pf-step #s1-1}

The source figure shows $C$ oriented counterclockwise and enclosing the poles $i$ and $-i$, while the pole $-3$ lies outside.


::: pf-proof

The arrow on the upper-right portion of the drawn curve points from right to left, which is the counterclockwise orientation. The points $i$ and $-i$ lie inside the drawn loop, whereas $-3$ lies to the left of the loop.

:::

:::

::: {.pf-step #s1-2}

The residue of $f$ at $i$ is
$$
\operatorname{Res}(f;i)=\frac{1-2i}{10}.
$$


::: pf-proof

Because $i$ is a simple pole,
$$
\operatorname{Res}(f;i)
=\frac{i+1}{(i+3)(i+i)}
=\frac{1+i}{-2+6i}.
$$
Multiplying numerator and denominator by $-2-6i$ gives
$$
\frac{(1+i)(-2-6i)}{(-2)^2+6^2}
=\frac{4-8i}{40}
=\frac{1-2i}{10}.
$$

:::

:::

::: {.pf-step #s1-3}

The residue of $f$ at $-i$ is
$$
\operatorname{Res}(f;-i)=\frac{1+2i}{10}.
$$


::: pf-proof

Similarly,
$$
\operatorname{Res}(f;-i)
=\frac{1-i}{(3-i)(-2i)}
=\frac{1-i}{-2-6i}.
$$
Multiplying numerator and denominator by $-2+6i$ gives
$$
\frac{(1-i)(-2+6i)}{40}
=\frac{4+8i}{40}
=\frac{1+2i}{10}.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\int_C f(z)\,dz
=\boxed{\frac{2}{5}\pi i},
$$
so the answer is (D).


::: pf-proof

By the residue theorem and step [](#s1-1){.pf-ref},
$$
\int_C f(z)\,dz
=2\pi i\left(\operatorname{Res}(f;i)+\operatorname{Res}(f;-i)\right).
$$
Using steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}, the sum of residues is
$$
\frac{1-2i}{10}+\frac{1+2i}{10}=\frac15,
$$
which yields $2\pi i/5$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested contour integral.

:::

:::

:::
