---
schema: qual/card@1
id: P-ROEFL
kind: problem
title: Uniform compact convergence of $\sum f^{n}$ for analytic $f:\DD\to\DD$ with
  $f(0)=0$ not a rotation
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Uniform Convergence
  - Series of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-19
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'The source assumes only that f is analytic in the unit disk with f(0)=0 and f not a rotation. Without f(D) contained in D the claim is false (f(z)=2z), so the statement now assumes f maps D into D, as the Schwarz lemma argument requires.'
---

::: {.problem}
Assume $f(z)$ is analytic in ${\DD}$, maps ${\DD}$ into ${\DD}$, $f(0)=0$, and $f$ is not a rotation (i.e. $f(z) \neq e^{i \theta} z$). Show that $\displaystyle \sum_{n=1}^\infty f^{n}(z)$ converges uniformly to an analytic function on compact subsets of ${\DD}$, where $f^{n+1}(z) = f(f^{n}(z))$.
:::

::: {.solution}
Let $h(z)\coloneqq f(z)/z$ for $z\ne0$ and $h(0)\coloneqq f'(0)$; since $f(0)=0$, $h$ is holomorphic on $\DD$. Fix a compact set $K\subset\DD$ and $R<1$ with $K\subseteq\overline D(0,R)$.

::: pf

::: {.pf-step #strict}

$\abs{h(z)}<1$ for every $z\in\DD$.

::: pf-proof

By the Schwarz lemma, $\abs{f(z)}\le\abs z$, so $\abs h\le1$ on $\DD$. If $\abs{h(z_0)}=1$ for some $z_0\in\DD$, the maximum modulus principle makes $h$ a constant $e^{i\theta}$, so $f(z)=e^{i\theta}z$ is a rotation, contrary to hypothesis.

:::

:::

::: {.pf-step #contract}

There is $c<1$ with $\abs{f(z)}\le c\abs z$ for all $\abs z\le R$.

::: pf-proof

Let $c\coloneqq\max_{\abs z\le R}\abs{h(z)}$; it is attained on the compact disk, so $c<1$ by step [](#strict){.pf-ref}. Then $\abs{f(z)}=\abs z\abs{h(z)}\le c\abs z$.

:::

:::

::: {.pf-step #decay}

$\abs{f^n(z)}\le c^nR$ for all $n\ge1$ and $\abs z\le R$.

::: pf-proof

By step [](#contract){.pf-ref}, $f$ maps $\overline D(0,R)$ into itself, so induction on $n$ gives $\abs{f^{n+1}(z)}=\abs{f(f^n(z))}\le c\abs{f^n(z)}\le c^{n+1}\abs z\le c^{n+1}R$.

:::

:::

::: pf-step

$\sum_{n\ge1}f^n$ converges uniformly on compact subsets of $\DD$ to an analytic function.

::: pf-proof

By step [](#decay){.pf-ref} and the Weierstrass M-test with $M_n=c^nR$, the series converges uniformly on $K$; since $K$ is arbitrary, it converges uniformly on compact subsets of $\DD$. Each $f^n$ is holomorphic as a composition of holomorphic maps, and a locally uniform limit of holomorphic functions is holomorphic.

:::

:::

:::

:::
