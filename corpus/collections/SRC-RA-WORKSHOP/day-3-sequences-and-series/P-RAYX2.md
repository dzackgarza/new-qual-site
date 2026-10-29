---
schema: qual/card@1
id: P-RAYX2
kind: problem
title: $\liminf$ of a product of positive sequences
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Limits
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: Part (b) of the source assumed only that a_n converges, and a_n=1/n, b_n=n gives 1 against the undefined product 0 times infinity; part (b) now assumes a_n converges to a positive limit.
---
::: {.problem}
Produce sequences $\{a_n\},\,\{b_n\}$ of positive real numbers such that $$\liminf_{n\to\infty}(a_nb_n)>\left(\liminf_{n\to\infty} a_n\right) \left(\liminf_{n\to\infty} b_n\right).$$

If $\{a_n\},\,\{b_n\}$ are sequences of positive real numbers and $\{a_n\}$ converges to a positive limit, prove that $$\liminf_{n\to\infty}(a_nb_n)=\left(\lim_{n\to\infty}a_n\right)\left(\liminf_{n\to\infty}b_n\right).$$
:::
::: {.solution}

::: pf

::: {.pf-step #s1}

The sequences $a_n=2+(-1)^n$ and $b_n=2-(-1)^n$ satisfy the strict inequality in part (a).

::: pf-proof

Both sequences have terms in $\{1,3\}$, and each has lower limit $1$. On the other hand, $a_nb_n=4-(-1)^{2n}=3$ for every $n$. Thus
\[
\boxed{\liminf_{n\to\infty}(a_nb_n)=3>1
=\left(\liminf_{n\to\infty}a_n\right)
\left(\liminf_{n\to\infty}b_n\right)}.
\]

:::

:::

::: {.pf-step #s2}

In part (b), if $a_n\to a>0$, then $\liminf(a_nb_n)=a\liminf b_n$, including when $\liminf b_n=+\infty$.

::: pf-proof

Fix $0<\varepsilon<a$. Eventually
\[
(a-\varepsilon)b_n\leq a_nb_n\leq(a+\varepsilon)b_n.
\]
Let $L=\liminf b_n\in[0,+\infty]$. If $L<+\infty$, taking lower limits gives
\[
(a-\varepsilon)L\leq\liminf(a_nb_n)\leq(a+\varepsilon)L.
\]
Letting $\varepsilon\downarrow0$ proves the equality. If $L=+\infty$, the lower bound $(a-\varepsilon)b_n$ tends to $+\infty$, so $\liminf(a_nb_n)=+\infty=aL$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} answers part (a), and step [](#s2){.pf-ref} proves part (b).

:::

:::

:::
