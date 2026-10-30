---
schema: qual/card@1
id: P-X7WUF
kind: problem
title: Residue at a pole of order $m$, and $\oint_{\abs{z}=4}\frac{e^\tau}{(\tau^2+\pi^2)^2}\,d\tau$
classification:
  areas:
    - complex-analysis
  topics:
    - Residues
    - Poles
    - Contour Integration
relations: []
review: draft
---

::: {.problem}
(a) Let $F$ be an analytic function inside and on a simple closed curve $C$, except for a pole of order $m\geq 1$ at $z=a$ inside $C$. Prove that
$$
\frac{1}{2 \pi i}\oint_{C} F(\tau)\, d\tau =
\lim_{\tau\to a} \frac{d^{m-1}}{d\tau^{m-1}}\bigl((\tau-a)^m F(\tau)\bigr).
$$

(b) Evaluate
$$
\oint_{C}\frac{e^{\tau}}{(\tau^2+\pi^2)^2}\,d\tau,
$$
where $C$ is the circle $\abs{z}=4$, oriented counterclockwise.
:::

::: remark
The formula in part (a) omits the factor $\frac{1}{(m-1)!}$ on the right side. It is correct as printed only for $m\le2$. The solution proves the corrected formula.
:::

::: {.solution}

::: pf

::: {.pf-step #laurent}

$$
\frac{1}{2\pi i}\oint_C F(\tau)\,d\tau
=\frac{1}{(m-1)!}\lim_{\tau\to a}\frac{d^{m-1}}{d\tau^{m-1}}\bigl((\tau-a)^mF(\tau)\bigr).
$$

::: pf-proof

By the residue theorem, the left side is $\operatorname{Res}_{\tau=a}F=c_{-1}$, where $F(\tau)=\sum_{k\ge-m}c_k(\tau-a)^k$ near $a$. The function $g(\tau)=(\tau-a)^mF(\tau)=\sum_{j\ge0}c_{j-m}(\tau-a)^j$ has a removable singularity at $a$. Its Taylor coefficient of $(\tau-a)^{m-1}$ is $c_{-1}=g^{(m-1)}(a)/(m-1)!$, and $g^{(m-1)}(a)=\lim_{\tau\to a}g^{(m-1)}(\tau)$ because $g^{(m-1)}$ is continuous at $a$.

:::

:::

::: {.pf-step #res}

$$
\operatorname{Res}_{\tau=\pm i\pi}\frac{e^\tau}{(\tau^2+\pi^2)^2}=\frac{1}{4\pi^2}\pm\frac{i}{4\pi^3}.
$$

::: pf-proof

The integrand is $e^\tau(\tau-i\pi)^{-2}(\tau+i\pi)^{-2}$, with double poles at $\pm i\pi$. By Step [](#laurent){.pf-ref} with $m=2$, the residue at $i\pi$ is the derivative of $h(\tau)=e^\tau(\tau+i\pi)^{-2}$ at $i\pi$:
$$
h'(i\pi)=e^{i\pi}\left(\frac{1}{(2i\pi)^2}-\frac{2}{(2i\pi)^3}\right)
=-\left(-\frac{1}{4\pi^2}-\frac{i}{4\pi^3}\right)
=\frac{1}{4\pi^2}+\frac{i}{4\pi^3}.
$$
The same computation with $i$ replaced by $-i$ gives the residue at $-i\pi$, which is the complex conjugate.

:::

:::

::: {.pf-step #int}

$$
\boxed{\oint_C\frac{e^\tau}{(\tau^2+\pi^2)^2}\,d\tau=\frac{i}{\pi}}
$$

::: pf-proof

Both poles satisfy $\abs{\pm i\pi}=\pi<4$, so both lie inside $C$. By the residue theorem and Step [](#res){.pf-ref}, the integral is $2\pi i\cdot\frac{2}{4\pi^2}=\frac{i}{\pi}$.

:::

:::

::: pf-qed

Step [](#laurent){.pf-ref} proves the corrected part (a), and Step [](#int){.pf-ref} proves part (b).

:::

:::

:::
