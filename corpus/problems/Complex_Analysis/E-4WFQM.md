---
schema: qual/card@1
id: E-4WFQM
kind: problem
title: $\sum_{k\geq 1}\frac{1}{k^2+a^2}=\frac{\pi\coth(\pi a)}{2a}-\frac{1}{2a^2}$
  for $a>0$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Series of Numbers
  - Hyperbolic Functions
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that
$$
\sum_{k\geq 1}\frac{1}{k^2 + a^2} = \frac{1}{2}\frac{\pi \coth(\pi a)}{a} - \frac{1}{2a^2} \qquad a>0.
$$

:::

::: {.solution}
Fix $a>0$, let
$$
F(z)=\frac{\pi\cot(\pi z)}{z^2+a^2},
$$
and let $\Gamma_N$ be the positively oriented boundary of the square with vertices $(N+\tfrac12)(\pm1\pm i)$.

::: pf

::: {.pf-step #residues}
$\operatorname{Res}(F,k)=\dfrac1{k^2+a^2}$ for $k\in\ZZ$, and $\operatorname{Res}(F,ia)=\operatorname{Res}(F,-ia)=-\dfrac{\pi}{2a}\coth(\pi a)$.

::: pf-proof
At an integer $k$, $\pi\cot(\pi z)$ has a simple pole with residue $1$ and $1/(z^2+a^2)$ is holomorphic, giving $1/(k^2+a^2)$.
At $\pm ia$ the poles are simple, with residues $\pi\cot(\pm\pi ia)/(\pm2ia)$; since $\cot(iu)=-i\coth u$, both equal $-\frac{\pi}{2a}\coth(\pi a)$.
:::

:::

::: {.pf-step #vanish}
$\int_{\Gamma_N}F(z)\,dz\to0$ as $N\to\infty$.

::: pf-proof
On $\Gamma_N$ the function $\abs{\cot(\pi z)}$ is bounded independently of $N$, while $\abs{z^2+a^2}\ge (N+\tfrac12)^2-a^2$ and the length of $\Gamma_N$ is $O(N)$; so the integral is $O(1/N)$.
:::

:::

::: {.pf-step #full-sum}
$\displaystyle\sum_{k\in\ZZ}\frac1{k^2+a^2}=\frac{\pi}{a}\coth(\pi a)$.

::: pf-proof
For $N>a$, $\Gamma_N$ encloses $\pm ia$ and the integers $-N,\ldots,N$.
By the residue theorem and step [](#residues){.pf-ref},
$$
\frac1{2\pi i}\int_{\Gamma_N}F(z)\,dz=\sum_{k=-N}^N\frac1{k^2+a^2}-\frac{\pi}{a}\coth(\pi a),
$$
and step [](#vanish){.pf-ref} lets $N\to\infty$.
:::

:::

::: pf-step
$\displaystyle\sum_{k=1}^\infty\frac1{k^2+a^2}=\frac{\pi\coth(\pi a)}{2a}-\frac1{2a^2}$.

::: pf-proof
The sum over $\ZZ$ is $\frac1{a^2}+2\sum_{k=1}^\infty\frac1{k^2+a^2}$; solve with step [](#full-sum){.pf-ref}.
:::

:::

:::

:::
