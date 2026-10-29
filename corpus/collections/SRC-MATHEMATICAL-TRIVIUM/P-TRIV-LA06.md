---
schema: qual/card@1
id: P-TRIV-LA06
kind: problem
title: $\log\det A=\operatorname{Tr}\log A$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 6, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Let A be a non-degenerate matrix.
Show that log det $A = \operatorname { T r } \log A$
:::

::: {.remark}
The source suppresses the branch choice for both logarithms. For an arbitrary
matrix logarithm $L$ with $e^L=A$, the unconditional statement is
$$
e^{\operatorname{Tr}L}=\det A,
$$
equivalently
$$
\operatorname{Tr}L\equiv \log(\det A)\pmod{2\pi i\ZZ}.
$$
The displayed equality in the problem holds when the scalar logarithm of
$\det A$ is chosen compatibly with the matrix logarithm.
:::

::: {.solution}

Let $L$ be a matrix logarithm of $A$, so
$$
e^L=A.
$$

::: pf

::: {.pf-step #s1-1}

For every square complex matrix $X$,
$$
\det(e^X)=e^{\operatorname{Tr}X}.
$$


::: pf-proof

Triangularize $X$ over $\CC$: there exists an invertible $P$ such that
$$
T=P^{-1}XP
$$
is upper triangular. Then
$$
e^T=P^{-1}e^X P
$$
is upper triangular with diagonal entries
$$
e^{t_{11}},\ldots,e^{t_{nn}}.
$$
Therefore
$$
\det(e^X)
=
\det(e^T)
=
\prod_{j=1}^n e^{t_{jj}}
=
e^{\sum_j t_{jj}}
=
e^{\operatorname{Tr}T}
=
e^{\operatorname{Tr}X}.
$$

:::

:::

::: {.pf-step #s1-2}

Applying step [](#s1-1){.pf-ref} to $L$ gives
$$
\boxed{e^{\operatorname{Tr}L}=\det A}.
$$


::: pf-proof

Since $e^L=A$,
$$
\det A
=
\det(e^L)
=
e^{\operatorname{Tr}L}.
$$

:::

:::

::: {.pf-step #s1-3}

Thus $\operatorname{Tr}L$ is a scalar logarithm of $\det A$.


::: pf-proof

By definition, a scalar $w$ is a logarithm of $\det A$ exactly when
$$
e^w=\det A.
$$
Step [](#s1-2){.pf-ref} gives this with
$$
w=\operatorname{Tr}L.
$$

:::

:::

::: {.pf-step #s1-4}

If a scalar branch $\log(\det A)$ is fixed independently, then
$$
\boxed{
\operatorname{Tr}(\log A)
=
\log(\det A)+2\pi i k
}
$$
for some $k\in\ZZ$.


::: pf-proof

Any two scalar logarithms of the same nonzero complex number differ by an
integer multiple of $2\pi i$. Apply this to the logarithm from step [](#s1-3){.pf-ref} and
the chosen scalar logarithm.

:::

:::

::: {.pf-step #s1-5}

With compatible branches,
$$
\boxed{\log\det A=\operatorname{Tr}\log A}.
$$


::: pf-proof

Choose the scalar logarithm of $\det A$ to be the logarithm supplied by
step [](#s1-3){.pf-ref}. Then the integer $k$ in step [](#s1-4){.pf-ref} is zero.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} through [](#s1-5){.pf-ref} give the precise branch-independent identity and the source's
formula under compatible choices.

:::

:::

:::
