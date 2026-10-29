---
schema: qual/card@1
id: P-APA22F
kind: problem
title: Inner products of skew Schur functions and the number of SYT of shape $(5,3,2,2,1)$
classification:
  areas:
  - applied-algebra
  topics:
  - Symmetric Functions
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
(a) Let $s$ denote the Schur symmetric functions, and let $\langle -, - \rangle$ denote the usual scalar product on the ring of symmetric functions.
Compute
$$
\left\langle s_{(4,4,2,2)/(2,1)},\ s_{(4,3,2,2)/(1,1)} \right\rangle.
$$

(b) What is the number of standard Young tableaux of shape $(5, 3, 2, 2, 1)$?
:::

::: {.solution}
For a skew shape $\lambda/\mu$, the Littlewood--Richardson rule gives $s_{\lambda/\mu}=\sum_\nu c^\lambda_{\mu\nu}s_\nu$, where $c^\lambda_{\mu\nu}$ is the number of semistandard fillings of $\lambda/\nu$ with content $\mu$ whose reverse reading word (rows top to bottom, each row right to left) is a lattice word.

::: pf

::: pf-step
(a) $\left\langle s_{(4,4,2,2)/(2,1)},\ s_{(4,3,2,2)/(1,1)}\right\rangle=\boxed{4}$.

::: pf-proof

::: {.pf-step #vertical-strip}
$s_{(4,3,2,2)/(1,1)}=s_{(3,2,2,2)}+s_{(3,3,2,1)}+s_{(4,2,2,1)}+s_{(4,3,1,1)}$.

::: pf-proof
For $\mu=(1,1)$, a lattice filling with content $(1,1)$ puts $1$ above $2$, so $c^\lambda_{(1,1)\nu}=1$ exactly when $\lambda/\nu$ is a vertical strip of two boxes, and $0$ otherwise. The vertical $2$-strips of $(4,3,2,2)$ remove one corner box from two different rows and leave a partition: rows $1,2$ give $(3,2,2,2)$, rows $1,4$ give $(3,3,2,1)$, rows $2,4$ give $(4,2,2,1)$, and rows $3,4$ give $(4,3,1,1)$. Rows $1,3$ and $2,3$ leave a row $3$ shorter than row $4$.
:::

:::

::: {.pf-step #lr-coefficients}
$c^{(4,4,2,2)}_{(2,1)\nu}=1$ for each of the four $\nu$ of step [](#vertical-strip){.pf-ref}.

::: pf-proof
For each $\nu$ the skew shape $(4,4,2,2)/\nu$ has three boxes, and there is exactly one lattice filling with content $(2,1)$. For $\nu=(3,2,2,2)$ the boxes are $(1,4),(2,3),(2,4)$: column $4$ must read $1,2$ and then $(2,3)=1$, with reading word $1,2,1$. For $\nu=(3,3,2,1)$ the boxes are $(1,4),(2,4),(4,2)$: column $4$ reads $1,2$ and $(4,2)=1$. For $\nu=(4,2,2,1)$ the boxes are $(2,3),(2,4),(4,2)$: the row-$2$ filling $1,2$ has reading word starting with $2$, so row $2$ is $1,1$ and $(4,2)=2$. For $\nu=(4,3,1,1)$ the boxes are $(2,4),(3,2),(4,2)$: column $2$ reads $1,2$ and $(2,4)=1$.
:::

:::

::: pf-qed
The Schur functions are orthonormal, so the inner product is $\sum_\nu c^{(4,4,2,2)}_{(2,1)\nu}\,c^{(4,3,2,2)}_{(1,1)\nu}$, and only the four $\nu$ of step [](#vertical-strip){.pf-ref} contribute, each with product $1\cdot1$ by step [](#lr-coefficients){.pf-ref}. The full expansion $s_{(4,4,2,2)/(2,1)}=s_{(3,2,2,2)}+s_{(3,3,2,1)}+s_{(4,2,2,1)}+s_{(4,3,1,1)}+s_{(4,3,2)}+s_{(4,4,1)}$ (checked in Sage) has two further terms, which do not occur in step [](#vertical-strip){.pf-ref}.
:::

:::

:::

::: pf-step
(b) The number of standard Young tableaux of shape $(5,3,2,2,1)$ is $\boxed{21450}$.

::: pf-proof
By the hook length formula, $f^\lambda=n!/\prod_{c\in\lambda}h(c)$. For $\lambda=(5,3,2,2,1)$, $n=13$ and the hook lengths are $9,7,4,2,1$ in row $1$, $6,4,1$ in row $2$, $4,2$ in row $3$, $3,1$ in row $4$ and $1$ in row $5$, whose product is $504\cdot24\cdot8\cdot3=290304$. Hence $f^\lambda=13!/290304=6227020800/290304=21450$.
:::

:::

:::
:::
