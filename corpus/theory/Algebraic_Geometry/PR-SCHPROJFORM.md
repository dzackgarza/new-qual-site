---
schema: qual/card@1
id: PR-SCHPROJFORM
kind: proposition
title: The projection formula
slogan: 'Tensor by a pulled-back finite-rank bundle upstairs, or tensor every higher direct image downstairs: the result is the same.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Direct Image Functor
  - Locally Free Sheaves
  - Higher Direct Images
relations:
- kind: uses
  target: D-MODPULL
- kind: related-to
  target: D-DEFTALG
review: draft
prompts:
- What is Serre's projection formula?
---

::: {.proposition title="Projection formula"}
Let $f \colon X \to Y$ be a morphism of ringed spaces, $\mathcal{F}$ an $\OO_X$-module, and $\mathcal{E}$ a locally free $\OO_Y$-module of finite rank.
Then there are natural isomorphisms
$$
R^i f_* (\mathcal{F} \otimes_{\OO_X} f^* \mathcal{E}) \cong R^i f_* \mathcal{F} \otimes_{\OO_Y} \mathcal{E}
$$
for all $i \geq 0$.
[@Har10a, Exercise III.8.3]
:::

::: {.proof}
The statement is local on $Y$. Let $U\subseteq Y$ be an open set on which
$$
\mathcal E\restrict_U\cong\OO_U^{\oplus r}.
$$
Write $f_U\colon f^{-1}(U)\to U$ and $\mathcal F_U=\mathcal F\restrict_{f^{-1}(U)}$. Then
$$
\mathcal F_U\otimes_{\OO_{f^{-1}(U)}}f_U^*(\mathcal E\restrict_U)
\cong
\mathcal F_U^{\oplus r}.
$$
Since the right derived functors of the additive functor $f_*$ commute with finite direct sums,
$$
\bigl(R^if_*(\mathcal F\otimes f^*\mathcal E)\bigr)\restrict_U
\cong
R^i(f_U)_*(\mathcal F_U^{\oplus r})
\cong
\bigl(R^i(f_U)_*\mathcal F_U\bigr)^{\oplus r}
\cong
\bigl(R^if_*\mathcal F\otimes_{\OO_Y}\mathcal E\bigr)\restrict_U.
$$
These local isomorphisms are the restrictions of the natural projection-formula morphism, so they glue to the stated global isomorphism.
:::

::: {.example}
Let $\mathcal V$ be finite locally free on $Y$ and use the quotient convention
$$
\PP(\mathcal V)=\operatorname{Proj}_Y\Sym^\bullet\mathcal V
$$
from [[D-DEFTALG]]. For $\pi\colon\PP(\mathcal V)\to Y$, a line bundle $\mathcal L$ on $Y$, and $m\geq0$,
$$
\pi_*\bigl(\OO_{\PP(\mathcal V)}(m)\otimes\pi^*\mathcal L\bigr)
\cong
\Sym^m\mathcal V\otimes\mathcal L.
$$
This is the degree-zero projection formula together with $\pi_*\OO_{\PP(\mathcal V)}(m)\cong\Sym^m\mathcal V$.
:::
