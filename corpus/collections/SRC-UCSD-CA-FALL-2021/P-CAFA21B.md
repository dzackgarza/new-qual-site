---
schema: qual/card@1
id: P-CAFA21B
kind: problem
title: "Polynomial approximation and polynomial hull of a compact set"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-18
  note: Read against the UCSD Complex Analysis Qualifying Exam, Fall 2021; both parts match.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    No retained solution set covers this examination. Structured the card's own argument:
    the two bounded complementary components, the maximum-modulus proof that 1 lies in
    the polynomial hull, the resulting obstruction to polynomial approximation, and the
    identification of the hull with the outer closed disk.
---

::: {.problem}
Let $K = \{ z \in \CC : \abs{z} \leq 3,\, \abs{z-1} \geq 1,\, \abs{z+1} \geq 1 \}$.

(i) True/false: every holomorphic function in a neighborhood of $K$ is the local uniform limit on $K$ of a sequence of polynomials.
Please justify your answer.

(ii) Determine, with justification, the set
$$
\widehat{K} = \{ z \in \CC : \abs{p(z)} \leq \sup_{w \in K} \abs{p(w)} \text{ for all polynomials } p \}.
$$
:::

::: {.solution}

No retained solution set covers this examination; the argument below is the card's own.

::: pf

::: {.pf-step #complement}
The complement of $K$ has exactly three components: the unbounded component, the open disk $D_1=\{\abs{z-1}<1\}$, and the open disk $D_{-1}=\{\abs{z+1}<1\}$.

::: pf-proof
$K$ is the closed disk $\abs z\le3$ with the two open unit disks removed. Each removed disk is connected and is a component of the complement; outside the closed disk $\abs z\le3$ the complement is connected and reaches infinity.
:::
:::

::: {.pf-step #point-in-hull}
The point $1$ belongs to the polynomial hull of $K$.

::: pf-proof
The boundary circle $\abs{z-1}=1$ lies in $K$: it is inside $\abs z\le3$, and on it $\abs{z+1}=\abs{2+(z-1)}\ge2-1=1$. For any polynomial $q$, the maximum modulus principle applied on the disk $D_1$ gives
$$
\abs{q(1)}\le\max_{\abs{z-1}=1}\abs{q(z)}\le\sup_{w\in K}\abs{q(w)}.
$$
This is exactly the defining inequality for $1$ to lie in $\widehat K$.
:::
:::

::: {.pf-step #not-approximable}
The function $f(z)=1/(z-1)$ cannot be uniformly approximated on $K$ by polynomials.

::: pf-proof
If polynomials $p_n$ converged uniformly to $f$ on $K$, then $q_n(z)=(z-1)p_n(z)-1$ would converge uniformly to $0$ on $K$. Step [](#point-in-hull){.pf-ref} gives $\abs{q_n(1)}\le\sup_K\abs{q_n}$, whose right side tends to $0$, but $q_n(1)=-1$ for every $n$. This contradiction proves that (i) is false.
:::
:::

::: {.pf-step #hull}
$\widehat K=\{z:\abs z\le3\}$.

::: pf-proof
Every point of either bounded complementary component lies in the hull by the maximum-modulus argument of step [](#point-in-hull){.pf-ref}. Thus the closed disk $\abs z\le3$ is contained in the hull. Conversely, if $\abs{z_0}>3$, the polynomial $p(z)=z$ gives $\abs{p(z_0)}>3=\sup_K\abs z$, so $z_0$ is not in the hull. Hence the hull is exactly the closed disk of radius $3$, proving (ii).
:::
:::

:::
:::
