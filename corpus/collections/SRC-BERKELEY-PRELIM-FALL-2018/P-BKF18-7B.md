---
schema: qual/card@1
id: P-BKF18-7B
kind: problem
title: Multivariate Gaussian integral with a linear term
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
For a real symmetric positive definite matrix $A$ and $v\in\RR^n$, show that
$$
\int_{\RR^n}\exp(-x^TAx+2v^Tx)\,dx
=\frac{\pi^{n/2}}{\sqrt{\det A}}\exp(v^TA^{-1}v).
$$
You may assume that $\int_{-\infty}^{\infty}e^{-x^2}\,dx=\sqrt\pi$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

With $w=A^{-1}v$ and $y=x-w$,
$$
-x^TAx+2v^Tx=-y^TAy+v^TA^{-1}v.
$$

::: pf-proof

Expand $-(y+w)^TA(y+w)+2v^T(y+w)$. Since $A$ is symmetric and $Aw=v$, the terms linear in $y$ are $-2w^TAy+2v^Ty=0$, and the constant terms are $-w^TAw+2v^Tw=v^TA^{-1}v$.

:::

:::

::: {.pf-step #s2}

$$
\int_{\RR^n}e^{-y^TAy}\,dy=\frac{\pi^{n/2}}{\sqrt{\det A}}.
$$

::: pf-proof

Write $A=UDU^T$ with $U$ orthogonal and $D=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$, $\lambda_k>0$. The substitution $y=Uz$ has Jacobian $1$, and $y^TAy=\sum_k\lambda_kz_k^2$. By Tonelli's theorem the integral is $\prod_k\int_\RR e^{-\lambda_kt^2}\,dt=\prod_k\sqrt{\pi/\lambda_k}=\pi^{n/2}/\sqrt{\det A}$, using $\int_\RR e^{-\lambda t^2}\,dt=\lambda^{-1/2}\sqrt\pi$ (substitute $s=\sqrt\lambda\,t$).

:::

:::

::: pf-qed

The translation $y=x-w$ preserves Lebesgue measure. Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give
$$
\int_{\RR^n}\exp(-x^TAx+2v^Tx)\,dx=e^{v^TA^{-1}v}\int_{\RR^n}e^{-y^TAy}\,dy=\frac{\pi^{n/2}}{\sqrt{\det A}}\exp(v^TA^{-1}v).
$$

:::

:::

:::
