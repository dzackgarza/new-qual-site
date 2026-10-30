---
schema: qual/card@1
id: P-UGAP09S-03
kind: problem
title: A function whose $n$th derivative is $1/\sqrt{3+x^4}$
classification:
  areas: [prelim]
  topics:
  - Integrals
  - Induction
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Prove that for every natural number $n$ there exists a function $f:\RR\to\RR$ whose $n$th derivative is
$$
f^{(n)}(x)=\frac1{\sqrt{3+x^4}}.
$$
:::

::: {.solution}

Fix $n\in\NN$ and define
$$
F_0(x)=\frac1{\sqrt{3+x^4}}.
$$
Recursively, for $k=1,\dots,n$, define
$$
F_k(x)=\int_0^x F_{k-1}(t)\,dt.
$$

::: pf

::: {.pf-step #s1-1}

Each $F_k$ is continuously differentiable and
$$
F_k'(x)=F_{k-1}(x)
\qquad(k=1,\dots,n).
$$


::: pf-proof

The function $F_0$ is continuous on $\RR$. If $F_{k-1}$ is continuous,
then the Fundamental Theorem of Calculus applied to
$$
F_k(x)=\int_0^xF_{k-1}(t)\,dt
$$
shows that $F_k$ is differentiable and
$$
F_k'=F_{k-1}.
$$
Induction gives the claim for every $k\le n$.

:::

:::

::: {.pf-step #s1-2}

The function
$$
\boxed{f=F_n}
$$
satisfies
$$
f^{(n)}(x)=\frac1{\sqrt{3+x^4}}
\qquad(x\in\RR).
$$


::: pf-proof

Repeatedly applying step [](#s1-1){.pf-ref} gives
$$
F_n^{(n)}
=F_{n-1}^{(n-1)}
=\cdots
=F_1'
=F_0.
$$
By definition of $F_0$, this is the required derivative.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} constructs the required function for the arbitrary natural number
$n$.

:::

:::

:::
