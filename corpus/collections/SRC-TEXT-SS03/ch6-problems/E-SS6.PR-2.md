---
schema: qual/card@1
id: E-SS6.PR-2
kind: problem
title: $\zeta(s)=\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}\,dx$ for $\Re(s)>0$
classification:
  areas:
  - complex-analysis
  topics:
  - Zeta Function
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Read against the printed item, Chapter 6, Problem 2 on printed p. 180 (PDF p. 199): the statement
    is the print's, and the asterisk the print sets before "2." is recorded in the remark. The
    summation by parts was checked line by line, including
    $s\int_1^M x^{-s}dx=\frac{s}{s-1}(1-M^{1-s})$ and the cancellation of the $M^{1-s}$ terms. One
    addition: the closing step said "by analytic continuation" without saying why the identity
    extends across $\operatorname{Re}(s)=1$, and the step now records that the right-hand side is
    analytic on $\operatorname{Re}(s)>0$ minus $s=1$ by the uniform convergence already proved, that
    the domain is connected and meets $\operatorname{Re}(s)>1$, and that $s=1$ is excluded because
    both sides have a simple pole there. Not checked: nothing else; the item carries no hint.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Provenance sentence added, which the card lacked: a published solution of this Problem is Wang
    Zirui, *Complete Solutions for Chapter 6*, in the public repository
    `wzr-0831/stein-shakarchi-princeton-lectures-in-analysis-solutions`, read at its Problem 2 and
    checked against Chapter 6, Problem 2: it integrates the counting function $\lfloor x\rfloor=x-\{x\}$
    by parts, giving $\zeta(s)=s\int_1^\infty\lfloor x\rfloor x^{-s-1}dx=s/(s-1)-s\int_1^\infty\{x\}x^{-s-1}dx$.
    That is the card's step s1's identity; the card's later steps supply the uniform convergence and
    the continuation that the published text compresses. Not checked: anything in that document
    outside its Problem 2.
---

::: {.exercise}
Prove that for $\operatorname{Re}(s) > 0$,
$$
\zeta(s) = \frac{s}{s-1} - s \int_1^\infty \frac{\{x\}}{x^{s+1}}\,dx,
$$
where $\{x\} = x - \lfloor x \rfloor$ is the fractional part of $x$.
:::

::: {.remark}
The book marks this problem with an asterisk (Chapter 6, Problem 2). Both sides have a simple pole at $s=1$, so the identity is read on $\operatorname{Re}(s)>0$ with $s\ne1$.
:::

::: {.solution}
A published solution of this Problem is Wang Zirui, *Complete Solutions for Chapter 6* (Problem 2), in the repository `wzr-0831/stein-shakarchi-princeton-lectures-in-analysis-solutions`: it integrates the counting function $\lfloor x\rfloor=x-\{x\}$ by parts, which gives $\zeta(s)=s\int_1^\infty\lfloor x\rfloor x^{-s-1}\,dx=\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}\,dx$ on $\Re(s)>0$. The steps below follow that route and supply the convergence and continuation detail it compresses; the audit trail records the comparison.

::: pf

::: {.pf-step #s1}

The representation holds on $\Re(s)>0$.

::: pf-proof

::: pf-step

For $\Re(s) > 1$ and $M \in \NN$, apply Abel summation (integration by parts):
    $$\sum_{n=1}^M n^{-s} = \int_{1^-}^M x^{-s}\,d\lfloor x \rfloor = \frac{\lfloor M \rfloor}{M^s} + s \int_1^M \frac{\lfloor x \rfloor}{x^{s+1}}\,dx = M^{1-s} + s \int_1^M \frac{x - \{x\}}{x^{s+1}}\,dx.$$

:::

::: pf-step

Split the integral:
    $$s \int_1^M \frac{x}{x^{s+1}}\,dx = s \int_1^M x^{-s}\,dx = s \left[ \frac{x^{1-s}}{1-s} \right]_1^M = \frac{s}{s-1} (1 - M^{1-s}).$$

:::

::: pf-step

Thus
    $$\sum_{n=1}^M n^{-s} = \frac{s}{s-1} + M^{1-s} \left(1 - \frac{s}{s-1}\right) - s \int_1^M \frac{\{x\}}{x^{s+1}}\,dx = \frac{s}{s-1} - \frac{M^{1-s}}{s-1} - s \int_1^M \frac{\{x\}}{x^{s+1}}\,dx.$$

:::

::: pf-step

For $\Re(s) > 1$, as $M \to \infty$, $\abs{M^{1-s}} = M^{1-\Re(s)} \to 0$.

:::

::: pf-step

Because $0 \le \{x\} < 1$, the integral $\int_1^\infty \frac{\{x\}}{x^{s+1}}\,dx$ converges absolutely and uniformly on compact subsets of $\Re(s) > 0$.

:::

::: pf-step

Taking $M \to \infty$ gives $\zeta(s) = \frac{s}{s-1} - s \int_1^\infty \frac{\{x\}}{x^{s+1}}\,dx$ for $\Re(s) > 1$, and by analytic continuation this holds for all $\Re(s) > 0$ with $s \neq 1$.

::: pf-proof

The right-hand side is analytic on $\Re(s)>0$ with $s=1$ removed, by the uniform convergence on compact subsets just recorded, and $\zeta$ is meromorphic there with the simple pole at $s=1$. The domain $\Re(s)>0$, $s\ne1$, is connected and meets $\Re(s)>1$, where the identity was proved, so the identity theorem extends it to the whole domain; at $s=1$ both sides have a simple pole, and the printed claim is read with $s\ne1$ excluded.

:::

:::

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} is the claim.

:::

:::

:::
