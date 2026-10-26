---
schema: qual/card@1
id: P-GREPT-14
kind: problem
title: "Nonzero solutions of $y''=(y')^2$"
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
---

::: {.problem}
Find the family of all nonzero solutions of the equation

$$\frac{d^2y}{dx^2} = \left(\frac{dy}{dx}\right)^2$$

(A) $y = \frac{1}{x + c_1} + c_2$
(B) $y = c_2 + \log(c_1 - x)$
(C) $y = c_2 - \log(c_1 - x^2)$
(D) $y = c_2 + \log(c_1 + x)$
(E) $y = c_2 - \log(c_1 + x)$
:::

::: pf

::: pf-step

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

::: pf-step

Every constant function
$$
y\equiv C
$$
is a solution.


::: pf-proof

For a constant function, $y'=0$ and $y''=0$, so both sides of
$y''=(y')^2$ are zero. In particular, every $C\ne0$ gives a nonzero solution
of the equation as printed.

:::

:::

::: pf-step

Every nonconstant real solution on a connected interval has the form
$$
y=C_2-\log|x+C_1|,
$$
where the interval does not contain $-C_1$.


::: pf-proof

For a nonconstant solution, $u=y'$ cannot vanish at a point: the initial-value
problem $u'=u^2$, $u(x_0)=0$ has the unique solution $u\equiv0$, which would
make $y$ constant. Hence $u$ is nowhere zero. Separating variables in step
<1>1 gives
$$
\frac{du}{u^2}=dx,
$$
so
$$
-\frac1u=x+C_1
\qquad\text{and hence}\qquad
u=-\frac1{x+C_1}.
$$
Integrating once more gives
$$
y=C_2-\log|x+C_1|.
$$

:::

:::

::: pf-step

Therefore
$$
\boxed{\text{none of the listed choices gives all nonzero solutions}}
$$
for the problem as stated.


::: pf-proof

Step <1>2 shows that $y\equiv1$, for example, is a nonzero solution. Every
listed choice (A)--(E) is a nonconstant family and therefore omits this
solution. Step <1>3 gives the remaining nonconstant solutions.

:::

:::

::: pf-qed

Steps <1>2--<1>4 classify the literal solutions and prove that no listed
answer is complete.

:::

:::

::: {.remark}
The source selects (E) after explicitly discarding the solution $u=y'\equiv0$.
If the question is instead read as asking only for nonconstant solutions and
one works on an interval where $x+C_1>0$, step <1>3 becomes
$y=C_2-\log(x+C_1)$, which is choice (E).
:::
