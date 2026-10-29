---
schema: qual/card@1
id: P-MAXAT-1-08
kind: problem
title: Maxim algebraic topology 1.8
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 1, problem 8 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Show that the Euler characteristic of a closed, oriented, $( 4 n + 2 )$ -dimensional manifold is even.
:::

::: {.solution}

Let $M$ be a closed oriented manifold of dimension
$$
d=4n+2.
$$
Work with rational coefficients and write $b_i=\dim_{\QQ}H^i(M;\QQ)$.

::: pf

::: {.pf-step #s1-1}

Poincaré duality gives
$$
b_i=b_{d-i}.
$$


::: pf-proof

Since $M$ is closed and oriented, the pairing
$$
H^i(M;\QQ)\times H^{d-i}(M;\QQ)
\longrightarrow\QQ,
\qquad
(x,y)\longmapsto\langle x\smile y,[M]\rangle
$$
is perfect. Therefore the two vector spaces have equal dimension.

:::

:::

::: {.pf-step #s1-2}

Pairing all degrees except the middle one gives
$$
\chi(M)\equiv b_{2n+1}\pmod2.
$$


::: pf-proof

The Euler characteristic is
$$
\chi(M)=\sum_{i=0}^{d}(-1)^ib_i.
$$
For $i\ne d-i$, step [](#s1-1){.pf-ref} pairs the $i$th and $(d-i)$th terms. Since $d$ is even, they have the same sign, so each pair contributes
$$
2(-1)^ib_i,
$$
which is even. The only unpaired degree is
$$
i=d/2=2n+1.
$$
Thus modulo $2$, only $b_{2n+1}$ remains.

:::

:::

::: {.pf-step #s1-3}

The middle-dimensional cup-product pairing
$$
Q(x,y)=\langle x\smile y,[M]\rangle,
\qquad
x,y\in H^{2n+1}(M;\QQ),
$$
is nondegenerate and skew-symmetric.


::: pf-proof

Nondegeneracy is Poincaré duality. Graded commutativity gives
$$
x\smile y=(-1)^{(2n+1)^2}y\smile x=-y\smile x,
$$
because $2n+1$ is odd. Hence $Q(x,y)=-Q(y,x)$.

:::

:::

::: {.pf-step #s1-4}

A finite-dimensional vector space over $\QQ$ carrying a nondegenerate skew-symmetric bilinear form has even dimension.


::: pf-proof

Let $V$ carry such a form. Choose $0\ne v\in V$. Nondegeneracy gives $w\in V$ with $Q(v,w)\ne0$, so the span $U=\langle v,w\rangle$ is a nondegenerate $2$-dimensional subspace. Then
$$
V=U\oplus U^{\perp}.
$$
The restriction to $U^{\perp}$ is again nondegenerate and skew-symmetric. Induction on $\dim V$ decomposes $V$ into $2$-dimensional summands, so $\dim V$ is even.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
b_{2n+1}\equiv0\pmod2.
$$


::: pf-proof

Apply step [](#s1-4){.pf-ref} to the middle cohomology vector space and its pairing from step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{\chi(M)\equiv0\pmod2}.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives $\chi(M)\equiv b_{2n+1}\pmod2$, and step [](#s1-5){.pf-ref} shows the latter is even.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
