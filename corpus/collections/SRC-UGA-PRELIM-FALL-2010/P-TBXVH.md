---
schema: qual/card@1
id: P-TBXVH
kind: problem
title: The $\varepsilon$-$\delta$ definition of $\lim_{x\to a}f(x)=\ell$, and $\lim_{x\to
  2}\frac{2x+1}{x^2+1}$
classification:
  areas:
  - prelim
  topics:
  - Limits
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the card's prose answer into Lamport steps, with the parts of the estimate
    that the prose passed over made explicit: that the candidate limit is 1 because the
    rational function is continuous at 2 and its denominator does not vanish there; that the
    error factors as |x| |x-2| over x^2+1; that |x-2| < 1 gives both |x| < 3 and x^2+1 >= 1,
    so the two bounds multiply; and that the resulting delta = min{1, eps/3} is positive.
    One point of the printed part (a) is now stated as such: the definition excludes x = a,
    which is why the display uses 0 < |x-a|. The statement was not re-read against the exam
    scan in this pass: the collection's provenance,
    assets/attachments/grad_prelim_Fall10.pdf, is a scan with no text layer, and the
    statement is left as the card carries it.
---

::: {.problem}
Suppose $f: \RR \to \RR$.

(a) Give the $\delta$-$\varepsilon$ definition of $\lim_{x \to a} f(x) = \ell$.

(b) Determine the limit and use the definition to prove your answer: $$\lim_{x \to 2} \frac{2x+1}{x^2+1} = ?$$
:::

::: {.solution}
No retained solution set covers this problem — the collection's provenance, `assets/attachments/grad_prelim_Fall10.pdf`, is the examination paper — so the argument is the card's own, in the form the exercise prescribes: the limit is identified and then verified from the definition.

::: pf

::: {.pf-step #definition}
(a) $\lim_{x\to a}f(x)=\ell$ means: for every $\varepsilon>0$ there is $\delta>0$ such that every $x$ with $0<\abs{x-a}<\delta$ satisfies $\abs{f(x)-\ell}<\varepsilon$.

::: pf-proof
This is the definition: the inequality on $f$ is required only on a punctured neighbourhood of $a$, so the value $f(a)$ plays no role and $f$ need not even be defined at $a$; that is why the hypothesis is written $0<\abs{x-a}$ rather than $\abs{x-a}<\delta$.
:::

:::

::: {.pf-step #candidate}
(b) The value of the expression at $x=2$ is $\frac{2\cdot2+1}{2^2+1}=\frac55=1$, and $1$ is the limit.

::: pf-proof
The numerator and denominator are polynomials, hence continuous, and the denominator $x^2+1$ is at least $1$ and in particular nonzero at $x=2$; a quotient of continuous functions with nonvanishing denominator is continuous at the point, so the limit equals the value computed above. This identifies the candidate; the next steps verify it from the definition of part (a), as the exercise requires.
:::

:::

::: {.pf-step #error}
For $x\neq2$, $\abs{\frac{2x+1}{x^2+1}-1}=\frac{\abs{x}\abs{x-2}}{x^2+1}$.

::: pf-proof
Putting the difference over the common denominator,
$\frac{2x+1}{x^2+1}-1=\frac{2x+1-(x^2+1)}{x^2+1}=\frac{2x-x^2}{x^2+1}=\frac{-x(x-2)}{x^2+1}$,
and taking absolute values gives $\frac{\abs{x}\abs{x-2}}{x^2+1}$ because $\abs{-1}=1$ and $\abs{x^2+1}=x^2+1>0$.
:::

:::

::: {.pf-step #estimate}
If $0<\abs{x-2}<1$ then $\abs{\frac{2x+1}{x^2+1}-1}<3\abs{x-2}$.

::: pf-proof
From $\abs{x-2}<1$ we get $\abs x=\abs{(x-2)+2}\le\abs{x-2}+2<3$. Also $x^2+1\ge1$, so $\frac{\abs x}{x^2+1}\le\abs x<3$. Multiplying the estimate of step [](#error){.pf-ref} by that bound, $\abs{\frac{2x+1}{x^2+1}-1}=\frac{\abs x}{x^2+1}\abs{x-2}<3\abs{x-2}$.
:::

:::

::: {.pf-step #delta}
Given $\varepsilon>0$, $\delta=\min\{1,\varepsilon/3\}$ is positive and $0<\abs{x-2}<\delta$ implies $\abs{\frac{2x+1}{x^2+1}-1}<\varepsilon$.

::: pf-proof
$\delta>0$ because both $1$ and $\varepsilon/3$ are positive. If $0<\abs{x-2}<\delta$ then $\abs{x-2}<1$, so step [](#estimate){.pf-ref} applies, and $\abs{x-2}<\varepsilon/3$ by the choice of $\delta$; hence the error is less than $3\cdot\frac\varepsilon3=\varepsilon$.
:::

:::

::: {.pf-step #conclusion}
$\lim_{x\to2}\frac{2x+1}{x^2+1}=1$, proved from the definition of part (a).

::: pf-proof
Steps [](#candidate){.pf-ref} and [](#delta){.pf-ref} supply the limit and, for every $\varepsilon>0$, a $\delta>0$ satisfying the condition of step [](#definition){.pf-ref}. So the limit is $1$ in the sense of the definition, which is what part (b) asks for.
:::

:::

:::
:::
