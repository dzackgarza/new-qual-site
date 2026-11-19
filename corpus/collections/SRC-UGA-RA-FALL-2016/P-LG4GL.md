---
schema: qual/card@1
id: P-LG4GL
kind: problem
title: $\left(\int\frac{\abs{\phi}^n}{1+x^2}\,dx\right)^{1/n}\to\norm{\phi}_\infty$
classification:
  areas:
  - real-analysis
  topics:
  - L∞
  - Lp Spaces
  - Limits
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 5 of the official UGA August 2016 real-analysis qualifying exam; normalized the weighted finite-measure Lp-to-Linfinity argument.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Added what the prose left implicit:
    that A_n is finite because |phi|^n/(1+x^2) <= M^n/(1+x^2) with integral pi M^n, evaluating
    the integral of 1/(1+x^2) as pi; that E_eps has positive measure by the definition of the
    essential supremum; and that c_eps > 0 so c_eps^{1/n} -> 1, which is what makes the lower
    bound converge. The two-sided conclusion is stated as limsup <= liminf = M. Statement
    unchanged; the card says the argument is its own.
---

::: {.problem}
Let $\phi\in L^\infty(\RR)$. Show that the following limit exists and satisfies the equality
$$
\lim _{n \to \infty} \left(\int _{\RR} \frac{\abs{\phi(x)}^{n}}{1+x^{2}} \, dx \right) ^ {\frac{1}{n}} 
= \norm{\phi}_\infty.
$$
:::

::: {.solution}
Both bounds come from the same inequality: $\abs\phi\le M$ bounds $\int\abs\phi^n/(1+x^2)$ above by $\pi M^n$, and on the set where $\abs\phi>M-\varepsilon$, of positive measure, it bounds the integral below by $(M-\varepsilon)^n$ times the positive number $\int_{E_\varepsilon}\frac{\dd x}{1+x^2}$, whose $n$-th root tends to $1$. The argument is this card's own: no retained solution set covers this exam.

::: pf

::: {.pf-step #setup}
Put $M=\norm\phi_\infty$ and $A_n=\Bigl(\int_\RR\dfrac{\abs{\phi(x)}^n}{1+x^2}\,\dd x\Bigr)^{1/n}$; then $A_n$ is defined and finite for every $n\ge1$.

::: pf-proof
$\abs\phi\le M$ almost everywhere, so $\abs\phi^n/(1+x^2)\le M^n/(1+x^2)$, which is integrable on $\RR$ with integral $\pi M^n$; hence the integral defining $A_n$ is finite and nonnegative, and $A_n$ is its nonnegative $n$-th root. If $M=0$ then $\phi=0$ almost everywhere and $A_n=0$ for every $n$, so the limit is $0=\norm\phi_\infty$; assume $M>0$ from here.
:::

:::


::: {.pf-step #upper}
$\limsup_nA_n\le M$.

::: pf-proof
By step [](#setup){.pf-ref}, $A_n^n\le M^n\int_\RR\frac{\dd x}{1+x^2}=\pi M^n$, since $\int_\RR\frac{\dd x}{1+x^2}=\arctan x\,\evalfrom_{-\infty}^{\infty}=\pi$. Taking $n$-th roots, $A_n\le\pi^{1/n}M$, and $\pi^{1/n}\to1$, so $\limsup_nA_n\le M$.
:::

:::


::: {.pf-step #lower}
For each $0<\varepsilon<M$, $\liminf_nA_n\ge M-\varepsilon$.

::: pf-proof
Let $E_\varepsilon=\{x:\abs{\phi(x)}>M-\varepsilon\}$. By the definition of the essential supremum as the infimum of the $t$ with $\abs\phi\le t$ almost everywhere, $E_\varepsilon$ has positive Lebesgue measure $m(E_\varepsilon)>0$; otherwise $\abs\phi\le M-\varepsilon$ almost everywhere. Put $c_\varepsilon=\int_{E_\varepsilon}\frac{\dd x}{1+x^2}$, which is positive because the integrand is positive everywhere and $E_\varepsilon$ has positive measure. On $E_\varepsilon$ one has $\abs\phi^n>(M-\varepsilon)^n$, so
$$
A_n^n\ge\int_{E_\varepsilon}\frac{\abs\phi^n}{1+x^2}\,\dd x\ge(M-\varepsilon)^n c_\varepsilon,
$$
the first inequality because the integrand is nonnegative off $E_\varepsilon$. Taking $n$-th roots, $A_n\ge(M-\varepsilon)c_\varepsilon^{1/n}$, and $c_\varepsilon^{1/n}\to1$ as $n\to\infty$ because $c_\varepsilon>0$; hence $\liminf_nA_n\ge M-\varepsilon$. Since $\varepsilon\in(0,M)$ is arbitrary and the bound is monotone in $\varepsilon$, $\liminf_nA_n\ge M$.
:::

:::


::: {.pf-step #conclusion}
$\displaystyle\lim_{n\to\infty}\Bigl(\int_\RR\frac{\abs{\phi(x)}^n}{1+x^2}\,\dd x\Bigr)^{1/n}=\norm\phi_\infty$.

::: pf-proof
Steps [](#upper){.pf-ref} and [](#lower){.pf-ref} give $\limsup_nA_n\le M\le\liminf_nA_n$, so the limit exists and equals $M=\norm\phi_\infty$; the case $M=0$ is settled in step [](#setup){.pf-ref}.
:::

:::

:::
:::
