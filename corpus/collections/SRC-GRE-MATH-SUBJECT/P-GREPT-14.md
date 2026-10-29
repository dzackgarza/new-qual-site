---
schema: qual/card@1
id: P-GREPT-14
kind: problem
title: "Nonconstant solutions of $y''=(y')^2$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 14 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source asked for all nonzero solutions, but nonzero constants are solutions that no choice lists; the source answer (E) discards y' = 0. The statement now asks for the nonconstant solutions.
---

::: {.problem}
Find the family of all nonconstant solutions of the equation

$$\frac{d^2y}{dx^2} = \left(\frac{dy}{dx}\right)^2$$

(A) $y = \frac{1}{x + c_1} + c_2$
(B) $y = c_2 + \log(c_1 - x)$
(C) $y = c_2 - \log(c_1 - x^2)$
(D) $y = c_2 + \log(c_1 + x)$
(E) $y = c_2 - \log(c_1 + x)$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

With
$$
u=y',
$$
the differential equation becomes
$$
u'=u^2.
$$


::: pf-proof

By definition $u'=y''$, while $u^2=(y')^2$, so the two equations are
equivalent.

:::

:::

::: {.pf-step #s1-2}

Every nonconstant solution on an interval on which $x+C_1>0$ has the form
$$
y=C_2-\log(x+C_1).
$$


::: pf-proof

For a nonconstant solution, $u=y'$ cannot vanish at a point: the initial-value
problem $u'=u^2$, $u(x_0)=0$ has the unique solution $u\equiv0$, which would
make $y$ constant. Hence $u$ is nowhere zero. Separating variables in step
[](#s1-1){.pf-ref} gives
$$
\frac{du}{u^2}=dx,
$$
so
$$
-\frac1u=x+C_1
\qquad\text{and hence}\qquad
u=-\frac1{x+C_1}.
$$
Integrating once more gives $y=C_2-\log|x+C_1|$, which is
$y=C_2-\log(x+C_1)$ where $x+C_1>0$. Conversely, this function satisfies
$y'=-1/(x+C_1)$ and $y''=1/(x+C_1)^2=(y')^2$.

:::

:::

::: {.pf-step #s1-3}

The answer is $\boxed{\text{(E)}}$.


::: pf-proof

Choice (E) is the family of step [](#s1-2){.pf-ref}. Choices (A), (B), (C) and (D)
fail: for (A), $y''=2/(x+c_1)^3$ while $(y')^2=1/(x+c_1)^4$; for (B), $y'=-1/(c_1-x)$ and
$y''=-1/(c_1-x)^2\ne(y')^2$; for (D), $y''=-1/(c_1+x)^2\ne(y')^2$; for (C),
$y'=2x/(c_1-x^2)$ and $y''=2(c_1+x^2)/(c_1-x^2)^2$, while $(y')^2=4x^2/(c_1-x^2)^2$, and these differ at $x=0$ whenever $c_1\ne0$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} finds all nonconstant solutions, and step [](#s1-3){.pf-ref} identifies them with choice (E).

:::

:::

:::
