---
schema: qual/card@1
id: P-RA-WORKSHOP-D6-W1
kind: problem
title: Products of bounded Riemann-integrable functions
classification:
  areas:
  - real-analysis
  topics:
  - Riemann Integrability
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
([KRD10, 6.4.N]) If $f$ and $g$ are bounded on $[a,b]$ and both are Riemann integrable on $[a,b]$, show that $fg\in\mathcal R$ on $[a,b]$.
:::

::: {.solution}
For a bounded function $h$ and a partition $P$, write $D(h,P)\coloneqq U(h,P)-L(h,P)$.

::: pf

::: {.pf-step #s1}

If $h,k$ are bounded Riemann-integrable functions, then $h+k$ and $ch$ are Riemann integrable for every $c\in\RR$.

::: pf-proof

For any interval $I$, oscillation satisfies
$$
\operatorname{osc}_I(h+k)\leq\operatorname{osc}_I(h)+\operatorname{osc}_I(k),
\qquad \operatorname{osc}_I(ch)=\abs{c}\operatorname{osc}_I(h).
$$
Consequently $D(h+k,P)\leq D(h,P)+D(k,P)$ and $D(ch,P)=\abs{c}D(h,P)$. Given $\varepsilon>0$, the Darboux criterion supplies partitions $P_h,P_k$ with $D(h,P_h),D(k,P_k)<\varepsilon/2$. Their common refinement $P$ has $D(h,P)+D(k,P)<\varepsilon$, proving integrability of $h+k$. The scalar case follows directly from the same criterion, including $c=0$.

:::

:::

::: {.pf-step #s2}

If $h$ is bounded and Riemann integrable, then $h^2$ is Riemann integrable.

::: pf-proof

Choose $M\geq0$ with $\abs{h}\leq M$. For any $u,v\in I$,
$$
\abs{h(u)^2-h(v)^2}=\abs{h(u)-h(v)}\,\abs{h(u)+h(v)}
\leq2M\abs{h(u)-h(v)}.
$$
Taking suprema over $u,v$ gives $\operatorname{osc}_I(h^2)\leq2M\operatorname{osc}_I(h)$, hence $D(h^2,P)\leq2M D(h,P)$. The Darboux criterion for $h$, with an arbitrarily small oscillation sum, proves the assertion, also when $M=0$.

:::

:::

::: pf-step

The product $fg$ is Riemann integrable on $[a,b]$.

::: pf-proof

Step [](#s1){.pf-ref} gives $f+g,f-g\in\mathcal R$. Step [](#s2){.pf-ref} gives $(f+g)^2,(f-g)^2\in\mathcal R$. Applying step [](#s1){.pf-ref} again to
$$
fg=\frac14\bigl((f+g)^2-(f-g)^2\bigr)
$$
establishes $fg\in\mathcal R$.

:::

:::

:::

:::
