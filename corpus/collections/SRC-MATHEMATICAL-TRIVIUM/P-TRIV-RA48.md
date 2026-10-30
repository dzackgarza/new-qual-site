---
schema: qual/card@1
id: P-TRIV-RA48
kind: problem
title: Fourier transforms under scaling and translation
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 48, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
(a) The functions $f(x)$ and $g(x)$ are related by $f(x) = g(ax)$. How are their Fourier images related?

(b) The functions $f(x)$ and $g(x)$ are related by $f(x) = g(x - x_0)$. How are their Fourier images related?
:::

::: {.remark}
Use the Fourier convention from Problems 45--47:
$$
\widetilde h(k)
=
\frac1{2\pi}
\int_{-\infty}^{\infty}
h(x)e^{-ikx}
\,dx.
$$
In part (a), assume $a\neq0$.
:::

::: {.solution}

::: pf

::: pf-step

Suppose
$$
f(x)=g(ax),
\qquad
a\neq0.
$$
Then
$$
\widetilde f(k)
=
\frac1{2\pi}
\int_{-\infty}^{\infty}
g(ax)e^{-ikx}
\,dx.
$$


::: pf-proof

This is the definition of the Fourier transform applied to $f$.

:::

:::

::: {.pf-step #s1-2}

With
$$
u=ax,
$$
one obtains
$$
\boxed{
\widetilde f(k)
=
\frac1{\abs{a}}
\widetilde g\left(\frac{k}{a}\right).
}
$$


::: pf-proof

If $a>0$, then
$$
dx=\frac{du}{a}
$$
and the endpoints retain their order, giving
$$
\widetilde f(k)
=
\frac1a
\frac1{2\pi}
\int_{-\infty}^{\infty}
g(u)e^{-i(k/a)u}
\,du
=
\frac1a\widetilde g(k/a).
$$

If $a<0$, the substitution reverses the endpoints, contributing an additional
minus sign that changes $1/a$ to $1/\abs{a}$. The argument remains $k/a$.

:::

:::

::: {.pf-step #s1-3}

Part (a) follows.


::: pf-proof

This is step [](#s1-2){.pf-ref}.

:::

:::

::: pf-step

Suppose
$$
f(x)=g(x-x_0).
$$
Then
$$
\widetilde f(k)
=
\frac1{2\pi}
\int_{-\infty}^{\infty}
g(x-x_0)e^{-ikx}
\,dx.
$$


::: pf-proof

Again this is the Fourier-transform definition.

:::

:::

::: {.pf-step #s1-5}

Set
$$
u=x-x_0.
$$
Then
$$
\boxed{
\widetilde f(k)
=
e^{-ikx_0}\widetilde g(k).
}
$$


::: pf-proof

The substitution gives
$$
x=u+x_0,
\qquad
dx=du.
$$
Therefore
$$
\begin{aligned}
\widetilde f(k)
&=
\frac1{2\pi}
\int_{-\infty}^{\infty}
g(u)e^{-ik(u+x_0)}
\,du\\
&=
e^{-ikx_0}
\frac1{2\pi}
\int_{-\infty}^{\infty}
g(u)e^{-iku}
\,du\\
&=
e^{-ikx_0}\widetilde g(k).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-6}

Part (b) follows.


::: pf-proof

This is step [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref} and [](#s1-6){.pf-ref} establish parts (a) and (b), respectively.

:::

:::

:::
