---
schema: qual/card@1
id: FF-QILDV
kind: fact
title: Finitely generated flat modules over a Noetherian local ring are free
prompts:
- Give a categorical/homological corollary of Nakayama's lemma.
classification:
  areas:
  - algebra
  topics:
  - Nakayama's Lemma
  - Free Modules
  - Modules
relations: []
review: draft
---

::: {.fact}
Let $(R,\mfm)$ be a Noetherian [[D-TGB4R|local ring]] and let $M$ be a finitely generated [[D-DEFFLAT|flat]] $R$-module.
Then $M$ is [[D-LIEMF|free]].
:::

::: {.proof}
Let $k=R/\mfm$ and $n=\dim_kM/\mfm M$.
By [[FF-45SK3|Nakayama's lemma for a local ring]], lifts of a $k$-basis of $M/\mfm M$ give a surjection $R^n\to M$; let $K$ be its kernel, which is finitely generated because $R$ is Noetherian.
Since $M$ is flat, $\Tor_1^R(k,M)=0$, so applying $k\otimes_R-$ to $0\to K\to R^n\to M\to0$ gives an exact sequence
$$
0\to K/\mfm K\to k^n\to M/\mfm M\to0.
$$
The map $k^n\to M/\mfm M$ is a surjection between $k$-vector spaces of dimension $n$, hence an isomorphism, so $K/\mfm K=0$.
By [[FF-NREXC|Nakayama's lemma]], $K=0$, and $M\cong R^n$.
:::

::: {.remark}
Applied to stalks, this shows that a [[D-QNTZY|coherent]] sheaf $\mathcal F$ on a Noetherian scheme $X$ whose stalks $\mathcal F_x$ are flat $\OO_{X,x}$-modules has free stalks, and is therefore locally free, that is, the sheaf of sections of a vector bundle.
:::
