---
schema: qual/card@1
id: P-2ZMDH
kind: problem
title: Unique zero of $z-a-qf(z)$, residue formula, and series for $1/F$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Residues
  - Zeros
  - Power Series
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source asks only that the circle K lie in D; Rouché''s theorem and the residue theorem need the closed disc bounded by K in D, so the statement assumes it.'
---

::: {.problem}
Suppose that $f$ is an analytic function in the region $D$ which
contains the point $a$. Let
$$F(z)= z-a-qf(z),\quad \text{where}~ q \ \text{is a complex parameter}.$$

(a) Let $K$ be a circle with the center at point $a$ such that the closed disc $\bar{K}$ whose boundary is $K$ lies in $D$, and also we assume that $f(z)\not =0$ for $z\in K$.
Prove that the function $F$ has one and only one zero $z=w$ on $\bar{K}$ if $\displaystyle{\abs{q}<\min_{z\in K} \frac{\abs{z-a}}{\abs{f(z)}}.}$

(b) Let $G(z)$ be an analytic function on the disk $\bar{K}$. Apply
the residue theorem to prove that
$\displaystyle{ \frac{G(w)}{F'(w)}=\frac{1}{2\pi
i}\int_K \frac{G(z)}{F(z)} dz,}$ where $w$ is the zero from (a).

(c) If $z\in K$, prove that the function
$\displaystyle{\frac{1}{F(z)}}$ can be represented as a convergent
series with respect to $q$: $\displaystyle{
\frac{1}{F(z)}=\sum_{n=0}^{\infty} \frac{(qf(z))^n}{(z-a)^{n+1}}.}$
:::

::: {.solution}

Let $R$ be the radius of $K$.

::: pf

::: {.pf-step #boundary}
$\abs{qf(z)}<\abs{z-a}=R$ for every $z\in K$.

::: pf-proof
This is the hypothesis on $q$ multiplied by $\abs{f(z)}>0$.
:::

:::

::: {.pf-step #unique-zero}
(a) $F$ has exactly one zero $w$ in $\bar K$, it lies in the open disc, and it is simple, so $F'(w)\neq0$.

::: pf-proof
By step [](#boundary){.pf-ref} and Rouché's theorem, $F=(z-a)-qf(z)$ and $z-a$ have the same number of zeros, counted with multiplicity, in the open disc bounded by $K$.
The function $z-a$ has exactly one zero there, and it is simple.
By step [](#boundary){.pf-ref}, $\abs{F(z)}\geq R-\abs{qf(z)}>0$ on $K$, so $F$ has no zero on $K$.
:::

:::

::: pf-step
(b) $\dfrac{G(w)}{F'(w)}=\dfrac1{2\pi i}\displaystyle\int_K\frac{G(z)}{F(z)}\,dz$.

::: pf-proof
By step [](#unique-zero){.pf-ref}, $G/F$ is meromorphic on a neighborhood of $\bar K$ whose only pole in $\bar K$ is at most a simple pole at $w$, with $\Res_{z=w}\frac{G}{F}=\frac{G(w)}{F'(w)}$.
The residue theorem gives the formula.
:::

:::

::: pf-step
(c) For $z\in K$, $\dfrac1{F(z)}=\displaystyle\sum_{n=0}^\infty\frac{(qf(z))^n}{(z-a)^{n+1}}$, and the series converges absolutely.

::: pf-proof
By step [](#boundary){.pf-ref}, $\abs{\frac{qf(z)}{z-a}}<1$, so the geometric series gives
$$
\frac1{F(z)}
=\frac1{z-a}\cdot\frac1{1-\frac{qf(z)}{z-a}}
=\frac1{z-a}\sum_{n=0}^\infty\left(\frac{qf(z)}{z-a}\right)^n.
$$
:::

:::

:::

:::
