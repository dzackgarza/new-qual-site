---
schema: qual/card@1
id: P-UCLAB01F-07
kind: problem
title: Annihilator of an image and rank of the transpose
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 of the retained UCLA Basic Exam, Fall 2001 PDF.
---

::: {.problem}
Let $V$ be a real vector space and $X\subseteq V$ a subspace.
Write
\[
V^*=\{f:V\to\mathbb R:f\text{ is linear}\}
\]
and
\[
X^0=\{f\in V^*:f(x)=0\text{ for every }x\in X\}.
\]
Let $T:V\to W$ be a linear transformation of finite-dimensional real vector spaces, and let its transpose $T^t:W^*\to V^*$ be defined by $T^t(f)=f\circ T$.
Prove that
\[
(\operatorname{im}T)^0=\ker(T^t)
\]
and
\[
\dim\operatorname{im}T=\dim\operatorname{im}T^t.
\]
:::

::: pf

::: pf-step

One has
\[
(\operatorname{im}T)^0\subseteq\ker(T^t).
\]


::: pf-proof

Let $f\in(\operatorname{im}T)^0$. For every $v\in V$,
\[
(T^tf)(v)=(f\circ T)(v)=f(Tv).
\]
Since $Tv\in\operatorname{im}T$ and $f$ vanishes on $\operatorname{im}T$, this value is $0$. Hence $T^tf=0$, so $f\in\ker(T^t)$.

:::

:::

::: pf-step

One has
\[
\ker(T^t)\subseteq(\operatorname{im}T)^0.
\]


::: pf-proof

Let $f\in\ker(T^t)$. Then
\[
f(Tv)=(T^tf)(v)=0
\]
for every $v\in V$. Every vector in $\operatorname{im}T$ has the form $Tv$, so $f$ vanishes on $\operatorname{im}T$. Thus $f\in(\operatorname{im}T)^0$.

:::

:::

::: pf-step

Therefore
\[
\boxed{(\operatorname{im}T)^0=\ker(T^t)}.
\]


::: pf-proof

Steps <1>1 and <1>2 prove the two inclusions.

:::

:::

::: pf-step

If $Y$ is a subspace of a finite-dimensional real vector space $W$, then
\[
\dim Y^0=\dim W-\dim Y.
\]


::: pf-proof

Let
\[
y_1,\ldots,y_r
\]
be a basis of $Y$, and extend it to a basis
\[
y_1,\ldots,y_r,w_{r+1},\ldots,w_m
\]
of $W$, where $m=\dim W$. Let
\[
y_1^*,\ldots,y_r^*,w_{r+1}^*,\ldots,w_m^*
\]
be the dual basis of $W^*$. A functional lies in $Y^0$ exactly when its coefficients on
\[
y_1^*,\ldots,y_r^*
\]
are zero. Hence
\[
Y^0=\operatorname{span}\{w_{r+1}^*,\ldots,w_m^*\},
\]
so
\[
\dim Y^0=m-r=\dim W-\dim Y.
\]

:::

:::

::: pf-step

The nullity of $T^t$ is
\[
\dim\ker(T^t)=\dim W-\dim\operatorname{im}T.
\]


::: pf-proof

By step <1>3,
\[
\ker(T^t)=(\operatorname{im}T)^0.
\]
Apply step <1>4 with $Y=\operatorname{im}T\subseteq W$.

:::

:::

::: pf-step

The ranks of $T$ and $T^t$ are equal:
\[
\boxed{\dim\operatorname{im}T=\dim\operatorname{im}T^t}.
\]


::: pf-proof

Apply rank-nullity to
\[
T^t:W^*\to V^*.
\]
Since $\dim W^*=\dim W$, step <1>5 gives
\[
\begin{aligned}
\dim\operatorname{im}T^t
&=\dim W^*-\dim\ker(T^t)\\
&=\dim W-(\dim W-\dim\operatorname{im}T)\\
&=\dim\operatorname{im}T.
\end{aligned}
\]

:::

:::

::: pf-qed

Step <1>3 proves the first assertion, and step <1>6 proves the second.

:::

:::
