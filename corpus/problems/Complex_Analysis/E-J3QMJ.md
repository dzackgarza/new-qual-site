---
schema: qual/card@1
id: E-J3QMJ
kind: problem
title: Constancy on a closed subdisk of $\DD$ implies constancy on $\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Identity Theorem
  - Maximum Modulus Principle
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured: the card's single step was correct but carried none of the hypotheses' roles,
    so it is now separated into the value on the closed disc, the openness and nonemptiness of
    the interior disc inside the connected domain, and the identity theorem with its two
    hypotheses named (holomorphy on a domain, vanishing on a nonempty open set). Nothing
    mathematical was changed; in particular the closed disc enters only through its interior,
    which is worth seeing because it is the weakest form the hypothesis needs.
---

::: {.exercise}
Show that if $f\in\Hol(\DD)$ is constant on a closed disk $r\overline\DD$ for some $0<r<1$, then $f$ is constant on $\DD$.
:::

::: {.solution}
Throughout $\DD$ is the open unit disc, $0 < r < 1$, $r\DD = \theset{z \mid \abs{z} < r}$ is the open disc of radius $r$ and $r\overline{\DD} = \theset{z \mid \abs{z} \le r}$ its closure; $f \in \Hol(\DD)$ means $f$ is holomorphic on $\DD$.

::: pf

::: {.pf-step #value}
There is $c \in \CC$ with $f = c$ on $r\overline{\DD}$, hence on the open set $r\DD$.

::: pf-proof
This is the hypothesis: $f$ is constant on the closed disc of radius $r$, with value $c$; the open disc $r\DD$ is contained in $r\overline{\DD}$.

:::

:::

::: {.pf-step #open}
$r\DD$ is a nonempty open subset of the connected domain $\DD$.

::: pf-proof
$r\DD$ is open as a union of open discs about its points, and nonempty because $r > 0$ puts $0$ in it; it is contained in $\DD$ because $r < 1$. The disc $\DD$ is convex, hence connected.

:::

:::

::: {.pf-step #identity}
$f - c$ vanishes identically on $\DD$.

::: pf-proof
$f - c$ is holomorphic on $\DD$, being a constant subtracted from a holomorphic function, and it vanishes on the nonempty open set $r\DD$ by step [](#value){.pf-ref}. The identity theorem says that a holomorphic function on a domain which vanishes on a nonempty open subset vanishes everywhere; the domain here is $\DD$, connected by step [](#open){.pf-ref}.

:::

:::

::: pf-step
$f$ is constant on $\DD$, with the value $c$ it takes on $r\overline{\DD}$.

::: pf-proof
By step [](#identity){.pf-ref} $f - c \equiv 0$, that is $f \equiv c$ on $\DD$.

:::

:::

:::
:::
