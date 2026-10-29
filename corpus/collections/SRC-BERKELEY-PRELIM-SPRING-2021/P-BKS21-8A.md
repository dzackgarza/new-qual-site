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

::: {.solution}

Set
$$
\zeta\coloneqq e^{2\pi i/7},
\qquad
x\coloneqq \zeta+\zeta^{-1}=2\cos\frac{2\pi}{7}.
$$

::: pf

::: {.pf-step #s1-1}

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

::: {.pf-step #s1-2}

The polynomial
$$
p(t)=t^3+t^2-2t-1
$$
is irreducible over $\ZZ$.


::: pf-proof

The polynomial is primitive. Modulo $2$ it becomes
$$
\overline p(t)=t^3+t^2+1\in\FF_2[t].
$$
A cubic over a field is reducible if and only if it has a root. But
$$
\overline p(0)=1,
\qquad
\overline p(1)=1+1+1=1
$$
in $\FF_2$, so $\overline p$ has no root and is irreducible. Gauss's lemma therefore implies that $p$ is irreducible over $\ZZ$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
[\QQ(x):\QQ]=3.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} shows that $x$ is algebraic and annihilated by $p$. Step [](#s1-2){.pf-ref} shows that $p$ is irreducible of degree $3$, so it is the minimal polynomial of $x$ over $\QQ$.

:::

:::

::: {.pf-step #s1-4}

The number $x$ is not contained in any finite extension $K/\QQ$ whose degree is a power of $2$.


::: pf-proof

Suppose $x\in K$ and
$$
[K:\QQ]=2^m.
$$
Then
$$
\QQ\subseteq\QQ(x)\subseteq K.
$$
By the tower law and step [](#s1-3){.pf-ref},
$$
2^m=[K:\QQ]
=[K:\QQ(x)]\,[\QQ(x):\QQ]
=3[K:\QQ(x)].
$$
Thus $3$ divides $2^m$, which is impossible.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} give the required irreducible polynomial, and step [](#s1-4){.pf-ref} gives the field-degree obstruction.

:::

:::

:::
