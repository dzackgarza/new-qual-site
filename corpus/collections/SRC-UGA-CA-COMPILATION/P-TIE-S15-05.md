---
schema: qual/card@1
id: P-TIE-S15-05
kind: problem
title: $z^{-m}$ is not a uniform limit of polynomials on an annulus
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 5.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source asks to show M_R > 1 for every polynomial p, which fails for p = 0 (M_R = 1), and writes the annulus with r < R only. Part (1) now assumes p is nonzero, and part (2) assumes 0 < r < R.
---

::: {.problem}
(1) Let $p(z)$ be a nonzero polynomial, $R > 0$ any positive number, and $m \geq 1$ an integer.
Let $M_{R} = \sup\{ |z^{m} p(z) - 1| : |z| = R \}$. Show that $M_{R} > 1$.

(2) Let $m \geq 1$ be an integer and $K = \{ z \in \CC : r \leq |z| \leq R \}$ where $0 < r < R$. Show (i) using (1) as well as, (ii) without using (1) that there exists a positive number $\varepsilon_{0} > 0$ such that for each polynomial $p(z)$,

$$
\sup\{ |p(z) - z^{-m}| : z \in K \} \geq \varepsilon_{0}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every polynomial $p$,
$$
M_R\ge1.
$$
If $p\ne0$, then in fact
$$
M_R>1.
$$


::: pf-proof

Define
$$
q(z)\coloneqq z^mp(z)-1.
$$
Then $q$ is entire and
$$
q(0)=-1.
$$
By the maximum modulus principle on the disk $\abs{z}\le R$,
$$
1
=
\abs{q(0)}
\le
\max_{\abs{z}=R}\abs{q(z)}
=
M_R.
$$
Thus $M_R\ge1$.

Suppose now that $p\ne0$ and $M_R=1$. Then $\abs{q}$ attains its maximum value $1$ at the interior point $0$. The strong maximum modulus principle forces $q$ to be constant. Since $q(0)=-1$,
$$
q\equiv-1,
$$
so
$$
z^mp(z)\equiv0.
$$
Hence $p\equiv0$, a contradiction. Therefore $M_R>1$ when $p\ne0$.

:::

:::

::: {.pf-step #s1-2}

Using step [](#s1-1){.pf-ref}, every polynomial $p$ satisfies
$$
\sup_{z\in K}\abs{p(z)-z^{-m}}
\ge
R^{-m}.
$$


::: pf-proof

The outer circle $\abs{z}=R$ is contained in $K$. On that circle,
$$
\abs{p(z)-z^{-m}}
=
R^{-m}\abs{z^mp(z)-1}.
$$
Therefore
$$
\begin{aligned}
\sup_{z\in K}\abs{p(z)-z^{-m}}
&\ge
\sup_{\abs{z}=R}\abs{p(z)-z^{-m}}\\
&=
R^{-m}M_R\\
&\ge
R^{-m}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

Without using step [](#s1-1){.pf-ref}, every polynomial $p$ still satisfies
$$
\sup_{z\in K}\abs{p(z)-z^{-m}}
\ge
R^{-m}.
$$


::: pf-proof

Let $C_R$ be the positively oriented circle $\abs{z}=R$. Since $m\ge1$,
$$
p(z)z^{m-1}
$$
is a polynomial, so direct parametrization of $C_R$ gives
$$
\int_{C_R}p(z)z^{m-1}\,dz=0.
$$
Also,
$$
\int_{C_R}z^{-1}\,dz=2\pi i.
$$
Hence
$$
\begin{aligned}
2\pi
&=
\abs{
\int_{C_R}
\left(z^{-m}-p(z)\right)z^{m-1}\,dz
}\\
&\le
2\pi R\,
R^{m-1}
\sup_{\abs{z}=R}
\abs{p(z)-z^{-m}}.
\end{aligned}
$$
Dividing by $2\pi R^m$ gives
$$
\sup_{\abs{z}=R}
\abs{p(z)-z^{-m}}
\ge
R^{-m}.
$$
Since $C_R\subset K$, the same lower bound holds for the supremum over $K$.

:::

:::

::: {.pf-step #s1-4}

Thus one may take
$$
\boxed{\varepsilon_0=R^{-m}>0}
$$
in part (2).


::: pf-proof

Steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} each prove
$$
\sup_{z\in K}\abs{p(z)-z^{-m}}
\ge
R^{-m}
$$
for every polynomial $p$, respectively with and without using part (1).

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves part (1). Step [](#s1-4){.pf-ref} proves part (2) by both requested methods.

:::

:::

:::
