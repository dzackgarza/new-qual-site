---
schema: qual/card@1
id: E-AMD-CY7I27YM
kind: problem
title: Algebraic extensions are transitive
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Superseded by P-FHW1-02, which states the same theorem and is the card
    the wiki transcludes on wiki/algebra/fields/extensions.md. Read again
    here: the solution proves the statement by sufficiency of the tower $F\subseteq F_0\subseteq F_0(\alpha)$ and the tower law,
    so the card adds no mathematics the survivor lacks. The card is kept
    for the two dated events above and is listed by no collection; its
    statement and solution are unchanged.
---

::: {.exercise}
Show that if $L/K/F$ with $K/F$ algebraic and $L/K$ algebraic then $L$ is algebraic.
:::

::: {.solution}

The argument is the card's own: pass to the finitely generated field obtained by adjoining the coefficients, and apply the tower law.

Let $F\subseteq K\subseteq L$ with $K/F$ algebraic and $L/K$ algebraic; write $[E:F]$ for the degree of an extension.

::: pf

::: {.pf-step #polynomial}
Every $\alpha\in L$ satisfies a nonzero polynomial over $K$.

::: pf-proof
$\alpha$ is algebraic over $K$, so by definition there is a nonzero $p\in K[x]$ with $p(\alpha)=0$; write $p=a_{0}+a_{1}x+\cdots+a_{n}x^{n}$ with $a_{n}\ne0$ and $n\ge1$, since a nonzero constant polynomial cannot vanish at $\alpha$.
:::

:::

::: {.pf-step #finite}
$F_{0}=F(a_{0},\ldots,a_{n})$ is a finite extension of $F$.

::: pf-proof
Each $a_{i}$ lies in $K$, hence is algebraic over $F$ because $K/F$ is algebraic. Adjoining one algebraic element gives a finite extension, and a finite number of successive finite extensions is finite: $[F(a_{0},\ldots,a_{j+1}):F(a_{0},\ldots,a_{j})]$ is the degree of the minimal polynomial of $a_{j+1}$ over $F(a_{0},\ldots,a_{j})$, which is finite since $a_{j+1}$ is algebraic over $F$ and hence over the larger field. Multiplying these degrees gives $[F_{0}:F]<\infty$, and it is nonzero.
:::

:::

::: {.pf-step #alpha-algebraic}
$\alpha$ is algebraic over $F_{0}$, so $[F_{0}(\alpha):F_{0}]<\infty$.

::: pf-proof
$p$ has all its coefficients in $F_{0}\subseteq F_{0}(\alpha)$, so $p\in F_{0}[x]$ is a nonzero polynomial with $p(\alpha)=0$; hence $\alpha$ is algebraic over $F_{0}$ and $F_{0}(\alpha)/F_{0}$ is finite, of degree the degree of the minimal polynomial of $\alpha$ over $F_{0}$.
:::

:::

::: {.pf-step #conclusion}
Every $\alpha\in L$ is algebraic over $F$, so $L/F$ is algebraic.

::: pf-proof
By the tower law applied to $F\subseteq F_{0}\subseteq F_{0}(\alpha)$,
$$
[F_{0}(\alpha):F]=[F_{0}(\alpha):F_{0}]\,[F_{0}:F]<\infty
$$
by steps [](#finite){.pf-ref} and [](#alpha-algebraic){.pf-ref}. An element lying in a finite extension of $F$ is algebraic over $F$ — it lies in $F(\alpha)$, and $[F(\alpha):F]\le[F_{0}(\alpha):F]<\infty$ — so $\alpha$ is algebraic over $F$. Since $\alpha\in L$ was arbitrary, every element of $L$ is algebraic over $F$, that is $L/F$ is algebraic.
:::

:::

:::
:::
