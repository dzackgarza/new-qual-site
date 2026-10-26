---
schema: qual/card@1
id: P-BKS21-8A
kind: problem
title: The minimal polynomial of $2\cos(2\pi/7)$ and constructibility
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Find an irreducible polynomial over $\ZZ$ having $2\cos(2\pi/7)$ as a root, and use it to show that this number is not contained in any extension of $\QQ$ whose degree is a power of $2$.
:::

Set
$$
\zeta\coloneqq e^{2\pi i/7},
\qquad
x\coloneqq \zeta+\zeta^{-1}=2\cos\frac{2\pi}{7}.
$$

::: pf

::: pf-step

The number $x$ satisfies
$$
\boxed{x^3+x^2-2x-1=0}.
$$


::: pf-proof

Since $\zeta^7=1$ and $\zeta\neq1$,
$$
1+\zeta+\zeta^2+\cdots+\zeta^6=0.
$$
Also
$$
x^2=(\zeta+\zeta^{-1})^2
=\zeta^2+\zeta^{-2}+2,
$$
and
$$
x^3
=(\zeta+\zeta^{-1})^3
=\zeta^3+\zeta^{-3}+3(\zeta+\zeta^{-1}).
$$
Therefore
$$
\begin{aligned}
x^3+x^2-2x-1
&=
\zeta^3+\zeta^{-3}
+\zeta^2+\zeta^{-2}
+\zeta+\zeta^{-1}
+1\\
&=
\zeta^3+\zeta^4+\zeta^2+\zeta^5+\zeta+\zeta^6+1\\
&=0,
\end{aligned}
$$
where $\zeta^{-k}=\zeta^{7-k}$.

:::

:::

::: pf-step

The polynomial
$$
p(t)=t^3+t^2-2t-1
$$
is irreducible over $\mathbb Z$.


::: pf-proof

The polynomial is primitive. Modulo $2$ it becomes
$$
\overline p(t)=t^3+t^2+1\in\mathbb F_2[t].
$$
A cubic over a field is reducible if and only if it has a root. But
$$
\overline p(0)=1,
\qquad
\overline p(1)=1+1+1=1
$$
in $\mathbb F_2$, so $\overline p$ has no root and is irreducible. Gauss's lemma therefore implies that $p$ is irreducible over $\mathbb Z$.

:::

:::

::: pf-step

One has
$$
[\mathbb Q(x):\mathbb Q]=3.
$$


::: pf-proof

Step <1>1 shows that $x$ is algebraic and annihilated by $p$. Step <1>2 shows that $p$ is irreducible of degree $3$, so it is the minimal polynomial of $x$ over $\mathbb Q$.

:::

:::

::: pf-step

The number $x$ is not contained in any finite extension $K/\mathbb Q$ whose degree is a power of $2$.


::: pf-proof

Suppose $x\in K$ and
$$
[K:\mathbb Q]=2^m.
$$
Then
$$
\mathbb Q\subseteq\mathbb Q(x)\subseteq K.
$$
By the tower law and step <1>3,
$$
2^m=[K:\mathbb Q]
=[K:\mathbb Q(x)]\,[\mathbb Q(x):\mathbb Q]
=3[K:\mathbb Q(x)].
$$
Thus $3$ divides $2^m$, which is impossible.

:::

:::

::: pf-qed

Steps <1>1--<1>2 give the required irreducible polynomial, and step <1>4 gives the field-degree obstruction.

:::

:::
