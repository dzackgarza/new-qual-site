---
schema: qual/card@1
id: P-WESRA08-II3
kind: problem
title: Rational-translation invariant measurable sets are null or conull
classification:
  areas: [real-analysis]
  topics: [Lebesgue Measure, Translation Invariance, Lebesgue Density Theorem]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the argument already on the card, which is correct.
    Repaired the card's notation slip, where the convolution was defined as nu_epsilon and then
    used as u_epsilon, and its statement that 'u_epsilon is a continuous function' before being
    introduced. Added: the dominated-convergence reason for continuity of the convolution, the
    change of variables that turns the period of the indicator into a period of the convolution,
    the one-line proof that a continuous function with a dense period set is constant, and the
    identification of the two limits as the approximation identity at Lebesgue points. Not
    claimed: a retained solution set; the collection's provenance is the examination compilation
    only.
---

::: {.problem}
Suppose that $A\subseteq\RR$ is Lebesgue measurable and
$$
A+r=A
$$
for every rational number $r$.
Prove that either
$$
m(A)=0
\qquad\text{or}\qquad
m(\RR\setminus A)=0.
$$
:::

::: {.solution}
Throughout $m$ is Lebesgue measure on $\RR$, $\mathbf{1}_{A}$ is the indicator of the measurable set $A$, $A^{c} = \RR\setminus A$, and $\varphi \in C_{c}^{\infty}(\RR)$ is nonnegative with $\int_{\RR}\varphi = 1$, with $\varphi_{\varepsilon}(x) = \varepsilon^{-1}\varphi(x/\varepsilon)$ and $\nu_{\varepsilon} \coloneqq \mathbf{1}_{A} * \varphi_{\varepsilon}$. The collection's `provenance` is the Wesleyan analysis compilation, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #setup}
Assume $m(A) > 0$ and $m(A^{c}) > 0$.

::: pf-proof
This is the negation of the conclusion, since the conclusion is that one of the two measures vanishes.

:::

:::

::: {.pf-step #continuous}
For every $\varepsilon > 0$ the function $\nu_{\varepsilon}$ is continuous on $\RR$.

::: pf-proof
$\mathbf{1}_{A}$ is bounded and measurable, hence locally integrable, and $\varphi_{\varepsilon}$ is smooth and compactly supported; the convolution of an $L^{\infty}$ function with an $L^{1}$ function of compact support is continuous, indeed $\nu_{\varepsilon}(x) = \int \mathbf{1}_{A}(y)\varphi_{\varepsilon}(x-y)dy$ is continuous in $x$ by dominated convergence with dominating function $\norm{\varphi_{\varepsilon}}_{\infty}\mathbf{1}_{\operatorname{supp}\varphi_{\varepsilon}}(x-\cdot)$.

:::

:::

::: {.pf-step #periods}
$\nu_{\varepsilon}(x + q) = \nu_{\varepsilon}(x)$ for every $q \in \QQ$ and every $x \in \RR$.

::: pf-proof
The hypothesis $A + q = A$ gives $\mathbf{1}_{A}(y+q) = \mathbf{1}_{A}(y)$ for all $y$. Then $\nu_{\varepsilon}(x+q) = \int \mathbf{1}_{A}(y)\varphi_{\varepsilon}(x+q-y)dy$, and substituting $y = z + q$ turns this into $\int \mathbf{1}_{A}(z+q)\varphi_{\varepsilon}(x-z)dz = \int \mathbf{1}_{A}(z)\varphi_{\varepsilon}(x-z)dz = \nu_{\varepsilon}(x)$.

:::

:::

::: {.pf-step #constant}
Each $\nu_{\varepsilon}$ is constant on $\RR$.

::: pf-proof
By step [](#periods){.pf-ref} the period group of $\nu_{\varepsilon}$ contains $\QQ$, which is dense in $\RR$, and step [](#continuous){.pf-ref} makes $\nu_{\varepsilon}$ continuous; a continuous function with a dense period set is constant, because for any $x, x'$ one takes $q_{n} \to x' - x$ and gets $\nu_{\varepsilon}(x') = \lim_{n}\nu_{\varepsilon}(x + q_{n}) = \nu_{\varepsilon}(x)$.

:::

:::

::: {.pf-step #density}
There are points $a \in A$ and $b \in A^{c}$ that are Lebesgue points of $\mathbf{1}_{A}$, and at them $\nu_{\varepsilon}(a) \to 1$ and $\nu_{\varepsilon}(b) \to 0$ as $\varepsilon \downarrow 0$.

::: pf-proof
By the Lebesgue density theorem almost every point of $A$ is a density point of $A$, so one exists because $m(A) > 0$; likewise almost every point of $A^{c}$ is a density point of $A^{c}$ because $m(A^{c}) > 0$, and such a point is a Lebesgue point of $\mathbf{1}_{A}$ with value $0$. The approximation identity $\nu_{\varepsilon} \to \mathbf{1}_{A}$ in $L^{1}_{\mathrm{loc}}$ with $\varphi$ a mollifier gives $\nu_{\varepsilon}(x) \to \mathbf{1}_{A}(x)$ at every Lebesgue point $x$, which is the two limits asserted.

:::

:::

::: {.pf-step #contradiction}
The assumptions of step [](#setup){.pf-ref} are false.

::: pf-proof
For every $\varepsilon > 0$ step [](#constant){.pf-ref} gives $\nu_{\varepsilon}(a) = \nu_{\varepsilon}(b)$, so the two limits of step [](#density){.pf-ref} coincide; they are $1$ and $0$, a contradiction.

:::

:::

::: pf-step
Either $m(A) = 0$ or $m(\RR\setminus A) = 0$.

::: pf-proof
Step [](#contradiction){.pf-ref} shows that $A$ and its complement cannot both have positive measure, which is the dichotomy asserted.

:::

:::

:::
:::
