---
schema: qual/card@1
id: P-RA-WORKSHOP-D6-W4
kind: problem
title: Vanishing Stieltjes integrals force a monotone integrator to be constant
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
([Apo74, 7.2]) Let $\alpha:[a,b]\to\mathbb R$ be increasing. If $f\in\mathcal R(\alpha)$ and $\int_a^b f\,d\alpha=0$ for every monotone function $f:[a,b]\to\mathbb R$, prove that $\alpha$ is constant on $[a,b]$.
:::

::: {.solution}
<1>1. The endpoints satisfy $\alpha(a)=\alpha(b)$.

::: {.proof}
The constant function $f\equiv1$ is monotone and Riemann–Stieltjes integrable with respect to every increasing $\alpha$: every tagged sum telescopes to $\alpha(b)-\alpha(a)$. The hypothesis therefore gives
\[
0=\int_a^b1\,d\alpha=\alpha(b)-\alpha(a).
\]
:::

<1>2. The integrator $\alpha$ is constant on $[a,b]$.

::: {.proof}
For every $x\in[a,b]$, monotonicity of $\alpha$ and step <1>1 give
\[
\alpha(a)\leq\alpha(x)\leq\alpha(b)=\alpha(a).
\]
Hence $\alpha(x)=\alpha(a)$.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 establishes the required constancy.
:::
:::
