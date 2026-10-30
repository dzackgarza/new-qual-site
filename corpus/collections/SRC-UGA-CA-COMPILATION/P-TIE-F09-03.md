---
schema: qual/card@1
id: P-TIE-F09-03
kind: problem
title: Lagrange inversion for $z-a-qf(z)=0$ via the residue theorem
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2009, question 3.
---

::: {.problem}
Suppose that $f$ is an analytic function in the region $D$ which contains the point $a$. Let $F(z) = z - a - qf(z)$, where $q$ is a complex parameter.

(1) Let $K \subset D$ be a circle with the center at point $a$ and also we assume that $f(z) \neq 0$ for $z \in K$. Prove that the function $F$ has one and only one zero $z = w$ on the closed disc $K$ whose boundary is the circle $K$ if
$$
\abs{q} < \min_{z \in K} \frac{\abs{z - a}}{\abs{f(z)}}.
$$

(2) Let $G(z)$ be an analytic function on the disk $K$. Apply the residue theorem to prove that
$$
\frac{G(w)}{F'(w)} = \frac{1}{2\pi i}\int_{K} \frac{G(z)}{F(z)} \, dz,
$$
where $w$ is the zero from (1).

(3) If $z \in K$, prove that the function $\dfrac{1}{F(z)}$ can be represented as a convergent series with respect to $q$:
$$
\frac{1}{F(z)} = \sum_{n=0}^{\infty} \frac{(qf(z))^{n}}{(z - a)^{n+1}}.
$$
:::

::: {.solution}

Let $C$ denote the circle called $K$ in the problem, let its radius be $\rho$, and let
$\overline\Delta$ be the closed disk bounded by $C$.

::: pf

::: {.pf-step #s1-1}

On $C$,
$$
\abs{qf(z)}<\abs{z-a}.
$$


::: pf-proof

The hypothesis is
$$
\abs{q}
<
\min_{z\in C}
\frac{\abs{z-a}}{\abs{f(z)}}.
$$
Since $f(z)\ne0$ on $C$, multiplying by $\abs{f(z)}$ gives the asserted strict inequality for every
$z\in C$.

:::

:::

::: {.pf-step #s1-2}

The function
$$
F(z)=z-a-qf(z)
$$
has exactly one zero in $\Delta$, counted with multiplicity.


::: pf-proof

On $C$, step [](#s1-1){.pf-ref} gives
$$
\abs{F(z)-(z-a)}
=
\abs{qf(z)}
<
\abs{z-a}.
$$
By Rouché's theorem, $F$ and $z-a$ have the same number of zeros in $\Delta$, counted with
multiplicity. The function $z-a$ has exactly one zero there, namely $a$, with multiplicity one.
Therefore $F$ has exactly one zero in $\Delta$, counted with multiplicity.

:::

:::

::: {.pf-step #s1-3}

The unique zero $w$ of $F$ in $\overline\Delta$ lies in $\Delta$ and is simple.


::: pf-proof

Step [](#s1-1){.pf-ref} implies
$$
\abs{F(z)}
\ge
\abs{z-a}-\abs{qf(z)}
>0
$$
on $C$, so $F$ has no zero on the boundary. By step [](#s1-2){.pf-ref} there is exactly one zero in the
interior, counted with multiplicity one. Hence that zero $w$ is simple, so
$$
F'(w)\ne0.
$$

:::

:::

::: {.pf-step #s1-4}

If $G$ is analytic on a neighborhood of $\overline\Delta$, then
$$
\boxed{
\frac{G(w)}{F'(w)}
=
\frac1{2\pi i}\int_C\frac{G(z)}{F(z)}\,dz
}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, the meromorphic function
$$
\frac{G(z)}{F(z)}
$$
has exactly one pole in $\Delta$, at the simple zero $w$ of $F$. Its residue is
$$
\operatorname{Res}_{z=w}\frac{G(z)}{F(z)}
=
\frac{G(w)}{F'(w)}.
$$
The residue theorem therefore gives
$$
\frac1{2\pi i}\int_C\frac{G(z)}{F(z)}\,dz
=
\frac{G(w)}{F'(w)}.
$$

:::

:::

::: {.pf-step #s1-5}

There exists a constant $\lambda<1$ such that
$$
\abs{
\frac{qf(z)}{z-a}
}
\le\lambda
$$
for every $z\in C$.


::: pf-proof

The function
$$
z\longmapsto
\abs{\frac{qf(z)}{z-a}}
$$
is continuous on the compact circle $C$. By step [](#s1-1){.pf-ref} it is strictly less than $1$ at every
point. Its maximum $\lambda$ is therefore strictly less than $1$.

:::

:::

::: {.pf-step #s1-6}

For every $z\in C$,
$$
\boxed{
\frac1{F(z)}
=
\sum_{n=0}^{\infty}
\frac{(qf(z))^n}{(z-a)^{n+1}}
},
$$
and the series converges uniformly on $C$.


::: pf-proof

Since
$$
F(z)
=(z-a)
\left(
1-\frac{qf(z)}{z-a}
\right),
$$
one has
$$
\frac1{F(z)}
=
\frac1{z-a}
\frac1{1-\frac{qf(z)}{z-a}}.
$$
By step [](#s1-5){.pf-ref}, the ratio in the geometric series has absolute value at most $\lambda<1$
uniformly on $C$. Hence
$$
\frac1{1-\frac{qf(z)}{z-a}}
=
\sum_{n=0}^{\infty}
\left(
\frac{qf(z)}{z-a}
\right)^n
$$
uniformly on $C$. Multiplying by $1/(z-a)$ gives the displayed expansion.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} prove part (1), step [](#s1-4){.pf-ref} proves part (2), and steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref} prove
part (3).

:::

:::

:::
