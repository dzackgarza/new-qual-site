---
schema: qual/card@1
id: P-BKS05-3B
kind: problem
title: Generalized inverses of square matrices over a field
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against fresh deterministic MinerU Flash extractions of the UC Berkeley Spring 2005 exam and its companion solution packet; unambiguous duplicated-statement extraction defects were normalized.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently checked the retained splitting argument: invert A on a
    complement of its kernel onto its image, extend that inverse linearly,
    and obtain AXA=A.
---

::: {.problem}
Let $M _ { n } ( F )$ be the ring of $n \times n$ matrices over a field F . Prove that for every $A \in M _ { n } ( F )$ there exists $X \in M _ { n } ( F )$ such that $A X A = A$
:::

::: {.solution}
Let
$$
\phi:F^n\longrightarrow F^n
$$
be the linear map represented by $A$.

::: pf

::: {.pf-step #s1}

There is a subspace $V\subseteq F^n$ such that
$$
F^n=\ker\phi\oplus V
$$
and the restriction
$$
\phi|_V:V\longrightarrow\im\phi
$$
is an isomorphism.

::: pf-proof

Choose any vector-space complement $V$ of $\ker\phi$. The restriction
$\phi|_V$ is injective because
$$
V\cap\ker\phi=\{0\}.
$$
It is surjective onto $\im\phi$: if $u=\phi(w)$, write
$$
w=w_0+v
$$
with $w_0\in\ker\phi$ and $v\in V$. Then
$$
u=\phi(w)=\phi(v).
$$
Thus the restriction is an isomorphism.

:::

:::

::: {.pf-step #s2}

There is a linear map
$$
\psi:F^n\longrightarrow F^n
$$
such that
$$
\phi\psi(u)=u
$$
for every $u\in\im\phi$.

::: pf-proof

Let
$$
\psi_0:(\im\phi)\longrightarrow V
$$
be the inverse of the isomorphism in step [](#s1){.pf-ref}. Choose a complement
$Z$ with
$$
F^n=\im\phi\oplus Z,
$$
and define
$$
\psi(u+z)\coloneqq\psi_0(u)
$$
for $u\in\im\phi$ and $z\in Z$. Then for $u\in\im\phi$,
$$
\phi\psi(u)
=
\phi\psi_0(u)
=u.
$$

:::

:::

::: {.pf-step #s3}

The endomorphisms satisfy
$$
\phi\psi\phi=\phi.
$$

::: pf-proof

For every $w\in F^n$, the vector $\phi(w)$ lies in $\im\phi$.
Applying step [](#s2){.pf-ref} to this vector gives
$$
\phi\psi\phi(w)=\phi(w).
$$
Since this holds for every $w$, the endomorphisms are equal.

:::

:::

::: {.pf-step #s4}

If $X$ is the matrix of $\psi$ in the standard basis, then
$$
AXA=A.
$$

::: pf-proof

Matrix multiplication represents composition of the corresponding
endomorphisms. Thus the matrix identity is exactly the endomorphism
identity from step [](#s3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} constructs the required matrix $X$.

:::

:::

:::
