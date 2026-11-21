---
schema: qual/card@1
id: P-CAF06G
kind: problem
title: "Interpolation by entire functions at prescribed points"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that the node set is closed and discrete
    because the a_n are distinct and tend to infinity, so the Weierstrass product gives an
    entire g with simple zeros exactly there and g'(a_n) nonzero, that Mittag-Leffler gives
    a meromorphic H with the principal parts A_n/(g'(a_n)(z-a_n)) and no other poles, that g
    H is holomorphic off the nodes, and the local expansion showing f(z) - A_n = O(z - a_n)
    so the singularities are removable with the prescribed values. The argument is the
    card's own; no retained set is cited. No repair needed.
---

::: {.problem}
Suppose that the $a_n$ are pairwise distinct, $a_n \to \infty$, and $A_n$ are arbitrary complex numbers.
Show that there exists an entire function $f(z)$ which satisfies $f(a_n) = A_n$.
:::

::: {.remark}
The Fall 2006 source does not state that the interpolation nodes are distinct.
That hypothesis is necessary for arbitrary prescribed values: repeated nodes
with different $A_n$ would make the interpolation conditions inconsistent.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on it. It uses the two classical existence theorems of the chapter, the Weierstrass product theorem and the Mittag--Leffler theorem; the nodes are pairwise distinct and tend to $\infty$.

::: pf

::: {.pf-step #zero-function}
There is an entire $g$ whose zeros are exactly the $a_{n}$, each simple; in particular $g'(a_{n})\ne0$ for every $n$.

::: pf-proof
The set $\{a_{n}\}$ has no finite accumulation point, since $a_{n}\to\infty$ and the $a_{n}$ are distinct, so it is a closed discrete subset of $\CC$. The Weierstrass product theorem for such a set gives an entire function vanishing exactly on it, and the product can be built so that every zero is of order one: the standard construction assigns to each $a_{n}$ a factor $(1-z/a_{n})$ when $a_{n}\ne0$ and the factor $z$ when $a_{n}=0$, with convergence factors chosen to make the product converge locally uniformly. At a simple zero $g'(a_{n})\ne0$ by the factorisation $g(z)=(z-a_{n})h(z)$ with $h$ holomorphic and $h(a_{n})\ne0$.
:::

:::

::: {.pf-step #meromorphic}
There is a meromorphic $H$ on $\CC$ whose only poles are the $a_{n}$ and whose principal part at $a_{n}$ is $\dfrac{A_{n}}{g'(a_{n})(z-a_{n})}$.

::: pf-proof
This is the Mittag--Leffler theorem applied to the closed discrete set $\{a_{n}\}$ with the prescribed principal parts $A_{n}/(g'(a_{n})(z-a_{n}))$, each a pole of order one: the theorem produces a meromorphic function with exactly those poles and principal parts and no others.
:::

:::

::: {.pf-step #holomorphic-off}
$f=gH$ is holomorphic on $\CC-\{a_{n}\}$.

::: pf-proof
On $\CC-\{a_{n}\}$ the function $g$ is holomorphic (it is entire) and $H$ is holomorphic, having no poles there by step [](#meromorphic){.pf-ref}; a product of holomorphic functions is holomorphic.
:::

:::

::: {.pf-step #node}
At each $a_{n}$ the function $f$ has a removable singularity, with limiting value $A_{n}$.

::: pf-proof
Expand at $a_{n}$: since the zero is simple,
$$
g(z)=(z-a_{n})g'(a_{n})+O\big((z-a_{n})^{2}\big),
$$
and by step [](#meromorphic){.pf-ref},
$$
H(z)=\frac{A_{n}}{g'(a_{n})(z-a_{n})}+h(z)
$$
with $h$ holomorphic near $a_{n}$. Multiplying,
$$
f(z)=g(z)H(z)=A_{n}+\big(A_{n}\,\tfrac{g(z)}{g'(a_{n})(z-a_{n})}-A_{n}\big)+g(z)h(z),
$$
and the bracket is $O(z-a_{n})$ while $g(z)h(z)=O(z-a_{n})$; so $f(z)-A_{n}=O(z-a_{n})$, the singularity is removable, and the extended value at $a_{n}$ is $A_{n}$.
:::

:::

::: {.pf-step}
There is an entire $f$ with $f(a_{n})=A_{n}$ for all $n$.

::: pf-proof
Define $f$ by the product away from the nodes and by $f(a_{n})=A_{n}$ at the nodes. By steps [](#holomorphic-off){.pf-ref} and [](#node){.pf-ref} this is holomorphic off the nodes and has a removable singularity at each of them, so the extension is entire; and by construction it takes the prescribed values.
:::

:::

:::
:::
