---
schema: qual/card@1
id: P-GREPT-57
kind: problem
title: "Flaw in a proof of Cauchy's mean value formula"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 57 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Cauchy's Mean-Value formula says that if $f$ and $g$ are two functions that are continuous on the nonempty, closed interval $[a, b]$ and differentiable on $(a, b)$, then there exists at least one number $c$, with $a < c < b$, such that:

$$g'(c)[f(b) - f(a)] = f'(c)[g(b) - g(a)]$$

Consider the following argument:

(1) "The functions $f$ and $g$ in the result above satisfy the hypotheses of the Mean-Value theorem, so there exists a number $c$, with $a < c < b$, such that

$$f'(c) = \frac{f(b) - f(a)}{b - a} \quad \text{and} \quad g'(c) = \frac{g(b) - g(a)}{b - a}.\text{"}$$

(2) "The equations in Step (1) imply that

$$b - a = \frac{f(b) - f(a)}{f'(c)} \quad \text{and} \quad b - a = \frac{g(b) - g(a)}{g'(c)}.\text{"}$$

(3) "The equations in Step (2) imply that

$$\frac{f(b) - f(a)}{f'(c)} = \frac{g(b) - g(a)}{g'(c)}.\text{"}$$

(4) "Cross multiplying, we get $g'(c)[f(b) - f(a)] = f'(c)[g(b) - g(a)]$."

Which of the following statements is/are true?

I. Step (1) is not valid.

II. The conclusion of Step (1) does not imply the result of Step (2).

III. The conclusion of Step (2) does not imply the result of Step (3).

IV. The conclusion of Step (3) does not imply the result of Step (4).

(A) I only
(B) II only
(C) I and II only
(D) IV only
(E) None are true; the argument is a valid proof of Cauchy's Mean-Value formula.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Statement I is true: Step (1) is not valid.


::: pf-proof

The ordinary mean-value theorem applied separately to $f$ and $g$ may
produce different points. For example, on $[0,1]$, take $f(x)=x^2$ and
$g(x)=x^3$. The equation required for $f$ in Step (1) is $2c=1$, so it
forces $c=1/2$. The equation required for $g$ is $3c^2=1$, so for
$0<c<1$ it forces $c=3^{-1/2}$. These points are distinct. Thus the two
separate applications of the mean-value theorem do not justify the
existence of one $c$ satisfying both equations.

:::

:::

::: {.pf-step #s1-2}

Statement II is true: even if the conclusion of Step (1) holds,
it need not imply Step (2).


::: pf-proof

Passing from Step (1) to Step (2) divides by $f'(c)$ and $g'(c)$, but
Step (1) does not assert that these derivatives are nonzero. For
example, on $[0,1]$, let $f(x)=0$ and $g(x)=x$. Every $c$ in $(0,1)$
satisfies both equations in Step (1): the derivative and secant slope
of $f$ are both $0$, while the derivative and secant slope of $g$ are
both $1$. The first displayed quotient in Step (2) would then be
$0/0$, which is undefined. Hence Step (1) does not imply Step (2).

:::

:::

::: {.pf-step #s1-3}

Statements III and IV are false.


::: pf-proof

If the equations in Step (2) hold, then both displayed quotients are
defined and both equal $b-a$; therefore they are equal, which is
exactly Step (3). Moreover, the quotients in Step (3) being defined
means that both denominators are nonzero. Multiplying its equality by
$f'(c)g'(c)$ therefore gives
$$
g'(c)[f(b)-f(a)]=f'(c)[g(b)-g(a)],
$$
which is Step (4).

:::

:::

::: {.pf-step #s1-4}

Therefore the correct answer is $\boxed{\text{(C) I and II only}}$.


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} prove I and II, while step [](#s1-3){.pf-ref} proves that III and IV
are false.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required choice.

:::

:::

:::
