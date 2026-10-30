---
schema: qual/card@1
id: P-PRACT20-W5-35
kind: problem
title: Entire functions of linear growth are linear polynomials
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 35).
---

::: {.problem}
Suppose that $f : \CC \to \CC$ is an entire function such that $\abs{f(z)} \leq C\abs{z}$ for all $z$ sufficienty large. Prove that $f(z) = c_1 + c_2 z$ for some constants $c_1, c_2$. [Note: this is a generalization of Liouville’s Theorem. It can actually be generalized further: if $f$ is entire and $\abs{f(z)} \leq C\abs{z}^n$ for sufficiently large $z$, then $f$ is a polynomial of degree $\leq n$.]
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

There is $R_0>0$ such that for every $R\ge R_0$,
$$
\max_{\abs{z}=R}\abs{f(z)}\le CR.
$$


::: pf-proof

The hypothesis says that
$$
\abs{f(z)}\le C\abs{z}
$$
whenever $\abs{z}$ is sufficiently large. Choose $R_0$ beyond that threshold.
On the circle $\abs{z}=R\ge R_0$, the bound is therefore $CR$.

:::

:::

::: {.pf-step #s1-2}

For every integer $n\ge0$ and every $R\ge R_0$,
$$
\abs{f^{(n)}(0)}
\le
n!C R^{1-n}.
$$


::: pf-proof

Cauchy's derivative estimate on the circle $\abs{z}=R$ gives
$$
\abs{f^{(n)}(0)}
\le
\frac{n!}{R^n}
\max_{\abs{z}=R}\abs{f(z)}.
$$
Apply step [](#s1-1){.pf-ref} to obtain
$$
\abs{f^{(n)}(0)}
\le
\frac{n!}{R^n}(CR)
=
n!C R^{1-n}.
$$

:::

:::

::: {.pf-step #s1-3}

For every $n\ge2$,
$$
f^{(n)}(0)=0.
$$


::: pf-proof

Fix $n\ge2$. Step [](#s1-2){.pf-ref} holds for every sufficiently large $R$, and
$$
n!C R^{1-n}\longrightarrow0
\qquad(R\to\infty).
$$
Hence
$$
\abs{f^{(n)}(0)}=0.
$$

:::

:::

::: {.pf-step #s1-4}

The Taylor series of $f$ at $0$ terminates after degree $1$:
$$
f(z)=f(0)+f'(0)z
\qquad(z\in\CC).
$$


::: pf-proof

Because $f$ is entire, its Taylor series at $0$ converges to $f$ on all of
$\CC$:
$$
f(z)
=
\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}z^n.
$$
By step [](#s1-3){.pf-ref}, every coefficient with $n\ge2$ vanishes, leaving only the
constant and linear terms.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{f(z)=c_1+c_2z}
$$
for the constants
$$
c_1=f(0),
\qquad
c_2=f'(0).
$$


::: pf-proof

This is exactly the formula in step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
