---
schema: qual/card@1
id: P-RA-WORKSHOP-D6-W4
kind: problem
title: 'Vanishing Stieltjes integrals force a monotone integrator to be constant'
classification:
  areas:
  - real-analysis
  topics:
  - riemann-integrability
  - integrals
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
([Apo74, 7.2]) If $f\in\mathcal R(\alpha)$ on $[a,b]$ and $\int_a^b f\,d\alpha=0$ for every $f$ which is monotonic on $[a,b]$, prove that $\alpha$ must be constant on $[a,b]$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Apply the hypothesis to $f \equiv 1$ (constant, hence monotone).
Proof: $\int_a^b 1\,d\alpha = \alpha(b) - \alpha(a) = 0$, so $\alpha(a) = \alpha(b)$.
<1>2. Apply the hypothesis to $f(x) = x$ (monotone increasing).
Proof: $\int_a^b x\,d\alpha = 0$.
By the Stieltjes integration-by-parts formula (valid since $f$ is continuous and $\alpha$ is monotone, both of bounded variation), \[\int_a^b x\,d\alpha = b\alpha(b) - a\alpha(a) - \int_a^b \alpha(x)\,dx.\] Using $\alpha(a) = \alpha(b) =: c$ from <1>1: \[0 = b c - a c - \int_a^b \alpha(x)\,dx = c(b-a) - \int_a^b \alpha(x)\,dx,\] so $\int_a^b (\alpha(x) - c)\,dx = 0$.
<1>3. $\alpha \equiv c$ on $[a,b]$.
Proof: $\alpha$ is increasing, so $\alpha(x) - c = \alpha(x) - \alpha(a) \ge 0$ for all $x$.
A non-negative Riemann-integrable function with zero integral is $0$ a.e., so $\alpha(x) = c$ for a.e. $x \in [a,b]$.
Since $\alpha$ is monotone, if $\alpha(x_0) > c$ at some point then $\alpha \ge \alpha(x_0) > c$ on $[x_0, b]$, a set of positive measure — contradiction.
Hence $\alpha(x) = c$ for all $x \in [a,b]$; $\alpha$ is constant.
<1>4. Q.E.D.
:::
