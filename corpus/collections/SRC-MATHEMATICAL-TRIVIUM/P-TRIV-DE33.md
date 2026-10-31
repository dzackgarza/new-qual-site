---
schema: qual/card@1
id: P-TRIV-DE33
kind: problem
title: Composition of the Dirac delta with a function
classification:
  areas: [prelim]
  topics:
  - Dirac Delta
  - Distributions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 33, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Show that $\delta(\alpha x) = \frac{1}{\alpha}\delta(x)$, and more generally, $\delta(f(x)) = \sum_i \frac{\delta(x - x_i)}{\abs{f'(x_i)}}$ where $x_i$ are the root of $f$, i.e. $f(x_i) = 0$.
:::

::: {.solution}

Assume throughout that the zeros $x_i$ of $f$ are simple, so $f'(x_i)\ne0$. The scaling formula is stated for real $\alpha\ne0$.

::: pf

::: {.pf-step #s1-1}

For every test function $\phi$,
$$
\langle\delta(\alpha x),\phi\rangle
=\frac1{\abs{\alpha}}\phi(0).
$$


::: pf-proof

Using $u=\alpha x$ and reversing the integration limits when $\alpha<0$ gives
$$
\int_{-\infty}^{\infty}\delta(\alpha x)\phi(x)\,dx
=\frac1{\abs{\alpha}}
\int_{-\infty}^{\infty}\delta(u)\phi(u/\alpha)\,du
=\frac1{\abs{\alpha}}\phi(0).
$$

:::

:::

::: {.pf-step #s1-2}

Therefore the correct scaling identity is
$$
\boxed{\delta(\alpha x)=\frac1{\abs{\alpha}}\delta(x)}.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} agrees with the action of $\abs{\alpha}^{-1}\delta$ on every test function. If the source implicitly assumes $\alpha>0$, this reduces to its stated formula $\delta(\alpha x)=\alpha^{-1}\delta(x)$.

:::

:::

::: pf-step

Around each simple zero $x_i$, there is an interval $U_i$ on which $f$ is one-to-one and has a smooth inverse.


::: pf-proof

Since $f'(x_i)\ne0$, the inverse function theorem supplies such an interval. The intervals may be chosen disjoint when considering the finitely many zeros meeting the compact support of a fixed test function.

:::

:::

::: {.pf-step #s1-4}

For every test function $\phi$ supported in the union of these intervals,
$$
\int\delta(f(x))\phi(x)\,dx
=\sum_i\frac{\phi(x_i)}{\abs{f'(x_i)}}.
$$


::: pf-proof

On $U_i$, set $u=f(x)$. The change-of-variables formula gives
$$
\int_{U_i}\delta(f(x))\phi(x)\,dx
=\int_{f(U_i)}\delta(u)
\frac{\phi(f_i^{-1}(u))}{\abs{f'(f_i^{-1}(u))}}\,du
=\frac{\phi(x_i)}{\abs{f'(x_i)}}.
$$
Summing over the disjoint neighborhoods gives the identity. Regions containing no zero contribute nothing because the pullback of $\delta_0$ is supported on $f^{-1}(0)$.

:::

:::

::: {.pf-step #s1-5}

Hence, distributionally,
$$
\boxed{
\delta(f(x))=\sum_i\frac{\delta(x-x_i)}{\abs{f'(x_i)}}}.
$$


::: pf-proof

The right side acts on a test function as the expression obtained in step [](#s1-4){.pf-ref}. A partition of unity reduces an arbitrary compactly supported test function to neighborhoods of the zeros and a region disjoint from them.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves the scaling law, with the necessary absolute value for arbitrary real $\alpha$, and step [](#s1-5){.pf-ref} proves the general simple-zero formula.

:::

:::

:::
