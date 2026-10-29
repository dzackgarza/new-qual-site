---
schema: qual/card@1
id: P-2DANW
kind: problem
title: 'Groups of order $240$: Sylow numbers and subgroups of order $15$'
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Semidirect Products
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Corrected the missing n_3=16 Sylow possibility and retained the normalizer argument for the final restriction.
---

::: {.problem}
Let $\abs G=240=2^4\cdot3\cdot5$.

(a) Determine the Sylow-number possibilities for $p=2,3,5$.

(b) Show that a subgroup of order $15$ is cyclic.

(c) If $G$ has no subgroup of order $15$, show that $n_3\in\{10,40\}$.
:::

::: {.solution}
Write $n_p$ for the number of Sylow $p$-subgroups of $G$.

::: pf

::: pf-step

(a) $n_2\in\{1,3,5,15\}$, $n_3\in\{1,4,10,16,40\}$, and $n_5\in\{1,6,16\}$.

::: pf-proof

Sylow's theorems give $n_p\mid\abs G/p^{v_p(\abs G)}$ and $n_p\equiv1\pmod p$:
$$
n_2\mid15,\quad n_2\equiv1\pmod2;\qquad
n_3\mid80,\quad n_3\equiv1\pmod3;\qquad
n_5\mid48,\quad n_5\equiv1\pmod5.
$$
The divisors of $15$ are all odd; the divisors of $80$ congruent to $1$ modulo $3$ are $1,4,10,16,40$; the divisors of $48$ congruent to $1$ modulo $5$ are $1,6,16$.

:::

:::

::: pf-step

(b) Every subgroup $H\le G$ of order $15$ is cyclic.

::: pf-proof

In $H$, the number of Sylow $5$-subgroups divides $3$ and is $1$ modulo $5$, so it is $1$; the number of Sylow $3$-subgroups divides $5$ and is $1$ modulo $3$, so it is $1$. Both Sylow subgroups are therefore normal in $H$, they intersect trivially, and their product has order $15$. Hence
$$
H\cong C_5\times C_3\cong C_{15}.
$$

:::

:::

::: {.pf-step #no-five}

(c) If $G$ has no subgroup of order $15$ and $P$ is a Sylow $3$-subgroup, then $5\nmid\abs{N_G(P)}$.

::: pf-proof

If $5\mid\abs{N_G(P)}$, Cauchy's theorem gives $y\in N_G(P)$ of order $5$. Then $P\trianglelefteq\langle P,y\rangle=P\langle y\rangle$, and this subgroup has order $3\cdot5=15$, a contradiction.

:::

:::

::: pf-step

If $G$ has no subgroup of order $15$, then $n_3\in\{10,40\}$.

::: pf-proof

By step [](#no-five){.pf-ref}, $5$ does not divide $\abs{N_G(P)}=240/n_3$. Since $5\mid240$, this forces $5\mid n_3$. Among $1,4,10,16,40$ this leaves $n_3\in\{10,40\}$.

:::

:::

:::

:::
