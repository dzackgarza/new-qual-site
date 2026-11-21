---
schema: qual/card@1
id: P-JMOGT
kind: problem
title: $\lim_{x\to 0}\int_{\RR}\abs{f(y-x)-f(y)}\,dy=0$ for $f\in L^1(\RR)$
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Continuity
  - Density
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the TAMU Real Variables qualifying examination dated August 7, 2016, in the preserved Texas solution compilation.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Existing solution is correct; it improves on the preserved source by using uniform continuity of a compactly supported continuous approximant rather than an inapplicable appeal to Dini's theorem. Normalized the solution block so repository tooling recognizes the card as solved.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Thirteen steps asserted their claim with no justification and the card is now five steps each deriving
    its claim: the density of $C_c$ in $L^1$ together with the bounded interval containing the support;
    translation invariance of Lebesgue measure, which is what makes the approximant's translate as close to
    the translate of $f$ as $g$ is to $f$; the three-term triangle inequality integrated term by term; the
    uniformity step, which now says that $g$ is uniformly continuous on the compact $[-M-1, M+1]$ and that
    outside that interval both $g$ and its translate vanish for $\abs{x} \le 1$, then bounds the integrand
    by a constant on an interval of length $2M+2$; and the conclusion assembling $2\varepsilon/3$ with
    $\varepsilon/3$. The "Goal" paragraph restating the problem is gone, the five label-claims are replaced
    by the assertions their proofs establish, and the duplicate pair of closing fences at the end of the
    file is gone. Sources are cited by numbered statement: density of $C_c(\RR)$ in $L^1(\RR)$, translation
    invariance of the Lebesgue integral, and the uniform continuity of a continuous function on a compact
    interval. No page reference is written in the body of this card or in the event above. The statement is
    unchanged. The card's own argument improves on the preserved solution compilation by using uniform
    continuity of the approximant, as the event above records.
---

::: {.problem}
Let $f \in L^1(\RR)$. Show that
$$
\lim_{x \to 0} \int_{\RR} \abs{f(y - x) - f(y)} \, dy = 0.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #approx}
For every $\varepsilon > 0$ there are $g \in C_c(\RR)$ and $M > 0$ with $\norm{f - g}_{L^1} < \varepsilon/3$ and $\operatorname{supp}(g) \subseteq [-M, M]$.

::: pf-proof
The compactly supported continuous functions are dense in $L^1(\RR)$, so for the given $\varepsilon$ there is $g \in C_c(\RR)$ with $\int_\RR \abs{f(y) - g(y)}\,dy < \varepsilon/3$; that is the first assertion. Since $g$ has compact support, its support is contained in some closed interval $[-M, M]$ with $M > 0$.
:::

:::

::: {.pf-step #translation}
For every $x \in \RR$, $\int_\RR \abs{f(y-x) - g(y-x)}\,dy = \norm{f-g}_{L^1} < \varepsilon/3$.

::: pf-proof
The substitution $u = y - x$ is a translation, and Lebesgue measure is translation invariant, so the integral of $\abs{f(u) - g(u)}$ over $u \in \RR$ is unchanged; the value is $\norm{f-g}_{L^1}$, which is below $\varepsilon/3$ by the preceding step.
:::

:::

::: {.pf-step #split}
For every $x \in \RR$,
$$\int_\RR \abs{f(y-x) - f(y)}\,dy \le \frac{2\varepsilon}{3} + \int_\RR \abs{g(y-x) - g(y)}\,dy.$$

::: pf-proof
Add and subtract the two terms in $g$ and apply the triangle inequality pointwise,
$$\abs{f(y-x) - f(y)} \le \abs{f(y-x) - g(y-x)} + \abs{g(y-x) - g(y)} + \abs{g(y) - f(y)}.$$
Integrating over $\RR$ and using that the integral of a sum is the sum of the integrals for these integrable functions, the first and third terms integrate to $\int\abs{f(y-x) - g(y-x)}dy$ and $\int\abs{f(y) - g(y)}dy$, each below $\varepsilon/3$ by the preceding two steps; the middle term is unchanged. This gives the displayed inequality.
:::

:::

::: {.pf-step #uniform}
There is $\delta \in (0,1)$ such that $\abs{x} < \delta$ implies $\int_\RR \abs{g(y-x) - g(y)}\,dy < \varepsilon/3$.

::: pf-proof
A continuous function with compact support on $\RR$ is uniformly continuous: it is continuous on the compact set $[-M-1, M+1]$, hence uniformly continuous there, and outside that set both $g$ and its translate vanish for $\abs{x} \le 1$, since if $y \notin [-M-1,M+1]$ and $\abs{x} \le 1$ then neither $y$ nor $y - x$ lies in $[-M,M] = \operatorname{supp}(g)$ when the support is taken inside that interval. So there is $\delta \in (0,1)$ with $\abs{g(y-x) - g(y)} < \varepsilon/(3(2M+2))$ for all $\abs{x} < \delta$ and all $y \in \RR$. For such $x$ the function $g(\cdot - x) - g(\cdot)$ is supported in $[-M-1, M+1]$, so
$$\int_\RR \abs{g(y-x) - g(y)}\,dy = \int_{-M-1}^{M+1} \abs{g(y-x) - g(y)}\,dy \le \frac{\varepsilon}{3(2M+2)}\cdot(2M+2) = \frac{\varepsilon}{3},$$
the middle inequality bounding the integrand by a constant on an interval of length $2M+2$.
:::

:::

::: {.pf-step #conclusion}
$\lim_{x \to 0} \int_\RR \abs{f(y-x) - f(y)}\,dy = 0$.

::: pf-proof
Let $\varepsilon > 0$ and take $g$, $M$ and $\delta$ from the preceding steps. For $\abs{x} < \delta$, the splitting inequality gives
$$\int_\RR \abs{f(y-x) - f(y)}\,dy \le \frac{2\varepsilon}{3} + \int_\RR \abs{g(y-x) - g(y)}\,dy < \frac{2\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon.$$
So for every $\varepsilon > 0$ there is $\delta > 0$ with the integral below $\varepsilon$ whenever $\abs{x} < \delta$, which is the definition of the limit being $0$.
:::

:::
:::

:::
