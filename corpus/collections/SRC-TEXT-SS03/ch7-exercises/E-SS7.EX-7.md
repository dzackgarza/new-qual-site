---
schema: qual/card@1
id: E-SS7.EX-7
kind: problem
title: Reality of the completed zeta function on two lines
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Zeta Function
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 7, §3, exercise 7, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the printed
    exercise; nothing was changed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Proved. On the real axis $\xi$ takes real values; by Schwarz reflection $\xi(\bar s)=\overline{\xi(s)}$;
    and the functional equation $\xi(s)=\xi(1-s)$ at $s=1/2+it$ reads $\xi(s)=\xi(\bar s)$, so
    $\xi(s)$ equals its own conjugate. The poles at $0$ and $1$ lie off both loci considered.
---

::: {.exercise}
Show that
$$
\xi(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)
$$
is real when $s$ is real or when $\Re s=1/2$.
:::

::: {.solution}

Let $\xi(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$, which satisfies the functional equation $\xi(s)=\xi(1-s)$.

::: pf

::: {.pf-step #s1}

$\xi$ is real on the real axis away from its poles, and $\xi(\bar s)=\overline{\xi(s)}$.

::: pf-proof

For real $s>1$ each factor $\pi^{-s/2}$, $\Gamma(s/2)$ and $\zeta(s)=\sum n^{-s}$ is real and positive, so $\xi(s)$ is real; by the functional equation the same holds for real $s<0$ away from the poles at $0,1$.

The function $\xi$ is meromorphic on $\CC$, with poles only where $\Gamma(s/2)$ has them or where $\zeta$ does, that is at $s=0,1,-2,-4,\dots$ (and $\zeta$'s pole at $1$ is matched by the pole of $\Gamma$ at $0$ through $\xi(s)=\xi(1-s)$). Its restriction to the real axis is real-valued on the set $(1,\infty)$, which accumulates at every real point not a pole. Hence, by Schwarz reflection, $\xi(\bar s)=\overline{\xi(s)}$ at every point where $\xi$ is holomorphic.

:::

:::

::: {.pf-step #s2}

If $\Re s=1/2$ then $\xi(s)$ is real.

::: pf-proof

Write $s=\tfrac12+it$. Then $1-s=\tfrac12-it=\bar s$, so by the functional equation and step [](#s1){.pf-ref},
$$
\xi(s)=\xi(1-s)=\xi(\bar s)=\overline{\xi(s)} .
$$
A complex number equal to its own conjugate is real. Neither $s$ nor $\bar s$ is a pole, since the poles are $0,1,-2,-4,\dots$ and $\Re s=1/2$.

:::

:::

:::

:::
