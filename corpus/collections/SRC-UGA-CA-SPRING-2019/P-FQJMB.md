---
schema: qual/card@1
id: P-FQJMB
kind: problem
title: $e^x(\cos y+i\sin y)$ is the unique entire solution of $E'=E$, $E(0)=1$
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Entire Functions
  - Power Series
  - Identity Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-18
  note: >-
    The statement is the one this examination card stores; no printed examination paper is retained,
    so it was not re-read against the original.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured both parts into numbered steps. Supplied the verification that E(z)E(-z) = 1 from the
    real and imaginary parts, which is what makes E zero-free and lets F/E be differentiated; the
    quotient rule computation for (F/E)'; and the ratio-test radius for the exponential series. The
    mathematics is the card's own; no defect found.
---

::: {.problem}
Define

$$
E(z)=e^{x}(\cos y+i \sin y) .
$$

- Show that $E(z)$ is the unique function analytic on $\CC$ that satisfies

$$
E^{\prime}(z)=E(z), \quad E(0)=1 .
$$

- Conclude from the first part that 
$$
E(z)=\sum_{n=0}^{\infty} \frac{z^{n}}{n !}
.$$
:::

::: {.solution}

The argument is the card's own; the card is an examination problem and no published solution is retained for it.

Write $z=x+iy$ with $x,y\in\RR$ and $E(z)=e^{x}(\cos y+i\sin y)$.

::: pf

::: {.pf-step #entire}
$E$ is entire, $E'(z)=E(z)$ and $E(0)=1$.

::: pf-proof
With $u(x,y)=e^{x}\cos y$ and $v(x,y)=e^{x}\sin y$ we have $u_{x}=e^{x}\cos y=v_{y}$ and $u_{y}=-e^{x}\sin y=-v_{x}$, so the Cauchy--Riemann equations hold at every point and, the partials being continuous, $E$ is holomorphic on $\CC$ with $E'(z)=u_{x}+iv_{x}=e^{x}(\cos y+i\sin y)=E(z)$. Finally $E(0)=e^{0}(\cos0+i\sin0)=1$.
:::

:::

::: {.pf-step #nonzero}
$E(z)E(-z)=1$ for every $z$, so $E$ has no zeros.

::: pf-proof
$E(-z)=e^{-x}\bigl(\cos(-y)+i\sin(-y)\bigr)=e^{-x}(\cos y-i\sin y)$, so $E(z)E(-z)=e^{x}e^{-x}(\cos y+i\sin y)(\cos y-i\sin y)=\cos^{2}y+\sin^{2}y=1$. Hence $E(z)\neq0$ for every $z$, with inverse $E(-z)$.
:::

:::

::: {.pf-step #unique}
A function $F$ analytic on $\CC$ with $F'=F$ and $F(0)=1$ equals $E$.

::: pf-proof
$E$ is entire and zero-free by steps [](#entire){.pf-ref} and [](#nonzero){.pf-ref}, so $F/E$ is entire, and the quotient rule gives $\bigl(F/E\bigr)'=(F'E-FE')/E^{2}=(FE-FE)/E^{2}=0$. An entire function with zero derivative is constant, so $F/E=c$; evaluating at $0$ gives $c=F(0)/E(0)=1$. Hence $F=E$.
:::

:::

::: {.pf-step #series}
The power series $S(z)=\sum_{n\geq0}z^{n}/n!$ converges on all of $\CC$, satisfies $S'=S$ and $S(0)=1$, hence equals $E$.

::: pf-proof
The ratio of successive coefficients is $\abs{z^{n+1}/(n+1)!}\big/\abs{z^{n}/n!}=\abs{z}/(n+1)\to0$ for every $z$, so the series has infinite radius of convergence and defines an entire function, which may be differentiated termwise inside its disc of convergence:
$$
S'(z)=\sum_{n\geq1}\frac{nz^{n-1}}{n!}=\sum_{n\geq1}\frac{z^{n-1}}{(n-1)!}=\sum_{m\geq0}\frac{z^{m}}{m!}=S(z),
$$
and $S(0)=1/0!=1$. By step [](#unique){.pf-ref}, $E=S$.
:::

:::

::: {.pf-step}
$E(z)=e^{x}(\cos y+i\sin y)$ is the unique entire function with $E'=E$, $E(0)=1$, and it equals $\sum_{n\geq0}z^{n}/n!$.

::: pf-proof
Steps [](#entire){.pf-ref} and [](#unique){.pf-ref} give existence and uniqueness, and step [](#series){.pf-ref} identifies the power series with $E$.
:::

:::

:::

:::
