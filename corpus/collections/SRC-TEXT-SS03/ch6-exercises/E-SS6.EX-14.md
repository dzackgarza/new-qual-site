---
schema: qual/card@1
id: E-SS6.EX-14
kind: problem
title: An asymptotic formula for $\log n!$
classification:
  areas:
  - complex-analysis
  topics:
  - Gamma Function
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Repaired a transcription defect in the exercise statement before solving.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained set covers this exercise, so the argument is the
    card's own and the card says so; the printed hint is used exactly where it is needed. Each step
    re-read: Leibniz' rule and Gamma(x+1) = x Gamma(x) give I'(x) = log x and hence
    I(x) = x log x - x + c; monotonicity of Gamma sandwiches log Gamma(n) between I(n-1) and I(n);
    the two bounds are n log n + O(n); and dividing by n log n gives the asymptotic. The
    monotonicity step is stated as the hint's hypothesis, with a one-line reason (log-convexity plus
    Gamma tending to infinity) rather than a proof, and the card says so. Not claimed: Stirling's
    formula or any estimate with a smaller error term.
---

::: {.exercise}
This exercise gives an asymptotic formula for $\log n!$. A more refined asymptotic formula for $\Gamma(s)$ as $s \to \infty$ (Stirling's formula) is given in Appendix A.

(a) Show that
$$
\frac{d}{dx}\int_{x}^{x+1} \log\Gamma(t)\,dt = \log x, \qquad \text{for } x > 0,
$$
and as a result
$$
\int_{x}^{x+1} \log\Gamma(t)\,dt = x\log x - x + c.
$$

(b) Show as a consequence that $\log\Gamma(n) \sim n\log n$ as $n \to \infty$. In fact, prove that $\log\Gamma(n) = n\log n + O(n)$ as $n \to \infty$. [Hint: Use the fact that $\Gamma(x)$ is monotonically increasing for all large $x$.]
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and none was located for this exercise among the retained sets. It is checked against Stein and Shakarchi, Complex Analysis (2003), Chapter 6 Exercise 14, and follows the printed hint.

::: pf

::: {.pf-step #parta}
$\dfrac{d}{dx}\int_{x}^{x+1}\log\Gamma(t)\,dt=\log x$ and $\int_{x}^{x+1}\log\Gamma(t)\,dt=x\log x-x+c$.

::: pf-proof
Let $I(x)=\int_{x}^{x+1}\log\Gamma(t)dt$. Leibniz' rule gives $I'(x)=\log\Gamma(x+1)-\log\Gamma(x)=\log\bigl(\Gamma(x+1)/\Gamma(x)\bigr)=\log x$, using $\Gamma(x+1)=x\Gamma(x)$. An antiderivative of $\log x$ is $x\log x-x$, so $I(x)=x\log x-x+c$ on $(0,\infty)$, the difference of two functions with the same derivative being constant on the interval.
:::

:::

::: {.pf-step #monotone}
$\Gamma$ is increasing for all sufficiently large $x$.

::: pf-proof
This is the fact the exercise's hint supplies. It follows from the log-convexity of $\Gamma$ together with $\Gamma(x)\to\infty$: a convex function that tends to infinity is eventually increasing, and $\log\Gamma$ is convex on $(0,\infty)$.
:::

:::

::: {.pf-step #sandwich}
For all large integers $n$, $I(n-1)\le\log\Gamma(n)\le I(n)$.

::: pf-proof
On $[n-1,n]$, monotonicity gives $\log\Gamma(t)\le\log\Gamma(n)$, so $I(n-1)=\int_{n-1}^{n}\log\Gamma\le\log\Gamma(n)\cdot1$. On $[n,n+1]$, monotonicity gives $\log\Gamma(t)\ge\log\Gamma(n)$, so $I(n)\ge\log\Gamma(n)$.
:::

:::

::: {.pf-step #bounds}
$(n-1)\log(n-1)-(n-1)+c\le\log\Gamma(n)\le n\log n-n+c$ for large $n$.

::: pf-proof
Substitute step [](#parta){.pf-ref} into step [](#sandwich){.pf-ref}: $I(n-1)=(n-1)\log(n-1)-(n-1)+c$ and $I(n)=n\log n-n+c$.
:::

:::

::: {.pf-step #asymptotic}
$\log\Gamma(n)=n\log n+O(n)$.

::: pf-proof
The upper bound of step [](#bounds){.pf-ref} is $n\log n+O(n)$. For the lower bound, $(n-1)\log(n-1)=n\log n+O(n)$, since $\log(n-1)=\log n+O(1/n)$ and $(n-1)\log n=n\log n-\log n$; hence the lower bound is also $n\log n+O(n)$. So $\log\Gamma(n)$ is trapped between two expressions differing from $n\log n$ by $O(n)$, which gives the claim.
:::

:::

::: {.pf-step}
$\log\Gamma(n)\sim n\log n$ as $n\to\infty$.

::: pf-proof
Dividing the estimate of step [](#asymptotic){.pf-ref} by $n\log n$ gives $\log\Gamma(n)/(n\log n)=1+O(1/\log n)\to1$:
$$
\boxed{\log\Gamma(n)=n\log n+O(n),\qquad \log\Gamma(n)\sim n\log n.}
$$
This is weaker than Stirling's formula, which the exercise notes is proved in the appendix.
:::

:::

:::
:::
