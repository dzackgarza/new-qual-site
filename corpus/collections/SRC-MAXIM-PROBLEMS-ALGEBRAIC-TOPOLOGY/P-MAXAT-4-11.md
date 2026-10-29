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

::: {.solution}

For $n\ge2$, use Serre's finite-generation theorem together with rational
homotopy theory.

::: pf

::: {.pf-step #s1-1}

For every $n\ge2$ and every $k\ge2$, the group
$$
\pi_k(S^n)
$$
is finitely generated.


::: pf-proof

The sphere $S^n$ is a simply connected finite CW complex. Serre's
finite-generation theorem says that every homotopy group of a simply
connected finite-type CW complex is finitely generated.

:::

:::

::: {.pf-step #s1-2}

A finitely generated abelian group $A$ is torsion if and only if
$$
A\otimes\QQ=0.
$$


::: pf-proof

By the structure theorem,
$$
A\cong\ZZ^r\oplus T
$$
with $T$ finite. Tensoring with $\QQ$ gives
$$
A\otimes\QQ
\cong
\QQ^r.
$$
Thus the tensor product vanishes exactly when $r=0$, equivalently exactly
when $A$ is torsion.

:::

:::

::: {.pf-step #s1-3}

If $n$ is odd, a minimal Sullivan model for $S^n$ is
$$
(\Lambda(x_n),d=0),
\qquad
|x_n|=n.
$$


::: pf-proof

The rational cohomology ring of an odd sphere is
$$
H^*(S^n;\QQ)
\cong
\Lambda_{\QQ}(x_n),
$$
because the degree-$n$ generator is odd and therefore has square zero in a
graded-commutative algebra. The free graded-commutative DGA
$$
(\Lambda(x_n),0)
$$
already has exactly this cohomology and is minimal, so it is the minimal
Sullivan model of the sphere.

:::

:::

::: {.pf-step #s1-4}

If $n$ is even, a minimal Sullivan model for $S^n$ is
$$
(\Lambda(x_n,y_{2n-1}),d),
$$
with
$$
d x_n=0,
\qquad
d y_{2n-1}=x_n^2.
$$


::: pf-proof

For even $n$, the free graded-commutative algebra on $x_n$ would contain
the unwanted nonzero powers
$$
x_n^2,x_n^3,\dots,
$$
whereas
$$
H^*(S^n;\QQ)
\cong
\QQ\oplus\QQ x_n
$$
has no cohomology above degree $n$.

Introduce a generator
$$
y_{2n-1}
$$
and set
$$
d y_{2n-1}=x_n^2.
$$
This kills $x_n^2$ and consequently all higher powers of $x_n$ in
cohomology. The resulting DGA is minimal and has the rational cohomology
ring of $S^n$, hence is the minimal Sullivan model.

:::

:::

::: {.pf-step #s1-5}

If
$$
(\Lambda V,d)
$$
is the minimal Sullivan model of a simply connected finite-type space
$X$, then
$$
(V^k)^\vee
\cong
\pi_k(X)\otimes\QQ.
$$


::: pf-proof

This is the fundamental correspondence between minimal Sullivan models
and rational homotopy groups: the indecomposable generators in degree $k$
of the minimal model are dual to the degree-$k$ rational homotopy group.

:::

:::

::: {.pf-step #s1-6}

If $n$ is odd and $n\ge3$, then
$$
\pi_k(S^n)\otimes\QQ
\cong
\begin{cases}
\QQ,&k=n,\\
0,&k\ne n.
\end{cases}
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, the minimal model has exactly one indecomposable generator,
namely $x_n$ in degree $n$. Apply step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

If $n$ is even, then
$$
\pi_k(S^n)\otimes\QQ
\cong
\begin{cases}
\QQ,&k=n,\\
\QQ,&k=2n-1,\\
0,&k\ne n,2n-1.
\end{cases}
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, the minimal model has exactly two indecomposable generators:
$$
x_n
\quad\text{in degree }n
$$
and
$$
y_{2n-1}
\quad\text{in degree }2n-1.
$$
Apply step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

If $n\ge3$ is odd and $k\ne n$, then
$$
\pi_k(S^n)
$$
is a torsion group.


::: pf-proof

For $k<n$ the group is zero because $S^n$ is $(n-1)$-connected. For
$k>n$, step [](#s1-1){.pf-ref} gives finite generation and step [](#s1-6){.pf-ref} gives
$$
\pi_k(S^n)\otimes\QQ=0.
$$
Step [](#s1-2){.pf-ref} therefore implies that $\pi_k(S^n)$ is torsion.

:::

:::

::: {.pf-step #s1-9}

If $n$ is even and
$$
k\ne n,2n-1,
$$
then
$$
\pi_k(S^n)
$$
is a torsion group.


::: pf-proof

Again the groups below degree $n$ vanish. For $k\ge n$ outside the two
exceptional degrees, steps [](#s1-1){.pf-ref} and [](#s1-7){.pf-ref} give a finitely generated group
whose tensor product with $\QQ$ is zero. Apply step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

The exceptional degree $n$ is genuinely nontorsion:
$$
\pi_n(S^n)
\cong
\ZZ.
$$


::: pf-proof

The sphere $S^n$ is $(n-1)$-connected, so the Hurewicz theorem gives
$$
\pi_n(S^n)
\xrightarrow{\cong}
H_n(S^n;\ZZ)
\cong
\ZZ.
$$

:::

:::

::: {.pf-step #s1-11}

If $n$ is even, the exceptional group
$$
\pi_{2n-1}(S^n)
$$
has a free rank-one summand.


::: pf-proof

Step [](#s1-7){.pf-ref} gives
$$
\pi_{2n-1}(S^n)\otimes\QQ
\cong
\QQ.
$$
By step [](#s1-1){.pf-ref}, the integral group is finitely generated. Hence its free
rank is one:
$$
\pi_{2n-1}(S^n)
\cong
\ZZ\oplus T
$$
for some finite abelian group $T$.

:::

:::

::: {.pf-step #s1-12}

For $n=1$, the odd-sphere statement also holds.


::: pf-proof

One has
$$
\pi_1(S^1)\cong\ZZ
$$
and
$$
\pi_k(S^1)=0
\qquad(k>1).
$$
Thus the only nontorsion homotopy group is in degree $1=n$.

:::

:::

::: pf-qed

Steps [](#s1-8){.pf-ref} and [](#s1-10){.pf-ref}, and [](#s1-12){.pf-ref} prove part (a). Steps [](#s1-9){.pf-ref} through [](#s1-11){.pf-ref} prove
part (b).

:::

:::

:::
