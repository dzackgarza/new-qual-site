---
schema: qual/card@1
id: E-SS8.EX-1
kind: problem
title: A holomorphic map is a local bijection exactly where $f'\ne0$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Rouché
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The collection's provenance is the publisher's catalogue record only, with no retained text and no retained solution set, so the statement is taken as the card prints it; the argument is the card's own. Checked: the factorisation $f-f(z_0)=(z-z_0)g$ and the multiplicity-one zero; the Rouché comparison of the moduli $\abs{f(z)-w}$ and $\abs{f(z)-f(z_0)}$ on $\partial D$; and in the converse the local biholomorphy of $\phi$ together with the failure of injectivity of $w\mapsto w^m$.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained book `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, at its printed folio (the scan runs nineteen pages ahead of
    the printed page): the statement is Exercise 1 at the head of the Chapter 8 Exercises,
    printed p. 248, and its printed words are the card's. The chapter, the exercise number and
    the page are now named in the solution's opening sentence. Not checked in this pass: the
    argument, which the edit does not touch.
---

::: {.exercise}
A holomorphic mapping $f \colon U \to V$ is a local bijection on $U$ if for every $z \in U$ there exists an open disc $D \subset U$ centered at $z$, so that $f \colon D \to f(D)$ is a bijection.

Prove that a holomorphic map $f \colon U \to V$ is a local bijection on $U$ if and only if $f'(z) \neq 0$ for all $z \in U$.

[Hint: Use Rouché's theorem as in the proof of Proposition 1.1.]
:::

::: {.solution}
This is Exercise 1 of Chapter 8 of Stein and Shakarchi, *Complex Analysis*, retained in this repository as `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, printed p. 248; the statement below is its wording.
No retained text and no retained solution set for this collection: its provenance is the publisher's catalogue record, so the statement is taken as the card prints it, and the argument is the card's own, using Rouché's theorem as the printed hint directs.

::: pf

::: {.pf-step #nonvanishing}
If $f'(z_0)\neq0$ there is a closed disc $\overline D$ about $z_0$ on which $f(z)-f(z_0)$ has exactly one zero, counted with multiplicity.

::: pf-proof
Write $f(z)-f(z_0)=(z-z_0)g(z)$ with $g$ holomorphic near $z_0$ and $g(z_0)=f'(z_0)\neq0$. Choose $\overline D$ small enough that $g$ has no zeros on it; then $f(z)-f(z_0)$ vanishes on $D$ only at $z_0$, and there the factor $z-z_0$ is simple and $g\neq0$, so the zero has multiplicity one and $f(z)\neq f(z_0)$ on $\partial D$.
:::
:::

::: {.pf-step #rouche}
For $w$ with $\abs{w-f(z_0)}<m\coloneqq\min_{\partial D}\abs{f(z)-f(z_0)}$, the function $f(z)-w$ has exactly one zero in $D$.

::: pf-proof
On $\partial D$ we have $\abs{(f(z)-w)-(f(z)-f(z_0))}=\abs{f(z_0)-w}<m\le\abs{f(z)-f(z_0)}$, so by Rouché's theorem $f(z)-w$ has in $D$ as many zeros as $f(z)-f(z_0)$, namely one by step [](#nonvanishing){.pf-ref}.
:::
:::

::: {.pf-step #local}
If $f'$ never vanishes on $U$ then $f$ is a local bijection.

::: pf-proof
By step [](#rouche){.pf-ref} each $w$ near $f(z_0)$ has exactly one preimage in $D$, so $f$ restricted to $D$ is injective and onto an open set $f(D)$; hence $f:D\to f(D)$ is a bijection for a small disc $D$ about each point.
:::
:::

::: {.pf-step #converse}
If $f$ is a local bijection at $z_0$ then $f'(z_0)\neq0$.

::: pf-proof
If $f'(z_0)=0$ then $f(z)-f(z_0)=(z-z_0)^mg(z)$ with $m\ge2$ and $g(z_0)\neq0$. On a small disc $g$ has a holomorphic $m$-th root $h$, so $f(z)-f(z_0)=\phi(z)^m$ with $\phi(z)=(z-z_0)h(z)$; since $\phi'(z_0)=h(z_0)\neq0$, $\phi$ maps a neighbourhood of $z_0$ biholomorphically onto a neighbourhood of $0$, on which $w\mapsto w^m$ is not injective for $m\ge2$. So $f$ is not injective on any neighbourhood of $z_0$, contradicting local bijectivity.
:::
:::

::: {.pf-step}
$f$ is a local bijection on $U$ if and only if $f'(z)\neq0$ for every $z\in U$.

::: pf-proof
Step [](#local){.pf-ref} gives one direction and step [](#converse){.pf-ref} the other, at an arbitrary point $z_0$ of $U$.
:::
:::

:::
:::
