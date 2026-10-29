---
schema: qual/card@1
id: P-MAXAT-1-03
kind: problem
title: A $4n$-manifold bounding a compact oriented manifold has signature zero
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 1, problem 3 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Show that if $M ^ { 4 n }$ is a connected manifold which is the boundary of a compact oriented $( 4 n + 1 )$ -dimensional manifold V , then the signature of M is zero.
:::

::: {.solution}

Let $i:M=\partial V\hookrightarrow V$ be the inclusion. Work with rational coefficients. The intersection form of the closed oriented $4n$-manifold $M$ is
$$
Q_M(x,y)=\langle x\smile y,[M]\rangle,
\qquad x,y\in H^{2n}(M;\QQ).
$$

::: pf

::: {.pf-step #s1-1}

Let
$$
L=\operatorname{im}\bigl(i^*:H^{2n}(V;\QQ)\to H^{2n}(M;\QQ)\bigr).
$$
Then $L$ is isotropic for $Q_M$.


::: pf-proof

Take $x=i^*a$ and $y=i^*b$ in $L$. Then
$$
Q_M(x,y)
=\langle i^*(a\smile b),[M]\rangle.
$$
Since $[M]=\partial[V,M]$, naturality of the Kronecker pairing and the connecting morphisms gives
$$
\langle i^*(a\smile b),\partial[V,M]\rangle
=\langle \delta i^*(a\smile b),[V,M]\rangle=0,
$$
because exactness of the cohomology sequence of $(V,M)$ gives $\delta\circ i^*=0$. Hence $Q_M$ vanishes on $L\times L$.

:::

:::

::: {.pf-step #s1-2}

The long exact cohomology sequence of the pair contains
$$
H^{2n}(V)\xrightarrow{i^*}H^{2n}(M)
\xrightarrow{\delta}H^{2n+1}(V,M)
\xrightarrow{j^*}H^{2n+1}(V).
$$
Thus
$$
\dim H^{2n}(M)
=\dim L+\dim\ker j^*.
$$


::: pf-proof

Exactness gives $\ker\delta=L$ and $\operatorname{im}\delta=\ker j^*$. Therefore
$$
H^{2n}(M)/L\cong\ker j^*,
$$
and taking dimensions yields the formula.

:::

:::

::: {.pf-step #s1-3}

Poincaré--Lefschetz duality identifies the map $j^*$ in step [](#s1-2){.pf-ref} with the dual of
$$
i^*:H^{2n}(V)\to H^{2n}(M)
$$
in the sense that
$$
\dim\ker j^*=\dim L.
$$


::: pf-proof

Poincaré--Lefschetz duality gives perfect pairings
$$
H^{2n}(V)\times H^{2n+1}(V,M)\to\QQ
$$
and Poincaré duality gives a perfect pairing on $H^{2n}(M)$. Under these pairings, the connecting and restriction maps in the long exact sequence are adjoint up to sign. Consequently the exact sequence around the middle dimension is self-dual. In particular, the annihilator of $L=\operatorname{im}i^*$ is $L$ itself, equivalently
$$
\dim H^{2n}(M)=2\dim L.
$$
Combining this with step [](#s1-2){.pf-ref} gives $\dim\ker j^*=\dim L$.

:::

:::

::: {.pf-step #s1-4}

Hence $L$ is a Lagrangian subspace of the nonsingular symmetric form $Q_M$.


::: pf-proof

Step [](#s1-1){.pf-ref} shows that $L$ is isotropic, while step [](#s1-3){.pf-ref} gives
$$
\dim L=\frac12\dim H^{2n}(M;\QQ).
$$
The intersection form is nonsingular by Poincaré duality. An isotropic subspace of half the dimension of a nonsingular symmetric space is Lagrangian.

:::

:::

::: {.pf-step #s1-5}

A nonsingular symmetric bilinear form over $\QQ$ that has a Lagrangian has signature zero.


::: pf-proof

Extend a basis $e_1,\ldots,e_r$ of the Lagrangian $L$ to vectors $f_1,\ldots,f_r$ so that the pairing matrix between the $e_i$ and $f_j$ is the identity. In this basis the form has matrix
$$
\begin{pmatrix}
0&I\\
I&A
\end{pmatrix}
$$
for some symmetric $A$. Replacing $f_i$ by
$$
f_i-\frac12\sum_jA_{ij}e_j
$$
changes the matrix to
$$
\begin{pmatrix}0&I\\I&0\end{pmatrix}.
$$
Over $\RR$, this is a direct sum of $r$ hyperbolic planes, each with one positive and one negative eigenvalue. Thus the numbers of positive and negative eigenvalues agree and the signature is zero.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{\operatorname{sign}(M)=0}.
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, the middle-dimensional intersection form of $M$ has a Lagrangian. Step [](#s1-5){.pf-ref} therefore gives zero signature.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves the claim.

:::

:::

:::
