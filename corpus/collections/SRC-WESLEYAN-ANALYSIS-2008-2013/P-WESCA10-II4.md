---
schema: qual/card@1
id: P-WESCA10-II4
kind: problem
title: 'An injective analytic function has nonvanishing derivative'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $D\subset\CC$ be a domain and let $f:D\to\CC$ be analytic and injective.
Prove that
$$
f'(z)\ne0\qquad(z\in D).
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $a\in D$ and $f'(a)=0$, then there is an integer $m\ge2$ and a
holomorphic function $g$ near $a$ such that
$$
f(z)-f(a)=(z-a)^m g(z),
\qquad
g(a)\ne0.
$$


::: pf-proof

Because $f$ is injective, it is nonconstant. Hence the Taylor expansion of
$f-f(a)$ at $a$ has a first nonzero term. Since $f'(a)=0$, its order $m$ is at
least $2$. Factoring out $(z-a)^m$ gives the displayed expression, with
$g(a)\ne0$.

:::

:::

::: {.pf-step #s1-2}

There is a neighborhood $U$ of $a$ and a biholomorphic coordinate
$\phi:U\to\phi(U)$ with $\phi(a)=0$ such that
$$
f(z)-f(a)=\phi(z)^m
\qquad(z\in U).
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, after shrinking to a simply connected disk $U$ about $a$, the
function $g$ has no zeros on $U$. Therefore $g$ admits a holomorphic $m$-th
root $h$ on $U$, so $h^m=g$. Define
$$
\phi(z)=(z-a)h(z).
$$
Then
$$
f(z)-f(a)=\phi(z)^m.
$$
Moreover,
$$
\phi'(a)=h(a)\ne0,
$$
so the holomorphic inverse function theorem allows $U$ to be shrunk further
so that $\phi$ is biholomorphic onto the open neighborhood $\phi(U)$ of $0$.

:::

:::

::: {.pf-step #s1-3}

The assumption $f'(a)=0$ contradicts injectivity of $f$.


::: pf-proof

By step [](#s1-2){.pf-ref}, the open set $\phi(U)$ contains a disk centered at $0$.
Choose a nonzero $w$ in that disk small enough that
$$
w,\qquad e^{2\pi i/m}w
$$
both lie in $\phi(U)$. Since $m\ge2$, these two numbers are distinct but have
the same $m$-th power. Let
$$
z_1=\phi^{-1}(w),
\qquad
z_2=\phi^{-1}(e^{2\pi i/m}w).
$$
Then $z_1\ne z_2$, while step [](#s1-2){.pf-ref} gives
$$
f(z_1)-f(a)=w^m
=\bigl(e^{2\pi i/m}w\bigr)^m
=f(z_2)-f(a).
$$
Thus $f(z_1)=f(z_2)$, contradicting injectivity.

:::

:::

::: {.pf-step #s1-4}

Hence
$$
\boxed{f'(z)\ne0\qquad(z\in D)}.
$$


::: pf-proof

If $f'$ vanished at any $a\in D$, step [](#s1-3){.pf-ref} would contradict the hypothesis
that $f$ is injective.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
