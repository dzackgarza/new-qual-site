---
schema: qual/card@1
id: P-TRIV-LA34
kind: problem
title: Expansion of $e^{-\lambda B}Ae^{\lambda B}$ in nested commutators
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 34, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the matrices $A$, $B$ and let $\lambda \ll 1$ be a small parameter. Expand the expression $e^{-\lambda B} A e^{\lambda B}$

(a) to the first order in $\lambda$.

(b) to any order in $\lambda$.
:::

::: {.solution}

Define
$$
F(\lambda)
=
e^{-\lambda B}Ae^{\lambda B}.
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
F'(\lambda)
=
e^{-\lambda B}[A,B]e^{\lambda B}.
$$


::: pf-proof

Differentiate using the product rule:
$$
\begin{aligned}
F'(\lambda)
&=
-Be^{-\lambda B}Ae^{\lambda B}
+
e^{-\lambda B}ABe^{\lambda B}.
\end{aligned}
$$
Since $B$ commutes with $e^{-\lambda B}$,
$$
F'(\lambda)
=
e^{-\lambda B}(-BA+AB)e^{\lambda B}
=
e^{-\lambda B}[A,B]e^{\lambda B}.
$$

:::

:::

::: {.pf-step #s1-2}

At $\lambda=0$,
$$
F(0)=A
$$
and
$$
F'(0)=[A,B].
$$


::: pf-proof

Substitute $\lambda=0$ into the definitions in step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Therefore, to first order,
$$
\boxed{
e^{-\lambda B}Ae^{\lambda B}
=
A+\lambda[A,B]+O(\lambda^2).
}
$$


::: pf-proof

Apply the Taylor expansion of $F$ at $\lambda=0$ using step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Part (a) follows.


::: pf-proof

This is step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Define recursively
$$
C_0=A,
\qquad
C_{n+1}=[C_n,B].
$$
Then
$$
F^{(n)}(\lambda)
=
e^{-\lambda B}C_ne^{\lambda B}
$$
for every $n\geq0$.


::: pf-proof

For $n=0$ this is the definition of $F$. Suppose it holds for $n$. Differentiate:
$$
F^{(n+1)}(\lambda)
=
e^{-\lambda B}[C_n,B]e^{\lambda B}
=
e^{-\lambda B}C_{n+1}e^{\lambda B},
$$
using the same calculation as in step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Hence
$$
F^{(n)}(0)=C_n.
$$


::: pf-proof

Set $\lambda=0$ in step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Therefore the full expansion is
$$
\boxed{
e^{-\lambda B}Ae^{\lambda B}
=
\sum_{n=0}^{\infty}
\frac{\lambda^n}{n!}C_n
}
$$
with
$$
C_n
=
\underbrace{[\cdots[[A,B],B],\ldots,B]}_{n\text{ copies of }B}.
$$


::: pf-proof

Taylor-expand $F$ at $0$ and use step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Equivalently,
$$
\boxed{
e^{-\lambda B}Ae^{\lambda B}
=
A
+
\lambda[A,B]
+
\frac{\lambda^2}{2!}[[A,B],B]
+
\frac{\lambda^3}{3!}[[[A,B],B],B]
+
\cdots.
}
$$


::: pf-proof

Write out the first terms of the series in step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Part (b) follows.


::: pf-proof

Steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref} give the expansion to arbitrary order.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} and [](#s1-9){.pf-ref} establish parts (a) and (b), respectively.

:::

:::

:::
