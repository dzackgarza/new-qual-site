---
schema: qual/card@1
id: FE-SCHFFLAT
kind: example
title: Flatness of the affine line over the integers, and faithful flatness as faithfulness
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flat Morphisms
  - Faithfully Flat Modules
  - Affine Schemes
relations:
- kind: uses
  target: D-DEFFFLAT
review: draft
prompts:
- Show that $\AA^1_\ZZ$ is flat over $\Spec \ZZ$.
- Show that $M$ is faithfully flat if and only if $M$ is flat and $- \tensor_R M$ is a faithful functor.
---

::: {.example title="The affine line over the integers"}
$\AA^1_\ZZ = \Spec \ZZ[x] \to \Spec \ZZ$ is flat, because $\ZZ[x]$ is a free $\ZZ$-module with basis $1, x, x^2, \ldots$, and free modules are flat.
More generally $\AA^n_R \to \Spec R$ is flat for every ring $R$.
:::

::: {.proposition}
An $R$-module $M$ is faithfully flat if and only if $M$ is flat and the functor $- \tensor_R M$ on $R$-modules is faithful.
:::

::: {.proof}
Write $T \coloneqq -\tensor_R M$ and test exactness against the definition in [[D-DEFFFLAT]].

**Faithfully flat implies flat and faithful.**
If $M$ is faithfully flat and $A\to B$ is injective, then $0\to A\to B$ is an exact complex, so its tensor $0\to A\tensor_R M\to B\tensor_R M$ is exact and $M$ is flat.
For faithfulness, first note that $N\tensor_R M=0$ forces $N=0$: the complex $0\to N\to0$ is exact exactly when $N=0$, and its tensor $0\to N\tensor_R M\to0$ is exact exactly when $N\tensor_R M=0$.
Now let $f\colon N\to N'$ satisfy $T(f)=0$. Since $T$ is right exact, $\im T(f)=T(\im f)=\im f\tensor_R M$, so $\im f\tensor_R M=0$ and hence $\im f=0$, that is $f=0$. So $T$ is faithful.

**Flat and faithful imply faithfully flat.**
Let $M'\xrightarrow{f_1}M\xrightarrow{f_2}M''$ be a complex with $T$-exact tensor. Flatness of $M$ identifies the kernel and image there:
$$
\ker(f_2\tensor\id)=(\ker f_2)\tensor_R M,\qquad \im(f_1\tensor\id)=(\im f_1)\tensor_R M,
$$
the first by applying $T$ to the exact $0\to\ker f_2\to M\to\im f_2\to0$. So $(\ker f_2)\tensor_R M=(\im f_1)\tensor_R M$ inside $M\tensor_R M$, and right exactness of $T$ applied to $0\to\im f_1\to\ker f_2\to K\to0$, with $K\coloneqq\ker f_2/\im f_1$, gives
$$
K\tensor_R M=\frac{(\ker f_2)\tensor_R M}{(\im f_1)\tensor_R M}=0 .
$$
Faithfulness of $T$ forces $K=0$, that is $\ker f_2=\im f_1$, and the complex is exact.
:::

::: {.remark}
The flatness hypothesis is not redundant: faithfulness of $- \tensor_R M$ alone does not give flatness.
For $R = \ZZ$ and $M = \ZZ \oplus \ZZ/2$, $- \tensor_\ZZ M$ is faithful because $M$ has $\ZZ$ as a direct summand, but $M$ is not flat, since $\ZZ \xrightarrow{2} \ZZ$ tensored over $\ZZ$ with $\ZZ/2$ is the zero map on $\ZZ/2 \neq 0$.
:::
