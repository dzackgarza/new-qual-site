---
schema: qual/card@1
id: P-CAFA21G
kind: problem
title: "Entire functions with modulus 1 on the real line"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The reflection step now says why conj(f(conj z)) is entire (power series with conjugated coefficients) and why the identity theorem applies. The existence of an entire logarithm is derived rather than cited: f'/f is entire because f is zero-free, C is simply connected so f'/f has a primitive, and f e^{-g} is constant, the constant being absorbed. The passage from g to h = -ig with h real on R is shown, and the converse is proved. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair; the description of the class is correct.
---

::: {.problem}
Describe all entire functions $f : \CC \to \CC$ such that for all $z \in \RR$ we have $\abs{f(z)} = 1$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #reflect}
$f^*(z)=\overline{f(\overline z)}$ is entire, and $f(z)f^*(z)=1$ for every $z\in\CC$.

::: pf-proof
The map $z\mapsto\overline z$ is antiholomorphic and $f$ is holomorphic, so $z\mapsto f(\overline z)$ is antiholomorphic; conjugating its values gives an entire function, since on a disc $f(w)=\sum c_nw^n$ gives $f^*(z)=\sum\overline{c_n}z^n$. For real $x$, $f^*(x)=\overline{f(x)}$, so $f(x)f^*(x)=\abs{f(x)}^2=1$. The entire function $ff^*-1$ vanishes on $\RR$, which has accumulation points, so it vanishes identically by the identity theorem.
:::

:::

::: {.pf-step #zerofree}
$f$ has no zeros.

::: pf-proof
If $f(z_0)=0$ then $f(z_0)f^*(z_0)=0\ne1$, contradicting step [](#reflect){.pf-ref}.
:::

:::

::: {.pf-step #log}
$f=e^g$ for some entire $g$.

::: pf-proof
$f'/f$ is entire because $f$ has no zeros (step [](#zerofree){.pf-ref}). Since $\CC$ is simply connected, $f'/f$ has a primitive $g$, and then $\left(fe^{-g}\right)'=e^{-g}(f'-fg')=e^{-g}(f'-f\cdot f'/f)=0$, so $fe^{-g}$ is a constant $A\ne0$. Absorbing $A$ into $g$ (replacing $g$ by $g+\log A$ for a chosen logarithm) gives $f=e^g$.
:::

:::

::: {.pf-step #realpart}
For real $x$, $\operatorname{Re}g(x)=0$.

::: pf-proof
$1=\abs{f(x)}=\abs{e^{g(x)}}=e^{\operatorname{Re}g(x)}$, so $\operatorname{Re}g(x)=0$.
:::

:::

::: {.pf-step #form}
$f=e^{ih}$ with $h$ entire and $h(\RR)\subseteq\RR$.

::: pf-proof
Put $h=-ig$. Then $h$ is entire and, for real $x$, $h(x)=-ig(x)=\operatorname{Im}g(x)\in\RR$ because $\operatorname{Re}g(x)=0$; and $e^{ih}=e^{i(-ig)}=e^{g}=f$.
:::

:::

::: {.pf-step #converse}
Conversely, if $h$ is entire with $h(\RR)\subseteq\RR$, then $f=e^{ih}$ is entire with $\abs{f(x)}=1$ for real $x$.

::: pf-proof
$e^{ih}$ is entire as a composite. For real $x$, $h(x)\in\RR$ so $\abs{e^{ih(x)}}=1$.
:::

:::

::: {.pf-step}
The entire functions with $\abs{f}=1$ on $\RR$ are exactly those of the form $f=e^{ih}$ with $h$ entire and $h(\RR)\subseteq\RR$.

::: pf-proof
Steps [](#form){.pf-ref} and [](#converse){.pf-ref} give the two inclusions.
:::

:::

:::
:::
