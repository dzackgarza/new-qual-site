---
schema: qual/card@1
id: P-BKF92-9
kind: problem
title: Reality of a holomorphic function on both real rays outside the unit disk
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Compared f with the holomorphic reflected function conjugate(f(conjugate z))
    and applied the identity theorem on the connected exterior domain.
---

::: {.problem}
Let $f$ be analytic on $\{z\in\mathbb C:|z|>1\}$. Prove that if $f$ is real-valued on $(1,\infty)$, then it is also real-valued on $(-\infty,-1)$.
:::

::: {.solution}
Let
$$
\Omega\coloneqq\{z\in\CC:\abs z>1\}.
$$

::: pf

::: {.pf-step #s1}

The function
$$
g(z)\coloneqq\overline{f(\overline z)}
$$
is holomorphic on $\Omega$.

::: pf-proof

If $z_0\in\Omega$, then $\overline{z_0}\in\Omega$. Expanding $f$ in a power series around $\overline{z_0}$,
$$
f(w)=\sum_{n=0}^{\infty}a_n(w-\overline{z_0})^n,
$$
gives, near $z_0$,
$$
g(z)
=
\sum_{n=0}^{\infty}\overline{a_n}(z-z_0)^n.
$$
Thus $g$ is holomorphic.

:::

:::

::: {.pf-step #s2}

For every real $x>1$,
$$
g(x)=f(x).
$$

::: pf-proof

Since $x$ is real and $f(x)$ is real by hypothesis,
$$
g(x)
=
\overline{f(\overline x)}
=
\overline{f(x)}
=
f(x).
$$

:::

:::

::: {.pf-step #s3}

One has
$$
g=f
$$
throughout $\Omega$.

::: pf-proof

The domain $\Omega$ is connected. By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, the holomorphic functions $f$ and $g$ agree on the interval $(1,\infty)$, which has accumulation points in $\Omega$. The identity theorem gives $f=g$ on all of $\Omega$.

:::

:::

::: {.pf-step #s4}

For every real $x<-1$, the value $f(x)$ is real.

::: pf-proof

Such an $x$ lies in $\Omega$ and satisfies $\overline x=x$. By step [](#s3){.pf-ref},
$$
f(x)
=
g(x)
=
\overline{f(\overline x)}
=
\overline{f(x)}.
$$
A complex number equal to its conjugate is real. Hence
$$
\boxed{f(x)\in\RR\quad\text{for every }x<-1}.
$$

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
