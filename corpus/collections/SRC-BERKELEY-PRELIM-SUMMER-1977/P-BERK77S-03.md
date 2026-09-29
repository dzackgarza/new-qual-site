---
schema: qual/card@1
id: P-BERK77S-03
kind: problem
title: A polynomial in $\QQ[x]$ with root $\sqrt3+\sqrt5$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Squared alpha once to isolate sqrt(15), then squared again to obtain
    alpha^4-16 alpha^2+4=0. This gives an explicit nonzero polynomial in
    Q[x] with alpha as a root.
---

::: {.problem}
Prove that
\[
\alpha=\sqrt3+\sqrt5
\]
is algebraic over $\mathbb Q$ by explicitly finding a polynomial in $\mathbb Q[x]$ having $\alpha$ as a root.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

One has
$$
\alpha^2=8+2\sqrt{15}.
$$

::: pf-proof

By the definition of $\alpha$,
$$
\begin{aligned}
\alpha^2
&=
(\sqrt3+\sqrt5)^2\\
&=
3+5+2\sqrt{15}\\
&=
8+2\sqrt{15}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

The number $\alpha$ satisfies
$$
\alpha^4-16\alpha^2+4=0.
$$

::: pf-proof

Step [](#s1){.pf-ref} gives
$$
\alpha^2-8=2\sqrt{15}.
$$
Squaring both sides yields
$$
(\alpha^2-8)^2=60.
$$
Expanding and moving all terms to the left gives
$$
\alpha^4-16\alpha^2+64-60=0,
$$
hence
$$
\alpha^4-16\alpha^2+4=0.
$$

:::

:::

::: {.pf-step #s3}

An explicit polynomial with rational coefficients having $\alpha$ as
a root is
$$
\boxed{
p(x)=x^4-16x^2+4.
}
$$

::: pf-proof

The polynomial $p$ lies in $\QQ[x]$ and is nonzero. Step [](#s2){.pf-ref} says exactly
that $p(\alpha)=0$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves that $\alpha$ is algebraic over $\QQ$ and supplies the
requested polynomial.

:::

:::

:::
