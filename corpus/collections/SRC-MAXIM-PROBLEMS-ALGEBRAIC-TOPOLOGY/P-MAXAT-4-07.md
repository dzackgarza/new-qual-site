---
schema: qual/card@1
id: P-MAXAT-4-07
kind: problem
title: Rational cohomology of $K(\ZZ,n)$
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 4, problem 7 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Find $H ^ { * } ( K ( \ZZ , n ) ; \QQ )$
:::

::: {.solution}

Let
$$
X=K(\ZZ,n).
$$
Its rationalization is $K(\QQ,n)$, so the rational cohomology depends only on the parity of $n$.

::: pf

::: {.pf-step #s1-1}

The rationalization map
$$
K(\ZZ,n)\longrightarrow K(\QQ,n)
$$
induces an isomorphism on rational cohomology.


::: pf-proof

It induces the localization map $\ZZ\to\QQ$ on the only nonzero homotopy group and therefore is a rational homotopy equivalence between nilpotent CW complexes. Rational homology, and hence rational cohomology, is invariant under rationalization.

:::

:::

::: {.pf-step #s1-2}

A Sullivan minimal model for $K(\QQ,n)$ has one generator $x$ in degree $n$ and zero differential:
$$
(\Lambda(x_n),d=0).
$$


::: pf-proof

An Eilenberg--MacLane space $K(\QQ,n)$ has exactly one nonzero rational homotopy group, namely $\pi_n\otimes\QQ\cong\QQ$. In a minimal Sullivan model this corresponds to one indecomposable generator in degree $n$. There are no further rational homotopy groups requiring additional generators, and minimality leaves $dx=0$.

:::

:::

::: {.pf-step #s1-3}

If $n$ is odd, graded commutativity gives
$$
x^2=0,
$$
so
$$
\Lambda(x_n)
$$
is the exterior algebra on $x_n$.


::: pf-proof

For odd $n$,
$$
x^2=(-1)^{n^2}x^2=-x^2.
$$
Over $\QQ$, $2$ is invertible, hence $x^2=0$. Thus the free graded-commutative algebra on one odd generator is exterior.

:::

:::

::: {.pf-step #s1-4}

If $n$ is even, the free graded-commutative algebra on $x_n$ is the polynomial algebra
$$
\QQ[x_n].
$$


::: pf-proof

For even $n$, graded commutativity imposes no sign change on $x^2$, so no power of the free generator is forced to vanish. Hence the free graded-commutative algebra is polynomial.

:::

:::

::: {.pf-step #s1-5}

Since the differential in step [](#s1-2){.pf-ref} is zero, its cohomology is the algebra itself. Therefore
$$
\boxed{
H^*(K(\ZZ,n);\QQ)
\cong
\begin{cases}
\Lambda_{\QQ}(x_n),&n\text{ odd},\\
\QQ[x_n],&n\text{ even},
\end{cases}
\qquad \gradeddegree{x_n}=n.}
$$


::: pf-proof

Step [](#s1-1){.pf-ref} reduces the calculation to $K(\QQ,n)$. Step [](#s1-2){.pf-ref} gives its zero-differential model, and steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} identify the underlying graded-commutative algebra according to parity.

:::

:::

::: pf-step

In particular,
$$
H^*(K(\ZZ,3);\QQ)
\cong\Lambda_{\QQ}(x_3).
$$


::: pf-proof

Set $n=3$ in step [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the requested rational cohomology ring.

:::

:::

:::
