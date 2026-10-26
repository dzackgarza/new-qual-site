---
schema: qual/card@1
id: P-MAXAT-4-11
kind: problem
title: Maxim algebraic topology 4.11
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 4, problem 11 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Prove Serre’s theorem: (a) The homotopy groups of odd spheres $S ^ { n }$ are torsion except in dimension n; (b) The homotopy groups of even spheres $S ^ { n }$ are torsion except in dimension n and $2 n - 1$
:::

For $n\ge2$, use Serre's finite-generation theorem together with rational
homotopy theory.

::: pf

::: pf-step

For every $n\ge2$ and every $k\ge2$, the group
\[
\pi_k(S^n)
\]
is finitely generated.


::: pf-proof

The sphere $S^n$ is a simply connected finite CW complex. Serre's
finite-generation theorem says that every homotopy group of a simply
connected finite-type CW complex is finitely generated.

:::

:::

::: pf-step

A finitely generated abelian group $A$ is torsion if and only if
\[
A\otimes\mathbb Q=0.
\]


::: pf-proof

By the structure theorem,
\[
A\cong\mathbb Z^r\oplus T
\]
with $T$ finite. Tensoring with $\mathbb Q$ gives
\[
A\otimes\mathbb Q
\cong
\mathbb Q^r.
\]
Thus the tensor product vanishes exactly when $r=0$, equivalently exactly
when $A$ is torsion.

:::

:::

::: pf-step

If $n$ is odd, a minimal Sullivan model for $S^n$ is
\[
(\Lambda(x_n),d=0),
\qquad
|x_n|=n.
\]


::: pf-proof

The rational cohomology ring of an odd sphere is
\[
H^*(S^n;\mathbb Q)
\cong
\Lambda_{\mathbb Q}(x_n),
\]
because the degree-$n$ generator is odd and therefore has square zero in a
graded-commutative algebra. The free graded-commutative DGA
\[
(\Lambda(x_n),0)
\]
already has exactly this cohomology and is minimal, so it is the minimal
Sullivan model of the sphere.

:::

:::

::: pf-step

If $n$ is even, a minimal Sullivan model for $S^n$ is
\[
(\Lambda(x_n,y_{2n-1}),d),
\]
with
\[
d x_n=0,
\qquad
d y_{2n-1}=x_n^2.
\]


::: pf-proof

For even $n$, the free graded-commutative algebra on $x_n$ would contain
the unwanted nonzero powers
\[
x_n^2,x_n^3,\dots,
\]
whereas
\[
H^*(S^n;\mathbb Q)
\cong
\mathbb Q\oplus\mathbb Q x_n
\]
has no cohomology above degree $n$.

Introduce a generator
\[
y_{2n-1}
\]
and set
\[
d y_{2n-1}=x_n^2.
\]
This kills $x_n^2$ and consequently all higher powers of $x_n$ in
cohomology. The resulting DGA is minimal and has the rational cohomology
ring of $S^n$, hence is the minimal Sullivan model.

:::

:::

::: pf-step

If
\[
(\Lambda V,d)
\]
is the minimal Sullivan model of a simply connected finite-type space
$X$, then
\[
(V^k)^\vee
\cong
\pi_k(X)\otimes\mathbb Q.
\]


::: pf-proof

This is the fundamental correspondence between minimal Sullivan models
and rational homotopy groups: the indecomposable generators in degree $k$
of the minimal model are dual to the degree-$k$ rational homotopy group.

:::

:::

::: pf-step

If $n$ is odd and $n\ge3$, then
\[
\pi_k(S^n)\otimes\mathbb Q
\cong
\begin{cases}
\mathbb Q,&k=n,\\
0,&k\ne n.
\end{cases}
\]


::: pf-proof

By step <1>3, the minimal model has exactly one indecomposable generator,
namely $x_n$ in degree $n$. Apply step <1>5.

:::

:::

::: pf-step

If $n$ is even, then
\[
\pi_k(S^n)\otimes\mathbb Q
\cong
\begin{cases}
\mathbb Q,&k=n,\\
\mathbb Q,&k=2n-1,\\
0,&k\ne n,2n-1.
\end{cases}
\]


::: pf-proof

By step <1>4, the minimal model has exactly two indecomposable generators:
\[
x_n
\quad\text{in degree }n
\]
and
\[
y_{2n-1}
\quad\text{in degree }2n-1.
\]
Apply step <1>5.

:::

:::

::: pf-step

If $n\ge3$ is odd and $k\ne n$, then
\[
\pi_k(S^n)
\]
is a torsion group.


::: pf-proof

For $k<n$ the group is zero because $S^n$ is $(n-1)$-connected. For
$k>n$, step <1>1 gives finite generation and step <1>6 gives
\[
\pi_k(S^n)\otimes\mathbb Q=0.
\]
Step <1>2 therefore implies that $\pi_k(S^n)$ is torsion.

:::

:::

::: pf-step

If $n$ is even and
\[
k\ne n,2n-1,
\]
then
\[
\pi_k(S^n)
\]
is a torsion group.


::: pf-proof

Again the groups below degree $n$ vanish. For $k\ge n$ outside the two
exceptional degrees, steps <1>1 and <1>7 give a finitely generated group
whose tensor product with $\mathbb Q$ is zero. Apply step <1>2.

:::

:::

::: pf-step

The exceptional degree $n$ is genuinely nontorsion:
\[
\pi_n(S^n)
\cong
\mathbb Z.
\]


::: pf-proof

The sphere $S^n$ is $(n-1)$-connected, so the Hurewicz theorem gives
\[
\pi_n(S^n)
\xrightarrow{\cong}
H_n(S^n;\mathbb Z)
\cong
\mathbb Z.
\]

:::

:::

::: pf-step

If $n$ is even, the exceptional group
\[
\pi_{2n-1}(S^n)
\]
has a free rank-one summand.


::: pf-proof

Step <1>7 gives
\[
\pi_{2n-1}(S^n)\otimes\mathbb Q
\cong
\mathbb Q.
\]
By step <1>1, the integral group is finitely generated. Hence its free
rank is one:
\[
\pi_{2n-1}(S^n)
\cong
\mathbb Z\oplus T
\]
for some finite abelian group $T$.

:::

:::

::: pf-step

For $n=1$, the odd-sphere statement also holds.


::: pf-proof

One has
\[
\pi_1(S^1)\cong\mathbb Z
\]
and
\[
\pi_k(S^1)=0
\qquad(k>1).
\]
Thus the only nontorsion homotopy group is in degree $1=n$.

:::

:::

::: pf-qed

Steps <1>8, <1>10, and <1>12 prove part (a). Steps <1>9--<1>11 prove
part (b).

:::

:::
