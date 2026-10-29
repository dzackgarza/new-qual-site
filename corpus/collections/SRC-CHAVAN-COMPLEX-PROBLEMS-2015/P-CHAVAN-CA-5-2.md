---
schema: qual/card@1
id: P-CHAVAN-CA-5-2
kind: problem
title: Moduli of an open subset of the complex plane form a relatively open set
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $\Omega\subseteq\CC$ be open and define
$$
|\Omega|=\{|z|:z\in\Omega\}\subseteq\RR_{\ge0}.
$$
Show that $|\Omega|$ is relatively open in $\RR_{\ge0}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let $\rho\in|\Omega|$. Choose $a\in\Omega$ with
$$
|a|=\rho.
$$


::: pf-proof

This follows directly from the definition
$|\Omega|=\{|z|:z\in\Omega\}$.

:::

:::

::: {.pf-step #s1-2}

If $a\ne0$, then there is an $r>0$ such that
$$
(\rho-r,\rho+r)\subseteq|\Omega|.
$$


::: pf-proof

Since $\Omega$ is open, choose $r>0$ such that
$$
r<|a|
\qquad\text{and}\qquad
B(a,r)\subseteq\Omega.
$$
Let $t\in(\rho-r,\rho+r)$. Because $\rho=|a|>0$, define
$$
z=\frac{t}{\rho}a.
$$
Then $|z|=t$, and
$$
|z-a|
=\left|\frac{t}{\rho}-1\right||a|
=|t-\rho|
<r.
$$
Thus $z\in B(a,r)\subseteq\Omega$, so $t=|z|\in|\Omega|$.

:::

:::

::: {.pf-step #s1-3}

If $a=0$, then there is an $r>0$ such that
$$
[0,r)\subseteq|\Omega|.
$$


::: pf-proof

Since $0=a\in\Omega$ and $\Omega$ is open, choose $r>0$ with
$$
B(0,r)\subseteq\Omega.
$$
For every $t\in[0,r)$, the real number $t$ belongs to $B(0,r)$ and
has modulus $t$. Hence $t\in|\Omega|$.

:::

:::

::: {.pf-step #s1-4}

Every point of $|\Omega|$ has a neighborhood relative to $\RR_{\ge0}$ contained in $|\Omega|$.


::: pf-proof

Let $\rho\in|\Omega|$ and choose $a$ as in step [](#s1-1){.pf-ref}. If $a\ne0$,
step [](#s1-2){.pf-ref} gives an open interval about $\rho$ contained in
$|\Omega|$. If $a=0$, then $\rho=0$, and step [](#s1-3){.pf-ref} gives
$$
[0,r)=(-r,r)\cap\RR_{\ge0}
$$
contained in $|\Omega|$. These are exactly relative neighborhoods in
$\RR_{\ge0}$.

:::

:::

::: {.pf-step #s1-5}

Therefore $|\Omega|$ is relatively open in $\RR_{\ge0}$.


::: pf-proof

Step [](#s1-4){.pf-ref} is the definition of openness in the subspace topology on
$\RR_{\ge0}$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
