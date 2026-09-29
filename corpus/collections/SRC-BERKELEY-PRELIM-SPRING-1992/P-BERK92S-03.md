---
schema: qual/card@1
id: P-BERK92S-03
kind: problem
title: Pointwise vanishing of some derivative forces an analytic function to be a polynomial
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
  date: 2026-09-23
---

::: {.problem}
Let $f$ be analytic on a connected open subset $G\subset\mathbb C$. Suppose that for every $z\in G$ there is a positive integer $n$ such that
\[
f^{(n)}(z)=0.
\]
Prove that $f$ is a polynomial.
:::

::: {.solution}
Choose a closed disk $K=\overline{D(z_0,r)}$ contained in $G$. For
each positive integer $m$, set
$$
F_m\coloneqq\{z\in K:f^{(m)}(z)=0\}.
$$

::: pf

::: {.pf-step #s1}

There is a positive integer $N$ such that $f^{(N)}$ vanishes on
a nonempty open subset of $G$.

::: pf-proof

Each $F_m$ is closed in $K$, because $f^{(m)}$ is continuous. The
hypothesis gives
$$
K=\bigcup_{m=1}^{\infty}F_m.
$$
The closed disk $K$ is a complete metric space, so the Baire category
theorem implies that some $F_N$ has nonempty interior relative to
$K$. Any nonempty relatively open subset of a closed disk contains a
nonempty open disk lying in its interior. Hence $f^{(N)}$ vanishes on
a nonempty open subset of $G$.

:::

:::

::: {.pf-step #s2}

$f^{(N)}$ vanishes identically on $G$.

::: pf-proof

The function $f^{(N)}$ is analytic on the connected open set $G$ and,
by step [](#s1){.pf-ref}, vanishes on a nonempty open subset. The identity theorem
therefore gives
$$
f^{(N)}\equiv0
\qquad\text{on }G.
$$

:::

:::

::: {.pf-step #s3}

$f$ is the restriction to $G$ of a polynomial of degree at most
$N-1$.

::: pf-proof

Fix $w\in G$ and define
$$
p(z)\coloneqq
\sum_{k=0}^{N-1}\frac{f^{(k)}(w)}{k!}(z-w)^k.
$$
By step [](#s2){.pf-ref}, the Taylor series of $f$ at $w$ has no terms of degree
$N$ or higher. Thus $f=p$ on a neighborhood of $w$. The analytic
function $f-p$ therefore vanishes on a nonempty open subset of the
connected set $G$, so the identity theorem gives $f=p$ throughout
$G$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves that $f$ is a polynomial.

:::

:::

:::
