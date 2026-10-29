---
schema: qual/card@1
id: P-GRECH2-36
kind: problem
title: Solve an equation defined by nested logarithmic integrals
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 36 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. The chapter extraction read the upper limit as ae; the book's Chapter 8 solution integrates to a^e, the only reading consistent with the listed answers.
---

::: {.problem}
What positive value of $a$ satisfies the following equation?

$$
\int_{e}^{a^e} \frac{dx}{x \int_{a}^{ax} \frac{dy}{y}} = 1
$$

(A) $\frac{1}{e}$
(B) $\sqrt[4]{e}$
(C) $\sqrt{e}$
(D) $e$
(E) $e^2$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $a>0$ and $x>0$,
$$
\int_a^{ax}\frac{dy}{y}=\log x.
$$


::: pf-proof

Direct evaluation gives
$$
\int_a^{ax}\frac{dy}{y}
=\log(ax)-\log a
=\log x.
$$

:::

:::

::: {.pf-step #s1-2}

Any positive $a$ satisfying the equation must have $a>1$, and the equation becomes
$$
\int_e^{a^e}\frac{dx}{x\log x}=1.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives the displayed integrand. If $0<a\le1$, then $a^e\le1$, so the interval from $e$ to $a^e$ reaches the singular point $x=1$ of $1/(x\log x)$; the corresponding improper integral does not converge to a finite value. Hence a solution must satisfy $a>1$, and step [](#s1-1){.pf-ref} reduces the original equation to the displayed one.

:::

:::

::: {.pf-step #s1-3}

The equation in step [](#s1-2){.pf-ref} is equivalent to
$$
\log(e\log a)=1.
$$


::: pf-proof

For $x>1$,
$$
\frac{d}{dx}\log(\log x)=\frac1{x\log x}.
$$
Therefore
$$
\begin{aligned}
1
&=\left[\log(\log x)\right]_e^{a^e}\\
&=\log(\log(a^e))-\log(\log e)\\
&=\log(e\log a),
\end{aligned}
$$
because $\log e=1$.

:::

:::

::: {.pf-step #s1-4}

The unique positive solution is
$$
\boxed{a=e},
$$
so the answer is (D).


::: pf-proof

Exponentiating step [](#s1-3){.pf-ref} gives
$$
e\log a=e,
$$
so $\log a=1$ and hence $a=e$. This value is admissible and therefore is the unique solution.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested positive value and corresponding choice.

:::

:::

:::
