---
order: 30
problems:
  topics:
  - Continuity
  - Uniform Continuity
  - Fixed Points
---

# Continuity

::: {.remark}
Some inclusions on the real line:

- Differentiable with a bounded derivative $\subset$ Lipschitz continuous $\subset$ absolutely continuous $\subset$ uniformly continuous $\subset$ continuous

Proofs:

- Mean Value Theorem,

- Triangle inequality,

- Definition of absolute continuity specialized to one interval,

- Definition of uniform continuity
:::

[[L-75UZY]]

::: {.proof}
$f(x) = \frac 1 n$ if $x = r_n \in \QQ$ is an enumeration of the rationals, and zero otherwise.
The limit at every point is 0.
:::

[[PR-F5V7D]]

[[FF-AVBFU]] [[FF-5EBCJ]]

::: {.proof}
$D_f$ is always an $F_\sigma$ set, which follows by considering the oscillation $\omega_f$.
Use that $\omega_f(x) = 0 \iff f$ is continuous at $x$, and $D_f = \union_n A_{\frac 1 n}$ where $A_\varepsilon = \theset{\omega_f \geq \varepsilon}$ is closed.
:::

::: {.remark}
An alternative characterization of **uniform continuity**:
$$
\left\|\tau_{y} f-f\right\|_{u} \rightarrow 0 \text { as } y \rightarrow 0
$$
:::

[[PR-SX6NO]]

[[T-O4UD3]]

::: {.proof}
Fix $\eps>0$, we'll find a $\delta$ that works for all $x\in X$ uniformly.
For every $x\in X$, pick a $\delta_x$ neighborhood satisfying the conditions for (assumed) continuity.
Take an open cover by $\delta_x/2$ balls, extract a finite subcover, take $\delta$ the minimal radius.
:::

[[D-2CCDB]]

[[FD-TGBYP]] [[FD-XVMEE]]

[[FF-63IWC]]

[[FT-JQSOK]] [[FF-XZGIY]]
