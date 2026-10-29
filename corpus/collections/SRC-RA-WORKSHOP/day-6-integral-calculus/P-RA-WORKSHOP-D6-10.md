---
schema: qual/card@1
id: P-RA-WORKSHOP-D6-10
kind: problem
title: Reduction of a Stieltjes integral to a Riemann integral
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Riemann Integrability
relations:
- kind: uses
  target: T-RA-WORKSHOP-D6-5-3
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Let $a<b$, let $\alpha\colon[a,b]\to\RR$ be monotonically increasing and differentiable with $\alpha'$ Riemann integrable on $[a,b]$, and let $f\colon[a,b]\to\RR$ be bounded.
Prove that $f\in\mathcal R(\alpha)$ on $[a,b]$ if and only if $f\alpha'$ is Riemann integrable on $[a,b]$, and that in that case
$$
\int_a^b f\,d\alpha=\int_a^b f(x)\alpha'(x)\,dx.
$$
:::

::: {.solution}
Choose $M\geq0$ with $\abs{f}\leq M$. For a tagged partition $(P,\tau)$, write $S_\alpha(f;P,\tau)$ for its Stieltjes sum and $S(f\alpha';P,\tau)$ for its ordinary Riemann sum.

::: pf

::: {.pf-step #s1}

For every tagged partition $(P,\tau)$,
$$
\abs{S_\alpha(f;P,\tau)-S(f\alpha';P,\tau)}
\leq M\bigl(U(\alpha',P)-L(\alpha',P)\bigr).
$$

::: pf-proof

Since $\alpha'$ is Riemann integrable, it is bounded. The mean value theorem applied to $\alpha$ on each subinterval $I_i=[x_{i-1},x_i]$ gives $\Delta\alpha_i=\alpha'(\xi_i)\Delta x_i$ for some $\xi_i\in(x_{i-1},x_i)$. Thus
$$
\abs{\Delta\alpha_i-\alpha'(\tau_i)\Delta x_i}
\leq\operatorname{osc}_{I_i}(\alpha')\Delta x_i.
$$
Multiplying by $\abs{f(\tau_i)}\leq M$, summing, and using the definitions of the upper and lower Darboux sums gives the bound.

:::

:::

::: {.pf-step #s2}

For every $\varepsilon>0$ there is $\delta>0$ such that every partition $P$ with mesh less than $\delta$ satisfies
$$
U(\alpha',P)-L(\alpha',P)<\varepsilon.
$$

::: pf-proof

By Riemann integrability choose a partition $Q$ with $U(\alpha',Q)-L(\alpha',Q)<\varepsilon/2$. Let $B=\sup\abs{\alpha'}$ and let $r$ be the number of interior division points of $Q$. For any partition $P$, insert the points of $Q$ to obtain the common refinement $R$. The oscillation sum on $R$ is at most that on $Q$. At most $r$ intervals of $P$ contain an interior point of $Q$; on all other intervals refinement changes no oscillation contribution. Consequently
$$
U(\alpha',P)-L(\alpha',P)
\leq U(\alpha',Q)-L(\alpha',Q)+2Br\,\operatorname{mesh}(P).
$$
Choose $\delta$ so that $2Br\delta<\varepsilon/2$ when $Br>0$; otherwise any positive $\delta$ works.

:::

:::

::: {.pf-step #s3}

The tagged Stieltjes sums of $f$ and ordinary Riemann sums of $f\alpha'$ have the same limit whenever either family has a limit as the mesh tends to zero.

::: pf-proof

Step [](#s1){.pf-ref} and step [](#s2){.pf-ref} imply that the difference between the two sums tends uniformly to zero over all choices of tags as the mesh tends to zero. Hence convergence of either family to a number $I$, uniformly over tagged partitions of sufficiently small mesh, is equivalent to convergence of the other family to the same $I$.

:::

:::

::: pf-step

$f\in\mathcal R(\alpha)$ if and only if $f\alpha'\in\mathcal R$, and then $\int_a^b f\,d\alpha=\int_a^b f(x)\alpha'(x)\,dx$.

::: pf-proof

The tagged-sum characterization of Riemann integrability applies to $f\alpha'$. The corresponding tagged-sum characterization of Riemann–Stieltjes integrability applies because $\alpha$ is continuous and increasing; continuity follows from differentiability. Step [](#s3){.pf-ref} identifies both integrability conditions and their integral values.

:::

:::

:::

:::
