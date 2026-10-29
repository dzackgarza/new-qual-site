---
schema: qual/card@1
id: P-7ZRIQ
kind: problem
title: Rouché's theorem and $\max_{\abs{z}=1}\abs{P(z)}\ge 1$ for a monic polynomial $P$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Maximum Modulus Principle
  - Polynomials
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source's first part asks for a statement of Rouché's theorem; the card had replaced it with a hint note and now poses it as part (a). Part (b) states that n >= 1 and the a_k are complex, which the source leaves implicit.
---

::: {.problem}
(a) State Rouché's theorem.

(b) Let $n\ge1$ and $a_0,\ldots,a_{n-1}\in\CC$. Prove that
$$
\max_{\abs z = 1} \abs{a_0 + a_1 z + \cdots + a_{n-1}z^{n-1} + z^n} \geq 1.
$$
:::

::: {.solution}
Write $p(z) \coloneqq a_0 + a_1z + \cdots + a_{n-1}z^{n-1} + z^n$ and $q(z)\coloneqq p(z)-z^n$, a polynomial of degree at most $n-1$.

::: pf

::: {.pf-step #rouche}
(a) If $f$ and $g$ are holomorphic on an open set containing a closed disk $\overline D$ and $\abs{g(z)} < \abs{f(z)}$ for all $z\in\partial D$, then $f$ and $f+g$ have the same number of zeros in $D$, counted with multiplicity.

::: pf-proof
This is the statement requested.
:::

:::

::: {.pf-step #q-nonzero}
If $\abs{p(z)}<1$ on $\abs{z}=1$, then $q\not\equiv0$.

::: pf-proof
If $q\equiv0$ then $p(z)=z^n$, and $\abs{p(z)}=1$ on $\abs{z}=1$.
:::

:::

::: pf-step
(b) $\max_{\abs z=1}\abs{p(z)}\ge1$.

::: pf-proof
Suppose instead that $\abs{p(z)}<1=\abs{z^n}$ on $\abs z=1$.
Apply step [](#rouche){.pf-ref} with $f(z)=z^n$ and $g=-p$: the function $f+g=-q$ has $n$ zeros in $\DD$, as $z^n$ does.
By step [](#q-nonzero){.pf-ref}, $q$ is a nonzero polynomial of degree at most $n-1$, so it has at most $n-1$ zeros, a contradiction.
:::

:::

:::

:::
