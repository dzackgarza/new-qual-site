---
schema: qual/card@1
id: E-SS6.PR-3
kind: problem
title: Analytic continuation of $\zeta$ to $\Re(s)>-k$ by periodic antiderivatives of $\{x\}-\frac12$
classification:
  areas:
  - complex-analysis
  topics:
  - Zeta Function
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-09-28
---

::: {.exercise}
3.$^\ast$ If $Q ( x ) = \{ x \} - 1 / 2$ , then we can write the expression in the previous problem as

$$
\zeta (s) = \frac {s}{s - 1} - \frac {1}{2} - s \int_ {1} ^ {\infty} \frac {Q (x)}{x ^ {s + 1}} d x.
$$

Let us construct $Q _ { k } ( x )$ recursively so that

$$
\int_ {0} ^ {1} Q _ {k} (x) d x = 0, \quad \frac {d Q _ {k + 1}}{d x} = Q _ {k} (x), \quad Q _ {0} (x) = Q (x) \quad \text { and } \quad Q _ {k} (x + 1) = Q _ {k} (x).
$$

Then we can write

$$
\zeta (s) = \frac {s}{s - 1} - \frac {1}{2} - s \int_ {1} ^ {\infty} \left(\frac {d ^ {k}}{d x ^ {k}} Q _ {k} (x)\right) x ^ {- s - 1} d x,
$$

and a k-fold integration by parts gives the analytic continuation for $\zeta ( s )$ when $\operatorname { R e } ( s ) > - k$
:::

::: {.solution}
For $j\ge0$ and $\Re s>-j$ put $I_j(s)\da\int_1^\infty Q_j(x)x^{-s-1-j}\,dx$.

::: pf

::: {.pf-step #s1}

Each $Q_j$ is continuous for $j\ge1$, periodic, and bounded.

::: pf-proof

$Q_0$ is bounded and periodic. If $Q_j$ is bounded and periodic with $\int_0^1Q_j=0$, then $Q_{j+1}(x)=Q_{j+1}(0)+\int_0^xQ_j$ is continuous and satisfies $Q_{j+1}(x+1)-Q_{j+1}(x)=\int_x^{x+1}Q_j=0$, so it is periodic, hence bounded; the constant $Q_{j+1}(0)$ is fixed by $\int_0^1Q_{j+1}=0$.

:::

:::

::: {.pf-step #s2}

$I_j$ is holomorphic on $\Re s>-j$.

::: pf-proof

By step [](#s1){.pf-ref}, $\abs{Q_j(x)x^{-s-1-j}}\le Cx^{-\sigma-1-j}$ with $\sigma=\Re s$, which is integrable on $[1,\infty)$ uniformly for $\sigma\ge-j+\eps$. So the integral converges locally uniformly on $\Re s>-j$ and defines a holomorphic function.

:::

:::

::: {.pf-step #s3}

$I_j(s)=-Q_{j+1}(1)+(s+j+1)I_{j+1}(s)$ for $\Re s>-j$.

::: pf-proof

Integrate by parts on $[1,R]$ with $Q_j=Q_{j+1}'$: $\int_1^RQ_jx^{-s-1-j}\,dx=\bigl[Q_{j+1}x^{-s-1-j}\bigr]_1^R+(s+j+1)\int_1^RQ_{j+1}x^{-s-2-j}\,dx$. As $R\to\infty$ the boundary term at $R$ tends to $0$, since $Q_{j+1}$ is bounded and $\Re s>-j-1$.

:::

:::

::: pf-qed

For $\Re s>1$, the formula of the previous problem gives $\zeta(s)=\frac{s}{s-1}-\frac12-sI_0(s)$. Applying step [](#s3){.pf-ref} $k$ times,
$$I_0(s)=P_k(s)+(s+1)(s+2)\cdots(s+k)\,I_k(s),$$
where $P_k$ is a polynomial in $s$ built from the constants $Q_1(1),\ldots,Q_k(1)$. The right side is holomorphic on $\Re s>-k$ by step [](#s2){.pf-ref}, so $\frac{s}{s-1}-\frac12-s\bigl(P_k(s)+(s+1)\cdots(s+k)I_k(s)\bigr)$ is meromorphic on $\Re s>-k$ with only a simple pole at $s=1$, and it agrees with $\zeta$ on $\Re s>1$. This is the analytic continuation of $\zeta$ to $\Re s>-k$.

:::

:::

:::
