---
schema: qual/card@1
id: P-BKS21-8B
kind: problem
title: Unital homomorphisms $\ZZ[x]/(x^2+3)\to\ZZ[x]/(x^2-x+1)$
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Does there exist a unital homomorphism
$$
\ZZ[x]/(x^2+3)\longrightarrow\ZZ[x]/(x^2-x+1)?
$$
Either exhibit one or prove none exists.
:::

::: {.solution}

Let
$$
S\coloneqq \ZZ[t]/(t^2-t+1),
$$
and let $\alpha$ denote the class of $t$ in $S$.

::: pf

::: {.pf-step #s1-1}

In $S$ one has
$$
\alpha^2=\alpha-1.
$$


::: pf-proof

The defining relation
$$
t^2-t+1=0
$$
holds after passing to the quotient, so
$$
\alpha^2-\alpha+1=0.
$$

:::

:::

::: {.pf-step #s1-2}

The element
$$
u\coloneqq2\alpha-1
$$
satisfies
$$
u^2=-3
$$
in $S$.


::: pf-proof

Using step [](#s1-1){.pf-ref},
$$
\begin{aligned}
u^2
&=(2\alpha-1)^2\\
&=4\alpha^2-4\alpha+1\\
&=4(\alpha-1)-4\alpha+1\\
&=-3.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

The evaluation map
$$
\psi:\ZZ[x]\longrightarrow S,
\qquad
\psi(x)=u,
$$
is a unital ring homomorphism whose kernel contains $(x^2+3)$.


::: pf-proof

There is a unique unital ring homomorphism from the polynomial ring $\ZZ[x]$ to $S$ sending $x$ to the prescribed element $u$. By step [](#s1-2){.pf-ref},
$$
\psi(x^2+3)=u^2+3=0.
$$
Hence every multiple of $x^2+3$ lies in $\ker\psi$.

:::

:::

::: {.pf-step #s1-4}

Therefore $\psi$ descends to a unital homomorphism
$$
\boxed{
\overline\psi:
\ZZ[x]/(x^2+3)
\longrightarrow
\ZZ[t]/(t^2-t+1),
\qquad
\overline\psi([x])=2[t]-1
}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
(x^2+3)\subseteq\ker\psi.
$$
The universal property of the quotient ring therefore gives a unique induced unital homomorphism $\overline\psi$ with the displayed value on the class of $x$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} explicitly exhibits the required homomorphism.

:::

:::

:::
