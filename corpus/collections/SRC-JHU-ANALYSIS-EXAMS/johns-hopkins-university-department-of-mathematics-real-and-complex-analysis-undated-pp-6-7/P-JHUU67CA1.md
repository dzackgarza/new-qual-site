---
schema: qual/card@1
id: P-JHUU67CA1
kind: problem
title: Entire function with zero coefficient at every center is polynomial
classification:
  areas:
  - complex-analysis
  topics:
  - Identity Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared Problem 4 of the undated JHU exam on pages 6–7; the vanishing coefficient index may depend on the expansion center."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the countable closed cover by derivative zero sets, the exact Baire-category implication, the identity-theorem step, and the zeroth-derivative case."
---

::: {.problem}
Let $f$ be an entire function.
Suppose that for each $z_0 \in \mathbb{C}$, the power series expansion

$$f(z) = \sum_{n=0}^\infty c_n(z - z_0)^n$$

has at least one coefficient $c_n = 0$.
Show that $f$ is a polynomial.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

One fixed derivative of $f$ vanishes identically.

::: pf-proof

For each integer $n\geq0$, set
$$
Z_n=\{z\in\mathbb C:f^{(n)}(z)=0\},
\qquad f^{(0)}=f.
$$
The Taylor coefficient of order $n$ at $z_0$ is
$f^{(n)}(z_0)/n!$ [@SS03]. Thus the hypothesis says
$\mathbb C=\bigcup_{n\geq0}Z_n$. Each $Z_n$ is closed,
since the derivative is continuous.

By the Baire category theorem, the nonempty complete
metric space $\mathbb C$ cannot be a countable union
of closed sets with empty interior [@Fol13]. Hence
some $Z_m$ has nonempty interior. The entire function
$f^{(m)}$ vanishes on this open set. The identity theorem
on the connected plane gives $f^{(m)}\equiv0$ [@SS03].

:::

:::

::: pf-step

The entire Taylor series terminates.

::: pf-proof

If $m=0$, step [](#s1){.pf-ref} already says $f=0$, a polynomial.
If $m\geq1$, every derivative of order $n\geq m$
vanishes identically by differentiating $f^{(m)}=0$.
The Taylor series at zero, which represents the entire
function on all of $\mathbb C$, is therefore
$$
f(z)=\sum_{n=0}^{m-1}\frac{f^{(n)}(0)}{n!}z^n.
$$
This is a polynomial of degree at most $m-1$.

:::

:::

:::

:::
