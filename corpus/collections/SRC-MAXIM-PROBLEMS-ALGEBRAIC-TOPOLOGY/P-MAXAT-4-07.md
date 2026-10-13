---
schema: qual/card@1
id: P-MAXAT-4-07
kind: problem
title: Maxim algebraic topology 4.7
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
Find $H ^ { * } ( K ( \mathbb { Z } , n ) ; \mathbb { Q } )$
:::

::: {.solution}
Let
\[
X=K(\mathbb Z,n).
\]
Its rationalization is $K(\mathbb Q,n)$, so the rational cohomology depends only on the parity of $n$.

<1>1. The rationalization map
\[
K(\mathbb Z,n)\longrightarrow K(\mathbb Q,n)
\]
induces an isomorphism on rational cohomology.

::: {.proof}
It induces the localization map $\mathbb Z\to\mathbb Q$ on the only nonzero homotopy group and therefore is a rational homotopy equivalence between nilpotent CW complexes. Rational homology, and hence rational cohomology, is invariant under rationalization.
:::

<1>2. A Sullivan minimal model for $K(\mathbb Q,n)$ has one generator $x$ in degree $n$ and zero differential:
\[
(\Lambda(x_n),d=0).
\]

::: {.proof}
An Eilenberg--MacLane space $K(\mathbb Q,n)$ has exactly one nonzero rational homotopy group, namely $\pi_n\otimes\mathbb Q\cong\mathbb Q$. In a minimal Sullivan model this corresponds to one indecomposable generator in degree $n$. There are no further rational homotopy groups requiring additional generators, and minimality leaves $dx=0$.
:::

<1>3. If $n$ is odd, graded commutativity gives
\[
x^2=0,
\]
so
\[
\Lambda(x_n)
\]
is the exterior algebra on $x_n$.

::: {.proof}
For odd $n$,
\[
x^2=(-1)^{n^2}x^2=-x^2.
\]
Over $\mathbb Q$, $2$ is invertible, hence $x^2=0$. Thus the free graded-commutative algebra on one odd generator is exterior.
:::

<1>4. If $n$ is even, the free graded-commutative algebra on $x_n$ is the polynomial algebra
\[
\mathbb Q[x_n].
\]

::: {.proof}
For even $n$, graded commutativity imposes no sign change on $x^2$, so no power of the free generator is forced to vanish. Hence the free graded-commutative algebra is polynomial.
:::

<1>5. Since the differential in step <1>2 is zero, its cohomology is the algebra itself. Therefore
\[
\boxed{
H^*(K(\mathbb Z,n);\mathbb Q)
\cong
\begin{cases}
\Lambda_{\mathbb Q}(x_n),&n\text{ odd},\\
\mathbb Q[x_n],&n\text{ even},
\end{cases}
\qquad |x_n|=n.}
\]

::: {.proof}
Step <1>1 reduces the calculation to $K(\mathbb Q,n)$. Step <1>2 gives its zero-differential model, and steps <1>3--<1>4 identify the underlying graded-commutative algebra according to parity.
:::

<1>6. In particular,
\[
H^*(K(\mathbb Z,3);\mathbb Q)
\cong\Lambda_{\mathbb Q}(x_3).
\]

::: {.proof}
Set $n=3$ in step <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>5 is the requested rational cohomology ring.
:::
:::
