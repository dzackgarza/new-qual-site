---
schema: qual/card@1
id: FF-6K35J
kind: fact
title: Geometric interpretation of Nakayama's lemma
prompts:
- What is the geometric interpretation of Nakayama's lemma?
classification:
  areas:
  - algebra
  topics:
  - Nakayama's Lemma
  - Geometry
  - Modules
relations: []
review: draft
---

::: {.fact}
Let $X$ be a Noetherian scheme, let $\mathcal F$ be a [[D-QNTZY|coherent]] $\OO_X$-module, let $p\in X$, and let $\kappa(p)=\OO_{X,p}/\mfm_p$.
The fiber $\mathcal F(p)\coloneqq\mathcal F_p/\mfm_p\mathcal F_p$ of $\mathcal F$ at $p$ is a finite-dimensional $\kappa(p)$-vector space.

(a) Every lift to the [[D-0QSI0|stalk]] $\mathcal F_p$ of a basis of $\mathcal F(p)$ is a minimal generating set of $\mathcal F_p$.

(b) Given such a lift, there are an open neighborhood $U$ of $p$ and sections $s_1,\ldots,s_n\in\mathcal F(U)$ with these germs at $p$ that generate $\mathcal F_q$ for every $q\in U$.

(c) If $\mathcal F$ is locally free near $p$, the sections $s_1,\ldots,s_n$ of (b) can be chosen so that $\OO_U^n\to\mathcal F|_U$, $(f_i)\mapsto\sum_if_is_i$, is an isomorphism; that is, a basis of the fiber of a vector bundle at $p$ extends to a local frame on a neighborhood of $p$.
:::

::: {.proof}
The stalk $\mathcal F_p$ is a finitely generated module over the local ring $\OO_{X,p}$, so (a) is [[FF-45SK3|Nakayama's lemma for a local ring]].

For (b), choose an open neighborhood $V$ of $p$ on which all the germs are represented by sections $s_i\in\mathcal F(V)$, and let $\mathcal C$ be the cokernel of $\OO_V^n\to\mathcal F|_V$.
Then $\mathcal C$ is coherent with $\mathcal C_p=0$, and the support of a coherent sheaf is closed, so $\mathcal C$ vanishes on an open neighborhood $U\subseteq V$ of $p$.

For (c), shrink $U$ to an affine open $\Spec A$ containing $p$ on which $\mathcal F$ is free; its rank is $\dim_{\kappa(p)}\mathcal F(p)=n$.
Since $\OO_U^n\to\mathcal F|_U$ is surjective and $U$ is affine, the map $A^n\to\mathcal F(\Spec A)\cong A^n$ is a surjective endomorphism of a finitely generated $A$-module, hence an isomorphism.
:::
