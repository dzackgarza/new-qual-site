---
schema: qual/card@1
id: P-UCLAB02F-07
kind: problem
title: Transpose, annihilator of the image, and equality of ranks
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 of the retained UCLA Basic Examination, Fall 2002 PDF.
---

::: {.problem}
Let $T:V\to W$ be a linear transformation of finite-dimensional real vector spaces.
Define the transpose $T^t:W^*\to V^*$ and prove both of the following:

(i)
\[
(\operatorname{im}T)^0=\ker(T^t),
\]
where $(\operatorname{im}T)^0$ is the annihilator of the image of $T$.

(ii)
\[
\operatorname{rank}(T)=\operatorname{rank}(T^t).
\]
:::

::: {.solution}
Define
\[
T^t:W^*\to V^*
\]
by
\[
T^t(\varphi)=\varphi\circ T.
\]

<1>1. One has
\[
(\operatorname{im}T)^0\subseteq\ker(T^t).
\]

::: {.proof}
Let $\varphi\in(\operatorname{im}T)^0$. For every $v\in V$,
\[
(T^t\varphi)(v)
=
\varphi(Tv).
\]
Since $Tv\in\operatorname{im}T$ and $\varphi$ vanishes on $\operatorname{im}T$, this is $0$. Hence $T^t\varphi=0$.
:::

<1>2. One has
\[
\ker(T^t)\subseteq(\operatorname{im}T)^0.
\]

::: {.proof}
Let $\varphi\in\ker(T^t)$. If $w\in\operatorname{im}T$, then $w=Tv$ for some $v\in V$, and
\[
\varphi(w)
=
\varphi(Tv)
=
(T^t\varphi)(v)
=0.
\]
Thus $\varphi$ vanishes on $\operatorname{im}T$.
:::

<1>3. Therefore
\[
\boxed{(\operatorname{im}T)^0=\ker(T^t)}.
\]

::: {.proof}
Steps <1>1 and <1>2 prove the two inclusions.
:::

<1>4. For every subspace $Y\subseteq W$,
\[
\dim Y^0=\dim W-\dim Y.
\]

::: {.proof}
Let $y_1,\ldots,y_r$ be a basis of $Y$ and extend it to a basis
\[
y_1,\ldots,y_r,w_{r+1},\ldots,w_m
\]
of $W$. In the corresponding dual basis of $W^*$, the annihilator $Y^0$ is spanned by
\[
w_{r+1}^*,\ldots,w_m^*.
\]
Hence
\[
\dim Y^0=m-r=\dim W-\dim Y.
\]
:::

<1>5. One has
\[
\operatorname{rank}(T^t)=\operatorname{rank}(T).
\]

::: {.proof}
By rank-nullity for $T^t:W^*\to V^*$,
\[
\operatorname{rank}(T^t)
=
\dim W^*-\dim\ker(T^t).
\]
Since $W$ is finite-dimensional,
\[
\dim W^*=\dim W.
\]
By step <1>3 and then step <1>4,
\[
\dim\ker(T^t)
=
\dim(\operatorname{im}T)^0
=
\dim W-\dim\operatorname{im}T.
\]
Therefore
\[
\operatorname{rank}(T^t)
=
\dim\operatorname{im}T
=
\operatorname{rank}(T).
\]
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>3 proves part (i), and step <1>5 proves part (ii).
:::
:::
