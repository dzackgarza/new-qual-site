---
schema: qual/card@1
id: P-CAF09F
kind: problem
title: "An entire function with real plus imaginary part bounded is constant"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Suppose that $f(z) = u(z) + iv(z)$ is an entire function with real part $u(z)$ and imaginary part $v(z)$ such that for all $z$, $u(z) + v(z) < 1$.
Prove that $f(z)$ is a constant.
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper `assets/attachments/FA09_220_Complex_Analysis_Qual.pdf` and no solutions sheet accompanies it, so the argument below is the card's own. It uses Liouville's theorem and the two standard facts recorded as steps — that $\abs{\mathrm{e}^{w}}=\mathrm{e}^{\operatorname{Re}w}$ and that a holomorphic function on a domain with vanishing derivative is constant.

Throughout, $f=u+iv$ is entire with real part $u$ and imaginary part $v$, and $f(z)=u(z)+iv(z)$ satisfies $u(z)+v(z)<1$ for every $z\in\CC$.

::: pf

::: {.pf-step #g-entire}
$g(z)\coloneqq\mathrm{e}^{(1-i)f(z)}$ is entire.

::: pf-proof
$z\mapsto(1-i)f(z)$ is entire, being a constant multiple of the entire function $f$, and the exponential is entire; a composite of entire functions is entire, by the chain rule together with the fact that a composite of holomorphic functions is holomorphic.
:::

:::

::: {.pf-step #modulus}
For every $z$, $\abs{g(z)}=\mathrm{e}^{u(z)+v(z)}<\mathrm{e}$.

:::: pf-proof

::: {.pf-step #real-part}
$\operatorname{Re}\big((1-i)f(z)\big)=u(z)+v(z)$.

::: pf-proof
Multiplying out, $(1-i)(u+iv)=u+iv-iu-i^{2}v=u+iv-iu+v=(u+v)+i(v-u)$, using $i^{2}=-1$; the real part is $u+v$.
:::

:::

::: {.pf-step #absolute-value}
$\abs{\mathrm{e}^{w}}=\mathrm{e}^{\operatorname{Re}w}$ for every $w\in\CC$.

::: pf-proof
Writing $w=a+ib$ with $a,b$ real, $\mathrm{e}^{w}=\mathrm{e}^{a}\mathrm{e}^{ib}$ and $\abs{\mathrm{e}^{ib}}=\abs{\cos b+i\sin b}=1$ because $\cos^{2}b+\sin^{2}b=1$; so $\abs{\mathrm{e}^{w}}=\mathrm{e}^{a}=\mathrm{e}^{\operatorname{Re}w}$.
:::

:::

::: {.pf-step}
The claim follows.

::: pf-proof
Apply step [](#absolute-value){.pf-ref} to $w=(1-i)f(z)$ and use step [](#real-part){.pf-ref}: $\abs{g(z)}=\mathrm{e}^{u(z)+v(z)}$. The hypothesis $u(z)+v(z)<1$ and the strict increase of the exponential give $\abs{g(z)}<\mathrm{e}^{1}=\mathrm{e}$.
:::

:::

::::

:::

::: {.pf-step #constant}
$g$ is constant.

::: pf-proof
Step [](#modulus){.pf-ref} bounds $\abs{g}$ by $\mathrm{e}$ on all of $\CC$, so $g$ is bounded; by step [](#g-entire){.pf-ref} it is entire. Liouville's theorem, that a bounded entire function is constant, applies.
:::

:::

::: {.pf-step #derivative-vanishes}
$f'(z)=0$ for every $z\in\CC$.

::: pf-proof
By the chain rule, $g'(z)=(1-i)f'(z)\mathrm{e}^{(1-i)f(z)}=(1-i)f'(z)g(z)$. Since $g$ is constant by step [](#constant){.pf-ref}, $g'=0$; and $g(z)=\mathrm{e}^{(1-i)f(z)}$ is never $0$, because the exponential has no zeros. Hence $(1-i)f'(z)=0$, and $1-i\neq0$, so $f'(z)=0$.
:::

:::

::: pf-step
Therefore
$$
\boxed{f\text{ is constant,}}
$$
so the hypothesis that $u+v<1$ forces $f$ to be constant.

::: pf-proof
By step [](#derivative-vanishes){.pf-ref} the derivative of $f$ vanishes at every point of the domain $\CC$, and a holomorphic function on a domain whose derivative vanishes identically is constant: on a disc about any point the function equals its constant term in the power series expansion about that point, and $\CC$ is connected, so the constant is the same everywhere.
:::

:::

:::

:::
