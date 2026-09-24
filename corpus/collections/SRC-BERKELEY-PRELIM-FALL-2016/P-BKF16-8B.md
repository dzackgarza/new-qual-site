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

<1>1. The group $G$ is a finitely generated abelian group.

::: {.proof}
The image of an abelian group under a homomorphism is abelian. Since
$\varphi$ is surjective, $G$ is therefore abelian. The images under
$\varphi$ of the $n$ standard generators of $\ZZ^n$ generate $G$, so
$G$ is finitely generated.
:::

<1>2. There are an integer $r\ge0$ and a finite abelian group $T$ such
that
$$
G\cong\ZZ^r\oplus T.
$$

::: {.proof}
This is the structure theorem for finitely generated abelian groups,
applied to step <1>1.
:::

<1>3. The injection $\psi$ implies
$$
r\ge n.
$$

::: {.proof}
Identify $G$ with $\ZZ^r\oplus T$ as in step <1>2, and let
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

<1>4. The surjection $\varphi$ implies
$$
r\le n.
$$

::: {.proof}
With the decomposition from step <1>2, the composite
$$
\pi\circ\varphi:\ZZ^n\to\ZZ^r
$$
is surjective because both $\varphi$ and $\pi$ are surjective. A
surjective homomorphism from $\ZZ^n$ to $\ZZ^r$ requires $r\le n$.
:::

<1>5. Hence
$$
r=n.
$$

::: {.proof}
Combine steps <1>3 and <1>4.
:::

<1>6. The finite summand $T$ is trivial.

::: {.proof}
By step <1>5, identify
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

<1>7. Therefore
$$
\boxed{G\cong\ZZ^n}.
$$

::: {.proof}
Steps <1>2, <1>5, and <1>6 give
$$
G\cong\ZZ^n\oplus0\cong\ZZ^n.
$$
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required conclusion.
:::
:::
