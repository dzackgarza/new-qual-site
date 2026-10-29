---
schema: qual/card@1
id: P-2LX4F
kind: problem
title: Galois group of $x^6+x^3+1$ over $\FF_2$ and its intermediate fields
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Galois Theory
  - Splitting Fields
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $F$ be the field with 2 elements and $K$ a splitting field of $f(x) = x^6 + x^3 + 1$ over $F$.
You may assume that $f$ is irreducible over $F$.

a. Show that if $r$ is a root of $f$ in $K$, then $r^9 = 1$ but $r^3\neq 1$.

b. Find $\gal(K/F)$ and express each intermediate field between $F$ and $K$ as $F(\beta)$ for an appropriate $\beta \in K$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every root $r$ of $f$ satisfies $r^9=1$ and $r^3\neq1$.


::: pf-proof

The equation $r^6+r^3+1=0$ gives $(r^3-1)(r^6+r^3+1)=r^9-1=0$. But $r^3=1$ would imply $r^6+r^3+1=1$ in characteristic two, a contradiction. Since $r^9=1$ and $r^3\neq1$, the multiplicative order of $r$ is nine.

:::

:::

::: {.pf-step #s1-2}

The splitting field and Galois group are
$$
\boxed{K=F(r)\cong\FF_{64},\qquad
\operatorname{Gal}(K/F)=\langle\sigma\rangle\cong C_6,\quad\sigma(z)=z^2}.
$$


::: pf-proof

The assumed irreducibility of the degree-six polynomial gives $[F(r):F]=6$, hence $|F(r)|=64$. Finite fields are Galois over their prime fields and the Frobenius automorphism $\sigma(z)=z^2$ generates the Galois group of order six. In particular, the Frobenius conjugates of $r$ belong to $F(r)$, so this field contains all roots of $f$ and is its splitting field.

:::

:::

::: {.pf-step #s1-3}

All intermediate fields are
$$
\boxed{F,\quad F(r^3)\cong\FF_4,\quad
F(r+r^8)\cong\FF_8,\quad F(r)=K}.
$$


::: pf-proof

The cyclic group $C_6$ has exactly one subgroup of each order $1,2,3,6$, so the intermediate fields are the unique subfields of cardinalities $2,4,8,64$. By step [](#s1-1){.pf-ref}, $r^3$ has order three and satisfies the irreducible polynomial $x^2+x+1$, hence generates $\FF_4$.

Put $\beta=r+r^8$. Because $r^9=1$, one has $r^{64}=r$, and thus $\beta^8=r^8+r^{64}=\beta$. Hence $\beta$ belongs to $\FF_8$. It does not belong to $F$: if $\beta=0$ then $r^7=1$; if $\beta=1$, then multiplying $r+r^{-1}=1$ by $r$ gives $r^2+r+1=0$, implying $r^3=1$. Both contradict step [](#s1-1){.pf-ref}. Since $[F_8:F]=3$, the nontrivial extension $F(\beta)$ equals $\FF_8$. Finally $F(r)=K$ by step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves part (a); steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} prove part (b).

:::

:::

:::
