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
Let $\Omega\subseteq\mathbb C$ be open and define
\[
|\Omega|=\{|z|:z\in\Omega\}\subseteq\mathbb R_{\ge0}.
\]
Show that $|\Omega|$ is relatively open in $\mathbb R_{\ge0}$.
:::

::: pf

::: pf-step

Let $\rho\in|\Omega|$. Choose $a\in\Omega$ with
$$
|a|=\rho.
$$


::: pf-proof

This follows directly from the definition
$|\Omega|=\{|z|:z\in\Omega\}$.

:::

:::

::: pf-step

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

::: pf-step

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

::: pf-step

Every point of $|\Omega|$ has a neighborhood relative to $\mathbb R_{\ge0}$ contained in $|\Omega|$.


::: pf-proof

Let $\rho\in|\Omega|$ and choose $a$ as in step <1>1. If $a\ne0$,
step <1>2 gives an open interval about $\rho$ contained in
$|\Omega|$. If $a=0$, then $\rho=0$, and step <1>3 gives
$$
[0,r)=(-r,r)\cap\mathbb R_{\ge0}
$$
contained in $|\Omega|$. These are exactly relative neighborhoods in
$\mathbb R_{\ge0}$.

:::

:::

::: pf-step

Therefore $|\Omega|$ is relatively open in $\mathbb R_{\ge0}$.


::: pf-proof

Step <1>4 is the definition of openness in the subspace topology on
$\mathbb R_{\ge0}$.

:::

:::

::: pf-qed

Step <1>5 is the required conclusion.

:::

:::
