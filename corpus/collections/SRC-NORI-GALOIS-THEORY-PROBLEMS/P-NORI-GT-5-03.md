---
schema: qual/card@1
id: P-NORI-GT-5-03
kind: problem
title: Base change of separable, normal, and Galois extensions
classification:
  areas: [algebra]
  topics:
  - Base Change
  - Separable Extensions
  - Normal Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 5.3 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
Given $F \subset E \subset E'$ and $F \subset K \subset E'$, where $F, E, K$ are subfields of $E'$. *It is not assumed that $E$ is an algebraic extension of $F$.* Prove that

(a) If $K$ is a finite separable extension of $F$, then $EK$ is a finite separable extension of $E$.

(b) If $K$ is a finite normal extension of $F$, then $EK$ is a finite normal extension of $E$.

(c) If $K$ is a finite Galois extension of $F$, then $EK$ is a finite Galois extension of $E$.
:::

::: {.solution}

All composita are taken inside the given ambient field $E'$.

::: pf

::: {.pf-step #s1-1}

If $K/F$ is finite, then $EK/E$ is finite and
$$
[EK:E]\le [K:F].
$$


::: pf-proof

Choose an $F$-basis
$$
k_1,\ldots,k_n
$$
of $K$, and let
$$
V=Ek_1+\cdots+Ek_n\subseteq E'.
$$
The space $V$ contains $E$ and $K$. It is closed under multiplication because each product $k_i k_j\in K$ is an $F$-linear combination of the basis elements $k_1,\ldots,k_n$. Hence $V$ is a finite-dimensional $E$-subalgebra of the field $E'$.

If $0\ne v\in V$, multiplication by $v$ is an injective $E$-linear endomorphism of the finite-dimensional vector space $V$, hence is surjective. Thus there is $w\in V$ with $vw=1$, so every nonzero element of $V$ is invertible in $V$. Therefore $V$ is a field containing both $E$ and $K$, and consequently
$$
V=EK.
$$
Since $V$ is spanned over $E$ by $n$ elements,
$$
[EK:E]\le n=[K:F].
$$

:::

:::

::: {.pf-step #s1-2}

Suppose $K/F$ is finite separable. Then there exists $\alpha\in K$ with
$$
K=F(\alpha).
$$


::: pf-proof

This is the primitive element theorem for finite separable extensions.

:::

:::

::: {.pf-step #s1-3}

Under the hypothesis of step [](#s1-2){.pf-ref},
$$
EK=E(\alpha).
$$


::: pf-proof

Since $K=F(\alpha)$ and $F\subset E$,
$$
EK=E F(\alpha)=E(\alpha).
$$

:::

:::

::: {.pf-step #s1-4}

The minimal polynomial of $\alpha$ over $E$ is separable.


::: pf-proof

Let
$$
f\in F[X]
$$
be the minimal polynomial of $\alpha$ over $F$. Since $K/F$ is separable, $f$ has no repeated root in an algebraic closure.

Let
$$
g\in E[X]
$$
be the minimal polynomial of $\alpha$ over $E$. Since $f(\alpha)=0$, the polynomial $g$ divides $f$ in $E[X]$. Every divisor of a separable polynomial is separable, so $g$ is separable.

:::

:::

::: {.pf-step #s1-5}

Therefore if $K/F$ is finite separable, then
$$
\boxed{EK/E\text{ is finite separable}}.
$$


::: pf-proof

Finiteness is step [](#s1-1){.pf-ref}. By step [](#s1-3){.pf-ref}, $EK=E(\alpha)$, and step [](#s1-4){.pf-ref} shows that the minimal polynomial of the generator $\alpha$ over $E$ is separable.

:::

:::

::: {.pf-step #s1-6}

Suppose $K/F$ is finite normal. Choose elements
$$
\alpha_1,\ldots,\alpha_r\in K
$$
such that
$$
K=F(\alpha_1,\ldots,\alpha_r),
$$
and let $f_i\in F[X]$ be the minimal polynomial of $\alpha_i$ over $F$.
Then every $f_i$ splits completely over $K$.


::: pf-proof

The extension is finite, so it is finitely generated. Normality means that every irreducible polynomial over $F$ having a root in $K$ splits completely over $K$. Each $f_i$ is irreducible over $F$ and has root $\alpha_i\in K$.

:::

:::

::: {.pf-step #s1-7}

The field $EK$ is the splitting field over $E$ of the finite family
$$
f_1,\ldots,f_r.
$$


::: pf-proof

By step [](#s1-6){.pf-ref}, every root of every $f_i$ lies in $K$, hence in $EK$. Thus all the polynomials split over $EK$.

Conversely, any field containing $E$ in which all $f_i$ split contains in particular the chosen roots $\alpha_i$. Hence it contains
$$
E(\alpha_1,\ldots,\alpha_r)=EK.
$$
Therefore $EK$ is the smallest extension of $E$ splitting all the $f_i$.

:::

:::

::: {.pf-step #s1-8}

Therefore if $K/F$ is finite normal, then
$$
\boxed{EK/E\text{ is finite normal}}.
$$


::: pf-proof

Finiteness is step [](#s1-1){.pf-ref}. By step [](#s1-7){.pf-ref}, $EK$ is a splitting field over $E$ of a finite family of polynomials. Hence $EK/E$ is normal.

:::

:::

::: {.pf-step #s1-9}

If $K/F$ is finite Galois, then
$$
\boxed{EK/E\text{ is finite Galois}}.
$$


::: pf-proof

A finite Galois extension is both separable and normal. Apply step [](#s1-5){.pf-ref} to obtain separability of $EK/E$ and step [](#s1-8){.pf-ref} to obtain normality. A finite extension that is both separable and normal is Galois.

:::

:::

::: pf-qed

Steps [](#s1-5){.pf-ref} and [](#s1-8){.pf-ref}, and [](#s1-9){.pf-ref} prove parts (a), (b), and (c), respectively.

:::

:::

:::
