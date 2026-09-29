---
schema: qual/card@1
id: P-MLJMH
kind: problem
title: $L^\infty(\RR^n)$ is a Banach space, and $L^1\cap L^\infty\subset L^2$ with
  $\|f\|_2\le\|f\|_1^{1/2}\|f\|_\infty^{1/2}$
classification:
  areas:
  - real-analysis
  topics:
  - L∞
  - Lp Spaces
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
a. In parts:
  - Given a definition of $L^\infty(\RR^n)$.
  - Verify that $\norm{\wait}_\infty$ defines a norm on $L^\infty(\RR^n)$.
  - Carefully proved that $(L^\infty(\RR^n), \norm{\wait}_\infty)$ is a Banach space.

b. Prove that for any measurable $f:\RR^n \to \CC$,
\[
L^1(\RR^n) \intersect L^\infty(\RR^n) \subset L^2(\RR^n) \qtext{and} \norm{f}_2 \leq \norm{f}_1^{1\over 2} \cdot \norm{f}_\infty^{1\over 2}
.\]
:::
::: {.solution}
$L^\infty(\RR^n)$ is the space of a.e.-equivalence classes of measurable $f\colon \RR^n \to \CC$ with $\|f\|_\infty \coloneqq \inf\theset{M \ge 0 : |f| \le M \text{ a.e.}} < \infty$.

::: pf

::: {.pf-step #s1}

$|f| \le \|f\|_\infty$ a.e.

::: pf-proof

$\theset{|f| > \|f\|_\infty} = \bigcup_k \theset{|f| > \|f\|_\infty + 1/k}$ is a countable union of null sets.

:::

:::

::: pf-step

$\|\cdot\|_\infty$ is a norm on $L^\infty$.

::: pf-proof

By step [](#s1){.pf-ref}, $\|f\|_\infty = 0$ if and only if $f = 0$ a.e. $|\lambda f| \le M$ a.e. if and only if $|f| \le M/|\lambda|$ a.e., for $\lambda \neq 0$, so $\|\lambda f\|_\infty = |\lambda|\,\|f\|_\infty$. By step [](#s1){.pf-ref}, $|f + g| \le \|f\|_\infty + \|g\|_\infty$ off the union of two null sets, so $\|f + g\|_\infty \le \|f\|_\infty + \|g\|_\infty$.

:::

:::

::: pf-step

$L^\infty$ is complete.

::: pf-proof

Let $(f_k)$ be Cauchy in $L^\infty$. By step [](#s1){.pf-ref} there is a null set $N_{k,l}$ off which $|f_k - f_l| \le \|f_k - f_l\|_\infty$; let $N = \bigcup_{k,l}N_{k,l}$, a null set. Off $N$, $(f_k)$ is uniformly Cauchy, so it converges uniformly there to a measurable $f$; put $f = 0$ on $N$. Given $\eps > 0$ choose $K$ with $\|f_k - f_l\|_\infty < \eps$ for $k, l \ge K$. Letting $l \to \infty$ gives $|f_k - f| \le \eps$ off $N$ for $k \geq K$. So $f = (f - f_K) + f_K \in L^\infty$ and $\|f_k - f\|_\infty \le \eps$ for $k \ge K$.

:::

:::

::: pf-step

If $f \in L^1 \cap L^\infty$, then $\|f\|_2 \le \|f\|_1^{1/2}\|f\|_\infty^{1/2}$; in particular $f \in L^2$.

::: pf-proof

By step [](#s1){.pf-ref}, $|f|^2 \le \|f\|_\infty|f|$ a.e., so $\int|f|^2 \le \|f\|_\infty\|f\|_1$.

:::

:::

:::

:::
