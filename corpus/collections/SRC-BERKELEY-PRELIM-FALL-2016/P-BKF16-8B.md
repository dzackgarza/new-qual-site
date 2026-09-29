---
schema: qual/card@1
id: P-BKF16-8B
kind: problem
title: A group that is both a quotient and a subgroup of $\mathbb Z^n$ is isomorphic to $\mathbb Z^n$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2016 solution packet: the
    surjection makes G finitely generated abelian, the injection and
    surjection force free rank n, and equality of ranks forces the finite
    torsion summand to vanish.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the structure-theorem decomposition, both rank inequalities, and
    the final argument that a surjection from Z^n onto Z^n plus nonzero
    torsion is impossible.
---

::: {.problem}
Let G be a group and n be a positive integer.
Assume that there exists a surjective group homomorphism $\mathbb { Z } ^ { n } \to G$ and an injective group homomorphism $\mathbb { Z } ^ { n } \to G$ . Prove that the group G is isomorphic to $\mathbb { Z } ^ { n }$
:::

::: {.solution}
Let
$$
\varphi:\ZZ^n\to G
$$
be surjective and
$$
\psi:\ZZ^n\to G
$$
be injective.

::: pf

::: {.pf-step #s1}

The group $G$ is a finitely generated abelian group.

::: pf-proof

The image of an abelian group under a homomorphism is abelian. Since
$\varphi$ is surjective, $G$ is therefore abelian. The images under
$\varphi$ of the $n$ standard generators of $\ZZ^n$ generate $G$, so
$G$ is finitely generated.

:::

:::

::: {.pf-step #s2}

There are an integer $r\ge0$ and a finite abelian group $T$ such
that
$$
G\cong\ZZ^r\oplus T.
$$

::: pf-proof

This is the structure theorem for finitely generated abelian groups,
applied to step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

The injection $\psi$ implies
$$
r\ge n.
$$

::: pf-proof

Identify $G$ with $\ZZ^r\oplus T$ as in step [](#s2){.pf-ref}, and let
$$
\pi:\ZZ^r\oplus T\to\ZZ^r
$$
be projection. The subgroup $\psi(\ZZ^n)$ is torsion-free, so its
intersection with the finite torsion subgroup $T$ is trivial. Therefore
the restriction
$$
\pi|_{\psi(\ZZ^n)}:\psi(\ZZ^n)\to\ZZ^r
$$
is injective. Thus $\ZZ^n$ embeds into $\ZZ^r$. Every subgroup of
$\ZZ^r$ is free abelian of rank at most $r$, so $n\le r$.

:::

:::

::: {.pf-step #s4}

The surjection $\varphi$ implies
$$
r\le n.
$$

::: pf-proof

With the decomposition from step [](#s2){.pf-ref}, the composite
$$
\pi\circ\varphi:\ZZ^n\to\ZZ^r
$$
is surjective because both $\varphi$ and $\pi$ are surjective. A
surjective homomorphism from $\ZZ^n$ to $\ZZ^r$ requires $r\le n$.

:::

:::

::: {.pf-step #s5}

Hence
$$
r=n.
$$

::: pf-proof

Combine steps [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

The finite summand $T$ is trivial.

::: pf-proof

By step [](#s5){.pf-ref}, identify
$$
G\cong\ZZ^n\oplus T.
$$
Then
$$
\pi\circ\varphi:\ZZ^n\to\ZZ^n
$$
is a surjective endomorphism. A surjective endomorphism of the
finitely generated free abelian group $\ZZ^n$ is an automorphism, so
$$
\ker(\pi\circ\varphi)=0.
$$

Take any $t\in T$. Since $\varphi$ is surjective, there is
$x\in\ZZ^n$ with
$$
\varphi(x)=(0,t).
$$
Applying $\pi$ gives
$$
(\pi\circ\varphi)(x)=0.
$$
Hence $x=0$, and therefore
$$
(0,t)=\varphi(0)=0.
$$
Thus $t=0$. Since $t$ was arbitrary, $T=0$.

:::

:::

::: {.pf-step #s7}

Therefore
$$
\boxed{G\cong\ZZ^n}.
$$

::: pf-proof

Steps [](#s2){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} give
$$
G\cong\ZZ^n\oplus0\cong\ZZ^n.
$$

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the required conclusion.

:::

:::

:::
