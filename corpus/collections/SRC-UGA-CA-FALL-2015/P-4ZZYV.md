---
schema: qual/card@1
id: P-4ZZYV
kind: problem
title: Entire functions with $f(z)\to\infty$ as $z\to\infty$ are polynomials
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Polynomials
  - Singularities
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $f$ be entire and suppose that $\lim_{z \rightarrow \infty} f(z) = \infty$.
Show that $f$ is a polynomial.
:::

::: {.solution}
**Goal:** Prove that if $f$ is entire and $\lim_{z \to \infty} f(z) = \infty$, then $f$ is a polynomial.

::: pf

::: pf-step

Define $g(w) := f\qty(\frac{1}{w})$ for $w \neq 0$; then $g$ is holomorphic on $\CC \setminus \theset{0}$.

::: pf-proof

Composition of the holomorphic maps $w \mapsto 1/w$ and $f$.

:::

:::

::: {.pf-step #s2}

$w = 0$ is a pole of $g$, not an essential singularity.

::: pf-proof

::: pf-step

$\lim_{w \to 0} g(w) = \infty$.

::: pf-proof

As $w \to 0$, $1/w \to \infty$ in modulus, and $\lim_{z \to \infty} f(z) = \infty$ by hypothesis.

:::

:::

::: pf-step

$0$ is not essential.

::: pf-proof

If $0$ were an essential singularity, then by Casorati--Weierstrass the values $g(w)$ would be dense in $\CC$ for $w$ near $0$, contradicting $\abs{g(w)} \to \infty$; equivalently $1/g$ is bounded near $0$ with limit $0$, a removable singularity, so $g$ has a pole.

:::

:::

:::

:::

::: {.pf-step #s3}

$g$ has a pole of some order $m \geq 1$ at $0$, so its Laurent expansion is $g(w) = \sum_{k=-m}^{\infty} c_k w^k$.

::: pf-proof

By step [](#s2){.pf-ref}, the Laurent series about $0$ has only finitely many negative powers, the most negative being $-m$.

:::

:::

::: {.pf-step #s4}

For $z \neq 0$, $f(z) = \sum_{k=-m}^{\infty} c_k z^{-k} = \sum_{k=0}^{m} c_{-k} z^k + \sum_{j=1}^{\infty} c_j z^{-j}$.

::: pf-proof

Substitute $w = 1/z$ into step [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

The tail $\sum_{j=1}^{\infty} c_j z^{-j}$ vanishes: $c_j = 0$ for all $j \geq 1$.

::: pf-proof

$f$ is entire, so its Laurent expansion about $z = 0$ (which is step [](#s4){.pf-ref}, valid for $z \neq 0$ and hence on a punctured neighborhood of $0$) has no negative powers of $z$; the terms $c_j z^{-j}$ are exactly the negative powers.

:::

:::

::: {.pf-step #s6}

$f$ is a polynomial.

::: pf-proof

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} give $f(z) = \sum_{k=0}^{m} c_{-k} z^k$, a polynomial of degree at most $m$.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is the claim.

:::

:::

:::
