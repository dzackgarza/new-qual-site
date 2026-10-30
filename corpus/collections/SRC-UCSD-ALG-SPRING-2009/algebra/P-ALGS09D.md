---
schema: qual/card@1
id: P-ALGS09D
kind: problem
title: "Galois group of the splitting field of $\\sqrt{2+\\sqrt{2}}$ over $\\QQ$"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 4 of the official UCSD Spring 2009 algebra qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Corrected the splitting-field identification and exhibited an automorphism cycling the four roots, proving the Galois group is cyclic of order 4.
---

::: {.problem}
Let $\alpha = \sqrt{2 + \sqrt{2}}$ in $\CC$ and let $f$ be the minimal polynomial of $\alpha$ over $\QQ$.
Let $E$ be the splitting field for $f$ over $\QQ$.
Determine the Galois group $\operatorname{Gal}(E/\QQ)$.
:::

::: {.solution}
Let
$$
\alpha=\sqrt{2+\sqrt2},
\qquad
\beta=\sqrt{2-\sqrt2}.
$$

::: pf

::: {.pf-step #s1}

The minimal polynomial of $\alpha$ over $\QQ$ is
$$
f(x)=x^4-4x^2+2.
$$

::: pf-proof

Since
$$
\alpha^2=2+\sqrt2,
$$
we have
$$
(\alpha^2-2)^2=2,
$$
so $f(\alpha)=0$.
The polynomial $f$ is Eisenstein at $2$: every nonleading coefficient is divisible by $2$, and the constant term $2$ is not divisible by $4$.
Hence $f$ is irreducible over $\QQ$.
Therefore $f$ is the minimal polynomial of $\alpha$ and
$$
[\QQ(\alpha):\QQ]=4.
$$

:::

:::

::: {.pf-step #s2}

The roots of $f$ are
$$
\pm\alpha,
\qquad
\pm\beta.
$$

::: pf-proof

The equation $f(x)=0$ is equivalent to
$$
(x^2-2)^2=2,
$$
so
$$
x^2=2\pm\sqrt2.
$$
Taking square roots gives precisely the four displayed roots.

:::

:::

::: {.pf-step #s3}

The field $\QQ(\alpha)$ already contains $\beta$.

::: pf-proof

We have
$$
\sqrt2=\alpha^2-2\in\QQ(\alpha).
$$
Also
$$
\alpha\beta
=\sqrt{(2+\sqrt2)(2-\sqrt2)}
=\sqrt2,
$$
where the positive square root is taken because $\alpha,\beta>0$.
Thus
$$
\beta=\frac{\sqrt2}{\alpha}\in\QQ(\alpha).
$$

:::

:::

::: {.pf-step #s4}

The splitting field is
$$
E=\QQ(\alpha).
$$

::: pf-proof

By steps [](#s2){.pf-ref} and [](#s3){.pf-ref}, $\QQ(\alpha)$ contains all four roots $\pm\alpha,\pm\beta$ of $f$.
Hence it is the splitting field of $f$.
Since $f$ is separable over the characteristic-zero field $\QQ$, the extension $E/\QQ$ is Galois.
By step [](#s1){.pf-ref},
$$
\cardinality{\operatorname{Gal}(E/\QQ)}=[E:\QQ]=4.
$$

:::

:::

::: {.pf-step #s5}

There is an automorphism $\sigma\in\operatorname{Gal}(E/\QQ)$ satisfying
$$
\sigma(\alpha)=\beta,
$$
and it has order $4$.

::: pf-proof

Because $\beta$ is another root of the irreducible polynomial $f$, the assignment $\alpha\mapsto\beta$ defines a $\QQ$-embedding
$$
\QQ(\alpha)\longrightarrow E.
$$
Since $E=\QQ(\alpha)$ is finite over $\QQ$, this embedding is an automorphism; call it $\sigma$.

Now
$$
\sqrt2=\alpha^2-2,
$$
so
$$
\sigma(\sqrt2)=\beta^2-2=(2-\sqrt2)-2=-\sqrt2.
$$
Using $\beta=\sqrt2/\alpha$,
$$
\sigma(\beta)
=\frac{\sigma(\sqrt2)}{\sigma(\alpha)}
=\frac{-\sqrt2}{\beta}
=-\alpha.
$$
Therefore
$$
\alpha\xmapsto{\sigma}\beta
\xmapsto{\sigma}-\alpha
\xmapsto{\sigma}-\beta
\xmapsto{\sigma}\alpha.
$$
Thus $\sigma$ has order $4$.

:::

:::

::: pf-step

Consequently
$$
\operatorname{Gal}(E/\QQ)\cong C_4.
$$

::: pf-proof

By step [](#s4){.pf-ref} the Galois group has order $4$, and by step [](#s5){.pf-ref} it contains an element of order $4$.
Hence the group is cyclic of order $4$.

:::

:::

:::

:::
