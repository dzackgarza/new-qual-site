---
schema: qual/card@1
id: E-F2PUE
kind: problem
title: Transitivity of algebraic, normal, and separable extensions
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Separability
  - Splitting Fields
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
5. If $F$ is over $E$, and $E$ is $\quad$ over $K$ is $F$ necessarily over $K$ ? Answer this question for each of the words "algebraic," "normal," and "separable" in the blanks.
:::

::: {.solution}
Let $K\subseteq E\subseteq F$ be the tower. Algebraicity and separability are transitive; normality is not.

<1>1. If $F/E$ and $E/K$ are algebraic, then $F/K$ is algebraic.
::: {.proof}
Take $\alpha\in F$. Since $F/E$ is algebraic, $\alpha$ satisfies a polynomial over $E$. Let $e_1,\ldots,e_r\in E$ be its coefficients. Since each $e_i$ is algebraic over $K$, the extension $K(e_1,\ldots,e_r)/K$ is finite. The element $\alpha$ is algebraic over $K(e_1,\ldots,e_r)$, so $K(e_1,\ldots,e_r,\alpha)/K$ is finite. Hence $\alpha$ is algebraic over $K$.
:::

<1>2. If $F/E$ and $E/K$ are separable algebraic extensions, then $F/K$ is separable.
::: {.proof}
Take $\alpha\in F$, and let $f\in E[x]$ be its minimal polynomial over $E$. The finitely many coefficients of $f$ lie in some finite subextension $E_0/K$ of $E/K$. Because $E/K$ is separable, $E_0/K$ is finite separable.

The polynomial $f$ is separable, so it has no repeated root in an algebraic closure. Let $q\in E_0[x]$ be the minimal polynomial of $\alpha$ over $E_0$. Since $f(\alpha)=0$, the polynomial $q$ divides $f$ in $E_0[x]$. Hence $q$ also has no repeated root, so $\alpha$ is separable over $E_0$. Thus $E_0(\alpha)/E_0$ is finite separable.

Choose generators $e_1,\ldots,e_m$ for $E_0/K$ and then adjoin $\alpha$. Each successive generator is separable over the preceding field: each $e_i$ is separable over $K$, hence its minimal polynomial over an intermediate extension divides a separable polynomial over $K$, and $\alpha$ is separable over $E_0$. Therefore $E_0(\alpha)/K$ is separable. In particular $\alpha$ is separable over $K$. Since $\alpha$ was arbitrary, $F/K$ is separable.
:::

<1>3. Normality is not transitive.
::: {.proof}
Let
\[
K=\QQ,\qquad E=\QQ(\sqrt2),\qquad F=\QQ(\sqrt[4]{2}).
\]
The extension $E/K$ is quadratic, hence normal. Also $F/E$ is quadratic because $\sqrt[4]{2}$ satisfies $x^2-\sqrt2$, so $F/E$ is normal.

However, $F/K$ is not normal. The element $\sqrt[4]{2}$ has minimal polynomial $x^4-2$ over $\QQ$, whose roots are
\[
\pm\sqrt[4]{2},\qquad \pm i\sqrt[4]{2}.
\]
The field $F$ is contained in $\RR$, so it does not contain the two nonreal roots. Hence $x^4-2$ does not split over $F$.
:::

<1>4. Therefore the answers are: algebraic—yes; normal—no; separable—yes.
::: {.proof}
Combine <1>1--<1>3.
:::
:::
