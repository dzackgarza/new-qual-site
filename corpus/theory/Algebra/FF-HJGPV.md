---
schema: qual/card@1
id: FF-HJGPV
kind: fact
title: Geometric interpretation of Krull's intersection theorem
prompts:
- What is the geometric interpretation of Krull's intersection theorem?
classification:
  areas:
  - algebra
  topics:
  - Krull Dimension
  - Local Rings
  - Geometry
relations: []
review: draft
---

::: {.fact}
Let $X$ be a locally Noetherian scheme, for example a variety, let $p\in X$, and let $(\OO_{X,p},\mfm_p)$ be the local ring at $p$.
For $f\in\OO_{X,p}$, define the order of vanishing of $f$ at $p$ as
$$
\ord_p(f)\coloneqq\sup\theset{n\ge0\suchthat f\in\mfm_p^n}\in\ZZ_{\ge0}\cup\theset{\infty}.
$$
Then $\ord_p(f)=\infty$ if and only if $f=0$: a nonzero function vanishes to finite order at $p$.
:::

::: {.proof}
The local ring $\OO_{X,p}$ is Noetherian, and $\ord_p(f)=\infty$ means $f\in\bigcap_{n\ge0}\mfm_p^n$, which is $0$ by [[FF-3K36R|Krull's intersection theorem]].
:::

::: {.remark}
[[FF-45SK3|Nakayama's lemma for a local ring]] gives the companion statement for generators.
Let $k$ be a field and let $\mfm_0\subseteq\OO_{\AA^n_k,0}$ be the maximal ideal at the origin.
Functions $f_1,\ldots,f_n\in\mfm_0$ generate $\mfm_0$, that is, form a local coordinate system at $0$, if and only if their classes form a basis of the cotangent space $\mfm_0/\mfm_0^2$.
The class of $f$ in $\mfm_0/\mfm_0^2$ is its linear part, the differential $df_0=\sum_i\frac{\partial f}{\partial x_i}(0)\,dx_i$, so the condition is that the Jacobian matrix $\qty{\frac{\partial f_i}{\partial x_j}(0)}$ is invertible, as in the inverse function theorem.
:::
