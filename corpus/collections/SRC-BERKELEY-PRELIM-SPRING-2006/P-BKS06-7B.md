---
schema: qual/card@1
id: P-BKS06-7B
kind: problem
title: Sharp bound $\abs{f^{(m)}(0)}\le m!e^m/m^m$ for entire $f$ with $\abs{f(z)}\le e^{\abs{z}}$
classification:
  areas: [prelim]
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $m$ be a fixed positive integer.

(a) Show that if an entire function $f \colon \CC \to \CC$ satisfies $\abs{f(z)} \leq e^{\abs{z}}$ for all $z \in \CC$, then
$$
\abs{f^{(m)}(0)} \leq \frac{m!\, e^{m}}{m^{m}}.
$$

(b) Prove that there exists an entire function $f$ such that $\abs{f(z)} \leq e^{\abs{z}}$ for all $z$ and
$$
\abs{f^{(m)}(0)} = \frac{m!\, e^{m}}{m^{m}}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every $R>0$, $\abs{f^{(m)}(0)}\le m!\,e^R/R^m$.

::: pf-proof

By the Cauchy integral formula,
$$
\frac{f^{(m)}(0)}{m!}=\frac1{2\pi i}\oint_{\abs{z}=R}\frac{f(z)}{z^{m+1}}\,dz,
$$
and the integrand has modulus at most $e^R/R^{m+1}$ on a circle of length $2\pi R$.

:::

:::

::: {.pf-step #s2}

On $(0,\infty)$, the function $h(x)=e^x/x^m$ has minimum value $e^m/m^m$, taken at $x=m$.

::: pf-proof

$\frac{d}{dx}\log h(x)=1-\frac mx$ is negative for $x<m$ and positive for $x>m$.

:::

:::

::: {.pf-step #s3}

Part (a) holds.

::: pf-proof

Take $R=m$ in step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s4}

The function $f(z)=\dfrac{e^m}{m^m}z^m$ satisfies part (b).

::: pf-proof

$f^{(m)}(0)=m!\,e^m/m^m$. For $z\ne0$, step [](#s2){.pf-ref} gives $\abs{f(z)}=\frac{e^m}{m^m}\abs{z}^m\le\frac{e^{\abs{z}}}{\abs{z}^m}\abs{z}^m=e^{\abs{z}}$, and $\abs{f(0)}=0\le1$.

:::

:::

::: pf-qed

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} prove parts (a) and (b).

:::

:::

:::
