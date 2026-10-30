---
schema: qual/card@1
id: P-GRECH4-10
kind: problem
title: Integrating factor of monomial form
classification:
  areas:
  - real-analysis
  topics:
  - Integrating Factors
  - Exact Equations
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 4 review Question 10 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch4-review/, replacing the earlier chapter-4.pdf transcription.
---

::: {.problem}
Given that the following differential equation has an integrating factor of the form $\mu(x, y) = x^my^n$, determine its general solution.

$$
(3xy^2 - 5y)\,dx + (2x^2y - 3x)\,dy = 0
$$

(A) $x^4y^2(\frac{1}{2}xy - 1) = c$
(B) $x^4y^2(xy - 1) = c$
(C) $x^4y^2(2xy - 1) = c$
(D) $x^5y^3(\frac{1}{2}xy - 1) = c$
(E) $x^5y^3(2xy - 1) = c$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Exactness after multiplication by $\mu=x^my^n$ requires
$$
3(n+2)=2(m+2),
\qquad
5(n+1)=3(m+1).
$$


::: pf-proof

After multiplication, the differential form has coefficients
$$
\overline M
=3x^{m+1}y^{n+2}-5x^my^{n+1}
$$
and
$$
\overline N
=2x^{m+2}y^{n+1}-3x^{m+1}y^n.
$$
Hence
$$
\overline M_y
=3(n+2)x^{m+1}y^{n+1}
-5(n+1)x^my^n
$$
and
$$
\overline N_x
=2(m+2)x^{m+1}y^{n+1}
-3(m+1)x^my^n.
$$
Equating the coefficients of the two monomials gives the displayed system.

:::

:::

::: {.pf-step #s1-2}

The integrating factor exponents are
$$
m=4,\qquad n=2.
$$


::: pf-proof

The equations in step [](#s1-1){.pf-ref} are
$$
2m-3n=2,
\qquad
3m-5n=2.
$$
Subtracting suitable multiples gives $n=2$, and then $m=4$.

:::

:::

::: {.pf-step #s1-3}

A potential for the resulting exact differential form is
$$
F(x,y)=\frac12x^6y^4-x^5y^3.
$$


::: pf-proof

With the exponents from step [](#s1-2){.pf-ref},
$$
\overline M=3x^5y^4-5x^4y^3.
$$
Integrating with respect to $x$ gives
$$
F(x,y)
=\frac12x^6y^4-x^5y^3+h(y).
$$
Its $y$-derivative is
$$
F_y
=2x^6y^3-3x^5y^2+h'(y).
$$
But
$$
\overline N=2x^6y^3-3x^5y^2,
$$
so $h'(y)=0$, and a constant may be absorbed into the final level constant.

:::

:::

::: {.pf-step #s1-4}

The general integral is
$$
\boxed{x^5y^3\left(\frac12xy-1\right)=c},
$$
so the answer is (D).


::: pf-proof

Integral curves of the exact equation satisfy $F(x,y)=c$. Factoring the potential from step [](#s1-3){.pf-ref} gives
$$
F(x,y)
=x^5y^3\left(\frac12xy-1\right).
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested general solution and corresponding choice.

:::

:::

:::
